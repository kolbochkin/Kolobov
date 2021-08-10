def translate_number(number):
    note = {"one": "один", "One": "Один",
            "two": "два", "Two": "Два",
            "three": "три", "Three": "Три",
            "four": "четыре", "Four": "Четыре",
            "five": "пять", "Five": "Пять",
            "six": "шесть", "Six": "Шесть",
            "seven": "семь", "Seven": "Семь",
            "eight": "восемь", "Eight": "Восемь",
            "nine": "девять", "Nine": "Девять",
            "ten": "десять", "Ten": "Десять"}
    print(note.get(number))


translate_number("ten")
translate_number("Six")
translate_number("eleven")
translate_number("twelve")
