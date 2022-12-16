import time

class List:
    def __init__(self):
        self.list = []
        self.len = 0

    def insert(self, val):
        self.list.append(val)
        self.len = self.len + 1

    def search(self, val):
        if (self.list.count(val) > 0):
            return True
        return False

    def print(self):
        for i in range(0, self.len):
            print(self.list[i])


if __name__ == "__main__":
    start = time.time()
    list = List()
    end = time.time()
    print(f"Execution time to initialize list: {end-start} seconds")

    start = time.time()
    tiedosto = open("words_alpha.txt", "r")
    while (True):
        rivi = tiedosto.readline()
        if (len(rivi) == 0):
            break
        list.insert(rivi[:-1])
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
        if (list.search(rivi[:-1]) == True):
            found = found + 1
    tiedosto.close()
    print(f"Found {found} words.")
    end = time.time()
    print(f"Execution time to find the common words: {end-start} seconds")
    