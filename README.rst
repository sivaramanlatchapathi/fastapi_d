This demo project has been created using poetry.

Step 1: - Create new project named fastapi_d

cmd: poetry new fastapi_d

Created package fastapi_d in fastapi_d

% ls -ltr
total 8
drwxr-xr-x  3 siva  staff   96 Aug 10 11:13 fastapi_d
-rw-r--r--  1 siva  staff    0 Aug 10 11:13 README.rst
drwxr-xr-x  4 siva  staff  128 Aug 10 11:13 tests
-rw-r--r--  1 siva  staff  294 Aug 10 11:13 pyproject.toml


poetry add fastapi 'uvicorn[standard]'


FastAPI doc : https://fastapi.tiangolo.com/

Reg:-

Python 3.6+
FastAPI stands on the shoulders of giants:

    Starlette for the web parts.
    Pydantic for the data parts.

https://fastapi.tiangolo.com/tutorial/background-tasks/

uvicorn doc : https://www.uvicorn.org/
