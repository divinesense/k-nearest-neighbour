import csv
import math
from random import randint
def loadfile(file,trainingset,testset):
  with open(file,'r') as a:
    cs=csv.reader(a)
    li=list(cs)
    length=len(li)
    len1=int(length*0.67)
    len2=length-len1
    count = 0
    while count<len1:
      indx=randint(0,length-1)
      val=li[indx]
      for x in range(4):
        val[x]=val[x]
      if val not in trainingset:
        trainingset.append(val)
        count+=1
      else:
        pass  
    for line in li:
      for x in range(4):
        line[x]=line[x]
      if line not in trainingset:
        testset.append(line)
      else:
        pass
        
def calc_dist(train,test):
  dist=[]
  to_test=test[42]      #change index (0-50) here to test for different test instances 
  print "%"*12
  print to_test
  print "%"*12     
  leng=len(train)  
  for i in range(leng):#change to range(leng)
    distance=0
    for x in range(4):
      distance+=((float(to_test[x])-float(train[i][x]))**2)
    distance=math.sqrt(distance)
    dist.append([distance,train[i][4]])
  for i in range(leng-1):    
    for j in range(leng-1-i):
      if dist[j][0]>dist[j+1][0]:
        dist[j],dist[j+1]=dist[j+1],dist[j]
  return dist      
          

trainingset=[]
testset=[]
loadfile("flower.csv",trainingset,testset)
print trainingset
print '*'*12
print testset
dist=[]
dist=calc_dist(trainingset,testset)
print "eucledian distances are"
for i in range(len(dist)):
  print dist[i]
  
print len(dist)  
print "enter value of k...less than size but smaller (1-10)",
print "of training dataset which here is ",len(trainingset)
k=int(raw_input("k value "))
count_1=0 
count_2=0 
count_3=0
for i in range(k):
  if dist[i][1] == "Iris-setosa":
    count_1+=1
  elif dist[i][1] == "Iris-versicolor":
    count_2+=1
  elif dist[i][1] == "Iris-virginica":
    count_3+=1

print count_1
print count_2
print count_3
lis=[count_1,count_2,count_3]
max_val=max(lis)
if max_val == count_1:
  print "species is Iris-Setosa"
if max_val == count_2:
  print "species is Iris-Versicolor"
if max_val == count_3:
  print "species is Iris-Virginica"
