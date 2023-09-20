"""
Showcasing Continue.
Continue is used to skip the remainder of a loop; we generally use this to not print segments
For example how many words into the sentence is fox?
"""

a_list = "the quick brown fox jumped over the lazy dog".split(" ")
#the above just gets the sentence as a a list
print(a_list)

words_in_count = 0
for word in a_list:
    words_in_count += 1
    #Uncomment this to debug
    #print("Loop is currently at: " + word)
    if word != "fox":
        continue
    #notice this won't get executed unless word equals fox
    print("Loop is past continue and currently at: " + word)
    print("fox was the " + str(words_in_count) + "th word in the sentence.")

"""
Same as above, but a while loop
"""

a_list = "the quick brown fox jumped over the lazy dog".split(" ")
#the above just gets the sentence as a a list
print(a_list)

words_in_count = 0
size_of_a_list = len(a_list)
index = 0
while (index < size_of_a_list):
    words_in_count = (index + 1)
    #Uncomment this to debug
    #print("Loop is currently at: " + a_list[index])
    if a_list[index] != "fox":
        index += 1
        continue
    index += 1
    print("Loop is past continue and currently at: " + a_list[index])
    print("fox was the " + str(words_in_count) + "th word in the sentence.")
