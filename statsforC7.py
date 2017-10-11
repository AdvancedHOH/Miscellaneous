import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=np.array([[641,652,693,688,677],
[631,646,689,682,670],
[633,634,685,678,665],
[631,638,684,676,641],
[623,629,671,665,654],
[621,626,677,667,653],
[620,625,671,661,648]])
index=[2013,2014,2015,2016,2017]
columns=['PKU','THU','FDU','SJTU','USTC','ZJU','NJU']
colors=['red','purple','orange','royalblue','cornflowerblue','darkblue','darkviolet']
df=pd.DataFrame(data.T,columns=columns,index=index)
year=np.array(range(2013,2018))
fig=plt.figure()
ax=fig.add_subplot(111)
i=0
for col in df.columns:
    ax.plot(year,df[col],'o-',color=colors[i],label=col)
    i+=1
ax.set_xlim(2012.8,2017.2)
ax.set_xticks(np.array(range(2013,2018)))
ax.set_xlabel('Year')
ax.set_ylabel('Control Line')
ax.set_title('Anhui Province')
fig.suptitle('CEE CONTROL LINE')
plt.legend(loc='upper left')
plt.show()
