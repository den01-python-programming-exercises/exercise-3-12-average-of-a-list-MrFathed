def main():
    #write your code below this line
    numbers = []

    while True:
        number = int(input())

        if number == -1:
            break

        numbers.append(number)

    average = sum(numbers) / len(numbers)
    print("Average: " + str(average))

        

def sum(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

if __name__ == '__main__':
    main()
