# fastapi-experimentation

## Python version

### Env installation

#### Windows

> py -3.13 -m venv env

#### Source

> .\env\Scripts\Activate.ps1

## Packages
### Pip-Tools for Package.json like management

> pip install pip-tools

#### [dev-]requirements.txt generation
> pip-compile requirements.in

> pip-compile dev-requirements.in


This provides a layer allowing direct pinning of required requirements with their co-dependencies being managemented automatically

### Requirements

> pip install -r requirements.txt -r dev-requirements.txt

## Running Locally

> fastapi dev main.py

### Debug (within VSCode)

`launch.json`
```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: FastAPI",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "main:app",
                "--reload"
            ],
            "jinja": true
        }
    ]
}
```

Then `F5`

### Documentation

Will be hosted on: http://127.0.0.1:8000/docs

## Linting

### Mypy

Add `mypy` to `dev-requirements.in`

#### VSCode
setting section:
```json
{
  "mypy.dmypyExecutable": "${workspaceFolder}/env/Scripts/dmypy.exe"
}
```

## Takeaways

### Live reloading from code changes out of the box.

### Built in data validation on Pydantic
This is great! Automatically applies to Swagger output

### Native support for async 
For Flask its better to go with Quart (async fork or Flask) or Flask with )

### FastApi vs Flask

#### FastAPI Pros
- Async support
- native type support with Pydantic
- Async with ASGI
