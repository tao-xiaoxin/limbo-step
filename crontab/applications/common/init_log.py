from loguru import logger
from conf import env
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
LOG_PATH = BASE_DIR.joinpath('./logs').resolve()  # 获得文件夹的绝对路径
if not LOG_PATH.exists():  # 日志文件夹不存在就新建
    LOG_PATH.mkdir()
logger.add("{}/{}".format(LOG_PATH, env.log_file), retention="10 days")  # 定期清除日志
