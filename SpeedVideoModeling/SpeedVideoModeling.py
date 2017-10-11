import pandas as pd
import matplotlib.pyplot as plt
from numpy import *
from scipy import optimize
df=pd.read_excel(r'F:\Python programs\SpeedVideoModeling\SpeedVideoDataforModeling.xlsx')
global x,y,x0
x=array(df['播放阶段平均速率(kbps)'])
y=array(df['播放时长(ms)'])
fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(x,y,'.')
plt.show()
def f(z):
    s=0
    for i in range(len(x)):
        if(x[i]<x0):
            s=s+(y[i]-z[0]-z[1]*(x[i]-x0))**2
        else:
            s=s+(y[i]-z[0]-z[2]*(x[i]-x0))**2
    return s
answer=[]
result=[]
for i in range(10):
    x0=3000+i*100
    res=optimize.minimize(f,[28000,10,0],method='powell',options={'disp':True})
    answer.append(res.x)
    result.append(res.fun)
print(answer)
print(result)