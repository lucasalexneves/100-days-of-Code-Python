# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# print(type(height))
# print(type(weight))

float_height = float(height)
float_weight = float(weight)

bmi = float_weight / float_height ** 2

int_bmi = int(bmi)
print(int_bmi)


# Teacher's resolution
# bmi = int(weight) / float(height) ** 2
# bmi_as_int = int(bmi)
# print(bmi_as_int)