import pyodbc
from log import logger


def get_data_from_odbc(config, last_row_date):
    cnxn = pyodbc.connect(f"DSN={config.odbc_dsn};")
    cursor = cnxn.cursor()
    logger.debug(config.sql_text)
    print(last_row_date)
    if not last_row_date:
        cursor.execute(f"{config.last_row_sql_text}")
        rows = cursor.fetchone()
        last_row_date = rows[0]
    cursor.execute(f"{config.sql_text} > '{last_row_date}'")
    rows = cursor.fetchall()
    data = []
    if rows:
        for row in rows:
            data.append(dict(zip(config.fields, row)))
        print(data[:-1])
        last_row_date = data[-1][config.date_time_field]
        return data, last_row_date
    return [], last_row_date


if __name__ == '__main__':
    pass
