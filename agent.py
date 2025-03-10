import time

from config import load_config
from log import logger
from file_api import get_data_from_file
from kafka_api import send_data_to_kafka
from odbc_api import get_data_from_odbc


def get_data(data_source: str, last_row_date) -> dict:
    if data_source == 'file':
        return get_data_from_file()
    if data_source == 'odbc':
        return get_data_from_odbc(config, last_row_date)


if __name__ == '__main__':
    try:
        config = load_config()
        logger.setLevel(config.logging_level)
        last_row_date = ""
        while True:
            logger.debug(f"Получаем данные в режиме {config.input_mode}")
            data, last_row_date = get_data(config.input_mode, last_row_date)
            logger.debug("Данные получены")
            if data:
                send_data_to_kafka(data, config)
            time.sleep(config.loop_delay)

    except Exception as e:
        logger.error(e)
