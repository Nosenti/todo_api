# Flask To-Do App

This is a simple To-Do application built with Flask, providing a basic demonstration of a RESTful API for managing To-Do items. Each To-Do item has an `id` and a `title`.

## Features

- List all To-Do items.
- Get details of a specific To-Do item.
- Create a new To-Do item.
- Update an existing To-Do item.
- Delete a To-Do item.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Postman

If you don't have Flask installed, you can install it using pip:

```bash
pip install flask
```

### Running the App
- Clone the repository or download the source code
- Navigate to the project directory
- Run the app using the following command
```bash
python main.py
```
The app will start runnnig on http://127.0.0.1:5000/

### API Endpoints
- **GET /todos:** Returns a list of all To-Do items.
- **GET /todos/<int:todo_id>:** Returns details of a specific To-Do item.
- **POST /todos:** Creates a new To-Do item. Requires a JSON body with a title field.
- **PUT /todos/<int:todo_id>:** Updates an existing To-Do item. Requires a JSON body with a title field.
- **DELETE /todos/<int:todo_id>:** Deletes a specific To-Do item.

### Testing the API
You can test the API endpoints using tools like Postman: https://www.postman.com/

### Notes
This application is for demonstration purposes and does not use persistent storage. The To-Do items are stored in memory and will be lost when the server is restarted
