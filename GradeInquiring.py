from bs4 import BeautifulSoup
import pandas as pd
from numpy import *
r = open(r'F:\\Python programs\成绩查询\成绩查询.txt', 'r')
soup = BeautifulSoup(r, 'lxml')
l = soup.find_all('td')
src = [a.get_text() for a in l]
src = src[20::]
time = src[0::7]
code = src[1::7]
name = [s[:-5] for s in src[3::7]]
credit = array([float(x) for x in src[4::7]])
grade = [s[3::][:-1] for s in src[5::7]]
gpa = array([float(s[3::][:-1]) for s in src[6::7]])
prototype = [[code[i], name[i], credit[i], grade[i], gpa[i]] for i in range(len(time))]
df = pd.DataFrame(prototype, index=time,columns=['code', 'name', 'credit', 'grade', 'gpa'])
effective = df[df['gpa'] > 0]
TotalCredit = effective['credit'].sum()
TotalWeightedGpa = sum(array(effective['credit'])*array(effective['gpa']))
AverageGpa = TotalWeightedGpa/TotalCredit
print('Total Credit:%.1f\nTotal Weighted Gpa:%.1f\nAverageGpa:%f' % (TotalCredit, TotalWeightedGpa, AverageGpa))