fname = input("enter file :")
def read_file(fname):
    if len(fname) < 1:
        fname = "clown.txt"

hand = open(fname)
count = dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    individual_words = lin.split()
    print(individual_words)
    for word in individual_words:
        count[word] = count.get(word,0) + 1

largest = -1
the_word = None
for key, value in count.items():
    print(key,value)
    if value > largest:
        largest = value
        the_word = key
print("the most common word is",the_word,"occured", largest ,"times")
