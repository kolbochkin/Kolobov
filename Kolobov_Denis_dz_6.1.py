with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        request = line.replace('"', '').replace('-', '').replace('  ', '').split(' ')
        print(tuple([request[0], request[3], request[4]]))
