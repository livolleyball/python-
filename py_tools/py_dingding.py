# coding=utf-8

import datetime
import logging

import pymysql
import requests

# 钉钉url token
ding_url = 'https://oapi.dingtalk.com/robot/send?access_token='


# mysql:

mysql_host = ""
mysql_user = ""
mysql_password = ""
mysql_db = ""

#
logging.basicConfig(
    format='%(asctime)s [%(levelname)s %(filename)s %(lineno)d][%(message)s]',
    datefmt='[%Y-%m-%d %H:%M:%S %p]',
    filename="/data/task/dingding.log",
    level=logging.INFO
)


# 发送到Ding：####
def send2Ding(url, data):
    body = {"msgtype": "text", "text": {"content": {"消息内容": data}}}
    headers = {'content-type': "application/json; charset=utf8",
               "user-agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)"}
    # body= json.dumps(body);
    response = requests.post(url, json=body, headers=headers)
    logging.info("status_code======%s" % response.status_code)


# 从mysql获取数据：####
def get_data_from_mysql(sql):
    # Open database connection
    conn = pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_password, db=mysql_db, charset="utf8");
    cursor = conn.cursor()

    # 查询：
    cursor.execute(sql)
    result_tuple = cursor.fetchone()

    # 关闭
    cursor.close()
    conn.close()

    # return:
    return result_tuple


# 获取报警统计sql
def get_query_sql():
    today = datetime.datetime.today()
    dayid = today.strftime('%Y-%m-%d')  # "2018-07-13"

    # 报警统计sql：
    query_sql = """
        SELECT
        * 
        from tb 
        where day = %s limit 1;
        
    """ % (dayid)

    logging.info("query_sql=[%s]" % query_sql)
    return query_sql


if __name__ == "__main__":
    result_tuple = get_data_from_mysql(get_query_sql())
    is_error = result_tuple[0]
    a = result_tuple[1]
    b = result_tuple[2]

    time_hhmm = datetime.datetime.today().strftime("%H:%M")
    data = "信息1=[%s] 信息2=[%s]" % (a, b)

    if is_error == 0:
        status = '正常'
        message = "时间[%s] 当前健康情况：[%s] %s" % (time_hhmm, status, data)
        logging.info(message)
        # 钉钉url(poseidon告警群):
        send2Ding(ding_url, message)
    else:
        status = '异常'
        message = "时间[%s] 当前健康情况：[%s] %s" % (time_hhmm, status, data)
        logging.info(message)
        send2Ding(ding_url, message)

