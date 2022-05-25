import random


def main():
    while True:
        print("\t\t******Welcome to Book My Show*******")
        print("\t\t_________________________________________")
        print("\t\t\t -------Main Menu-------")
        print("\t\t_________________________________________")
        print("\t\t\t1-> Admin")
        print("\t\t\t2-> user")
        print("\t\t\t3-> Exit")
        choice1 = eval(input("\t\t\tEnter your choice(1/2/3):-"))
        if choice1 == 1:
            admin()
        elif choice1 == 2:
            client()
        elif choice1 == 3:
            exit()
        else:
            print("Invalid input")


def admin():
    while True:
        print("\t\t\t******Welcome to Book My Show*******")
        print("\t\t\tEmailid:admin@gmail.com ")
        Password = input("\t\t\tEnter Your Password:-")
        if Password == "admin":
            while True:
                print("\t\t\t******Welcome Admin*******")
                print("\t\t_________________________________________")
                print("\t\t\t -------Admin Menu-------")
                print("\t\t_________________________________________")
                print("\t\t\t1-> Add New Movie Info ")
                print("\t\t\t2-> Delete Movie info ")
                print("\t\t\t3-> Edit Movie Timings")
                print("\t\t\t4-> Go back to the menu ")
                choice2 = eval(input("\t\t\tEnter your choice(1/2/3/4):-"))
                if choice2 == 1:
                    add_movies()
                elif choice2 == 2:
                    remove_movies()
                elif choice2 == 3:
                    edit_timings()
                elif choice2 == 4:
                    main()
                else:
                    print("Invalid input")
        else:
            print("Wrong Password.")
            print("1-> Try again")
            print("2-> Go back to Main menu")
            choice = eval(input("Enter your choice:-"))
            if choice == 2:
                print("Proceding back to main menu...")
                main()


def add_movies():
    if len(Movies) < 5:
        cont = "y"  # do you want to continue variable
        while cont == "y":
            mov_name = input("Enter the name of the movie to be added:-")
            mov_name = mov_name.upper()
            mov_genre = input("genre of the movie:")
            mov_length = eval(input("Enter the length of the movie(in minutes):-"))
            mov_cast=input("Enter the name of cast: ")
            mov_director = input("Enter the name of the director: ")
            mov_rating=input("Admin rating:  ")
            mov_screen = eval(input("Enter the screen in which the movie shall be shown (1/2/3/4/5):-"))

            valid = 1
            while valid == 1:
                if mov_screen in range(1, 6):
                    for i in Movies:
                        if mov_screen == Movies[i][1]:
                            print("Screen already in use. Please choose another one.")
                            mov_screen = eval(
                                input("Enter the screen in which the movie shall be shown (1/2/3/4/5):-"))
                            break
                    else:
                        valid = 2  # for empty Movies={}
                else:
                    print("Invalid Screen no.")
                    mov_screen = input("Enter the screen in which the movie shall be shown (1/2/3/4/5):-")
            valid_ns = 1
            while valid_ns == 1:
                number_shows = eval(input("Enter the no. of Shows for this screen per day:-"))
                if number_shows < 1440 / (mov_length + 15):
                    valid_ns = 2
                else:
                    print("Too many shows in a single day. Please re-enter the no. of shows")
            timings = list(range(number_shows))
            for i in range(number_shows):
                validT = 1
                while validT == 1:
                    timings[i] = input("Enter the timing for the show(HH:MM):-")
                    if len(timings[i]) == 5:
                        if int(timings[i][:2]) < 24:
                            if int(timings[i][3:]) < 60:
                                validT = 2
                    else:
                        print("Invalid Timing")
            valid = 1
            while valid != 0:
                valid = 0
                for i in range(1, number_shows):
                    if (int(timings[i][:2]) - int(timings[i - 1][:2])) * 60 + int(timings[i][3:]) - int(
                            timings[i - 1][3:]) < mov_length + 15:
                        print("Time span between ", timings[i - 1], "and", timings[i],
                              "is not enough(There has to be a minimum time difference of", mov_length + 15,
                              "). Please choose another timing instead of")
                        print("1->", timings[i - 1])
                        print("2->", timings[i])
                        valid1 = 1
                        while valid1 == 1:

                            ch = eval(input("Which timing do you want to change(1/2)-"))
                            if ch == 1:
                                timings[i - 1] = input("Enter the timing for the show(HH:MM):-")
                                valid += 1
                                valid1 = 2
                            elif ch == 2:
                                timings[i] = input("Enter the timing for the show(HH:MM):-")
                                valid += 1
                                valid1 = 2
                            else:
                                print("Invalid Choice")

            validD = 1
            while validD == 1:
                start_date = input("Enter the date from which the movie will run(dd/mm/yyyy):-")
                if len(start_date) == 10:
                    if int(start_date[:2]) in range(1, 32):
                        if int(start_date[3:5]) in range(1, 13):
                            validD = 2
                        else:
                            print("Invalid date.")
                    else:
                        print("Invalid date.")
                else:
                    print("Invalid date.")

            mov_dates = list(range(7))
            for i in range(7):
                next_day = int(start_date[:2]) + i
                if int(start_date[3:5]) in [1, 3, 5, 7, 8, 10]:
                    if next_day > 31:
                        next_month = int(start_date[3:5]) + 1
                        next_day -= 31
                        if len(str(next_month)) == 1:
                            next_day = str(next_day) + "/" + "0" + str(next_month) + start_date[5:]
                        else:
                            next_day = str(next_day) + "/" + str(next_month) + start_date[5:]
                    else:
                        next_day = str(next_day) + start_date[2:]
                elif int(start_date[3:5]) in [4, 6, 9, 11]:
                    if next_day > 30:
                        next_month = int(start_date[3:5]) + 1
                        next_day -= 30
                        if len(str(next_month)) == 1:
                            next_day = str(next_day) + "/" + "0" + str(next_month) + start_date[5:]
                        else:
                            next_day = str(next_day) + "/" + str(next_month) + start_date[5:]
                    else:
                        next_day = str(next_day) + start_date[2:]
                elif int(start_date[3:5]) == 2:
                    if next_day > 28:
                        next_month = int(start_date[3:5]) + 1
                        next_day -= 28

                        next_day = str(next_day) + "/" + "0" + str(next_month) + start_date[5:]
                    else:
                        next_day = str(next_day) + start_date[2:]
                elif int(start_date[3:5]) == 12:
                    if next_day > 31:
                        next_month = 1
                        next_day -= 31
                        next_year = int(start_date[6:]) + 1
                        next_day = str(next_day) + "/" + "0" + str(next_month) + '/' + str(next_year)
                    else:
                        next_day = str(next_day) + start_date[2:]
                mov_dates[i] = next_day
            mov_dets = [mov_length, mov_screen, number_shows, timings, mov_dates, mov_genre, mov_cast, mov_director, mov_rating]
            Movies[mov_name] = mov_dets
            Seats = list(range(124))
            k = 1
            for j in range(124):
                Seats[j] = [k, False]
                k += 1
            Timings = {}
            for j in timings:
                Timings[j] = Seats
            Dates = {}
            for j in mov_dates:
                Dates[j] = Timings
            MoviesB[mov_name] = Dates
            if len(Movies) == 5:
                cont = 'n'
                print("No more Screens available. Proceeding back to menu......")
            else:
                cont = input("Do you want to add more movies(y/n):-")
    else:
        print("No more Screens available. Proceeding back to menu......")


def remove_movies():
    if Movies != {}:
        cont1 = "y"
        while cont1 == "y":
            print("The currently showing movies are:-")
            for i in Movies:
                print(i)
            print("******Welcome Admin*******")
            print("Do you want to:-")
            print("1-> Proceed to remove movies")
            print("2-> Go back to Admin menu")
            choice = eval(input("Enter your choice(1/2):-"))
            if choice == 1:
                mov_name_remov = input("Enter the name of the movie to be Removed:-")
                mov_name_remov = mov_name_remov.upper()
                print("Are you sure you want to delete", mov_name_remov, "from the movie list?")
                print("1-> Yes")

                print("2-> No")
                choice1 = eval(input("Enter your choice(1/2):-"))
                if choice1 == 1:
                    del Movies[mov_name_remov]
                    del MoviesB[mov_name_remov]
                    print()
                    mov_name_remov, "has been removed"
                    print("Now the currently showing movies are:-")
                    for i in Movies:
                        print(i)
                else:
                    print('Movie not deleted')
                if len(Movies) == 0:
                    cont1 = 'n'
                    print("No more movies to be removed. Proceding back to menu.......")
                else:
                    cont1 = eval(input("Do you want to remove more movies(y/n):-"))
            elif choice == 2:
                print("Proceding back to Admin menu...")
                cont1 = 'n'
    else:
        print("No movies available. Proceeding back to Admin menu.....")


def edit_timings():
    pass


def client():
    while True:
        print("Emailid:Username@gmail.com")
        Password = input("Enter Your Password:-")
        if Password == "user":
            while True:
                if Movies != {}:
                    while True:
                        print("\n\t\t\t******Welcome User1*******")
                        print("\t\t_________________________________________")
                        print("\n\t\t\t -------Client Menu-------")
                        print("\t\t_________________________________________")
                        print("\t\t\t1-> View movies")
                        print("\t\t\t2-> Go back to main menu")
                        choice2 = eval(input("\t\t\tEnter your choice(1/2):-"))
                        if choice2 == 1:
                            view_movies()
                        elif choice2 == 2:
                            main()
                        else:
                            print("Invalid input")
                else:
                    print("No movies Available. Returning to main menu .....")
                    return


def view_movies():
    print("The currently showing movies are:-")

    for i in Movies:
        print("\n")
        print(i, "\t\t Movie length(in min)-", Movies[i][0])
        print("Showing in Screen-", Movies[i][1])
        print("Available dates:")
        for j in range(7):
            print(Movies[i][4][j], "\t", end=' ')

Movies = {}
MoviesB = {}
Clients = {}
main()
