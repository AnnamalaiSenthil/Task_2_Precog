# This file is to test a certain dataset and come up with a prediction whether the dataset is hateful or not.

fh_bad=open("Freq_store_bad.txt","r")
fh_good=open("Freq_store_good.txt","r")

dict_bad={}
dict_good={}

star_words=[]

for line in fh_bad:
    line=line[:-1]
    lst=line.split()
    lst[0]=lst[0][:-1]
    val=float(lst[-1])
    dict_bad[lst[0]]=val
    star_words.append(lst[0])

for line in fh_good:
    line=line[:-1]
    lst=line.split()
    lst[0]=lst[0][:-1]
    val=float(lst[-1])
    dict_good[lst[0]]=val
    if(lst[0] not in star_words):
        star_words.append(lst[0])

updated_list=[]
weights={}

for it in star_words:
    v=dict_good.get(it,-1)
    if(v==-1):
        weights[it]=-0.5
        continue
    v=dict_bad.get(it,-1)
    if(v==-1):
        weights[it]=0.5
        continue
    weights[it]=dict_good[it]-dict_bad[it]

with open("weights.txt","w") as f:
    for i in star_words:
        lst=[]
        lst.append(i)
        lst.append(weights[i])
        lst=str(lst)
        f.write(lst+"\n")

fh_good.close()
fh_bad.close()