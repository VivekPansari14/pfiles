
def my_func():
    print("I m in module.py")

#__name__ and __main__ usuage also
#one
def func():
    print("func() ran in mymodule.py")

print("top-level print inside of mymodule.py")

if __name__ == "__main__":
    print("mymodule.py is being run directly")
else:
    print("mymodule.py is being imported into another module")