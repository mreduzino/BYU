with open(r"C:\Users\marce\OneDrive\Documentos\Repository\BYU\CSE_110_Intro_to_Programming\W06\books.txt") as book_file:
    for line in book_file:
        line = line.strip()
        print(line)