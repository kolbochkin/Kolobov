example = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
message = ''
for i in example:
    if 48 <= ord(i[0]) <= 57:
        message += f'"{int(i):02d}" '
    elif ord(i[0]) == 43:
        message += f'"+{int(i):02d}" '
    else:
        message += i + ' '
print(message)