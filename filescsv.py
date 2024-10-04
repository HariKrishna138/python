import csv
data=[['eid','ename','esal'],
      [101,"ramu",30000],
      [102,"raju",35000],
      [103,"ravi",32500],
      [104,"rajesh",27500]
      ]
with open("pq.csv",'w',newline='') as q:
    wf=csv.writer(q)
    wf.writerows(data)
with open("pq.csv",'r') as q:
    rf=csv.reader(q)
    for row in rf:
        print(row)