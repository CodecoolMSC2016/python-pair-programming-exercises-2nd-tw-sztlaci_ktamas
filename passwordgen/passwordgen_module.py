import string
from random import randint

WORD_LIST = ["kormány", "év", "ember", "törvény", "úr", "szó", "forint", "során", "ország", "elnök", "miniszter",
             "bizottság", "országgyűlés", "képviselő", "emberek", "semmi", "idő", "világ", "érdek", "év", "további"]


def passwordgen(strength="strong", length=8, wlist=None):
    PASS_STRENGTH = ("weak", "medium", "strong")
    password = ""
    if strength == PASS_STRENGTH[0] and wlist:
        for i in range(2):
            rand = randint(0, len(wlist) - 1)
            password += str(wlist[rand])
    elif strength == PASS_STRENGTH[1] or strength == PASS_STRENGTH[2]:
        passPool = ""
        if strength == PASS_STRENGTH[1]:
            passPool = string.ascii_lowercase[:]
        elif strength == PASS_STRENGTH[2]:
            passPool = string.ascii_lowercase[:] + string.ascii_uppercase[:] + string.digits[:] + "!@#$%^&*()?"

        for i in range(length):
            rand = randint(0, len(passPool) - 1)
            password += passPool[rand]
            rand = randint(0, 10)
    return password.strip()


def main():
    print(passwordgen("strong", wlist=WORD_LIST))
    return


if __name__ == '__main__':
    main()

# string.ascii_lowercase
# string.ascii_uppercase
# string.digits
# string.punctuation
