import string
import re
import sys

result = set()

sql_file = sys.argv[1]  # 脚本的路径
result_tb_name = sys.argv[2]  # 目标表

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'(ads|bi|dim|dm_risk|dm_tmp|dm_ugc|dmp|dw|dwa|dwd|dws|ods|push_data|rpt|upf)(\.)([a-zA-Z0-9_]+)')

try:
    openFile = open(sql_file, 'r', encoding='UTF-8')

    for line in openFile.readlines():
        match = pattern.findall(line)
        if match:
#             print(match)
            match_result=set(list(map(lambda x: "".join(x), match))) 
            result = result | (match_result)

    result.remove(result_tb_name)
except KeyError:
    print("Error: 目标表名有误,请检查")
else:
    print("目标表：", result_tb_name)
    print("-------------------------------------")
    print("依赖表：共 %d 个" % len(result))
    result_list = list(result)
    result_list.sort()
    for index, value in enumerate(result_list):
        print(index + 1, value)

finally:
    openFile.close()
