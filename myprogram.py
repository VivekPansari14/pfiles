from MyMainPackage import my_main_script
from MyMainPackage.Subpackage import my_sub_script
from mymodule import my_func
#my_func()
#my_main_script.main_report()
#my_sub_script.sub_report()

#__name__ and __main__ usuage also
#two
import mymodule

print("top-level print inside of myprogram.py")

mymodule.func()

if __name__ == "__main__":
    print("myprogram.py is being run directly")
else:
    print("myprogram.py is being imported into another module")



#for more info read the repo from the course github repository
