#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇

import random

random_coin = random.randint(0,1)
if random_coin == 0:
    random_coin = "Heads"
elif random_coin == 1:
    random_coin = "Tails"

print(random_coin)