from flask import Flask, request

'''
from flask:

This part tells Python that you want to import something from the flask module.
flask is a module that you need to have installed in your Python environment. You can install it using pip: pip install Flask.

import Flask:

This part specifies that you want to import the Flask class from the flask module.
Flask is the main class for creating a Flask application.
'''

app = Flask(__name__)

'''
Flask Object Creation:

Flask: As mentioned earlier, Flask is a class provided by the Flask framework that represents a Flask application. It is used to create instances of Flask applications.

__name__ Argument:

__name__: In Python, __name__ is a special variable that represents the name of the current module. When the Python interpreter runs a module, it sets __name__ to '__main__' if the module being run is the main program. If the module is being imported from another module, __name__ will be set to the module's name.

Application Instance:

app = Flask(__name__): This line creates an instance of a Flask application and assigns it to the variable app. The __name__ argument is typically used by Flask to determine the root path of the application. This helps Flask to locate resources such as templates and static files relative to the location of the module where Flask is instantiated.

Application Configuration:

The Flask(__name__) instantiation initializes the Flask application with sensible defaults, but you can further configure your Flask app by setting various configuration options using app.config.
'''

# storing the data (for simpliciity we are not using a database)

music_stores = [
    {
        "name": "Music Store A",
        "songs": [
            {"name": "Shape of You", "artist": "Ed Sheeran", "price": 1.29},
            {"name": "Blinding Lights", "artist": "The Weeknd", "price": 1.19},
            {"name": "Dance Monkey", "artist": "Tones and I", "price": 0.99}
        ]
    },
    {
        "name": "Music Store B",
        "songs": [
            {"name": "Someone Like You", "artist": "Adele", "price": 1.49},
            {"name": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars", "price": 1.39}
        ]
    }
]



'''
In Flask, setting up a route involves two main components:

Endpoint Decorator:

The endpoint decorator, such as @app.route("/music_stores"), marks the URL path (/music_stores) that the Flask application should recognize and handle. This decorator essentially tells Flask that when a client sends a request to /music_stores, it should invoke the associated function.

Route Handling Function:

The function decorated by @app.route("/music_stores"), let's say def get_music_stores(), defines what should happen when the /music_stores endpoint is accessed. This function handles the request by executing specific logic, which might involve querying a database, processing data, or performing other tasks.

#-----------------------------------------------------------------------------------#

At the end of its execution, this function typically returns a response. For REST APIs, this response is commonly in JSON format, although Flask supports returning various types of data such as HTML, XML, plain text, or custom formats like YAML.

The return value of the function gets converted into an HTTP response that Flask sends back to the client(here I have used Insomnia as the client) that made the request.

In essence, the endpoint decorator links a specific URL path (/music_stores in this case) to a Python function (get_music_stores()), which determines how the server responds to requests made to that URL. This separation of concerns allows Flask applications to efficiently handle different routes and their corresponding functionalities.
'''

# Retrieve all the music stores and their songs
# GET /music_stores

@app.route('/music_stores')
def get_music_stores():
    return {'All Music Stores': music_stores}

# Note 1: When we return a Python dictionary in a Flask route, Flask automatically turns it into JSON for us. 
# Note 2: JSON is just a (usually long) string whose contents follow a specific format.


# Create a new store 
# The insomnia client passes the data in a json format like this:
# {
#     "name": "Music Store C"
# }

@app.route('/music_stores' , methods= ['POST'])
def create_music_store():
    request_data = request.get_json()
    new_music_store = {
        "name":request_data['name'],
        "songs":[]
    }
    music_stores.append(new_music_store) # append the music store to the msuic stores
    return new_music_store, 201

'''
NOTE on STATUS CODE:
In Flask, HTTP status codes indicate the outcome of a server request. They inform the client whether the request was successful, encountered an error, or requires further action. Here's a breakdown of common status codes and how Flask handles them:

200 OK: This status code indicates that the request has succeeded. It is commonly used for successful GET requests where the server returns requested data.

201 Created: This status code indicates successful creation of a resource. It is typically returned by POST requests when a new resource (such as a store in your example) has been successfully created.

404 Not Found: This status code indicates that the server could not find the requested resource. It is commonly used when a client requests a URL that does not exist on the server.
'''

@app.route('/music_store/<string:music_store_name>/songs' , methods =['POST'])
def create_songs(music_store_name):
    request_data = request.get_json()
    # Search for the music store based on the name in the dynamic url 
    # Once found, save the list in a variable named target_song_list
    # if not found return a 404 error 
    found = False
    for music_store in music_stores:
        if music_store['name'] == music_store_name:
            found = True # make the flag True 
            target_song_list = music_store['songs']
    
    if not found:
        return {"message":"Store not found"}, 404
            
    # check whether the data is in the list
    # append the data as a dict to the target_song_list
    if isinstance(request_data, list):
        for data in request_data:
            name = data['name']
            artist = data['artist']
            price = data['price']
            song_to_append = {
                "name":name,
                "artist":artist,
                "price":price
                }
            target_song_list.append(song_to_append)
    return target_song_list


# Given its(music store's) name, retrieve an individual music store and all its songs.
@app.route("/music_store/<string:music_store_name>")
def get_music_store(music_store_name):
    for music_store in music_stores:
        if music_store['name'] == music_store_name:
            return music_store
    return {"message":"Store not found"},404

# Given a music store name, retrieve only a list of songs within it.
@app.route("/music_store/<string:music_store_name>/song")
def get_music_store_songs(music_store_name):
    for music_store in music_stores:
        if music_store['name'] == music_store_name:
            return music_store['songs']
    return {"message":"Store not found"},404
            