import time

if __name__ == "__main__":
    list = []

    start = time.time()
    tiedosto = open("words_alpha.txt", "r", encoding="utf-8")
    while (True):
        rivi = tiedosto.readline()
        if (len(rivi) == 0):
            break
        list.append(rivi[:-1]) # add words
    tiedosto.close()
    end = time.time()
    print(f"Execution time to add the words: {end-start} seconds")

    start = time.time()
    tiedosto = open("kaikkisanat.txt", "r", encoding="utf-8")
    found = 0
    while (True):
        rivi = tiedosto.readline()
        if (len(rivi) == 0):
            break
        if (list.count(rivi[:-1]) > 0): # word in a list
            found += 1
    tiedosto.close()
    end = time.time()
    print(f"Found {found} words.")
    print(f"Execution time to find the common words: {end-start} seconds")
    