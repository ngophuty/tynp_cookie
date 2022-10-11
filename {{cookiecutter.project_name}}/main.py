import uvicorn
from fastapi import FastAPI
from {{cookiecutter.fie_env_name}} import env

app = FastAPI()

@app.get('/',tags=['Hello'])
async def hello_world():
    return {'message':'hello world!'}


if __name__ == "__main__":
    uvicorn.run(
        'main:app',
        host= env.HOST,
        port= env.PORT,
        reload= True
    )
