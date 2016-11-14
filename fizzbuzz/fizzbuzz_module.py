def create_numbers():
    numbers = []

    for i in range(0, 100):
        numbers.append(int(i + 1))

    return numbers


def fizzbuzz(number):
    fizz_buzz = ""

    if number % 3 == 0:
        fizz_buzz += "Fizz"
    if number % 5 == 0:
        fizz_buzz += "Buzz"
    if not fizz_buzz:
        fizz_buzz = number
    return fizz_buzz


def main():
    nums = create_numbers()

    for num in nums:
        n = fizzbuzz(num)
        print(n)

if __name__ == '__main__':
    main()
