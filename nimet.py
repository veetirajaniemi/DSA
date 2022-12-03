# import urllib.request

# tiedosto = open("words2.txt", "w", encoding="utf-8")

# link = "https://raw.githubusercontent.com/hugovk/everyfinnishword/master/kaikkisanat.txt"
# file = urllib.request.urlopen(link)
# i = 1
# for line in file:
#     decoded_line = line.decode("utf-8")
    
#     word = str(decoded_line[:-1])
#     tiedosto.write(decoded_line)


# tiedosto = open("words.txt", "r")
# while (True):
#     rivi = tiedosto.readline()
#     if (len(rivi) == 0):
#         break
#     table.insert(rivi[:-1])
# tiedosto.close()

list = [0,1,2,3]
print(list.index(4))