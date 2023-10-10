from json import load

path="C:\\Users\\DIGI HUB\\OneDrive\\Desktop\\Python\\read_jason\\data.json"

with open(path) as f:
    records=load(f)

fw_names=[f.get("name") for f in records]
print(fw_names)

top_fw=max(records,key=lambda d:d.get("rating"))
print(top_fw)


# print(len(recordz))

py_fv=[r.get("name") for r in records if r.get("language")=="python"]

# print(be_fw)

be_fw=[r.get("name") for r in records if r.get("side")=="backend"]

# top fw

top_fw=max(records,key=lambda d:d.get("rating"))
print(top_fw)

