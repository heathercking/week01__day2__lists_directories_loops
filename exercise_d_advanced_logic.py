# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
for number in numbers:
    if number % 2 == 0:
        print(number)

for number in numbers:
    if number % 2 == 0:
        print(number, end = " ")

# 2. Print the difference between the largest and smallest value:
maximum = max(numbers)
minimum = min(numbers)

print(maximum - minimum)


# 3. Print True if the list contains a 2 next to a 2 somewhere.
previous_number = 0

for number in numbers:
    if number == 2 and previous_number == 2:
        print(True)
    previous_number = number


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
#
#    numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]
#    so we want to add 1, 1

sum = 0
index = 0

index_of_6 = numbers.index(6)
print(index_of_6)
index_of_7 = numbers.index(7)
print(index_of_7)

for number in numbers:
    sum += number

# don't know (yet)! the thought the next exercise was easier than this one!... will have to come back to it. 
    
print(sum)



# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

#    numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

index = 0
sum = 0

while index < len(numbers):
    number = numbers[index]
    if number == 13:
        pass
        index += 2
    else:
        sum += number
        index += + 1

print(sum)








