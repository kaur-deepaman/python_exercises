def line(x,y):
    
    if y =="": #if string is empty
        print (x*"*")
    else:
        print(x*y[0])
    return
if __name__ == "__main__":
    line(5, "%")
    line (7,"LOL")
    line(3,"")