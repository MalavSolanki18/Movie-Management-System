import csv
import random
import smtplib

# Define global variables
student_fields = ['booking_id', 'name', 'email', 'time', 'movie', 'seats']
ticket_database = 'ticket.csv'
with open("ticket.csv", "r+") as tickets_db :
    csvwriter = csv.writer(tickets_db)
    csvwriter.writerow(student_fields)


def display_menu() :
    print("----------------------------------------")
    print(" Welcome to Movie Ticket Booking System")
    print("----------------------------------------")
    print("1. Now Showing")
    print("2. Comming Soon")
    print("4. Cancellations")
    print("5. Contact us")
    print("6. Quit")


def now_showing() :
    print("-------------------------")
    print(" Now Showing in Cinemas")
    print("-------------------------")
    print("01. SPIDER-MAN : NO WAY HOME - ENGLISH")
    print("02. BRAHMASTRA PART ONE : SHIVA - HINDI")
    print("03. TOP GUN : MAVERICK - ENGLISH")
    print("04. LAAL SINGH CHADDHA - HINDI")
    print("05. JURASSIC WORLD DOMINION - ENGLISH")
    print("06. K.G.F. : CHAPTER 2 - KANNADA")
    print("07. RRR - TELUGU")
    print("08. PUSHPA : THE RISE - TELUGU")
    print("09. VIKRAM - TAMIL")
    print("10. JANA GANA MANA - MALAYALAM")
    print("for more information regarding the movie...(Press 00 to return to the main menu)")
    global m
    m = int(input("Enter the movie number:"))
    if m == 00 or 0 :
        print("Returning back to Main Menu....")
        display_menu()
    # SPIDER-MAN : NO WAY HOME - ENGLISH
    elif m == 1 :
        print("------------------------------------")
        print("SPIDER-MAN : NO WAY HOME - ENGLISH")
        print("------------------------------------")
        print(
            "Spider-Man seeks the help of Doctor Strange to forget his exposed secret identity as Peter Parker. However, Strange's spell goes horribly wrong, leading to unwanted guests entering their universe.")
        x = input("TO PROCEED TO BOOKING PAGE Press Y (OR) TO RETURN BACK TO MAIN MENU Press N:")
        if x == 'Y' :
            booking()
        elif x == 'N' :
            display_menu()
        else :
            print("Invalid Input")
            display_menu()
    # BRAHMASTRA PART ONE : SHIVA - HINDI
    elif m == 2 :
        print("------------------------------------")
        print("BRAHMASTRA PART ONE : SHIVA - HINDI")
        print("------------------------------------")
        print(
            "Brahmāstra: Part One – Shiva is a 2022 Indian Hindi-language fantasy-adventure film film written and directed by Ayan Mukerji.")
        x = input("TO PROCEED TO BOOKING PAGE Press Y (OR) TO RETURN BACK TO MAIN MENU Press N:")
        if x == 'Y' :
            booking()
        elif x == 'N' :
            display_menu()
        else :
            print("Invalid Input")
            display_menu()
    # TOP GUN : MAVERICK - ENGLISH
    elif m == 3 :
        print("------------------------------------")
        print("TOP GUN : MAVERICK - ENGLISH")
        print("------------------------------------")
        print(
            "Top Gun: Maverick is a 2022 American action drama film directed by Joseph Kosinski. It is the sequel to the 1986 film Top Gun and the second installment in the Top Gun film series. Written by Ehren Kruger, Eric Warren Singer, and Christopher McQuarrie, the film is based on a story by Peter Craig and Justin Marks.")
        x = input("TO PROCEED TO BOOKING PAGE Press Y (OR) TO RETURN BACK TO MAIN MENU Press N:")
        if x == 'Y' :
            booking()
        elif x == 'N' :
            display_menu()
        else :
            print("Invalid Input")
            display_menu()
    # LAAL SINGH CHADDHA - HINDI
    elif m == 4 :
        print("------------------------------------")
        print("LAAL SINGH CHADDHA - HINDI")
        print("------------------------------------")
        print(
            "Laal Singh Chaddha is a 2022 Indian Hindi-language comedy-drama film directed by Advait Chandan from a screenplay by Eric Roth and Atul Kulkarni. Produced by Aamir Khan Productions and Viacom18 Studios, it is a remake of the 1994 American film Forrest Gump which itself is an adaptation of the novel of the same name.")
        x = input("TO PROCEED TO BOOKING PAGE Press Y (OR) TO RETURN BACK TO MAIN MENU Press N:")
        if x == 'Y' :
            booking()
        elif x == 'N' :
            display_menu()
        else :
            print("Invalid Input")
            display_menu()
    # JURASSIC WORLD DOMINION - ENGLISH
    elif m == 5 :
        print("------------------------------------")
        print("JURASSIC WORLD DOMINION - ENGLISH")
        print("------------------------------------")
        print(
            "From Jurassic World architect and director Colin Trevorrow, Dominion takes place four years after Isla Nublar has been destroyed. Dinosaurs now live - and hunt - alongside humans all over the world. This fragile balance will reshape the future and determine, once and for all, whether human beings are to remain the apex predators on a planet they now share with history's most fearsome creatures.")
        x = input("TO PROCEED TO BOOKING PAGE Press Y (OR) TO RETURN BACK TO MAIN MENU Press N:")
        if x == 'Y' :
            booking()
        elif x == 'N' :
            display_menu()
        else :
            print("Invalid Input")
            display_menu()
    # K.G.F. : CHAPTER 2 - KANNADA
    elif m == 6 :
        print("------------------------------------")
        print("K.G.F. : CHAPTER 2 - KANNADA")
        print("------------------------------------")
        print(
            "Rocky takes control of the Kolar Gold Fields and his newfound power makes the government as well as his enemies jittery. However, he still has to confront Ramika, Adheera and Inayat.")
        x = input("TO PROCEED TO BOOKING PAGE Press Y (OR) TO RETURN BACK TO MAIN MENU Press N:")
        if x == 'Y' :
            booking()
        elif x == 'N' :
            display_menu()
        else :
            print("Invalid Input")
            display_menu()
    # RRR - TELUGU
    elif m == 7 :
        print("------------------------------------")
        print("RRR - TELUGU")
        print("------------------------------------")
        print(
            "A fearless revolutionary and an officer in the British force, who once shared a deep bond, decide to join forces and chart out an inspirational path of freedom against the despotic rulers.")
        x = input("TO PROCEED TO BOOKING PAGE Press Y (OR) TO RETURN BACK TO MAIN MENU Press N:")
        if x == 'Y' :
            booking()
        elif x == 'N' :
            display_menu()
        else :
            print("Invalid Input")
            display_menu()
    # PUSHPA : THE RISE - TELUGU
    elif m == 8 :
        print("------------------------------------")
        print("PUSHPA : THE RISE - TELUGU")
        print("------------------------------------")
        print(
            "A labourer named Pushpa makes enemies as he rises in the world of red sandalwood smuggling. However, violence erupts when the police attempt to bring down his illegal business.")
        x = input("TO PROCEED TO BOOKING PAGE Press Y (OR) TO RETURN BACK TO MAIN MENU Press N:")
        if x == 'Y' :
            booking()
        elif x == 'N' :
            display_menu()
        else :
            print("Invalid Input")
            display_menu()
    # VIKRAM - TAMIL
    elif m == 9 :
        print("------------------------------------")
        print("VIKRAM - TAMIL")
        print("------------------------------------")
        print(
            "A special agent investigates a murder committed by a masked group of serial killers. However, a tangled maze of clues soon leads him to the drug kingpin of Chennai.")
        x = input("TO PROCEED TO BOOKING PAGE Press Y (OR) TO RETURN BACK TO MAIN MENU Press N:")
        if x == 'Y' :
            booking()
        elif x == 'N' :
            display_menu()
        else :
            print("Invalid Input")
            display_menu()
    # JANA GANA MANA - MALAYALAM
    elif m == 10 :
        print("------------------------------------")
        print("JANA GANA MANA - MALAYALAM")
        print("------------------------------------")
        print(
            "A professor's death causes uproar across the nation and sends a policeman on a meticulous probe about the murder. However, the case soon puts the officer in trouble.")
        x = input("TO PROCEED TO BOOKING PAGE Press Y (OR) TO RETURN BACK TO MAIN MENU Press N:")
        if x == 'Y' :
            booking()
        elif x == 'N' :
            display_menu()
        else :
            print("Invalid Input")
            display_menu()


def booking() :
    print("----------------------------------------")
    print("WELCOME TO TICKET BOOKING WINDOW")
    print("----------------------------------------")
    K = [0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0]
    J = [0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0]
    I = [0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0]
    H = [0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0]
    G = [0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0]
    F = [0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0]
    E = [0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0]
    D = [0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0]
    C = [0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0]
    B = [0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0]
    A = [0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "**", 0, 0, 0, 0, 0]

    booking_id = random.randint(1000, 10000)
    name = input("Enter your name:")
    email = input("Enter your Email:")
    print("----------------------------------------")
    print("Available Showtimes")
    print("----------------------------------------")
    print("17:00                           [1]")
    print("18:00                           [2]")
    print("19:00                           [3]")
    print("20:00                           [4]")
    print("21:00                           [5]")
    print("22:00                           [6]")
    print("23:00                           [7]")
    print("----------------------------------------")

    showtime = int(input("Enter your prefered showtime:"))
    if showtime == 1 :
        time = '17:00'
    elif showtime == 2 :
        time = '18:00'
    elif showtime == 3 :
        time = '19:00'
    elif showtime == 4 :
        time = '20:00'
    elif showtime == 5 :
        time = '21:00'
    elif showtime == 6 :
        time = '22:00'
    elif showtime == 7 :
        time = '23:00'
    else :
        print("invalid input")

    
    if m == 1:
        movie = "SPIDER-MAN : NO WAY HOME - ENGLISH"
    elif m== 2:
        movie = "BRAHMASTRA PART ONE : SHIVA - HINDI"
    elif m== 3:
        movie = "TOP GUN : MAVERICK - ENGLISH"
    elif m== 4:
        movie = "LAAL SINGH CHADDHA - HINDI"
    elif m== 5:
        movie = "JURASSIC WORLD DOMINION - ENGLISH"
    elif m== 6:
        movie = "K.G.F. : CHAPTER 2 - KANNADA"
    elif m== 7:
        movie = "RRR - TELUGU"
    elif m== 8:
        movie = "PUSHPA : THE RISE - TELUGU"
    elif m== 9:
        movie = "VIKRAM - TAMIL"
    elif m== 10:
        movie = "JANA GANA MANA - MALAYALAM"
    
    print("---------------------------------------------------------------------------------------")
    print("                                SEAT SELECTION PROCESS")
    print("---------------------------------------------------------------------------------------")
    print("There are 11 rows starting from A to K.Each row consist of 5-15-5 seating arrangement.")
    print("The seats are numbered from 0 to 26 in which numbers 5 and 21 are reserved in every row.")
    print("---------------------------------------------------------------------------------------")
    print("0 - EMPTY SEATS                                                        1 - BOOKED SEATS")
    print("---------------------------------------------------------------------------------------")
    print(K)
    print(J)
    print(I)
    print(H)
    print(G)
    print(F)
    print(E)
    print(D)
    print(C)
    print(B)
    print(A)
    print("|                                                                                     |")
    print("|-------------------------------------------------------------------------------------|")
    print("|                                       SCREEN                                        |")
    print("|-------------------------------------------------------------------------------------|")
    n = int(input("How many tickets are to be booked?"))
    tickets = []
    for j in range(0, n) :
        print("---------------------------------------------------------------------------------------")
        print("Booking ticket #", j + 1)
        print("---------------------------------------------------------------------------------------")
        row = input("select your desired row:")
        if row == 'A' :
            i = int(input("Please choose your desired seat number:"))
            if i < 1 or i > 26 :
                print("Invalid Seat Number")
            elif i == 5 or i == 21 :
                print("Invalid Seat Number")
            else :
                A[i] = 1
                print("Your preffered seat is", row, '-', i)
        elif row == 'B' :
            i = int(input("Please choose your desired seat number:"))
            if i < 1 or i > 26 :
                print("Invalid Seat Number")
            elif i == 5 or i == 21 :
                print("Invalid Seat Number")
            else :
                B[i] = 1
                print("Your preffered seat is", row, '-', i)
        elif row == 'C' :
            i = int(input("Please choose your desired seat number:"))
            if i < 1 or i > 26 :
                print("Invalid Seat Number")
            elif i == 5 or i == 21 :
                print("Invalid Seat Number")
            else :
                C[i] = 1
                print("Your preffered seat is", row, '-', i)
        elif row == 'D' :
            i = int(input("Please choose your desired seat number:"))
            if i < 1 or i > 26 :
                print("Invalid Seat Number")
            elif i == 5 or i == 21 :
                print("Invalid Seat Number")
            else :
                D[i] = 1
                print("Your preffered seat is", row, '-', i)
        elif row == 'E' :
            i = int(input("Please choose your desired seat number:"))
            if i < 1 or i > 26 :
                print("Invalid Seat Number")
            elif i == 5 or i == 21 :
                print("Invalid Seat Number")
            else :
                E[i] = 1
                print("Your preffered seat is", row, '-', i)
        elif row == 'F' :
            i = int(input("Please choose your desired seat number:"))
            if i < 1 or i > 26 :
                print("Invalid Seat Number")
            elif i == 5 or i == 21 :
                print("Invalid Seat Number")
            else :
                F[i] = 1
                print("Your preffered seat is", row, '-', i)
        elif row == 'G' :
            i = int(input("Please choose your desired seat number:"))
            if i < 1 or i > 26 :
                print("Invalid Seat Number")
            elif i == 5 or i == 21 :
                print("Invalid Seat Number")
            else :
                G[i] = 1
                print("Your preffered seat is", row, '-', i)
        elif row == 'H' :
            i = int(input("Please choose your desired seat number:"))
            if i < 1 or i > 26 :
                print("Invalid Seat Number")
            elif i == 5 or i == 21 :
                print("Invalid Seat Number")
            else :
                H[i] = 1
                print("Your preffered seat is", row, '-', i)
        elif row == 'I' :
            i = int(input("Please choose your desired seat number:"))
            if i < 1 or i > 26 :
                print("Invalid Seat Number")
            elif i == 5 or i == 21 :
                print("Invalid Seat Number")
            else :
                I[i] = 1
                print("Your preffered seat is", row, '-', i)
        elif row == 'J' :
            i = int(input("Please choose your desired seat number:"))
            if i < 1 or i > 26 :
                print("Invalid Seat Number")
            elif i == 5 or i == 21 :
                print("Invalid Seat Number")
            else :
                J[i] = 1
                print("Your preffered seat is", row, '-', i)
        elif row == 'K' :
            i = int(input("Please choose your desired seat number:"))
            if i < 1 or i > 26 :
                print("Invalid Seat Number")
            elif i == 5 or i == 21 :
                print("Invalid Seat Number")
            else :
                K[i] = 1
                print("Your preffered seat is", row, '-', i)
        else :
            print("Invalid Input")
        s = str(i)
        a = row + s
        tickets.append(a)
        t = str(tickets)
    print("---------------------------------------------------------------------------------------")
    print("0 - EMPTY SEATS                                                        1 - BOOKED SEATS")
    print("---------------------------------------------------------------------------------------")
    print(K)
    print(J)
    print(I)
    print(H)
    print(G)
    print(F)
    print(E)
    print(D)
    print(C)
    print(B)
    print(A)
    print("|                                                                                     |")
    print("|-------------------------------------------------------------------------------------|")
    print("|                                       SCREEN                                        |")
    print("|-------------------------------------------------------------------------------------|")
    
        
    print("---------------------------------------------------------------------------------------")
    print("                                      PAYMENT")
    print("---------------------------------------------------------------------------------------")
    print(" ")
    print(" Total Payable Amount                                         ",n,"x 2.5 KWD =",n*2.5,"KWD")
    print(" ")
    print("---------------------------------------------------------------------------------------")
    print(" ")
    print("Choose a Payment option:")
    print("1.UPI")
    print("2.Credit/Debit/Atm Card")
    print("3.Netbanking")
    pay_option=int(input())
    if pay_option == 1:
        print("proceeding to UPI page. . . ")
        mn=input()
        data = [booking_id, name, email, time, movie, t]
        db = []
        db.append(data)
        with open("ticket.csv", "a") as tickets_db :
            csvwriter = csv.writer(tickets_db)
            csvwriter.writerows(db)
        print("BOOKING SUCCESSFUL!!\n ")
        print("##############################################")
        print("####","            MOVIE E-TICKET          ","####")
        print("##############################################")
        print("##############################################")
        print("####","Booking Id :",booking_id,"                   ####")
        print("####","Name       :",name,"          ####")
        print("####--------------------------------------####")
        print("####","                MOVIE               ","####")
        print("####--------------------------------------####")
        print("####",movie," ####")
        print("####",'Showtime :',time,"                    ####")
        print("####--------------------------------------####")
        print("####","                SEATS               ","####")
        print("####--------------------------------------####")
        for i in tickets:
            print("####","                ",i,"               ","####")
        print("####--------------------------------------####")
        print("##############################################")
        print("##############################################")
        display_menu()
    elif pay_option == 2 or pay_option == 3 :
        print("proceeding to Banking page . . . ")
        mn=input()
        data = [booking_id, name, email, time, movie, t]
        print(data)
        db = []
        db.append(data)
        with open("ticket.csv", "a") as tickets_db :
            csvwriter = csv.writer(tickets_db)
            csvwriter.writerows(db)
        print("BOOKING SUCCESSFUL!!\n ")
        print("##############################################")
        print("####","            MOVIE E-TICKET          ","####")
        print("##############################################")
        print("##############################################")
        print("####","Booking Id :",booking_id,"                   ####")
        print("####","Name       :",name,"          ####")
        print("####--------------------------------------####")
        print("####","                MOVIE               ","####")
        print("####--------------------------------------####")
        print("####",movie," ####")
        print("####",'Showtime :',time,"                    ####")
        print("####--------------------------------------####")
        print("####","                SEATS               ","####")
        print("####--------------------------------------####")
        for i in tickets:
            print("####","                ",i,"                ","####")
        print("####--------------------------------------####")
        print("##############################################")
        print("##############################################")
        display_menu()
    else:
        print("BOOKING FAILED!")
        display_menu()
            
'''def ticket():
    x=int(input("Enter Booking ID to Retrive Ticket:"))
    global booking_id,name,movie,time,t,data,db
    print(data)
    for i in data:
        if x == data:
            print("##############################################")
            print("####","            MOVIE E-TICKET          ","####")
            print("##############################################")
            print("##############################################")
            print("####","Booking Id :",booking_id,"                   ####")
            print("####","Name       :",name,"          ####")
            print("####--------------------------------------####")
            print("####","                MOVIE               ","####")
            print("####--------------------------------------####")
            print("####",movie," ####")
            print("####",'Showtime :',time,"                    ####")
            print("####--------------------------------------####")
            print("####","                SEATS               ","####")
            print("####--------------------------------------####")
            for i in t:
                print("####","                ",i,"               ","####")
            print("####--------------------------------------####")
            print("##############################################")
            print("##############################################")'''
now_showing()
