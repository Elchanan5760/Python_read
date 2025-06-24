try:
    with open("my_text.txt","r") as my_text:

        for row in my_text.readlines():
            cond = False
            for c in row:
                if c.isdigit():
                    cond = True
            if cond:
                print(row,end="")

except IOError as ex:
    print("Error performing I/O operations on the file: ",ex)