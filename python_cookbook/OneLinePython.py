#coding:utf8
# 在数字1～100中，遇见3的倍数输出fizz，遇见5的倍数输出buzz，遇见3和5的倍数输出fizzbuzz，其他输出本身数字

for i in range(1, 15):
    print("fizz"[i % 3 * 1:] + "buzz"[i % 5 * 2:] or i)

for i in range(1, 15):
    print("fizz"[i % 3 * 4:] + "buzz"[i % 5 * 4:] or i)
