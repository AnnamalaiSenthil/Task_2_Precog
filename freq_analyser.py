freq_sum=[]
dist_count=[]
for _ in range(91):
    freq_sum.append(0)
    dist_count.append(0)
c=0

with open ("freqgood_mod_test.txt","r") as file:
    for line in file:
        lst=eval(line)
        for i in range(len(lst)):
            freq_sum[i]+=lst[i]
            if(lst[i]):
                dist_count[i]+=1
        c+=1

for i in range(91):
    if(dist_count[i]!=0):
        freq_sum[i]/=dist_count[i]

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
fh=open("Freq_store_good.txt","w")
for i in range(1,91):
    if(class_mapping.get(i,-1)!=-1 and freq_sum[i]!=0):
        print(class_mapping[i],": ",freq_sum[i])
        st=str(class_mapping[i])+": "+str(freq_sum[i])
        fh.write(st+"\n")
fh.close()