from collections import Counter
labels= [0,1,2,3,2,2,1,1,0]
c = Counter(labels)
print(c.get(1))