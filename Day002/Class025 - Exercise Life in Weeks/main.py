# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_int = int(age)

# final_age = 90
# days_in_year = 365
# weeks_in_year = 52
# months_in_year = 12

rest_age = 90 - age_int
rest_days = rest_age * 365
rest_weeks = rest_age * 52
rest_months = rest_age * 12

# print(f"You have {rest_age} left")
print(f"You have {rest_days} days, {rest_weeks} weeks, and {rest_months} months left.")


