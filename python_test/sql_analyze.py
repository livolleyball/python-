import string
import re
import sys
result = set()

sql_file = sys.argv[1]          #脚本的路径
result_tb_name= sys.argv[2]    # 目标表

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'(ads|bi|dim|dm_risk|dm_tmp|dm_ugc|dmp|dw|dwa|dwd|dws|ods|push_data|rpt|upf)(\.)([a-zA-Z0-9_]+)')

try:
    openFile = open(sql_file, 'r', encoding='UTF-8')

    for line in openFile.readlines():
        # print(line)
        match = pattern.search(line)
        if match:
            match_result=match.group()
            result.add(match_result)

    result.remove(result_tb_name)
except KeyError:
    print("Error: 目标表名有误,请检查")
else:
    print("目标表：",result_tb_name)
    print("-------------------------------------")
    print("依赖表：共 %d 个",len(result))
    for index,value in enumerate(list(result)):
        print(index+1,value)

finally:
    openFile.close()
