#You create the variable name, and pass a  list in
any_list = [1,2,3,4]
for you_name_this in any_list:
    print("Each item in the list, one at a time, is: " + str(you_name_this))

last_names = ['smith', 'cyrus', 'cruz', 'chan', 'monroe', 'presley']

for index_in_list in range(0,len(last_names)):
    print('Index is ' + str(index_in_list))
    #last_names[0] = last_names[0].capitalize()
    last_names[index_in_list] = last_names[index_in_list].capitalize()
print("Now it should be captialized: ")
print(last_names)

#Sum the values from 1 to 100
one_to_one_hundred = range(1,101)
sum_to_one_hundred = 0
for number_in_list in one_to_one_hundred:
    #Note this is the same as
    #sum_to_one_hundred = sum_to_one_hundred + number_in_list
    sum_to_one_hundred += number_in_list
print('The sum of 1 to 100 is: ' + str(sum_to_one_hundred))
