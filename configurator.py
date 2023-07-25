import os
import sys
import json



config = {  
            "BookID": "something like UUID",
            "UserCookie": "gibberish",
            "GeneralURL": "https://urait.ru/viewer/page/",
            "DownalodInBrowser?": False,
            "LastPage": 1178,
          } #""" In LastPage you must put a number last page of the book"""
print('this is the config rn')
print(config)

print("Started writing dictionary to a file")
with open("config.json", "w") as fp:
    json.dump(config, fp)  # encode dict into JSON
print("Done writing GibeIriesh")