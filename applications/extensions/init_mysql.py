import pymysql
from applications.configs.config import configs

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
    cursor.execute(sql)
    results = cursor.fetchall()
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
    except:
        # Rollback in case there is any error
        db.rollback()


