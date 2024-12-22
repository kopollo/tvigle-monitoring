import json

from app.schemas import LogSchema


def parse_logs(dict_logs: str):
    log_list: list[LogSchema] = []
    for log in dict_logs:
        log_list.append(LogSchema.parse_obj(log))
    return log_list


def read_logs():
    with open('app/tvigle_logs.json', 'r') as file:
        logs = json.load(file)
    return logs


def send_logs():
    logs = parse_logs(read_logs())
    return logs


global_logs: list[LogSchema] = send_logs()[:20]
