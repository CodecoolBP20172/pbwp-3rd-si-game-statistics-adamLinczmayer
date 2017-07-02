import reports


def export_reports_answers(file_name, title, export_file):
    file = open(export_file, "w")
    file.write("The most played game is: {}\n".format(reports.get_most_played(file_name)))
    file.write("The total number of the copies have been sold is: {}\n".format(reports.sum_sold(file_name)))
    file.write("The average selling is: {}\n".format(reports.get_selling_avg(file_name)))
    file.write("The longest title cosists of {} characters.\n".format(reports.count_longest_title(file_name)))
    file.write("The average of the release dates is: {}\n".format(reports.get_date_avg(file_name)))
    file.write("The properties of the game is: {}\n".format(reports.get_game(file_name, title)))
    file.close()

export_reports_answers("game_stat.txt", "Minecraft", "reports_export.txt")

