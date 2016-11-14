def palindrome(string):
    return string[::-1].lower().replace(" ", "") == string.lower().replace(" ", "")


def main():
    print(palindrome("indulagorgaludni"))


if __name__ == '__main__':
    main()
