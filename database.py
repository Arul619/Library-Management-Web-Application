
bookid = []
titles = []
authors = []
pdate = []
mid = []
# the lists used to categorize the data when we read the database


def accessor_of_data(database):
    # it is used to access data
    # line is temporary holding ground for the data extracted
    # the system reads the file and puts in the list line
    # then the function returns the list line

    line = []
    try:
        f = open(database, "r")
        # prepares to file in order to read it
        for line in f:
            line = f.readlines()
        f.close()
        # it reads all the values of the file indicated and returns a list of all the strings it contains
    except IOError:
        print("Failure in reading file")
    return line


def format_database():
    # to be used in order to reformat the database file in case a new blank file is needed
    f = open("database.txt", "w")
    line = "ID | Title | Author | Purchase Date | Member ID"
    f.write(line)
    f.close()


def sort_data_to_present_database(list_input):
    # sorts the data retrieved from the database.txt file
    # it breaks it down to lists that comprise all the data of each individual book
    # it breaks the string into smaller elements

    for i in range(0, len(list_input)):
        now_list = str(list_input[i]).split("|")
        if len(now_list) > 1:
            print(now_list)
            bookid.append(now_list[0])
            titles.append(now_list[1])
            authors.append(now_list[2])
            pdate.append(now_list[3])
            mid.append(now_list[4].strip("\n"))


def module_check_for_presenter_and_accessor():
    # this function will test if the presenter sorting the data of the database as expected
    sort_data_to_present_database(accessor_of_data("database.txt"))
    print(bookid)
    print(authors_list())
    print(titles)
    print(mid)


def database_modifier(database, message):
    # it is used to add new strings in the file
    f = open(database, "a")
    f.write(message)
    f.close()


def book_id_giver():
    # returns a list of all books' ids stored
    return bookid


def book_titles():
    # returns a list of all books' titles stored
    return titles


def authors_list():
    # returns a list of all books' authors stored
    return authors


def purchase_date():
    # returns a list of all stored books' purchase date
    return pdate


def member_id():
    # returns a list of all stored books' member id, 0 if free, the member's id if taken
    return mid


def test_data():
    # it generates test data in the database in order to check the functions
    f = open("database.txt", "w")
    line = "ID | Title | Author | Purchase Date | Member ID \n"
    f.write(line)
    line1 = "01 | The Art of War | Sun Tzu | 09/08/2019| 0 \n"
    f.write(line1)
    f.close()


def data_terminator(line, database):
    # this function deletes certain lines from the a file given
    o = open(database, "r")
    lines = o.readlines()
    # creates a file of all the lines in the file
    o.close()
    for i in range(len(lines)):
        try:
            print(lines[i])
            if str(lines[i]).strip("\n").strip(" ") == str(line).strip("\n").strip(' '):
                # finds the line needed
                lines.pop(i)
                # pops it
                f = open(database, "w")
                f.writelines(lines)
                f.close()
                # it opens and overwrites the entire file.
                break
            else:
                print("Line not found")
        except ValueError:
            print("System Malfunction")


def database_overwrite(database, origvalue, aftvalue):
    # this function is used to replace a line with a new line at the end of the file
    # reads the entire file and produces a list of all the lines
    # checks that the line that we are looking for exists
    # removes that line
    # then rewrites the entire file

    o = open(database, "r")
    lines = o.readlines()
    o.close()
    for i in range(len(lines)):
        try:
            if str(lines[i]).strip("\n").strip(" ") == origvalue.strip("\n").strip(" "):
                # finds the value that needs to be overwritten
                lines.pop(i)
                # removes it
                lines.append(aftvalue)
                # and replaces it
                f = open(database, "w")
                f.writelines(lines)
                f.close()
                # and then overwrites the file
                break
        except RuntimeError:
            print("System Malfunction")


def overwrite_test():
    # tests that the overwrite function works
    database_overwrite("database.txt", {"message":[{"bookID":"35460","title":"Star Wars: Clone Wars Adventures  Volume 6","authors":"W. Haden Blackman/Matt Fillbach/Shawn Fillbach/Ronda Pattison/Mike Kennedy/Stewart McKenney/Rick Lacy/Dan Jackson/Michael David Thomas/Joshua Elliott","average_rating":"3.78","isbn":"1593075677","isbn13":"9781593075675","language_code":"eng","  num_pages":"88","ratings_count":"176","text_reviews_count":"10","publication_date":"8/23/2006","publisher":"Dark Horse Books"},{"bookID":"17828","title":"The Master and Margarita","authors":"Mikhail Bulgakov/Michael Karpelson","average_rating":"4.30","isbn":"1411683056","isbn13":"9781411683051","language_code":"eng","  num_pages":"332","ratings_count":"493","text_reviews_count":"47","publication_date":"4/1/2006","publisher":"Lulu Press"},{"bookID":"34908","title":"Here  There Be Dragons (Chronicles of the Imaginarium Geographica  #1)","authors":"James A. Owen","average_rating":"3.86","isbn":"1416912274","isbn13":"9781416912279","language_code":"en-US","  num_pages":"326","ratings_count":"10103","text_reviews_count":"917","publication_date":"9/26/2006","publisher":"Simon & Schuster Books for Young Readers"},{"bookID":"40395","title":"A Princess of Mars (Barsoom  #1)","authors":"Edgar Rice Burroughs/John Seelye","average_rating":"3.81","isbn":"0143104888","isbn13":"9780143104889","language_code":"eng","  num_pages":"186","ratings_count":"38926","text_reviews_count":"2355","publication_date":"1/30/2007","publisher":"Penguin Books"}]})


def test_data_removal():
    # it used a value that no longer exists
    data_terminator(" 1 | The Art of War | Sun Tzu | 09/08/2019| 0", "database.txt")


def resetdata():
    # resets all the lists of the entire file
    bookid = []
    titles = []
    authors = []
    pdate = []
    mid = []
    sort_data_to_present_database(accessor_of_data("database.txt"))


if __name__ == "__main__":
    overwrite_test()
    test_data_removal()
