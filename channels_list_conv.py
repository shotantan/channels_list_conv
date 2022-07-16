import json
import requests
import re

IP="192.168.0.15"
PORT=40772
URL="http://"+IP+":"+str(PORT)+"/api/channels"
FILE="all.m3u8"

try:
  list = json.loads(requests.get(URL).text)
except:
  print("Error")
  exit(-1)

out = []
for item in list:
  if "services" in item:
    for s in item["services"]:
      if item["type"] == "GR":
        o = re.sub(r"[\u3000 \t]", "", s["name"])
        out.append("#EXTINF:-1,地上波 - %s"%(o))
      else:
        o = re.sub(r"[\u3000 \t]", "", s["name"])
        out.append("#EXTINF:-1,%s - %s"%(item["type"], o))
      out.append("%s/%s/%s/services/%s/stream/"%(URL, item["type"], item["channel"], s["serviceId"]))
  else:
    o = re.sub(r"[\u3000 \t]", "", item["name"])
    out.append("#EXTINF:-1,地上波 - %s"%(o))
    out.append("%s/%s/%s/stream/"%(URL, item["type"], item["channel"]))

out = ("\n").join(out)
with open(FILE, 'w') as fp:
  fp.write(out)
