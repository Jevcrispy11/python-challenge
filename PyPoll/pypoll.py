import os
import csv
from collections import Counter

csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    data = list(csvreader)
    total_votes = len(data)
    
voters = []
for i in range(len(data)-1):
    voter_name = data[i][2]
    voters.append(voter_name)

vote_li = voters.count("Li")
vote_khan = voters.count("Khan")
vote_correy = voters.count("Correy")
vote_otooley = voters.count("O'Tooley")

li_percentage = (vote_li/total_votes)
khan_percentage = (vote_khan/total_votes)
correy_percentage = (vote_correy/total_votes)
otooley_percentage = (vote_otooley/total_votes)

Results = (
f"Small Town Vote Results \n"
f"-----------------------\n"
f"Total Votes: {total_votes} \n"
f"Li:{li_percentage:.0%} ({vote_li}) \n"
f"Khan:{khan_percentage:.0%} ({vote_khan}) \n"
f"Correy:{correy_percentage:.0%} ({vote_correy}) \n"
f"O'Tooley:{otooley_percentage:.0%} ({vote_otooley}) \n"
f"----------------------- \n"
f"Winner: Khan \n"
)

print(Results)

output = os.path.join('../PyPoll/Poll_analysis.txt')
with open(output, 'w') as file:
    txtwriter = file.write(Results)
