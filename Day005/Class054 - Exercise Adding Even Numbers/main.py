#Write your code below this row 👇

total_even = 0
for even in range(1, 101):
    if even % 2 == 0:
        total_even += even

print(total_even)

# Teacher
# for even in range(2, 101, 2):
#     total_even += even
# print(total_even)