duration = 400153
days = duration // (60 * 60 * 24)
hours = duration // (60 * 60) - days * 24
minutes = duration // 60 - days * 24 * 60 - hours * 60
seconds = duration - days * 24 * 60 * 60 - hours * 60 * 60 - minutes * 60
if days > 0:
    print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
if (hours > 0) and (days == 0):
    print(hours, 'час', minutes, 'мин', seconds, 'сек')
if minutes > 0 and days == 0 and hours == 0:
    print(minutes, 'мин', seconds, 'сек')
if seconds >= 0 and days == 0 and hours == 0 and minutes == 0:
    print(seconds, 'сек')
