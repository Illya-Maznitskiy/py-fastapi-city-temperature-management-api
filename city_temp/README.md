# **City and Temperature Tracker**

## **Description**
A FastAPI application to manage city data and track corresponding temperature records. This project includes:
- CRUD operations for city data.
- APIs to fetch and store temperature data for cities.

---

## Setup Instructions

### Clone the Repository
Clone the repository and navigate to the project folder.

### Install Dependencies
Ensure Python is installed and install the required dependencies by using `requirements.txt`.

### Set Up the Database
The application uses SQLite by default. Ensure the database is created, and any necessary migrations are applied.

### Create env file
Create the .env file with env.sample example

### Run the Application
Start the FastAPI server to run the application locally.

### Access the API Documentation
Once the server is running, access the API documentation at:
- Swagger UI: `/docs`
- ReDoc: `/redoc`

## Key Features

### City Management:
- Create, read, update, and delete city data.

### Temperature Tracking:
- Fetch current temperatures for all cities.
- Store and retrieve temperature history.
