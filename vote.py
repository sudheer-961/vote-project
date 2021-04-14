nom_1 = input("enter nominee 1 name :")
nom_2 = input("enter nominee 2 name:")
nom_3 = input("enter nominee 3 name:")
nom_1_votes = 0
nom_2_votes = 0
nom_3_votes = 0
votes_id = [1,2,3,4,5,6,7,8,9]
nbr_of_voters = len(votes_id)
while True:
    if votes_id == []:
        print("voting session over")
        if nom_1_votes>nom_2_votes and nom_1_votes>nom_3_votes:
            percent = (nom_1_votes/nbr_of_voters)*100
            print(nom_1,"has won with",percent,"%votes")
            break
    
        elif nom_2_votes>nom_1_votes and nom_2_votes>nom_3_votes:
                 percent = (nom_2_votes/nbr_of_voters)*100
                 print(nom_2,"has won with",percent,"%votes")
                 break
        else:
            percent = (nom_3_votes/nbr_of_voters)*100
            print(nom_3,"has won with",percent,"%votes")
            break
    else:    
        voter = int(input("enter your voter id no:"))
        if voter in votes_id:
            print("you are a voter")
            votes_id.remove(voter)
            vote = int(input("enter your vote 1 or 2 or 3:"))
            if vote==1:
                nom_1_votes+=1
                print("thank you for casting vote")
            elif vote==2:
                nom_2_votes+=1
                print("thank you for casting vote")
            else:
                nom_3_votes+=1
                print("thank you for casting vote")
    
        else:
            print("you are not a voter or your vote already voted")
