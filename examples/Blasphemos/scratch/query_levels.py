import json
d = json.load(open("blasnesmous.json"))
for v in d["levels"]:
    print("name=%s  width=%d  height=%d" % (v["name"], v["width"], v["height"]))
