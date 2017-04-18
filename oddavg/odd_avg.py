# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases

def odd_average(numbers):
    new_list = []
    try:
        for number in range(len(numbers)):
            if numbers[number] % 2 != 0:
                new_list.append(numbers[number])
        return sum(new_list) / len(new_list)
    except ZeroDivisionError:
        return None
odd_average([2, 3, 4])