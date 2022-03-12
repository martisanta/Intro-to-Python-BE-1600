d = {}
f = open("books.txt", "r")
for line in f:
    L = line.split(',')
    book = L[0]
    author = L[1]
    book = book.strip()
    author = author.strip()
    if author not in d.keys():
        d[author] = [book]
    else:
        d[author].append(book)
for j,k in d.items():
    print(j,k)
