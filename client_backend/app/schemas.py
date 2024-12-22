from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class LogSchema(BaseModel):
    timestamp: datetime
    user_id: str
    region: str
    device_type: str
    content_id: str
    initial_playback_delay_ms: int
    rebuffer_count: int
    total_stall_duration_ms: int
    average_bitrate_kbps: int
    cdn_response_time_ms: int
    segment_download_time_ms: List[int]
    final_resolution: str
    vod_duration_s: int
    vod_variant_name: str
    vod_bitrate: int
    vod_audio_codec: str
    vod_video_codec: str
    vod_width: int
    vod_height: int
    vod_seek: bool
    vod_error: Optional[str]
