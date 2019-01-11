# coding=utf-8
# 解决精度问题
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a+b)