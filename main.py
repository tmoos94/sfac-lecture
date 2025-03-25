from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()


# /static 디렉토리에서 정적 파일 제공
app.mount("/static", StaticFiles(directory="app"), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}

# favicon.ico 경로를 /static/favicon.png로 지정하여 아이콘 제공
@app.get("/favicon.ico")
async def favicon():
    return FileResponse("app/favicon.png")