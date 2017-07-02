import operator


def file_opening(file_name):
    game_list = []
    with open(file_name, 'r') as inputfile:
        for line in inputfile:
            game_list.append(line.strip().split('\t'))
    return game_list


def get_most_played(file_name):
    sold_list = []
    title_list = []
    for game in file_opening(file_name):
            sold_list.append(float(game[1]))
            title_list.append(game[0])
    return title_list[(sold_list.index(max(sold_list)))]


def sum_sold(file_name):
    sold_list = []
    for game in file_opening(file_name):
        sold_list.append(float(game[1]))
    return sum(sold_list)


def get_selling_avg(file_name):
    sold_list = []
    for game in file_opening(file_name):
        sold_list.append(float(game[1]))
    return sum(sold_list)/len(sold_list)


def count_longest_title(file_name):
    title_list = []
    for game in file_opening(file_name):
        title_list.append(len(game[0]))
    return max(title_list)


def get_date_avg(file_name):
    year_list = []
    for game in file_opening(file_name):
        year_list.append(int(game[2]))
    return round(sum(year_list)/len(year_list))


def get_game(file_name, title):
    properties_list = []
    for game in file_opening(file_name):
        if title in game:
            for properties in game:
                properties_list.append(properties)
    properties_list[1] = float(properties_list[1])
    properties_list[2] = int(properties_list[2])
    return properties_list