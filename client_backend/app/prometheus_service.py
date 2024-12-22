from prometheus_client import Counter, Histogram, Gauge, generate_latest, REGISTRY

import app.importer as importer
from app.schemas import LogSchema

# Задержка перед запуском
initial_playback_delay = Histogram(
    'initial_playback_delay_ms',
    'Задержка при старте воспроизведения, в миллисекундах.',
    ['region', 'device_type']
)

# Ребуферинг
rebuffer_count = Counter(
    'rebuffer_count',
    'Количество ребуферингов (остановок для загрузки) во время просмотра.',
    ['region', 'device_type']
)
total_stall_duration_ms = Histogram(
    'total_stall_duration_ms',
    'Общая продолжительность всех ребуферингов, в миллисекундах.',
    ['region', 'device_type']
)

# CDN
cdn_response_time_ms = Histogram(
    'cdn_response_time_ms',
    'CDN response time in milliseconds',
    ['region', 'device_type']
)

vod_errors = Counter(
    'vod_errors',
    'Number of playback errors',
    ['region', 'device_type']
)


def init_prometheus_log(log: LogSchema):
    labels = {
        'region': log.region,
        'device_type': log.device_type,
    }
    print(log)
    initial_playback_delay.labels(**labels).observe(log.initial_playback_delay_ms)
    rebuffer_count.labels(**labels).inc(log.rebuffer_count)
    total_stall_duration_ms.labels(**labels).observe(log.total_stall_duration_ms)
    cdn_response_time_ms.labels(**labels).observe(log.cdn_response_time_ms)

    # if log.vod_error:
    #     vod_errors.labels(**labels).inc()


def send_metrics():
    for log in importer.global_logs:
        init_prometheus_log(log)
    return generate_latest(REGISTRY)
