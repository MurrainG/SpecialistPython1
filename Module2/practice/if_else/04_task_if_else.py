number = int(input())
if number % 3 == 0 and number % 5 == 0:
    print("FooBar")
if number % 3 == 0 and number % 5 != 0:
    print("Foo")
if number % 3 != 0 and number % 5 == 0:
    print("Bar")
