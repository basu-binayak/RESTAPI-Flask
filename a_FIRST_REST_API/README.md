# Building the first REST API with Flask 

In this section we'll make a **simple REST API** that allows us to:

1. Create music stores, each with a name and a list of stocked songs.
2. Create a song within a music store, each with a name, artist, and price.
3. Retrieve a list of all music stores and their songs.
4. Given its(music store's) name, retrieve an individual music store and all its songs.
5. Given a music store name, retrieve only a list of songs within it.

### Create music stores
**Request:**

POST /store {"name": "Music Store"}

**Response:**

```json
{"name": "Music Store", "songs": []}
```

### Create songs
**Request:**

```
POST /store/Music Store/song {"name": "Shape of You", "artist": "Ed Sheeran", "price": 1.29}
```
**Response:**

```json
{"name": "Shape of You", "artist": "Ed Sheeran", "price": 1.29}
```

### Retrieve all music stores and their songs
**Request:**
```
GET /store
```
**Response:**

```json
{
    "stores": [
        {
            "name": "Music Store",
            "songs": [
                {
                    "name": "Shape of You",
                    "artist": "Ed Sheeran",
                    "price": 1.29
                }
            ]
        }
    ]
}
```
### Get a particular music store
**Request:**
```
GET /store/Music Store
```
**Response:**

```json
{
    "name": "Music Store",
    "songs": [
        {
            "name": "Shape of You",
            "artist": "Ed Sheeran",
            "price": 1.29
        }
    ]
}
```
### Get only songs in a music store
**Request:**
```
GET /store/Music Store/song
```
**Response:**

```json
[
    {
        "name": "Shape of You",
        "artist": "Ed Sheeran",
        "price": 1.29
    }
]
```
<hr>

## Some general instructions

### Create a new Conda environment:

```bash
conda create --prefix ./venv python
```

### Activate the virtual environment:

```bash
conda activate ./venv
```
### Create app.py from cmd 

```bash
echo>app.py
```

### Install Dependencies:
Use pip to install the dependencies listed in the requirements.txt file. Assuming your requirements.txt file is in the current directory:

```bash
pip install -r requirements.txt
```
This command reads the requirements.txt file and installs each package listed within it into your conda virtual environment.

### Verify Installation:
After installation completes, you can verify that the packages were installed correctly:

```bash
pip list
```
This command will display a list of installed packages in your virtual environment, including those from requirements.txt.

### Deactivate Conda Environment (Optional):
If you want to deactivate your conda environment, you can do so with:

```bash
conda deactivate
```
