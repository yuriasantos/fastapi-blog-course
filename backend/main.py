from fastapi import FastAPI

app = FastAPI(title='Blog', version='0.1.0')

@app.get('/')
def hello():
    return {'msg':'Hello FastAPI!'}
