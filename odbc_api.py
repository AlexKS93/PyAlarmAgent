import pyodbc
from log import logger


def get_data_from_odbc(config):
    cnxn = pyodbc.connect(f"DSN={config.odbc_dsn};")
    cursor = cnxn.cursor()
    logger.debug(config.sql_text)
    cursor.execute(f"{config.sql_text}")
    rows = cursor.fetchall()
    data = []
    if rows:
        for row in rows:
            data.append(dict(zip(config.fields, row)))
    print(data)


if __name__ == '__main__':
    pass
