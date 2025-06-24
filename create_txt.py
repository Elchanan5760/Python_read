
try:
    with open("my_text.txt", "w") as my_text:
        my_text.write("Hello world\n"
                      "It's the first exercise in I/O\n"
                      "That mean it is number 1\n"
                      "Not 2\n"
                      "Not three\n"
                      "It is exciting\n"
                      "And i am all 4 it")
except IOError as ex:
    print("Error performing I/O operations on the file: ",ex)
