# -*- coding: utf-8 -*-
import json
import redis  # pip install redis
import pymysql

def main():
    # 指定redis数据库信息
    rediscli = redis.StrictRedis(host='192.168.237.128', port = 6379, db = 0)
    # 指定mysql数据库
    mysqlcli = pymysql.connect(host='127.0.0.1', user='root', passwd='123455', db='lwt', charset='utf8')

    # 无限循环
    while True:
        source, data = rediscli.blpop(["zl:items"]) # 从redis里提取数据

        item = json.loads(data.decode('utf-8')) # 把 json转字典

        try:
            # 使用cursor()方法获取操作游标
            cur = mysqlcli.cursor()
            # sql = 'insert into zhilian_job(url,pname,location,company,smoney,emoney,ptype,person_num,tags,welfare,syear,eyear,time_pub,degree,desc_job,crawl_time,webname) ' \
            #       'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update time_pub=values(time_pub),smoney=VALUES(smoney),emoney=values(emoney)'
            # cur.execute(sql, (item["url"], item["pname"], item["location"], item["company"], item["smoney"], item["emoney"],item["ptype"], item["person_num"], item["tags"], item["welfare"], item["syear"], item["eyear"],item["time_pub"], item["degree"], item["desc_job"], item["crawl_time"], item["webname"]))

            sql = 'insert into zhilian_job(url,pname,location,company,ptype,tags,smoney,emoney,eyear,syear,degree,person_num,time_pub,desc_job,welfare,crawl_time,webname) ' \
                  'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update smoney=values(smoney),emoney=VALUES(emoney),person_num=values(person_num),crawl_time=values(crawl_time)'
            cur.execute(sql, (item["url"], item["pname"], item["location"], item["company"], item["ptype"], item["tags"], item["smoney"],item["emoney"], item["eyear"], item["syear"], item["degree"], item["person_num"], item["time_pub"],item["desc_job"], item["welfare"], item["crawl_time"],item["webname"]))

            # 提交sql事务
            mysqlcli.commit()
            #关闭本次操作
            cur.close()
            print ("插入 %s" % item['pname'])
        except pymysql.Error as e:
            mysqlcli.rollback()
            print(item)

            print ("插入错误" ,str(e))

if __name__ == '__main__':
    main()