import re

def numbers_from_string(str):
    number_pattern = r'(zero|one|two|three|four|five|six|seven|eight|nine|\d)'
    numbers = re.findall(number_pattern, str)
    final_list = []

    word_to_number = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for num in numbers:
        if num.isdigit():
            final_list.append(num)
        else:
            final_list.append(word_to_number[num])

    if len(final_list) >= 1:
        return int("" + final_list[0] + final_list[-1])
    return 0



def main():
    total = 0
    # read in lines of file and loop through them
    with open("./inputs/1a.txt", 'r') as file:
        for line in file:
            total += numbers_from_string(line.strip())

    return total