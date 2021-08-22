remote_adr = []
n = 0
z = 0
with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        request = line.replace('"', '').replace('-', '').replace('  ', '').split(' ')
        remote_adr.append(request[0])
for i in remote_adr:
    if remote_adr.count(i) > n:
        n = remote_adr.count(i)
        z = i
print(z)
print(n)
