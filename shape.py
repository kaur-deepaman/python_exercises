def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)
def shape(len,char,height,character):
    # You should call function line here with proper parameters
    for i in range(len+1):
     line(i,char)
    while height>0:
        line(len,character)
        height-=1
    return
if __name__ == "__main__":
    shape(5, "x", 2, "o")