# This file is to test a certain dataset and come up with a prediction whether the dataset is hateful or not.

fh_bad=open("bad_text.txt","r")
fh_good=open("good_text.txt","r")

dict_bad={}
dict_good={}

star_words=[]

for line in fh_bad:
    line=line[:-1]
    lst=eval(line)
    for i in lst:
        i=str(i)
        print(i)
        if(dict_bad.get(i,-1)==-1):
            dict_bad[i]=1
        else:
            dict_bad[i]+=1
        if i not in star_words:
            star_words.append(i)
    

for line in fh_good:
    line=line[:-1]
    lst=eval(line)
    for i in lst:
        i=str(i)
        if(dict_good.get(i,-1)==-1):
            dict_good[i]=1
        else:
            dict_good[i]+=1
        if i not in star_words:
            star_words.append(i)

updated_list=[]
weights={}

for it in star_words:
    v=dict_good.get(it,-1)
    if(v==-1):
        weights[it]=dict_bad[it]*-1
        continue
    v=dict_bad.get(it,-1)
    if(v==-1):
        weights[it]=dict_good[it]
        continue
    weights[it]=dict_good[it]-dict_bad[it]

with open("text_weights.txt","w") as f:
    for i in star_words:
        lst=[]
        lst.append(i)
        lst.append(weights[i])
        lst=str(lst)
        f.write(lst+"\n")

fh_good.close()
fh_bad.close()