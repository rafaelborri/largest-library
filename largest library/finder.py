def main():
    f = open("books_count.txt", "r")
    books_count = int(f.read())
    f.close()
    while True:
        find = False
        string = input("What are you looking for?\n")
        for i in range(books_count):
            book = str(i) + "book" + ".txt"
            f = open(book, "r")
            if string in f.read():
                print("It is in book " + book)
                f.close()
                find = True
            else:
                f.close()
        if find == False:
            print("Nothing found in all library!")



if __name__ == '__main__':
    main()