# Chocolask
Chocolask is a lightweight, single-threaded web server written in Python. It serves files and manages a simple TODO list.

## Features
- Handles GET and POST requests
- Parses HTTP requests and generates responses
- Can serve multiple types of files
- Routes requests to appropriate handlers
- Manages a simple TODO list (stored in a json file)
## Usage
- Clone the repository
- You need to create a `.env` file in the root directory of the project and define the necessary variables.
  - `HOST_NAME`: The host name of the server
  - `PORT`: The port number of the server
  - `TODOS_ROOT`: The path to the directory where the TODO list is stored
  - `BUFFER_SIZE`: The buffer size of the server
  - `JSON_INDENT`: The indentation of the JSON file
- Navigate to the cloned directory
- Run python3 main.py
- Open a web browser and go to localhost:8001
## License
This project is licensed under the MIT License.

