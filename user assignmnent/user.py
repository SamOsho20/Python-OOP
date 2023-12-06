class User:


    def __init__(self,first_name,last_name,email, age):
        #giving attributes different arguments 
        self.first_name = first_name
        self.last_name=last_name
        self.email=email
        self.age=age

        #default attributes 
        self.is_rewards_member =  False
        self.gold_card_points = 0
        

        # this method will print our instances the self arguments 
        # connect the info entered in the curly bracket down to our different  arguments entered for person 1 in line 22
    def display_info(self):
        print(f'Hello my first name is {self.first_name}')
        print(f'My last name is {self.last_name}')
        print(f'I am {self.age} years old')
        return self 
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        if self.gold_card_points >150:
            print("lets start spending")
        else:
            print("lets start saving ")
        print(f'it is  {self.is_rewards_member} i am a rewards member')
        print(f'and I have {self.gold_card_points} gold card points')
    # spend_points(self, amount) - have this method decrease the user's points by the amount specified.
        return self 
    def spend_points(self, amount):
        self.gold_card_points = 200 * (1 - amount)
        print(f'I just used my points so now I have {self.gold_card_points} gold card points')
        return self 

person1 = User("Sam","Osho","sameatspancakes@gmail.com", 23)

# print(display_info)
person1.display_info().enroll().spend_points(.20)
# person1.display_info()
# person1.enroll()
# person1.spend_points(.20)
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
