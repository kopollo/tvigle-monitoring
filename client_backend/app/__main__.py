from fastapi import FastAPI
from uvicorn import run

from app.endpoints import api_router

app = FastAPI(
    title="Very top cool best api",
    description="Система мониторинга для сбора и анализа качества воспроизведения в реальном времени",
    version="1.0.0",
)
app.include_router(api_router)
if __name__ == "__main__":  # pragma: no cover
    run(
        "app.__main__:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_dirs=["."],
        log_level="debug",
        proxy_headers=True,
    )
