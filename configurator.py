import os
import sys
import json



config = {  
            "BookID": "DC4D63AD-7BF9-4DCF-AF77-9F3EB6B9CF0D",
            "GeneralURL": "https://urait.ru/viewer/page/",
            "DownalodFromBrowser?": False,
            "LastPage": 336,
          } #""" In LastPage you must put a number last page of the book"""
            #and remember you should have a cookie for user that have access for book you want to download
print('this is the config rn')
print(config)

print("Started writing dictionary to a file")
with open("config.json", "w") as fp:
    json.dump(config, fp)  # encode dict into JSON
print("Done writing GibeIriesh")