def spruce(size):
    
    print("a spruce!")
    for i in range(1,size+1):
     print(" " * (size - i) + "*" * (2* i - 1))
    print(" " * (size - 1)+ "*")
     
    return
if __name__ == "__main__":
    spruce(3)