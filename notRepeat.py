with open("input.txt", "r") as file:
    # membaca teks dari file
    text = file.read()

    # memisahkan setiap kata
    words = text.split()

    # menyimpan setiap kata yang unik ke dalam list
    unique_words = list(set([word.lower() for word in text.split()]))

    # menyimpan setiap kata yang unik ke dalam file baru
    with open("unique_words.txt", "w") as new_file:
        for word in unique_words:
            new_file.write(word + "\n")
