import string
import re
import sys
import datetime

update_time =datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
result = set()

sql_file = sys.argv[1]  # 脚本的路径
result_tb_name = sys.argv[2]  # 目标表

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'(ads|bi|dim|dm_risk|dm_tmp|dm_ugc|dmp|dw|dwa|dwd|dws|ods|push_data|rpt|upf)(\.)([a-zA-Z0-9_]+)')


try:
    openFile = open(sql_file, 'r', encoding='UTF-8')

    for line in openFile.readlines():
        print(line)
        if line.startswith("--"):
            pass
        else:
            match = pattern.findall(line)
            if match:
                # print(match)
                match_result=set(list(map(lambda x: "".join(x), match)))
                result = result | (match_result)

    result.remove(result_tb_name)
except KeyError:
    print("Error: 目标表名有误,请检查")
else:
    print("目标表：", result_tb_name)
    print("-------------------------------------")
    print('-- 更新日期',update_time)
    print("-- 依赖表：共 %d 个" % len(result))
    result_list = list(result)
    result_list.sort()
    for index, value in enumerate(result_list):
        print('-- ',index + 1, value)

finally:
    openFile.close()

    # -- ------------------------------------------------------------------------------
    # -- 业务描述：司机各应用渠道\分部门的注册转化日报表
    # dm_njbi.create_source_driver_dailyreport
    # -- 创建时间：20180503
    # 袁振清
    # 新创建
    # -- 修改时间：
    # -- 调度周期：日
    # -- 依赖数据：
    # -- dm_njbi.user_create_source
    # -- upf.upf_cargo_call_driver_di
    # --
    # -- ------------------------------------------------------------------------------
