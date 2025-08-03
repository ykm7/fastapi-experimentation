from typing import Annotated
from fastapi import FastAPI, Path
from pydantic import BaseModel, Field

app = FastAPI()

class MyPerson(BaseModel):
    '''
    Haven't used pydantic before; primarily used TypedDict to perform some structure.
    This seems nicer though

    This all automatically appears SwaggerUI!! Very cool.
    '''
    name: str = "DEFAULT NAME"
    age: Annotated[int, Field(gt=0)] = Field(default=0, gt=0)

@app.get("/")
async def read_root() -> dict[str,str]:
    return {"Hello": "World"}

@app.get("/ping")
async def ping() -> str:
    return "pong"

@app.get("/person/{name}")
async def get_person(name: str = Path(..., min_length=3)) -> MyPerson:
    '''

    For:
        `return MyPerson(name=name, age=-1)`
    
    Testing limitation of mypy with pydantic. Hoped it would catch the negative age.

    Does result in a runtime error though:

        Input should be greater than 0 [type=greater_than, input_value=-1, input_type=int]
    '''
    return MyPerson(name=name, age=20)
