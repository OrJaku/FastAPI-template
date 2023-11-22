import os
import sys
import logging
from typing import List

from config import ProdConfig, DevConfig, TestsConfig
from utils import general

USER_CONFIG_FILENAME = "user_config.json"
USER_CONFIG_PATH = os.path.join("user_config", USER_CONFIG_FILENAME)
CHAINS_EXCHANGES_MAP_PATH = os.path.join("utils", "chains_exchanges_map.json")

def get_user_conf():
    return general.get_json("", USER_CONFIG_PATH)

def _prepare_configuraton():
    env = os.getenv("TENV", None)
    if env == "prod":
        return ProdConfig()
    elif env == "dev":
        return DevConfig()
    elif env == "tests":
        return TestsConfig()    
    else:
        logging.error("Parameter 'env' has not been passed (environemnt variable TENV is None). Application cannot start.")
        sys.exit()

conf = _prepare_configuraton()