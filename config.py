from dataclasses import dataclass, field
import configparser  # импортируем библиотеку

from log import logger
from logging import DEBUG, INFO


@dataclass
class Cfg():
    debug: str
    input_mode: str
    loop_delay: field(init=False)
    kafka_client_id: str
    kafka_con_string: str
    kafka_topic: str
    odbc_dsn: str
    table: str
    fields: list
    file_name: str
    logging_level: int = field(init=False)
    sql_text: str
    last_row_sql_text: str
    date_time_field: str

    def __post_init__(self):
        self.logging_level = DEBUG if self.debug else INFO
        self.loop_delay = int(self.loop_delay)
        self.fields = self.fields.split(",")


def load_config() -> Cfg:
    '''Загрузка конфигурации'''
    try:
        logger.debug("Загружаем конфиг...")
        config = configparser.ConfigParser()  # создаём объекта парсера
        logger.debug("Конфиг загружен")
        config.read("settings.ini")
        cfg = {}
        for section in config:
            for key in config[section]:
                cfg[key] = config[section][key]
        logger.info(cfg)
        return Cfg(**cfg)
    except Exception as e:
        logger.fatal(e)


if __name__ == '__main__':
    c = load_config()
    print(c)
