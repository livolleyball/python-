# coding:utf8
# 1.1 将list或者tuple分割成变量
p = (4, 5)
x, y = p
print("x:", x, "y:", y)

data = ["a", "b", "c", "d"]
A, B, C, D = data
print(A, B, C, D)

s = 'hello'
a, b, c, d, e = s
print(a, b, c, d, e)
# a,b,c,d,e,f=s
# ValueError: not enough values to unpack (expected 6, got 5)


data = [12.1, "b", "c", 5, (3, 4, 5)]
_, B, C, _, _ = data
print(B, C)


# 1.2 从任意长度的可迭代对象中获取元素
def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)


print(drop_first_last([1, 3, 4, 0]))

data = [12.1, "b", "c", 5, (3, 4, 5)]
A, B, *left = data
print(left)

records = [("foo", 1, 2), ("bar", "hello"), ("foo", 3, 4, 5)]


def do_foo(*args):
    print('foo', *args)


def do_bar(s):
    print("bar", s)


for tag, *args in records:
    if tag == "foo":
        do_foo(*args)
    elif tag == "bar":
        do_bar(*args)
