import reports


def reports_answers_prints(file_name, title):
    print(reports.get_most_played(file_name))
    print(reports.sum_sold(file_name))
    print(reports.get_selling_avg(file_name))
    print(reports.count_longest_title(file_name))
    print(reports.get_date_avg(file_name))
    print(reports.get_game(file_name, title))
    return

reports_answers_prints("game_stat.txt", "Terraria")
