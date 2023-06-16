# membuka file yang ingin diubah
with open('nama_file.txt', 'r') as file:
    # membaca setiap baris dalam file
    for line in file:
        # memisahkan setiap kata dalam baris
        words = line.strip().split()
        # mencari kata yang diawali dengan "a" dan kata-kata setelahnya
        selected_words = set([f"{words[i]} {words[i+1]} {words[i+2]} {words[i+3]}\n" for i in range(len(words)-2) if words[i] == 'a' and words[i+1].isalpha()])
        # mencetak kata-kata yang dipilih
        print(''.join(selected_words))
