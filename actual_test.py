class_mapping = {
    1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane',
    6: 'bus', 7: 'train', 8: 'truck', 9: 'boat', 10: 'traffic light',
    11: 'fire hydrant', 13: 'stop sign', 14: 'parking meter', 15: 'bench',
    16: 'bird', 17: 'cat', 18: 'dog', 19: 'horse', 20: 'sheep',
    21: 'cow', 22: 'elephant', 23: 'bear', 24: 'zebra', 25: 'giraffe',
    27: 'backpack', 28: 'umbrella', 31: 'handbag', 32: 'tie', 33: 'suitcase',
    34: 'frisbee', 35: 'skis', 36: 'snowboard', 37: 'sports ball', 38: 'kite',
    39: 'baseball bat', 40: 'baseball glove', 41: 'skateboard', 42: 'surfboard',
    43: 'tennis racket', 44: 'bottle', 46: 'wine glass', 47: 'cup', 48: 'fork',
    49: 'knife', 50: 'spoon', 51: 'bowl', 52: 'banana', 53: 'apple',
    54: 'sandwich', 55: 'orange', 56: 'broccoli', 57: 'carrot', 58: 'hot dog',
    59: 'pizza', 60: 'donut', 61: 'cake', 62: 'chair', 63: 'couch',
    64: 'potted plant', 65: 'bed', 67: 'dining table', 70: 'toilet', 72: 'tv',
    73: 'laptop', 74: 'mouse', 75: 'remote', 76: 'keyboard', 77: 'cell phone',
    78: 'microwave', 79: 'oven', 80: 'toaster', 81: 'sink', 82: 'refrigerator',
    84: 'book', 85: 'clock', 86: 'vase', 87: 'scissors', 88: 'teddy bear',
    89: 'hair drier', 90: 'toothbrush'
    }

lst=[]

with open ("freqgood_mod_test.txt","r") as fh:
    for line in fh:
        lst.append(eval(line))

with open ("freqbad_mod_test.txt","r") as fh:
    for line in fh:
        lst.append(eval(line))

weights={}
with open ("weights.txt","r") as fh:
    for line in fh:
        l=eval(line)
        weights[l[0]]=float(l[1])
    
text_weights={}
with open ("text_weights.txt","r") as fh:
    for line in fh:
        l=eval(line)
        text_weights[l[0]]=float(l[1])
count=0
# print(lst)
with open ("image_text0.txt","r") as fh:
    c=0
    for line in fh:
        l=eval(line)
        x=0
        for i in l:
            x+=text_weights.get(i,0)
        y=0
        if(1):
            for j in range(91):
                if(lst[c][j]==0):
                    continue
                st=class_mapping.get(j,-1)
                if(st==-1):
                    continue
                lt=st.split()
                st=lt[0]
                if(len(lt)!=1):
                    st=st[:-1]
                # print(st)
                y+=weights.get(st,0)
        print(x,y)
        if(y>-0.05 and x > -90):
            if(c>250):
                count+=1
        else:
            if(c<=250):
                count+=1
        c+=1
print(count)