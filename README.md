# FastAPI CRUD Application with Supabase Integration
This is a simple CRUD (Create, Read, Update, Delete) application built using FastAPI with integration to Supabase, a powerful and flexible open-source alternative to Firebase for data storage.

## Description
This application provides basic CRUD operations for managing data stored in a Supabase database. It includes endpoints to:
1. Fetch all data from a table
2. Fetch data by ID
3. Insert new data
4. Update existing data
5. Delete data by ID

## Requirements
1. Python 3.7+
2. FastAPI
3. Pydantic
4. Supabase Python client
5. Uvicorn (for running the FastAPI application)

## Installation:

### Importing necessary modules:
```
pip install fastapi
pip install supabase
```

### Configuration
Before running the application, you need to set up your Supabase credentials. Update the following variables in main.py:
```
export SUPABASE_URL="YOUR_SUPABASE_URL"
export SUPABASE_KEY="YOUR_SUPABASE_KEY"
```
### Usage
Run the FastAPI application:
```
uvicorn main:app --host 127.0.0.1 --port 8000
```
### API Endpoints
1. GET /: Returns a sample response.
2. GET /fetch: Fetches all data from the specified table.
3. GET /fetch/{id}: Fetches data by ID.
4. POST /insert: Inserts new data into the table.
5. PUT /update/{id}: Updates existing data by ID.
6. DELETE /delete/{id}: Deletes data by ID.

### Data Model
The application uses the following data model:
```
class Base(BaseModel):
    title: str
    description: str
```





