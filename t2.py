import json
l=[]
with open ("./data/train.jsonl","r") as fh:
    for line in fh:
        data_dict = json.loads(line)
        l.append(data_dict)
l.sort(key=lambda x: x['label'])
with open ("./data/train2.jsonl","w") as fh:
    for line in l:
        fh.write(json.dumps(line)+"\n")