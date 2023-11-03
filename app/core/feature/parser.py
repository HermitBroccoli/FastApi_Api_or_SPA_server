from ..config import *

APP_URL = os.getenv("APP_URL")

def parse_url(url):
    parts = url.split("://") if "://" in url else [None, url]
    protocol, rest = parts
    host_parts = rest.split(":") if ":" in rest else [rest]
    host, port = host_parts[0], host_parts[1] if len(host_parts) > 1 else None
    return [protocol, host, port]

protocol, host, port = parse_url(APP_URL)


uvicornObj = {
    "host": host,
    "port": int(port if port is not None else 8080),
    "log_level": "info",
    "reload": True,
}