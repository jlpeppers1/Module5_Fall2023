"""
Showcasing Break.
Break is often used to stop parsing through a list a certain time.
For example how many words into the sentence is fox?
"""

a_list = "the quick brown fox jumped over the lazy dog".split(" ")
#the above just gets the sentence as a a list
print(a_list)

words_in_count = 0
for word in a_list:
    print("Loop is currently at: " + word)
    words_in_count += 1
    if word == "fox":
        break
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
    print("Loop is currently at: " + a_list[index])
    words_in_count = (index + 1)
    if a_list[index] == "fox":
        break
    index += 1
print("fox was the " + str(words_in_count) + "th word in the sentence.")
