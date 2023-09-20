#Sentinel value exit

sent_val = 'continue'
counter = 0
while sent_val != 'quit':
    counter += 1
    print('You are still in the loop!')
    print("you have been in the loop " + str(counter) + " times.")
    sent_val = input('Type "quit" to exit: ')

