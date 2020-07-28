import os
import csv

pollfile = os.path.join("..", "..", "pythonwork", "python-challenge", "pypoll", "Resources", "election_data.csv")


candidates = []
uniquecandidates = []

with open(pollfile) as polldata:
    pollreader = csv.reader(polldata, delimiter=',')
    #print(pollreader)
    
    csv_header = next(polldata)
    #print(f"Header: {csv_header}")
    
    for row in pollreader:
        #print(row[0])
        candidates.append(row[2])
        if row[2] not in uniquecandidates:
            uniquecandidates.append(row[2])


        
khanvotes = candidates.count("Khan")
correyvotes = candidates.count("Correy")
livotes = candidates.count("Li")
otooleyvotes = candidates.count("O'Tooley")
votecount = len(candidates)
khanpercent = khanvotes / votecount
correypercent = correyvotes / votecount
lipercent = livotes / votecount
otooleypercent = otooleyvotes / votecount


print(votecount)
print(uniquecandidates)
print(khanvotes)

print(f"Total Votes: {votecount} Khan: {khanvotes} Correy: {correyvotes} Li: {livotes} O'Tooley: {otooleyvotes}", file = open(r"../../pythonwork/python-challenge/pypoll/analysis/results.txt","w+"))