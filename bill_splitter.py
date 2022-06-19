#stage one,Enter the number of friends joining (including you):> 5
friends= int(input("Enter the number of every friend (including you):\n"))
if friends<=0:
   print ("No one is joining for the party")
else: 
    friendcome ={}
    print("enter their names:")
    for x in range(1,friends+1):
        name = input()
        friendcome.update({name:0})
    print(friendcome)
    
    
    
    
    
    
    
    #stage two ,Do you want to use the "Who is lucky?" feature? Write Yes/No: > No
    #No one is going to be lucky
    import random
print("Enter the number of friends joining (including you):")
friends = input()
if int(friends) == 0 or int(friends) < 0:
    print("No one is joining for the party")
else:
    friendcome = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for u in range(int(friends)):
        name = input()
        friendcome.update({ name: 0})
    print("Enter the total bill value:")
    onebill = input()
    name= list(friendcome.keys())
    tatolbill = float(float(onebill) / int(friends))
    for n in name:
        friendcome.update({n: round(tatolbill, 2)})
    print(friendcome)
    
    
    
    
    
    #stage three ,Enter the number of friends joining (including you):> 0
    import random
print("Enter the number of friends joining (including you):")
number_of_friend = input()
if int(number_of_friend) == 0 or int(number_of_friend) < 0:
    print("No one is joining for the party")
else:
    people_joining_party = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for a in range(int(number_of_friend)):
        names_of_people = input()
        people_joining_party.update({ names_of_friend: 0})
    print("Enter the total bill value:")
    bilamount = input()
    names_of_friends = list(people_joining_party.keys())
    bill_amount_for_every_one = float(float(bilamount) / int(number_of_friend))
    for b in names_of_friends:
        people_joining_party.update({b: round(bill_amount_for_every_one, 2)})
    print("Do you want to use the 'Who is lucky?' feature? Write Yes/No:")
    response = input()
    if(response.upper() == "YES"):
        random_lucky = random.choice(names_of_friends)
        print("{} is the lucky one!".format(random_lucky))
    else:
        print("No one is going to be lucky")

        
        
        #stage four , 
        import random
print("Enter the number of friends joining (including you):")
number_of_friends = input()
if int(number_of_friends) == 0 or int(number_of_friends) < 0:
    print()
    print("No one is joining for the party")
else:
    friends_joining_the_party = {}
    print("Enter the name of every friend (including you), each on a new line:")
	
    for a in range(int(number_of_friends)):
        names_of_friends = input()
        friends_joining_the_party.update({ names_of_friends: 0})  
    print("Enter the total bill value:")
    bill_amount = input()
    friends_names = list(friends_joining_the_party.keys())
    bill_amount_for_every_one = int(bill_amount) / int(number_of_friends)
    for b in friends_names:
        friends_joining_the_party.update({b: round(float(bill_amount_for_every_one), 2)})
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
	
    choice_answer = input()
    if choice_answer.upper() == "YES":
        lucky_friend = random.choice(friends_names)
        print("{} is lucky one!".format(lucky_friend))
        for c in friends_names:
            if c == lucky_friend:
                friends_joining_the_party.update({c: 0})
            else:
                bill_amount_for_every_one = float(bill_amount) / float((int(number_of_friends) - 1))
                friends_joining_the_party.update({c: round(float(bill_amount_for_every_one), 2)})
        print(friends_joining_the_party)
    else:
        print("No one is going to be lucky")
        print(friends_joining_the_party)
