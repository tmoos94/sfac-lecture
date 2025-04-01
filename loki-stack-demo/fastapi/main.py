import logging
import time
from fastapi import FastAPI, Request
from datetime import datetime

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("/var/log/fastapi/app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("fastapi-app")

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    # 요청 로깅
    logger.info(f"Request started: {request.method} {request.url.path}")

    response = await call_next(request)

    # 응답 시간 계산
    process_time = time.time() - start_time
    logger.info(f"Request completed: {request.method} {request.url.path} - Took: {process_time:.4f}s")

    return response

@app.get("/")
async def root():
    logger.info("Root endpoint called")
    return {"message": "Hello World"}

@app.get("/health")
async def health():
    logger.info("Health check endpoint called")
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/error")
async def trigger_error():
    logger.error("Error endpoint called - Generating sample error")
    return {"error": "This is a sample error log message"}
