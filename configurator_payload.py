import os
import sys
import json



config = {  
            "Cookie": "CHANGE ME!!",
            "Accept": "image/avif,image/webp,*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Sec-Fetch-Dest": "image",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0"
          }
with open("payload.json", "w") as fp:
    json.dump(config, fp)  # encode dict into JSON
print("Done writing payload")