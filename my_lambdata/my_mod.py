

# my_lambdata/my_mod.py


def enlarge(n):
    '''
    Param n is a number
    Function will enlarge the number
    '''
    return n * 100

# This code breaks our ability to import 'enlarge' from other files.

# y = int(input('Please choose a number'))
# print(y,enlarge(y))


if __name__ == "__main__":
    print("HELLO")
    y = int(input('Please choose a number'))
    print(y,enlarge(y))
