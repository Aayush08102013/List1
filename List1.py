
# create a empty list
empty_list = []
print(empty_list)

# create a list of numbers:
number_list = [1, 2, 3]
print(number_list)

# Use * operator:
triples = [1,2,3]*3
print(triples)

# reverse the given list:
alist = [100, 200, 300, 400, 500, 600]
alist = alist[::-1]
print(alist, "\n")


# matching words:
# function to check wehter
# the first and last  words are the same
def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("list of words with the same first and last characters \n", lst)
    return ctr

count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])
print("Number of words with the same first and last letters:", count)


# playing with lists:
L = [ 4, 5, 1, 2, 9, 7, 10, 8]
print("The original list is:", L)
count = 0
for i in L: 
    count +=1
average = count/len(L)
print("sum", count)
print("average", average)
L.sort()
print("the smalest element is:", L[0])
print("the largest element is:", L[-1])


