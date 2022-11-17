# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

random_name = random.choice(names)
print(f"{random_name} is going to buy the meal today!")


# Teacher 

# num_itens = len(names)

# random_coice = random.randint(0, num_itens - 1)
# person_who_will_pay = names[random_coice]
# print(f"{person_who_will_pay} is going to buy the meal today!")
