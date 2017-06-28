import reports


def export_answers_from_reports(file_name, title, year, genre, export_file="reports_export.txt"):
    file = open(export_file, "w")
    file.write("Number of games in the file: {}\n".format(reports.count_games(file_name)))
    file.write("The latest game is: {}\n".format(reports.get_latest(file_name)))
    file.write("The number of games we have by the given genre: {}\n".format(reports.count_by_genre(file_name, genre))) 
    file.write("The line number of the given game is: {}\n".format(reports.get_line_number_by_title(file_name, title)))
    file.write("Alphabetical ordered list of the titles is: {}\n".format(reports.sort_abc(file_name)))
    file.write("Genres are: {}\n".format(reports.get_genres(file_name)))
    file.write("There is a game from a given year: {}\n".format(reports.decide(file_name, year)))
    file.write("Release date of the top sold FPS game is: {}\n".format(reports.when_was_top_sold_fps(file_name)))
    file.close()
    return export_file

export_answers_from_reports("game_stat.txt", "Terraria", 2004, "First-person shooter")
