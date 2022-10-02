import os

f = open("books_count.txt", "r")
books_count = int(f.read())
f.close()
def main():
    for i in range(books_count):
        book = str(i) + "book" + ".txt"
        os.remove(book)

if __name__ == '__main__':
    main()