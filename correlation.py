import plotly.express as cs
import csv
import numpy as mp
def getdatasrc(datapath):
    iceCreamSale=[]
    Coldrinksale=[]
    with open(datapath) as f:
        csvreader=csv.DictReader(f)
        for row in csvreader:
            iceCreamSale.append(float(row["Temperature"]))
            Coldrinksale.append(float(row["Ice"]))
    return{"x":iceCreamSale,"y":Coldrinksale}
def findcorolation(datasrc):    
    correlation=mp.corrcoef(datasrc["x"],datasrc["y"])
    print("correlation between tempreture and ice cream sale",correlation[0,1])
def setup():
    datapath="D:\Daksh\WhiteHatJr\C98\C106\Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    datasrc=getdatasrc(datapath)
    findcorolation(datasrc)
setup()    




















