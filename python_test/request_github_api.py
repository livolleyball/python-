# coding:utf8

import requests


headers = {"Authorization": "9c555ba8bccdda83e02320a8b142eac01c3ecc30"} # 前两行会在后面的代码中忽略掉不写

# user = requests.get('https://api.github.com/users/livolleyball', headers=headers).json()
commits = requests.get('https://api.github.com/repos/livolleyball/flask/commits').json()
print(commits[0]["commit"])