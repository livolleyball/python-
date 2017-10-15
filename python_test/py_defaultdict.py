# coding:utf8
import collections

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# defaultdict
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)
# Use dict and setdefault
g = {}
for k, v in s:
    g.setdefault(k, []).append(v)

# Use dict
e = {}
for k, v in s:
    e[k] = v


print(list(d.items()))

print(list(g.items()))

print(list(e.items()))

# s=[{"text":"a","item":{"id":1,"text":2}},{"text":"a","item":{"id":3,"text":4}}]
# d = collections.defaultdict(dict)
# e=[]
# for i in s:
#     print(i)
#     e.append(i)
#     for (k, v) in i.items():
#         print(k,v)
#
# print(list(d.items()))
