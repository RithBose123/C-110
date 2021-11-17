import csv
import plotly.figure_factory as ff
import random
import statistics as st
import plotly.graph_objects as go
import pandas as pd

df=pd.read_csv("data.csv")
data=df["reading_time"].tolist()
def randomSetofMean(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)
    mean=st.mean(dataSet)
    return mean
def showFig(meanList):
    df=meanList
    mean=st.mean(df)
    fig=ff.create_distplot([df],["average"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()
def setup():
    meanList=[]
    for i in range(0,100):
        setOfMeans=randomSetofMean(30)
        meanList.append(setOfMeans)
    showFig(meanList)
    mean=st.mean(meanList)
    median=st.median(meanList)
    mode=st.mode(meanList)
    stdev=st.stdev(meanList)
    print(mode,median,mean,stdev)
setup()