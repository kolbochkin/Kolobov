def main(argv):
    program, users_file, hobby_file, users_hobby_file = argv
    users = []
    hobby = []
    with open(users_file, 'r', encoding='utf-8') as file_1:
        for line in file_1:
            users.append(line.replace('\n', ''))
    with open(hobby_file, 'r', encoding='utf-8') as file_2:
        for line in file_2:
            hobby.append(line)
    if len(hobby) < len(users):
        for i in range(len(hobby), len(users)):
            hobby.append('None\n')
        users_hobby = ((users[i], ': ', hobby[i]) for i in range(0, len(users)))
    else:
        users_hobby = ((users[i], ': ', hobby[i]) for i in range(0, len(users)))
    with open(users_hobby_file, 'w', encoding='utf-8') as f:
        for item in users_hobby:
            f.writelines(item)

    return 0


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
