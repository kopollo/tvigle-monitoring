from fastapi import APIRouter
from starlette.responses import PlainTextResponse

import app.prometheus_service as prometheus_service
from app.schemas import LogSchema

api_router = APIRouter(
    prefix="",
    tags=["Metrics"],
)


@api_router.post(
    "/logs",
    description="Эндпоинт для отправки ваших логов о качестве воспроизведения видео.")
async def receive_logs(logs: list[LogSchema]):
    # for log in logs:
    #     prometheus_service.init_prometheus_log(log)
    return {"message": "Logs received successfully", "log_count": len(logs)}


@api_router.get(
    "/metrics",
    response_class=PlainTextResponse,
    description="Эндпоинт для перевода json схемы в формат Prometheus.")
async def metrics():
    return prometheus_service.send_metrics()
