import csv

#-----------------Reading CSV File By CSV Into List------------------
datex =[]
prolos =[]
with open('budget_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        datex.append(row['Date'])
        prolos.append(int(row['Profit/Losses']))


changes=[]

maxinc=0
maxdec=0

indexmax=0
indexmin=0

for p in range(len(prolos)):
    if p==(len(prolos)-1):
        break
    else:
        changep = prolos[p + 1] - prolos[p]
        if changep>maxinc:
            maxinc=changep
            indexmax=p+1
        else:
            pass
        if changep<maxdec:
            maxdec=changep
            indexmin=p+1
        else:
            pass
        changes.append(changep)
        pass


changesfinal=sum(changes)/len(changes)

maxincdate=datex[indexmax]
maxdecdate=datex[indexmin]


totalmonths=len(datex)
total=sum(prolos)
avgchange=round(changesfinal,2)

#-----------------Writing TO File------------------
f = open('Task1Result.txt', 'w')
print("Financial Analysis",file = f)
print("-------------------------------------",file = f)
print("Total Months: "+str(totalmonths),file = f)
print("Total: $"+str(total),file = f)
print("Average  Change: $"+str(avgchange),file = f)
print("Greatest Increase in Profits: "+str(maxincdate),"($"+str(maxinc)+")",file = f)
print("Greatest Decrease in Profits: "+str(maxdecdate),"($"+str(maxdec)+")",file = f)


#-----------------Writing TO Terminal------------------
print("Financial Analysis")
print("-------------------------------------")
print("Total Months: "+str(totalmonths))
print("Total: $"+str(total))
print("Average  Change: $"+str(avgchange))
print("Greatest Increase in Profits: "+str(maxincdate),"($"+str(maxinc)+")")
print("Greatest Decrease in Profits: "+str(maxdecdate),"($"+str(maxdec)+")")