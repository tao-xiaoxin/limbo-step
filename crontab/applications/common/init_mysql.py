import pymysql
from conf import env as configs
from applications.common.init_log import logger as logging

db = pymysql.connect(host=configs.MYSQL_HOST,
                     user=configs.MYSQL_USERNAME,
                     password=configs.MYSQL_PASSWORD,
                     database=configs.MYSQL_DATABASE,
                     port=configs.MYSQL_PORT, )
cursor = db.cursor()


def get_result(sql):
    '''
    查询数据
    :param sql:
    :return:
    '''
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except Exception as e:
        logging.error(e)
        return ''
    return results


def update_result(sql):
    '''
    更新数据
    :param sql:
    :return:
    '''
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except Exception as e:
        # Rollback in case there is any error
        db.rollback()
        logging.error(e)
