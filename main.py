from fastapi import FastAPI

app = FastAPI()

@app.get('/welcome')
def say_hello():
    return {
        'message':'hello world'
    }