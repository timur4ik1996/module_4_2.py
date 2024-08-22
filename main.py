def test_function():
    def inner_faction():
        print("Я в области видимости функции test_function")
    inner_faction()


inner_faction()()





