# Book Recreate API (Assignment Project)

This is a small API project I worked on for my class assignment.  
The task was given by my tutor for us to practice how to create REST APIs using FastAPI.

## What I did

For this project, I focused on:
- Setting up the API using FastAPI.
- Creating endpoints to handle users and books.
- Organizing the project into folders (like routers, schemas, and database simulation using lists).
- Testing the endpoints with pytest and httpx.

I used basic Python lists to simulate data. 
I also wrote simple tests just to make sure my endpoints are working fine.

## Tools I used

- FastAPI
- Pydantic
- Pytest
- Uvicorn
- httpx

## How I ran it

```bash
# activate virtual env
bookenv\Scripts\activate

# run the app
uvicorn main:app --reload

# run tests
pytest
