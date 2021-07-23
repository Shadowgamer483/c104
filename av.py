import plotly.express as cs
import csv
import numpy as mp
def getdatasrc(datapath):
    Marks=[]
    Days=[]
    with open(datapath) as f:
        csvreader=csv.DictReader(f)
        for row in csvreader:
            Marks.append(float(row["Marks"]))
            Days.append(float(row["Days"]))
    return{"x":Marks,"y":Days}
def findcorolation(datasrc):    
    correlation=mp.corrcoef(datasrc["x"],datasrc["y"])
    print("correlation between Size and average time spent",correlation[0,1])
def setup():
    datapath="D:\Daksh\WhiteHatJr\C98\C106\Student Marks vs Days Present.csv"
    datasrc=getdatasrc(datapath)
    findcorolation(datasrc)
setup()    




















 