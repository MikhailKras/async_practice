import time


def func1(x):
    print(x ** 2)
    time.sleep(3)
    print('func1 ended')


def func2(x):
    print(x ** 0.5)
    time.sleep(3)
    print('func2 ended')


def main():
    func1(4)
    func2(4)


print(type(func1))


main()


print(type(func1(4)))

