
try:
    with open("my_text.txt","r") as  my_text:
        counter_event_line = 0
        counter_words = 0
        counter_letters = 0
        dicti = {}
        for row in my_text.readlines():
            words_in_line = row.split(" ")
            for word in words_in_line:
                word = word.lower()

                if word[len(word)-1] == "\n":
                    word = word[:len(word)-1]
                counter_letters+=len(word)
                if not word in dicti:
                    dicti[word] = 0
                dicti[word] += 1
                if not word.isnumeric():
                    counter_words += 1
            if len(words_in_line)%2 == 0:
                counter_event_line+=1
        print(max(dicti.values()))
        print(counter_event_line)
        print(counter_words)
        print(counter_letters)
except IOError as ex:
    print("Error performing I/O operations on the file: ",ex)