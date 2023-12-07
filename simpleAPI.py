from fastapi import FastAPI
from models import Todo

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "WE LOVE TO CODE!!"}

todos = []
# todos
@app.get("/")
async def root():
    return {"message": "Todo list"}

# get single todo
@app.get("/todos/{todo_id}")
async def get_one_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "Error404: No todos found!"}

#get all todos
@app.get("/list")
async def get_todos():
    return {"todos": todos}

# create todo
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message": "Todo has been added"}

# update todo
@app.put("/todos")
async def update_todo(todo_id: int, todo_object: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_object.item
            return {"todo": todo}
        
    return {"message": "Error404, no todo found"}

# delete todo
@app.delete("/todos/{todo_id}")
async def delete_todos(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"messege": "Todo is deleted"}
        
    return {"message": "Error404, no todos found"}
