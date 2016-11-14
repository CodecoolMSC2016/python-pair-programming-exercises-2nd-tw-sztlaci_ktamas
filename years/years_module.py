import datetime




def years(age):
    return (int(datetime.datetime.now().year) - int(age)+100)


def main():
    name = input("Type your name: ")
    age = int(input(str(name) + "'s age: "))
    if age == 100:
        print (str(name) + " is 100 years old")
    elif age > 100:
        print(str(name) + " was 100 in " + str(years(age)))
    else:
        print(str(name) + " will be 100 in " + str(years(age)))


if __name__ == '__main__':
    main()
