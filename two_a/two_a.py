import re

LEGEND = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def game_possible(str):
    game_id = re.findall(r'(\d+)', str)[0]
    instances = str.strip().split(':')[1].split(';')
    instance_dict = {'red': 0, 'blue': 0, 'green': 0}
    possible = True
    for instance in instances:
        color_list = instance.split(',')
        for group in color_list:
            parts = group.strip().split()
            instance_dict[parts[1]] =  int(parts[0])
        possible = instance_possible(instance_dict)
        if (not possible):
            return 0
    return int(game_id)
    
def instance_possible(instance):
    # compare game to source to see if game exceeds the source
    if (instance['red'] > LEGEND['red'] or instance['green'] > LEGEND['green'] or instance['blue'] > LEGEND['blue']):
        return False
    return True
    

def main():
    total = 0
    # read in lines of file and loop through them
    with open("./inputs/2a.txt", 'r') as file:
        for line in file:
            val = game_possible(line.strip())
            total += val

    return total

print(main())