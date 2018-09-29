import string
import re
import sys
result = set()

sql_file = sys.argv[1]          #脚本的路径
result_tb_name= sys.argv[2]    # 目标表

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'(ods|dw|rpt|upf|dmp|dws|dwd|dm_njbi|dm_risk|push_data|dim|dm_algo|dwa|ads|bi|dm_prod|dm_crm|dm_tmp)(\.)([a-zA-Z0-9_]+)')

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
    print("依赖表：",result)

finally:
    openFile.close()