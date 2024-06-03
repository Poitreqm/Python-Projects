# The FizzBuzz Task
# Write the fizzbuzz test function, which returns an array that is formed according to the following rules:
# Numbers from 1 to 100 are processed
# If the number is a multiple of three, then enter the word Fizz in the array
# If the number is a multiple of five, then enter the word Buzz in the array
# If the number is a multiple of both three and five, then enter the word FizzBuzz in the array
# If the number is not a multiple of any of these numbers, then you just need to put the number itself in the array
# Note: Set the array of numbers to process directly inside the function - the function does not accept arguments.


fizzbuzztest = []

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        fizzbuzztest.append("FizzBuzz")
    elif i % 3 == 0:
        fizzbuzztest.append("Fizz")
    elif i % 5 == 0:
        fizzbuzztest.append("Buzz")

    else:
        fizzbuzztest.append(i)

print(fizzbuzztest)
