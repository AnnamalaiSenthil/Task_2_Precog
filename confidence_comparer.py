conf=[]
conf_mod=[]
with open ("conf.txt","r") as fh:
    for line in fh:
        conf.append(eval(line))
with open ("conf_mod.txt","r") as fh:
    for line in fh:
        conf_mod.append(eval(line))
mod_better_count=0
ini_better_count=0
mod=0
ini=0
mod_avg=0
ini_avg=0

for i in range(1000):
    if(len(conf[i])>len(conf_mod[i])):
        ini_better_count+=1
    elif(len(conf[i])<len(conf_mod[i])):
        mod_better_count+=1
    else:
        for k in range(len(conf[i])):
            if(conf[i][k]-conf_mod[i][k]>=0.02):
                ini+=1
                ini_avg+=conf[i][k]-conf_mod[i][k]
            elif(conf_mod[i][k]-conf[i][k]>=0.02):
                mod+=1
                mod_avg+=conf_mod[i][k]-conf[i][k]
with open ("Conf_stats_txt","w") as fh:
    st="Ini is better in "+ str(ini_better_count) + " cases with an avg factor of " + str(-1 if ini==0 else ini_avg/ini) + " " + str(ini)
    print(st)
    fh.write(st+"\n")
    st="Mod is better in "+ str(mod_better_count) + " cases with an avg factor of " + str(-1 if mod==0 else mod_avg/mod) + " " + str(mod)
    fh.write(st+"\n")
    print(st)
