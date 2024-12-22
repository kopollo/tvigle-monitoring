from fastapi import APIRouter
from starlette.responses import PlainTextResponse

import app.importer as importer
import app.prometheus_service as prometheus_service
from app.schemas import LogSchema

api_router = APIRouter(
    prefix="",
    tags=["Metrics"],
)


@api_router.post("/logs")
async def receive_logs(logs: list[LogSchema]):
    # logs = importer.send_logs()
    # for log in logs:
    #     prometheus_service.init_prometheus_log(log)
    return {"message": "Logs received successfully", "log_count": len(logs)}


@api_router.get("/metrics", response_class=PlainTextResponse)
async def metrics():
    return prometheus_service.send_metrics()
