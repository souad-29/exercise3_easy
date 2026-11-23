def get_first_last_element(numbers):
    if len(numbers) == 0:
        return []

    result = [numbers[0], numbers[-1]]
    return result

# ask the user how many numbers they want to enter in the list
while True:
    try:
        count = int(input("How many numbers do you want to enter in a list?"))
        if count < 1:
            print("Please enter at least 1 number.")
        else:
            break
    except ValueError:
        print("Please enter a valid integer.")

#collecting the numbers from the user
numbers = []

for i in range(count):
    while True:
        try:
            number = int(input(f"Enter number {i +1}: "))
            numbers.append(number)
            break
        except ValueError:
            print("Please enter a valid ineger.")

#using the function above to get and display the first and last elements
final_list = get_first_last_element(numbers)

print("the orignal list:", numbers)
print("the new list:", final_list)