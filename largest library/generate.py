import random

f = open("books_count.txt", "r")
books_count = f.read()
f.close()
books_count = int(books_count)

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def main():
    for i in range(books_count):
        book_name = str(i) + "book" + ".txt"
        f = open(book_name, "w")
        in_book = ""
        for i in range(10000):
            letter = str(random.choice(letters))
            print(*letter)
            in_book += letter
        f.write(in_book)
        f.close()

if __name__ == '__main__':
    main()