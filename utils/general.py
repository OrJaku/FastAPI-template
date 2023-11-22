import os
import logging
import json
import math
import pytz
from pathlib import Path
from datetime import datetime
from typing import List, Optional, Tuple, Any
from typing import SupportsFloat as Numeric


BASE_DIR = Path(__file__).resolve().parent.parent
TIMEZONE = 'Europe/Warsaw'

def get_json(dir: str, filename: str) -> dict:
    """
    Open JSON file a get data

    """
    file_path = os.path.join(BASE_DIR, dir, filename)
    try:
        with open(file_path) as f:
            data = json.load(f)
        return data
    except (FileExistsError, FileNotFoundError) as err:
        logging.error(f"File {file_path} not found")
        logging.debug(f"Error message {err}")


def datetime_now() -> datetime:
    tz = pytz.timezone(TIMEZONE)
    return datetime.now(tz).replace(tzinfo=None)


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 1)
   return f"{s} {size_name[i]}"
