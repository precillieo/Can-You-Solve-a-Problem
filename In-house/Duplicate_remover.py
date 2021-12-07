# ask for the user to enter a list of strings (one per line)
# and then print a new list with duplicate items removed

user_list = []

while True:
    user_input = input('Enter a list of strings (one per line): ')
    if user_input == '':
        break
    user_list.append(user_input)

new_list = []

for item in user_list:
    if item not in new_list:
        new_list.append(item)

print(new_list)