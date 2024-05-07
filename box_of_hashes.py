def line(x,y):
    
    if y =="":
        print (x*"*")
    else:
        print(x*y[0])
def box_of_hashes(height):
    while height>0:
        line(10,"#")
        height -=1
        
    # You should call function line here with proper parameters

    return
# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)