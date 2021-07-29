import sys

def addnumber(a,b):
    return a+b

if __name__=="__main__":
    while True:
        try:
            x = int(input("Please enter a number!"))
            y = int(input("Please enter a another number!"))
            test = addnumber(x,y)
        except TypeError:
            print('TypeError Occured!! Check you inputs')
        except:
            print('Some Error Occured!! Check you inputs')
        else:
            print(f'All ran well result is {test}')
            break