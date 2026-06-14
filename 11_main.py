from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = None

users = []

@app.get("/")
def home():
    return {"message": "Welcome"}

# Sample Output:
# {
#   "message": "Welcome"
# }

# Path Parameter

@app.get("/user/{id}")
def get_user(id: int):
    for user in users:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Sample Request:
# /user/1

# Sample Output:
# {
#   "id": 1,
#   "name": "Rahul",
#   "age": 25
# }


# 3. Query Parameter

@app.get("/search")
def search_user(name: Optional[str] = None):
    return [u for u in users if name and name in u.name]

# Sample Request:
# /search?name=Rahul

# Sample Output:
# [
#   {
#     "id": 1,
#     "name": "Rahul",
#     "age": 25
#   }
# ]


# POST (Create)

@app.post("/user")
def create_user(user: User):
    users.append(user)
    return {"message": "User added"}

# Sample Payload (JSON):
# {
#   "id": 1,
#   "name": "Rahul",
#   "age": 25
# }

# Sample Output:
# {
#   "message": "User added"
# }

# 5. PUT (Update)

@app.put("/user/{id}")
def update_user(id: int, new_user: User):
    for i, u in enumerate(users):
        if u.id == id:
            users[i] = new_user
            return {"message": "User updated"}
    raise HTTPException(status_code=404, detail="User not found")

# Sample Request:
# /user/1

# Sample Payload:
# {
#   "id": 1,
#   "name": "Rahul Updated",
#   "age": 26
# }

# Sample Output:
# {
#   "message": "User updated"
# }


# 7. DELETE

@app.delete("/user/{id}")
def delete_user(id: int):
    for u in users:
        if u.id == id:
            users.remove(u)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

# Sample Request:
# /user/1

# Sample Output:
# {
#   "message": "User deleted"
# }


# HOW TO RUN THIS CODE


# 1. Install dependencies:
#    pip install fastapi uvicorn

# 2. Save this file as:
#    main.py

# 3. Run the server:
#    uvicorn main:app --reload

# 4. Open in browser:
#    http://127.0.0.1:8000/docs
#    (Swagger UI for testing APIs)
