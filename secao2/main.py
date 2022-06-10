from fastapi import FastAPI

app = FastAPI()


@app.get('/msg')
async def message():
    return {
        "msg": "FastAPI na Geek University"
    }


@app.get('/')
async def home():
    return {
        "msg": "Home"
    }


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host="0.0.0.0", port=8000,
                log_level="info", reload=True)
