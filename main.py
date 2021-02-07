# This is a sample Python script.
from libs.knihovna import print_hi
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




def return_43():
    print("--------------")
    print(dir())
    print("--------------")
    print(globals())
    print("--------------")
    print(locals())
    print("--------------")
    return 5


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyChaa')
    print(print_hi.__dir__())
    return_43()
    print(__name__)


exit(2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
