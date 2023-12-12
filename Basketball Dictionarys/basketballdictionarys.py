# # Challenge 1: Update the constructor to accept 
# a dictionary (player) as an argument and
# set the attributes using the dictionary 



class Player:
    def __init__(self,dict):
        self.name = dict ["name"]
        self.age = dict["age"]
        self.position = dict["position"]
        self.team = dict["team"]
        
    @classmethod
    def get_team(cls,team_list):
    # cls stands for Players, so when you say cls(x) you are asking for all the items in players in a list 
    # the only diffrence between a self method and @classmethod is that it gives you access to 
    # all the methods in the class and constructor. so if we had a method called subtract player we could place this class method 
    # under it to call it
    # self methods are specific while @class methods are broad
        new_player = []
        for x in team_list:
            # print(x)
            # cls(x)
            new_player.append(cls(x))
            #cls = Player () and values in dict = x
        print(new_player[0].name)
        return new_player
    #  Ninja Bonus: Add an @class method called get_team(cls, team_list) that, 
    # given a list of dictionaries 
    # populates and returns a new list of Player objects
jaylen =Player ({"name": "Jaylen Brown", "age":26, "position": "small forward", "team":"Celtics"})
print(jaylen.name)

players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
]
list_players = Player.get_team(players)
list_players.append(jaylen)
print(list_players[5].name)


# Complete challenge 2: Create 3 instances of 
# the Player class using the given dictionaries
kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jayson = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
    

# Complete challenge 3:
# Populate a new list with Player instances from the list of player
# Write your for loop that will populate the these 
# Player objects into a new list called new_team
players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
]
# 

kevin =Player ({"name": "Kevin Durant", "age":34, "position": "small forward", "team":"Phoenix Suns"})
# new_team = []
print(kevin)
# # Write your for loop here to populate the new_team variable with Player objects.
# # x = len(players)
# # in this for loop line we are saying for the var x in the range of 0 to the 
# # length of players let x track the amount of items in players 
# for x in  range (0,len(players)):
#     # we are printing the amount of items in the index from its start (0) to its end (len(players)
#     # print(players[x])
#     # so the loop will run through the numbers 0 to 
#     # len(players) and print the items within each number of the index
#     new_team.append(players[x])
    
# print(f"{new_team}")




# @classmethod 
# def get_team(cls, team_list):
#     cls.players['name'][0]='sam'
#     return
    # Ninja Bonus: Add an @class method called get_team(cls, team_list) that, 
    # given a list of dictionaries 
    # populates and returns a new list of Player objects
    # i am struggling completing the ninja bonus, I  have created a class method that
    #  takes a list and set it equal to a key value in my list changing the name in the index of 0 to sam but it will not set 


# get_team(players)
# print(new_team[0]['name'])

# Write your for loop here to populate the new_team variable with Player objects.
    


# player1= Player(kevin["name"],kevin["age"], kevin["position"],kevin["team"])
# player2 = Player(jayson["name"],jayson["age"], jayson["position"],jayson["team"])
# player3 = Player(kyrie["name"],kyrie["age"], kyrie["position"],kyrie["team"])
# print(player1.name)




# Update the constructor to accept a dictionary 
# with a single player's information instead of individual arguments for the attributes.
