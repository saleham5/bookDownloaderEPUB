import logging
from gevent import sleep
from httpx import codes, get

logging.getLogger("httpx").setLevel(logging.WARNING)

TIME_OUT = 500
MAX_RETRIES = 30


def get_url_text(url: str) -> str:
    retries = 0
    while True:
        try:
            response = get(url, timeout=TIME_OUT)
            if response.status_code == codes.OK:
                return response.text or ""
        except Exception as e:
            # Log the exception if needed
            logging.error(f"Error fetching URL: {url}. Exception: {e}")

        # Exponential backoff
        if retries >= MAX_RETRIES:
            break  # Break out of the loop if maximum retries reached
        sleep(2 ** retries)
        retries += 1

    return ""
