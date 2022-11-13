import pandas as pd
import os
from configs.config import configs as settings
from utils.log import logger


def write_csv(data, columns=None, file_path=None):
    '''
    写入 csv
    :param file_path : 表格路径
    :param columns: 表格标题
    :param data: 表格值
    '''
    if not file_path:
        file_path = os.path.join(settings.BASE_DIR, 'docs', 'account', 'file_account.csv')
    else:
        file_path = os.path.join(settings.BASE_DIR, file_path)
    if not columns:
        columns = ["user", "password", 'gte', 'lte']
    df = pd.DataFrame(columns=columns, data=data, )
    # 导出csv
    # 解决追加模式写的表头重复问题
    if not os.path.exists(file_path):
        df.to_csv(file_path, header=columns, index=False, mode='a')
    else:
        df.to_csv(file_path, header=False, index=False, mode='a')


def read_csv(file_path=None):
    '''
    读取csv文件
    :param file_path:
    :return:
    '''
    if not file_path:
        file_path = os.path.join(settings.BASE_DIR, 'docs', 'account', 'file_account.csv')
    else:

        file_path = os.path.join(settings.BASE_DIR, file_path)
    s_data = pd.read_csv(file_path, dtype=str)
    return s_data.iterrows()
    # for index, values in t_reagent_class_type.iterrows():
