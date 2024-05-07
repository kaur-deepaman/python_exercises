
def line(x,y):
    if y =="":
        print (x*"*")
    else:
        print(x*y[0])   
def square_of_hashes(size):
    # You should call function line here with proper parameters
    for i in range(size):
     line(size,"#") #line function called here
      
    return
# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
    print()
    square_of_hashes(3)
    
    
