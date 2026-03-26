# Fizz buzz

def fizz_buzz(input):
    input = int(input)
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"


print(fizz_buzz(10))  # Output: "Fizz"
