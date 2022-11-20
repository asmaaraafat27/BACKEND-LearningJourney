# The below code has one problem. It is trying to locate an item from the list that does not exist.
# Add exception handling to stop the error from being thrown
# Starter code
items = [1,2,3,4,5]
try:
    item = items[6]
    print(item)
except Exception as e:
    print("Item does not exist in the list -->", e )

# The below code is trying to do just that and will throw a ZeroDivisionError. 
# Add exception handling to return back 0 instead of allowing the error to be thrown.
# Starter code
def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, "Something went wrong!")
ans = divide_by(20, 0)
print(ans)

# The code below is looking for a file that does not exist. Add exception handling to catch this error.
# Starter code
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except Exception as e:
        print("Unable to locate file --> ",e)
