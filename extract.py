

import json
from pathlib import Path
#obj=dict()


dirname = Path.cwd().joinpath('data')

filename='activesprints'
suffix ='.json'
file = (Path(dirname,filename).with_suffix(suffix))
pathname="/pathname/file.json"
def extract(key,value):
    if(type(value)==str):
        result = "{'"+key+"' : '"+value+"'}"
        print(result)
        #obj[key]=value
        return

    t = 0
    if(type(value)==list):
        for i in value:
            extract(key+"_"+str(t),i)
            t = t + 1
        return

    if(type(value)==dict):
        for i in value.keys():
            if key:
                key_i = key+"_"+i
            else:
                key_i = i
            extract(key_i,value[i])
        return

def compute():
    with open(file)as f:
        dat=f.read()
        json_data=json.loads(dat)
        d=dict(json_data)
        extract(None,d)
        #print(obj)

if __name__=="__main__":
    compute()