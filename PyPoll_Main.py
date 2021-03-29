import os
import csv

election_csv = os.path.join("resources","election_data.csv")
output_path = os.path.join("resources", "election_data_output.csv")

total_votes = 0
candidates = 0
votes_winner = 0
candidate_list = []
winning_votes =["",0]
votes = {}

with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_reader)

    for row in csv_reader:
        total_votes +=1
        candidates =row[2]
        
        if candidates not in candidate_list:
            candidate_list.append(row[2])
            votes[row[2]] = 1
        else:
           votes[row[2]] = votes[row[2]]+1


#if total_votes > votes_winner:
    #winning_votes[1] = votes
    #winning_votes[0] = row[2]


with open (output_path, 'w',) as output_file:
    print("Election Results")
    output_file.write("Election Results")
    output_file.write("\n")
    print("-----------------------------------------------------")
    output_file.write("-----------------------------------------------------")
    print(f"Total Votes: {total_votes}")
    output_file.write("\n")
    output_file.write("Total Votes: " + str(total_votes))
    output_file.write("\n")
    print("-----------------------------------------------------")
    output_file.write("-----------------------------------------------------")
    output_file.write("\n")
    for people in votes:
        vote = votes.get(people)
        if vote > votes_winner:
            votes_winner = vote
            winning_votes[1] = vote
            winning_votes[0] = people
        print(f"{people}: {round(((vote/total_votes)*100))}% ({vote})")
        output_file.write(str(people) + str((vote/total_votes)*100).format(0.00) + " (" + str(vote) + ")")
        output_file.write("\n")
    print("-----------------------------------------------------")
    output_file.write("-----------------------------------------------------")
    output_file.write("\n")
    print(f"Winner: {winning_votes[0]}")
    output_file.write("Winner: " + str(winning_votes[0]))
    output_file.write("\n")
#with open (output_path, 'w',) as output_file:
    #output_file.write("Election Results")
    #output_file.write("\n")
    #output_file.write("-----------------------------------------------------")
    #output_file.write("\n")
    #output_file.write("Total Votes: " + str(total_votes))
    #output_file.write("\n")
    #output_file.write("-----------------------------------------------------")
    #output_file.write("\n")
    