
def line(x,y):
    
    if y =="":
        print (x*"*")
    else:
        print(x*y[0])
def square(size, character):
    # You should call function line here with proper parameters
    for i in range(size):
     line(size,character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "*")
    print()
    square(3,"o")