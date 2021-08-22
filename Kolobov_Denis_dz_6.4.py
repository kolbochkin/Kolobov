users = []
hobby = []
with open('users.csv', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        users.append(line.replace('\n', ''))
with open('hobby.csv', 'r', encoding='utf-8') as file_2:
    for line in file_2:
        hobby.append(line)
if len(hobby) < len(users):
    for i in range(len(hobby), len(users)):
        hobby.append('None\n')
    users_hobby = ((users[i], ': ', hobby[i]) for i in range(0, len(users)))
else:
    users_hobby = ((users[i], ': ', hobby[i]) for i in range(0, len(users)))
with open('users_hobby.txt', 'w', encoding='utf-8') as f:
    for item in users_hobby:
        f.writelines(item)
