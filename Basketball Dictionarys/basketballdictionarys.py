class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

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

# print(len(players))



# Create your Player instances here!
# player_jason = ???


kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team":"Phoenix Suns"}
# ... (class definition and large list of players here)
new_team = []
x = len(players)
for x in  range (0,x):
    # print(players[x])
    new_team.append(players[x])
    
# print(f"{new_team}")

print(new_team[0]['name'])

# Write your for loop here to populate the new_team variable with Player objects.
    


# player1= Player(kevin["name"],kevin["age"], kevin["position"],kevin["team"])
# player2 = Player(jayson["name"],jayson["age"], jayson["position"],jayson["team"])
# player3 = Player(kyrie["name"],kyrie["age"], kyrie["position"],kyrie["team"])
# print(player1.name)




# Update the constructor to accept a dictionary 
# with a single player's information instead of individual arguments for the attributes.
