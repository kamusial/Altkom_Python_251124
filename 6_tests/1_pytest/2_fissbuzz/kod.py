def fizzbuzz(number):
    if not isinstance(number, str) and number > 0:
        number = int(number)
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        elif number % 3 == 0:
            return 'Fizz'
        elif number % 5 == 0:
            return 'Buzz'
        return str(number)
    return None