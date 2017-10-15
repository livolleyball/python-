# coding:utf8

import pymysql
import datetime
conn=pymysql.connect(host='localhost',user='root',passwd='liyi',port=3306,db='report560',charset='utf8')
cur=conn.cursor()
rv =cur.execute('''SELECT id,cityId,parentId,`level`,cityName FROM  city where level<>3 ;''')
# rv =cur.execute('''SELECT id,cityId,parentId,`level`,cityName FROM  city ;''')
print(rv)
list=[]
def getall():
    for i in cur.fetchall():
        temp={"cityId":i[1],"cityName":i[4],"pid":i[2]}
        list.append(temp)
    return list


def gettree(date,pid):

    tree = []
    for i in date:
        if i['pid']==pid:
            # print(i['pid'],pid)
            if len(gettree(date, i['cityId'])) > 0:
                i['children']=gettree(date,i['cityId'])
            tree.append(i)
        else:
            pass
    # print(tree)
    return tree


def main():
    starttime = datetime.datetime.now()
    data=getall()
    # print(data)
    starttime1 = datetime.datetime.now()
    gettree(data,0)
    # print(gettree(data, 0))
    print(gettree(data, 0))
    endtime = datetime.datetime.now()
    print ('getall()',(starttime1 - starttime).seconds)
    print ('gettree()',(endtime - starttime1).seconds)
    print('ALL', (endtime - starttime).seconds)



if __name__=='__main__':
    main()
