def test_function():
    def inner_faction():
        print("Я в области видимости функции test_function")
    inner_faction()

inner_faction() #NameError: name 'inner_faction' is not defined

test_function()






