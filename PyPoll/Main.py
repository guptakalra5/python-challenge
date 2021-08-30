import csv


#-----------------Reading CSV File By CSV Into List------------------
candidate =[]
with open('election_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        candidate.append(row['Candidate'])


#-----------------Making Dictionary Of All Possible Candidates------------------
cleancan= list(dict.fromkeys(candidate))
d = {}
for i in cleancan:
    d[i] = 0

#-----------------Counting Vote Of Each Candidate And Putting In List------------------
for v in candidate:
    val = d[v]
    d[v]=val+1


#-----------------Total Votes------------------
totalvotes=len(candidate)


#-----------------Winner------------------

winner=max(d, key=lambda key: d[key])

#-----------------Writing TO File------------------
f = open('Task2Result.txt', 'w')
print("Election Results",file = f)
print("-------------------------------------",file = f)
print("Total Votes: ", totalvotes,file = f)
print("-------------------------------------",file = f)
for i in cleancan:
  percentvote = (d[i] / totalvotes) * 100
  print(i+": "+str(round(percentvote,3))+'% '+'('+str(d[i])+')',file = f)
print("-------------------------------------",file = f)
print("Winner: ",winner,file = f)
print("-------------------------------------",file = f)


#-----------------Writing TO Terminal------------------
print("Election Results")
print("-------------------------------------")
print("Total Votes: ", totalvotes)
print("-------------------------------------")
for i in cleancan:
    percentvote = (d[i] / totalvotes) * 100
    print(i + ": " + str(round(percentvote, 3)) + '% ' + '(' + str(d[i]) + ')')
print("-------------------------------------")
print("Winner: ",winner)
print("-------------------------------------")