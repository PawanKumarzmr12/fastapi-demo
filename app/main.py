from fastapi import FastAPI
from app.routes import students

app = FastAPI(title="FastAPI Demo Project")

# Register routers
app.include_router(students.router, prefix="/students", tags=["Students"])

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Demo!"}
