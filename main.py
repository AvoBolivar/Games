
import time
from tkinter import *
from tkinter import Frame
from tkinter.messagebox import showerror
import webbrowser

root = Tk()

# makes first windows of the program
InstructionsWindow: Frame = Frame(root)
InstructionsWindow.grid(row=0, column=0)

ClassWindow: Frame = Frame(root)
ClassWindow.grid(row=1, column=0)

bottomWindow: Frame = Frame(root)
bottomWindow.grid(row=2, column=0)

# lists of classes, types, and connections
classButtons = ["Math", "Science", "Social Studies", "Language Arts", "Connections"]
difficulty = ["On-Level", "Honors/Accelerated", "AP class", "A year or more ahead"]
ExtraClass = ["Criminal Justice", "Fine Arts", "Music", "Language", "Physical Fitness", "Culinary", "Technology",
              "AP class"]

Instructions = " * Please only check the box that applies to you and" \
               " one check per category except for the Connections Category. *"
# all the clubs in alpharetta highs chool sorted in categories
# flenzy matching
clubs_in_school = [
    "Acapella/Momentum-Hype",
    "AHS Digital Photo Club",
    "Avionics Club",
    "Chemistry Club",
    "Cultural Music Club",
    "Gay Straight Alliance",
    "Math competition team",
    "Model UN",
    "National art honors society",
    "Yearbook club",
    "TRI-M Music Honors Society",
    "Philosophy club",
    "Orchestra",
    # break 12
    "A.I. Club",
    "FIRSTS (Robotics)",
    "Cover to Cover",
    "Alpharetta Geomapping Club",
    "Alpharetta Hack Club",
    "AP World History Study Help",
    "Avionics Club",
    "Astronomy Club",
    "Chemistry Club",
    "Chess Club",
    "Girls Who Code",
    "Science Olympiad",
    "Rocket Club",
    "Quiz Bowl",
    "Policy Debate",
    "National Technical Honor Society",
    "National Science Honors Society",
    "National Honor Society",
    # break 30
    "AHS Spikeball Club",
    "Band/Color Guard",
    "FCA",
    "Fencing Club",
    "Alpharetta Rowing Club",
    "United raiders club",
    "Table tennis",
    "Ping pong",
    "Or school sport",
    # break 38
    "Alpharetta Red Cross",
    "American Red Cross Club",
    "Animal Rights and Rescue",
    "BETA Club",
    "Black Student Union",
    "Environmental Club",
    "FCCLA",
    "Global Relief Club",
    "Habitat for Humanity",
    "Key club",
    "HOSA",
    "Mu alpha theta",
    "United non-profit",
    "UNICEF",
    "Thrombosis Awareness Club",
    "Teens against drugs",
    "Raider for the Cure",
    "Raider mentors",
    "Latina Club",
    # break 55
    "Indian culture club",
    "French club",
    "Latin club",
    "Latino mentorship",
    "We dine together",
    "United Latina club",
    "Thespian Society",
    "The Meridian News & Litary Mag",
    "The Knit Wits",
    "SADD",
    "Speech Team",
    "Secular Student Alliance",
    "Progressive Student Union",
    "PATH",
    "Nintendo Switch Club",
    # break
    "National Chinese Honor Society",
    "National Spanish Honor Society",
    "National French Honors Society",
    "National English Honor Society"
    # break
    "Junior State of America",
    "FBLA",
    "Girls in government",
    "Key club",
    "Link crew",
    "Women in stem",
    "student council",
    "Raider Ambassadors"
]

font = ("Helvetica", "18", "bold")
subt = ("Helvetica", "11", "bold")

# this is earned by sports, band, or other sports that would be considered sportive
sportive = 0
# the class score is mainly makes this score
smart = 0
# community service hours and certain clubs
helpful = 0
# roles in clubs would generally make up this category
leader = 0
# having outside sports, jobs, or responsibilities
responsible = 0
# Certain clubs helps in this category
creative = 0

# categories to put students based on interests
categories = ["Sportive", "School Smart", "Helpful", "Leader", "Responsible", "Creative"]
scale_names = ["sp", "sm", "hf", "ld", "rb", "cr"]
category_scores = []

# info you get back from the first window
mVar = IntVar()
mVar1 = IntVar()
mVar2 = IntVar()
mVar3 = IntVar()

sVar = IntVar()
sVar1 = IntVar()
sVar2 = IntVar()
sVar3 = IntVar()

ssVar = IntVar()
ssVar1 = IntVar()
ssVar2 = IntVar()
ssVar3 = IntVar()

litVar = IntVar()
litVar1 = IntVar()
litVar2 = IntVar()
litVar3 = IntVar()

# other info you get back from the entries
# amount of clubs
amount = StringVar()
# club name
club = StringVar()
# amount of community service hours
serviceHours = StringVar()
# this is list of the class tyoe for each class
cs = []
# gpa
gpa = StringVar()

mathType = 0
scienceType = 0
ssType = 0
litType = 0


class making_options:
    def __init__(self, name):
        self.name = name

# error pages
def error():
    showerror("Error", "Please only check one box per category and do not leave any blank.")


def club_error():
    showerror("Error", "Please make sure you are entering the name correctly")


# to set borders
def h_space(window, row, column):
    space = Label(window, text="   |   ")
    space.grid(row=row, column=column, sticky=W)


def v_space(window, row, column):
    space = Label(window, text=" ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
    space.grid(row=row, column=column)


def showing_results():
    def callback(url):
        webbrowser.open_new(url)

    print("Bruh, this page gotta be decorated")
    font2 = ("Times", "16", "bold italic")
    colors = ["dark orange", "gold", "dodgerblue2", "green2", "purple2", "red"]
    max = 0
    max_place = 0
    i = 0
    graph_page = Frame(root)
    graph_page.grid(row=0, column=0)

    results = Frame(root)
    results.grid(row=1, column=0)

    title2 = Label(results, text="Results:", font=font)
    title2.grid(row=0, column=0)

    while i < 6:
        graphWord = Label(graph_page, text=categories[i], font=font2)
        graphWord.grid(row=i + 1, column=0)

        win = Canvas(graph_page, width=230, height=50)
        win.grid(row=i + 1, column=1)
        win.create_rectangle(5, 15, category_scores[i] * 2, 30, outline=colors[i], fill=colors[i])
        if max < category_scores[i]:
            max = category_scores[i]
            max_place = i
        i += 1
    i += 1

    # this would give them a scholarship link depending on what they are interested in
    if max_place == 0:
        def yes():
            print("clicked yes")
            greet2 = Label(results, text="That is a solid choice, it is highly recommended that you try to stay in\n"
                                         "the sport all 4 years to show dedication. If you are looking to play sports\n"
                                         "in college you can visit the website below and find out the steps you can\n"
                                         "take to accomplish this goal.")
            greet2.grid(row=2, column=0)
            v_space(results, 3, 0)
            link_label = Label(results, text="Scholarship websites under your interest: ")
            link_label.grid(row=4, column=0)
            link = Label(results, text="Sport - based Scholarships", fg="blue", cursor="hand2")
            link.grid(row=5, column=0)
            link.bind("<Button-1>", lambda e: callback(
                "https://www.unigo.com/scholarships/athletic"))

        def no():
            print("clicked no")
            greet2 = Label(results, text="If your are in a sports team outside of school that is great as well.\n"
                                         "Although if you are not joining your favorite sports team due to financial\n"
                                         "issues it is highly recommended you talk to your councilor to hopefully\n"
                                         "find a solution."
                                         "\n"
                                         "\n"
                                         "Though if still interested in seeing what scholarships are out there under\n"
                                         "the sports category check the link bellow.")
            greet2.grid(row=2, column=0)
            v_space(results, 3, 0)
            link_label = Label(results, text="Scholarship websites under your interest: ")
            link_label.grid(row=4, column=0)
            link = Label(results, text="Sport - based Scholarships", fg="blue", cursor="hand2")
            link.grid(row=5, column=0)
            link.bind("<Button-1>", lambda e: callback(
                "https://www.unigo.com/scholarships/athletic"))

        greet = Label(results, text="As shown in the chart above, we could see that your favorite activity is Sports\n"
                                    "If you play a school sports click yes bellow and if not click no.")
        greet.grid(row=0, column=0)
        y = Button(results, text="Yes", )
        y.config(command=yes)
        y.grid(row=1, column=0)

        n = Button(results, text="No")
        n.config(command=no)
        n.grid(row=1, column=1)

    if max_place == 1:
        greet = Label(results, text="As shown in the chart above, you could see that your favorite activity is "
                                    "Study based.\n"
                                    "This is a really good trait to have though do not forget to expand your horizons\n"
                                    "and expand your background with sports and other clubs. ")
        greet.grid(row=0, column=0)
        v_space(results, 1, 0)
        link_label = Label(results, text="Scholarship websites under your interest: ")
        link_label.grid(row=2, column=0)
        link = Label(results, text="Academic Excellence - based Scholarships", fg="blue", cursor="hand2")
        link.grid(row=3, column=0)
        link.bind("<Button-1>", lambda e: callback(
            "https://www.scholarships.com/financial-aid/college-scholarships/scholarships-by-type/academic-scholarships-and-merit-scholarships/"))
    if max_place == 2:
        greet = Label(results, text="As shown in the chart above, you could see that your favorite activity is "
                                    "being helpful.\n"
                                    "By being helpful and earning multiple community service hours, opens the door\n"
                                    "to many scholarships and colleges. They love to see community ready students.")
        greet.grid(row=0, column=0)
        v_space(results, 1, 0)
        link_label = Label(results, text="Scholarship websites under your interest: ")
        link_label.grid(row=2, column=0)
        link = Label(results, text="Community Service - based Scholarships", fg="blue", cursor="hand2")
        link.grid(row=3, column=0)
        link.bind("<Button-1>", lambda e: callback(
            "https://blog.prepscholar.com/community-service-scholarships-complete-list"))
    if max_place == 3:
        greet = Label(results, text="As shown in the chart above, you could see that your favorite activity is "
                                    "leading others.\n"
                                    "Being a leader though is more than just telling people what to do\n"
                                    "What the work environment and colleges look for in a leader is someone who is\n"
                                    "challenge ready, great with communication, and respectful. ")
        greet.grid(row=0, column=0)
        v_space(results, 1, 0)
        link_label = Label(results, text="Scholarship websites under your interest: ")
        link_label.grid(row=2, column=0)
        link = Label(results, text="Leadership - based Scholarships", fg="blue", cursor="hand2")
        link.grid(row=3, column=0)
        link.bind("<Button-1>", lambda e: callback(
            "https://www.newvisions.org/pages/leadership-community-service-scholarships"))
    if max_place == 4:
        greet = Label(results, text="As shown in the chart above, you could see that your favorite activity is "
                                    "being a responsible person.\n"
                                    "Being responsible is a great trait to have and overall puts ahead of\n"
                                    "everybody else. Do not let the lazy get to you. ")
        greet.grid(row=0, column=0)
        v_space(results, 1, 0)
        link_label = Label(results, text="Scholarship websites under your interest: ")
        link_label.grid(row=2, column=0)
        link = Label(results, text="Responsible Scholarships", fg="blue", cursor="hand2")
        link.grid(row=3, column=0)
        link.bind("<Button-1>", lambda e: callback(
            "https://www.unigo.com/scholarships"))
    if max_place == 5:
        greet = Label(results, text="As shown in the chart above, you could see that your favorite activity is "
                                    "creativity.\n"
                                    "Creativity is really broad group, containing music, art, theater, and more.\n"
                                    "If you desire to pursue this path, Good Luck.")
        greet.grid(row=0, column=0)
        v_space(results, 1, 0)
        link_label = Label(results, text="Scholarship websites under your interest: ")
        link_label.grid(row=2, column=0)
        link = Label(results, text="Theater - Performance Scholarships", fg="blue", cursor="hand2")
        link.grid(row=3, column=0)
        link.bind("<Button-1>", lambda e: callback(
            "https://www.scholarships.com/financial-aid/college-scholarships/scholarship-directory/artistic-ability/theater-performance"))
        link2 = Label(results, text="Music - Based Scholarships", fg="blue", cursor="hand2")
        link2.grid(row=4, column=0)
        link2.bind("<Button-1>", lambda e: callback(
            "https://www.thebalance.com/college-scholarships-for-musicians-795392"))
        link3 = Label(results, text="Artist - Based Scholarships", fg="blue", cursor="hand2")
        link3.grid(row=5, column=0)
        link3.bind("<Button-1>", lambda e: callback(
            "https://www.scholarships.com/financial-aid/college-scholarships/scholarship-directory/artistic-ability/art-drawing"))

    i = 6
    sh = int(serviceHours.get())
    v_space(results, i, 0)
    i += 1

    # depending on their community service hours this will show
    if sh < 50:
        service_frame = Frame(root)
        service_frame.grid(row=3, column=0)
        s_label = Label(results, text="Having low community service hours is not good. Colleges and maybe future "
                                      "jobs\n"
                                      "want to see that you are a person who does not just care for yourself but, "
                                      "also\n"
                                      "for other people and the environment. Being able to add Community Service hours"
                                      "\n"
                                      "could potentially set you apart from the others.\n"
                                      "\n"
                                      "In school their are many clubs that help kids get community service hours. "
                                      "Check\n"
                                      "the list bellow to find out which one your are interested in. Then contact\n"
                                      "your counselor to find out further information about the club.")
        i += 1
        s_label.grid(row=i, column=0)
        i += 1
        index = 40
        r = 1
        c = 0
        while index <= 50:
            if r >= 4:
                c += 1
                h_space(service_frame, 1, c)
                c += 1
                r = 1
            help_clubs = Label(service_frame, text=clubs_in_school[index])
            help_clubs.grid(row=r, column=c, sticky=W)
            index += 1
            r += 1

    clubb = 0
    r = 0
    c = 0
    font3 = ("Times", 16, "italic")
    sub_font3 = ("Times", 8)
    normal_font3 = ("Times", 10)


    # depending on how rigorous their classes are this will show
    if smart < 6.25:
        class_advice = Frame(root)
        class_advice.grid(row=0, column=1)

        class_intro = Frame(class_advice)
        class_intro.grid(row=0, column=0)
        club_chart = Frame(class_advice)
        club_chart.grid(row=1, column=0)

        advise_one = Label(class_intro, text="We see from you class score, you would need to show colleges that you \n"
                                             "have strong interest in other things other than being \n"
                                             "academically smart. "
                                             "Colleges do not just look for rigorous classes. A well rounded \n"
                                             "student is always preferred. So we \n"
                                             "encourage you join clubs you would be interested which are \n"
                                             "listed bellow. \n"
                                             "\n")
        advise_one.grid(row=0, column=0, sticky=W)

        # this checks what their interests are and then gives them clubs depending on what they like
        if max_place == 0:
            print("sport based clubs")
            # 30 - 38
            clubb = 30
            while clubb <= 38:
                advise_two = Label(club_chart, text=clubs_in_school[clubb])
                advise_two.grid(row=r, column=c, sticky=W)
                r += 1
                if r == 5:
                    c += 1
                    h_space(club_chart, 0, c)
                    r = 0
                    c += 1
                clubb += 1

        if max_place == 1:
            clubb = 12
            while clubb <= 30:
                advise_two = Label(club_chart, text=clubs_in_school[clubb])
                advise_two.grid(row=r, column=c, sticky=W)
                r += 1
                if r == 5:
                    c += 1
                    h_space(club_chart, 0, c)
                    r = 0
                    c += 1
                clubb += 1
            # 12 - 30
        if max_place == 2:
            clubb = 42
            while clubb <= 50:
                advise_two = Label(club_chart, text=clubs_in_school[clubb])
                advise_two.grid(row=r, column=c, sticky=W)
                r += 1
                if r == 5:
                    c += 1
                    h_space(club_chart, 0, c)
                    r = 0
                    c += 1
                clubb += 1
        if max_place == 3:
            clubb = 60
            while clubb <= 68:
                advise_two = Label(club_chart, text=clubs_in_school[clubb])
                advise_two.grid(row=r, column=c, sticky=W)
                r += 1
                if r == 5:
                    c += 1
                    h_space(club_chart, 0, c)
                    r = 0
                    c += 1
                clubb += 1
            print("leader based clubs")
            # 60 - 68
        if max_place == 4:
            clubb = 12
            while clubb <= 24:
                advise_two = Label(club_chart, text=clubs_in_school[clubb])
                advise_two.grid(row=r, column=c, sticky=W)
                r += 1
                if r == 5:
                    c += 1
                    h_space(club_chart, 0, c)
                    r = 0
                    c += 1
                clubb += 1
            print("smart clubs")
            # 12 - 30
        if max_place == 5:
            clubb = 0
            while clubb <= 12:
                advise_two = Label(club_chart, text=clubs_in_school[clubb])
                advise_two.grid(row=r, column=c, sticky=W)
                r += 1
                if r == 5:
                    c += 1
                    h_space(club_chart, 0, c)
                    r = 0
                    c += 1
                clubb += 1
            print("creative clubs")
            # clubs 0 - 12

    if smart < 6.25:
        school_advise = Frame(root)
        school_advise.grid(row=1, column=1)
    else:
        school_advise = Frame(root)
        school_advise.grid(row=0, column=0)

    school_intro = Frame(school_advise)
    school_intro.grid(row=0, column=0)
    school_grid = Frame(school_advise)
    school_grid.grid(row=1, column=0)

    # this opens up the urls
    def linking(url):
        webbrowser.open_new(url)

    class Schools:
        def __init__(self, name, sat, acceptance_rate, home_page, diversity, tour):
            self.name = name
            self.sat = sat
            self.acceptance_rate = acceptance_rate
            self.home_page = home_page
            self.diversity = diversity
            self.tour = tour

    # this is the a list of college info which is made using the function above

    kentucky = Schools("University of Kentucky", "1170 - 1290", "90.8%",
                       "http://www.uky.edu/UKHome/",
                       "https://www.collegefactual.com/colleges/university-of-kentucky/student-life/diversity/",
                       "https://www.uky.edu/admission/schedule-tour")

    georgia = Schools("University of Georgia", "1270", "53.9%",
                      "https://www.uga.edu/",
                      "https://www.collegefactual.com/colleges/university-of-georgia/student-life/diversity/chart-overall-diversity.html",
                      "https://visit.uga.edu/tours/")

    columbia = Schools("Columbia University", "1450 - 1580", "6.8%",
                       "https://www.columbia.edu/",
                       "https://www.collegefactual.com/colleges/columbia-university-in-the-city-of-new-york/student-life/diversity/",
                       "https://undergrad.admissions.columbia.edu/visit/tours/campus")

    tech = Schools("Georgia Tech", "1230 - 1600", "25.8%",
                   "https://www.gatech.edu/",
                   "https://www.collegefactual.com/colleges/georgia-institute-of-technology-main-campus/student-life/diversity/",
                   "http://admission.gatech.edu/visit")

    auburn = Schools("Auburn University", "1130 - 1330", "80.5%",
                     "http://www.auburn.edu/",
                     "https://www.collegefactual.com/colleges/auburn-university/student-life/diversity/",
                     "http://www.auburn.edu/admissions/visit/index.php")

    indiana = Schools("Indiana State University", "1240 - 1350", "78.7%",
                      "https://indiana.edu/index.html",
                      "https://www.collegefactual.com/colleges/indiana-university-bloomington/student-life/diversity/",
                      "https://admissions.indiana.edu/visit/index.html")

    arizona = Schools("Arizona State University", "1230 - 1600", "82.5%",
                      "https://www.asu.edu/",
                      "https://datausa.io/profile/university/arizona-state-university-tempe",
                      "https://visit.asu.edu/")

    ung = Schools("University of North Georgia", "1020 - 1100", "75%",
                  "https://ung.edu/",
                  "https://www.collegefactual.com/colleges/university-of-north-georgia/student-life/diversity/",
                  "https://ung.edu/undergraduate-admissions/visit/index.php")

    cali_state = Schools("California State University", "1100, 1300", "63.70%",
                         "https://www2.calstate.edu/",
                         "https://www2.calstate.edu/impact-of-the-csu/diversity",
                         "http://www.calstatela.edu/studentservices/nspp/campus-tours")

    scad = Schools("Savannah College of Art and Design", "1110 - 1600", "71.70%",
                   "https://www.scad.edu/",
                   "https://www.collegefactual.com/colleges/savannah-college-of-art-and-design/student-life/diversity/",
                   "https://www.visitsavannah.com/article/how-to-experience-the-savannah-college-art-and-design")

    clemson = Schools("Clemson University", "1220 - 1390", "50.5%",
                      "http://www.clemson.edu/",
                      "https://www.collegefactual.com/colleges/clemson-university/student-life/diversity/",
                      "http://www.clemson.edu/visit/")

    art_atlanta = Schools("Art Institute of Atlanta", "840 - 1300", "43%",
                          "https://www.artinstitutes.edu/atlanta",
                          "https://www.collegefactual.com/colleges/the-art-institute-of-atlanta/student-life/diversity/",
                          "https://www.artinstitutes.edu/atlanta/admissions/visit-us/appointment")

    harvard = Schools("Harvard", "1460 - 1600", "5.4%",
                      "https://www.harvard.edu/",
                      "https://datausa.io/profile/university/harvard-university",
                      "https://www.harvard.edu/on-campus/visit-harvard/tours")

    advise_two = Label(school_intro, text="Some colleges you should look into based on interest: ")
    advise_two.grid(row=0, column=0)

    # this is a colleges that would apppear depending on the users interests
    # this shows name, sat, acceptance rate, diversity link, home page link, and tour link

    if max_place == 0:
        print(smart)
        if smart < 6.25:
            school_name = Label(school_grid, text=kentucky.name, font=font3)
            school_name.grid(row=0, column=0)
            school_gpa = Label(school_grid, text=("Average SAT score: %s " % kentucky.sat), font=normal_font3)
            school_gpa.grid(row=1, column=0)
            school_acceptance = Label(school_grid, text="Acceptance Rate: %s" % kentucky.acceptance_rate)
            school_acceptance.grid(row=2, column=0)
            school_website = Label(school_grid, text="Home Page", font=sub_font3, cursor="hand2", fg="blue")
            school_website.grid(row=3, column=0)
            school_website.bind("<Button-1>", lambda e: linking(kentucky.home_page))
            school_diversity = Label(school_grid, text="Click to learn about school's Diversity",
                                     cursor="hand2", fg="blue")
            school_diversity.grid(row=4, column=0)
            school_diversity.bind("<Button-1>", lambda e: linking(kentucky.diversity))
            school_tour = Label(school_grid, text="Click for information about school tour", fg="blue", cursor="hand2")
            school_tour.grid(row=5, column=0)
            school_tour.bind("<Button-1>", lambda e: linking(kentucky.tour))
        else:
            school_name = Label(school_grid, text=tech.name, font=font3)
            school_name.grid(row=0, column=0)
            school_gpa = Label(school_grid, text=("Average SAT score: %s " % tech.sat), font=normal_font3)
            school_gpa.grid(row=1, column=0)
            school_acceptance = Label(school_grid, text="Acceptance Rate: %s" % kentucky.acceptance_rate)
            school_acceptance.grid(row=2, column=0)
            school_website = Label(school_grid, text="Home Page", font=sub_font3, cursor="hand2", fg="blue")
            school_website.grid(row=3, column=0)
            school_website.bind("<Button-1>", lambda e: linking(tech.home_page))
            school_diversity = Label(school_grid, text="Click to learn about school's Diversity",
                                     cursor="hand2", fg="blue")
            school_diversity.grid(row=4, column=0)
            school_diversity.bind("<Button-1>", lambda e: linking(tech.diversity))
            school_tour = Label(school_grid, text="Click for information about school tour", fg="blue",
                                cursor="hand2")
            school_tour.grid(row=5, column=0)
            school_tour.bind("<Button-1>", lambda e: linking(tech.tour))

        v_space(school_grid, 6, 0)

        school_name = Label(school_grid, text=georgia.name, font=font3)
        school_name.grid(row=7, column=0)
        school_gpa = Label(school_grid, text=("Average SAT score: %s " % georgia.sat), font=normal_font3)
        school_gpa.grid(row=8, column=0)
        school_acceptance = Label(school_grid, text="Acceptance Rate: %s" % georgia.acceptance_rate)
        school_acceptance.grid(row=9, column=0)
        school_website = Label(school_grid, text="Home Page", font=sub_font3, cursor="hand2", fg="blue")
        school_website.grid(row=10, column=0)
        school_website.bind("<Button-1>", lambda e: linking(georgia.home_page))
        school_diversity = Label(school_grid, text="Click to learn about school's Diversity",
                                 cursor="hand2", fg="blue")
        school_diversity.grid(row=11, column=0)
        school_diversity.bind("<Button-1>", lambda e: linking(georgia.diversity))
        school_tour = Label(school_grid, text="Click for information about school tour", fg="blue", cursor="hand2")
        school_tour.grid(row=12, column=0)
        school_tour.bind("<Button-1>", lambda e: linking(georgia.tour))

    if max_place == 1:
        school_name = Label(school_grid, text=columbia.name, font=font3)
        school_name.grid(row=0, column=0)
        school_gpa = Label(school_grid, text=("Average SAT score: %s " % columbia.sat), font=normal_font3)
        school_gpa.grid(row=1, column=0)
        school_acceptance = Label(school_grid, text="Acceptance Rate: %s" % columbia.acceptance_rate)
        school_acceptance.grid(row=2, column=0)
        school_website = Label(school_grid, text="Home Page", font=sub_font3, cursor="hand2", fg="blue")
        school_website.grid(row=3, column=0)
        school_website.bind("<Button-1>", lambda e: linking(columbia.home_page))
        school_diversity = Label(school_grid, text="Click to learn about school's Diversity",
                                 cursor="hand2", fg="blue")
        school_diversity.grid(row=4, column=0)
        school_diversity.bind("<Button-1>", lambda e: linking(columbia.diversity))
        school_tour = Label(school_grid, text="Click for information about school tour", fg="blue", cursor="hand2")
        school_tour.grid(row=5, column=0)
        school_tour.bind("<Button-1>", lambda e: linking(columbia.tour))

        v_space(school_grid, 6, 0)

        school_name = Label(school_grid, text=tech.name, font=font3)
        school_name.grid(row=7, column=0)
        school_gpa = Label(school_grid, text=("Average SAT score: %s " % tech.sat), font=normal_font3)
        school_gpa.grid(row=8, column=0)
        school_acceptance = Label(school_grid, text="Acceptance Rate: %s" % tech.acceptance_rate)
        school_acceptance.grid(row=9, column=0)
        school_website = Label(school_grid, text="Home Page", font=sub_font3, cursor="hand2", fg="blue")
        school_website.grid(row=10, column=0)
        school_website.bind("<Button-1>", lambda e: linking(tech.home_page))
        school_diversity = Label(school_grid, text="Click to learn about school's Diversity",
                                 cursor="hand2", fg="blue")
        school_diversity.grid(row=11, column=0)
        school_diversity.bind("<Button-1>", lambda e: linking(tech.diversity))
        school_tour = Label(school_grid, text="Click for information about school tour", fg="blue", cursor="hand2")
        school_tour.grid(row=12, column=0)
        school_tour.bind("<Button-1>", lambda e: linking(tech.tour))

    if max_place == 2:
        school_name = Label(school_grid, text=indiana.name, font=font3)
        school_name.grid(row=0, column=0)
        school_gpa = Label(school_grid, text=("Average SAT score: %s " % indiana.sat), font=normal_font3)
        school_gpa.grid(row=1, column=0)
        school_acceptance = Label(school_grid, text="Acceptance Rate: %s" % indiana.acceptance_rate)
        school_acceptance.grid(row=2, column=0)
        school_website = Label(school_grid, text="Home Page", font=sub_font3, cursor="hand2", fg="blue")
        school_website.grid(row=3, column=0)
        school_website.bind("<Button-1>", lambda e: linking(indiana.home_page))
        school_diversity = Label(school_grid, text="Click to learn about school's Diversity",
                                 cursor="hand2", fg="blue")
        school_diversity.grid(row=4, column=0)
        school_diversity.bind("<Button-1>", lambda e: linking(indiana.diversity))
        school_tour = Label(school_grid, text="Click for information about school tour", fg="blue", cursor="hand2")
        school_tour.grid(row=5, column=0)
        school_tour.bind("<Button-1>", lambda e: linking(indiana.tour))
        v_space(school_grid, 6, 0)

        school_name = Label(school_grid, text=auburn.name, font=font3)
        school_name.grid(row=7, column=0)
        school_gpa = Label(school_grid, text=("Average SAT score: %s " % auburn.sat), font=normal_font3)
        school_gpa.grid(row=8, column=0)
        school_acceptance = Label(school_grid, text="Acceptance Rate: %s" % auburn.acceptance_rate)
        school_acceptance.grid(row=9, column=0)
        school_website = Label(school_grid, text="Home Page", font=sub_font3, cursor="hand2", fg="blue")
        school_website.grid(row=10, column=0)
        school_website.bind("<Button-1>", lambda e: linking(auburn.home_page))
        school_diversity = Label(school_grid, text="Click to learn about school's Diversity",
                                 cursor="hand2", fg="blue")
        school_diversity.grid(row=11, column=0)
        school_diversity.bind("<Button-1>", lambda e: linking(auburn.diversity))
        school_tour = Label(school_grid, text="Click for information about school tour", fg="blue", cursor="hand2")
        school_tour.grid(row=12, column=0)
        school_tour.bind("<Button-1>", lambda e: linking(auburn.tour))

    if max_place == 3:
        school_name = Label(school_grid, text=arizona.name, font=font3)
        school_name.grid(row=0, column=0)
        school_gpa = Label(school_grid, text=("Average SAT score: %s " % arizona.sat), font=normal_font3)
        school_gpa.grid(row=1, column=0)
        school_acceptance = Label(school_grid, text="Acceptance Rate: %s" % arizona.acceptance_rate)
        school_acceptance.grid(row=2, column=0)
        school_website = Label(school_grid, text="Home Page", font=sub_font3, cursor="hand2", fg="blue")
        school_website.grid(row=3, column=0)
        school_website.bind("<Button-1>", lambda e: linking(arizona.home_page))
        school_diversity = Label(school_grid, text="Click to learn about school's Diversity",
                                 cursor="hand2", fg="blue")
        school_diversity.grid(row=4, column=0)
        school_diversity.bind("<Button-1>", lambda e: linking(arizona.diversity))
        school_tour = Label(school_grid, text="Click for information about school tour", fg="blue", cursor="hand2")
        school_tour.grid(row=5, column=0)
        school_tour.bind("<Button-1>", lambda e: linking(arizona.tour))
        v_space(school_grid, 6, 0)

        school_name = Label(school_grid, text=ung.name, font=font3)
        school_name.grid(row=7, column=0)
        school_gpa = Label(school_grid, text=("Average SAT score: %s " % ung.sat), font=normal_font3)
        school_gpa.grid(row=8, column=0)
        school_acceptance = Label(school_grid, text="Acceptance Rate: %s" % ung.acceptance_rate)
        school_acceptance.grid(row=9, column=0)
        school_website = Label(school_grid, text="Home Page", font=sub_font3, cursor="hand2", fg="blue")
        school_website.grid(row=10, column=0)
        school_website.bind("<Button-1>", lambda e: linking(ung.home_page))
        school_diversity = Label(school_grid, text="Click to learn about school's Diversity",
                                 cursor="hand2", fg="blue")
        school_diversity.grid(row=11, column=0)
        school_diversity.bind("<Button-1>", lambda e: linking(ung.diversity))
        school_tour = Label(school_grid, text="Click for information about school tour", fg="blue", cursor="hand2")
        school_tour.grid(row=12, column=0)
        school_tour.bind("<Button-1>", lambda e: linking(ung.tour))
    if max_place == 4:
        school_name = Label(school_grid, text=cali_state.name, font=font3)
        school_name.grid(row=0, column=0)
        school_gpa = Label(school_grid, text=("Average SAT score: %s " % cali_state.sat), font=normal_font3)
        school_gpa.grid(row=1, column=0)
        school_acceptance = Label(school_grid, text="Acceptance Rate: %s" % cali_state.acceptance_rate)
        school_acceptance.grid(row=2, column=0)
        school_website = Label(school_grid, text="Home Page", font=sub_font3, cursor="hand2", fg="blue")
        school_website.grid(row=3, column=0)
        school_website.bind("<Button-1>", lambda e: linking(cali_state.home_page))
        school_diversity = Label(school_grid, text="Click to learn about school's Diversity",
                                 cursor="hand2", fg="blue")
        school_diversity.grid(row=4, column=0)
        school_diversity.bind("<Button-1>", lambda e: linking(cali_state.diversity))
        school_tour = Label(school_grid, text="Click for information about school tour", fg="blue", cursor="hand2")
        school_tour.grid(row=5, column=0)
        school_tour.bind("<Button-1>", lambda e: linking(cali_state.tour))
        v_space(school_grid, 6, 0)

        school_name = Label(school_grid, text=clemson.name, font=font3)
        school_name.grid(row=7, column=0)
        school_gpa = Label(school_grid, text=("Average SAT score: %s " % clemson.sat), font=normal_font3)
        school_gpa.grid(row=8, column=0)
        school_acceptance = Label(school_grid, text="Acceptance Rate: %s" % clemson.acceptance_rate)
        school_acceptance.grid(row=9, column=0)
        school_website = Label(school_grid, text="Home Page", font=sub_font3, cursor="hand2", fg="blue")
        school_website.grid(row=10, column=0)
        school_website.bind("<Button-1>", lambda e: linking(clemson.home_page))
        school_diversity = Label(school_grid, text="Click to learn about school's Diversity",
                                 cursor="hand2", fg="blue")
        school_diversity.grid(row=11, column=0)
        school_diversity.bind("<Button-1>", lambda e: linking(clemson.diversity))
        school_tour = Label(school_grid, text="Click for information about school tour", fg="blue", cursor="hand2")
        school_tour.grid(row=12, column=0)
        school_tour.bind("<Button-1>", lambda e: linking(clemson.tour))
    if max_place == 5:
        school_name = Label(school_grid, text=scad.name, font=font3)
        school_name.grid(row=0, column=0)
        school_gpa = Label(school_grid, text=("Average SAT score: %s " % scad.sat), font=normal_font3)
        school_gpa.grid(row=1, column=0)
        school_acceptance = Label(school_grid, text="Acceptance Rate: %s" % scad.acceptance_rate)
        school_acceptance.grid(row=2, column=0)
        school_website = Label(school_grid, text="Home Page", font=sub_font3, cursor="hand2", fg="blue")
        school_website.grid(row=3, column=0)
        school_website.bind("<Button-1>", lambda e: linking(scad.home_page))
        school_diversity = Label(school_grid, text="Click to learn about school's Diversity",
                                 cursor="hand2", fg="blue")
        school_diversity.grid(row=4, column=0)
        school_diversity.bind("<Button-1>", lambda e: linking(scad.diversity))
        school_tour = Label(school_grid, text="Click for information about school tour", fg="blue", cursor="hand2")
        school_tour.grid(row=5, column=0)
        school_tour.bind("<Button-1>", lambda e: linking(scad.tour))
        v_space(school_grid, 6, 0)

        school_name = Label(school_grid, text=art_atlanta.name, font=font3)
        school_name.grid(row=7, column=0)
        school_gpa = Label(school_grid, text=("Average SAT score: %s " % art_atlanta.sat), font=normal_font3)
        school_gpa.grid(row=8, column=0)
        school_acceptance = Label(school_grid, text="Acceptance Rate: %s" % art_atlanta.acceptance_rate)
        school_acceptance.grid(row=9, column=0)
        school_website = Label(school_grid, text="Home Page", font=sub_font3, cursor="hand2", fg="blue")
        school_website.grid(row=10, column=0)
        school_website.bind("<Button-1>", lambda e: linking(art_atlanta.home_page))
        school_diversity = Label(school_grid, text="Click to learn about school's Diversity",
                                 cursor="hand2", fg="blue")
        school_diversity.grid(row=11, column=0)
        school_diversity.bind("<Button-1>", lambda e: linking(art_atlanta.diversity))
        school_tour = Label(school_grid, text="Click for information about school tour", fg="blue", cursor="hand2")
        school_tour.grid(row=12, column=0)
        school_tour.bind("<Button-1>", lambda e: linking(art_atlanta.tour))


def community_service_page():
    # this asks for the amount of community service hours you are in
    # as well as you gpa, providing a link to to check
    def next_page():
        short_page.destroy()
        showing_results()

    def callback(link):
        webbrowser.open_new(link)

    print("final page")
    short_page = Frame(root)
    short_page.grid(row=0, column=0)

    title = Label(short_page, text="Community Service", font=font)
    title.grid(row=0, column=0, sticky=W)

    prompt = Label(short_page, text="How many community service hours do you have: ")
    prompt.grid(row=1, column=0)
    prompt_entry = Entry(short_page, textvariable=serviceHours)
    prompt_entry.grid(row=1, column=1)

    next = Button(short_page, text="Next")
    next.grid(row=3, column=0)
    next.config(command=next_page)

    v_space(short_page, 4, 0)

    gpa_label = Label(short_page, text="Type in your GPA:")
    gpa_label.grid(row=5, column=0)

    gpa_entry = Entry(short_page, textvariable=gpa)
    gpa_entry.grid(row=5, column=1)

    gpa_warning = Label(short_page, text="If you do not know your GPA, click on the link.")
    gpa_warning.grid(row=6, column=0)

    gpa_link = Label(short_page, text="GPA Calculator", cursor="hand2", fg="blue")
    gpa_link.bind("<Button-1>", lambda e: callback("https://gpacalculator.net/high-school-gpa-calculator/"))
    gpa_link.grid(row=7, column=0)


def interests_service():
    def service():
        print("Print service part, finish category scores before doing this part")

    def scale_label(type, text, row):
        v_space(last_screen_hopefully, row, 0)
        row += 1
        type = Label(last_screen_hopefully, text=text, font=font)
        type.grid(row=row, column=0)
        row += 1

    def scale_data():
        # this adds all the scores to a list and then clears the window
        category_scores.append(sp.get())
        category_scores.append(sm.get())
        category_scores.append(hf.get())
        category_scores.append(ld.get())
        category_scores.append(rb.get())
        category_scores.append(cr.get())
        print(category_scores)
        last_screen_hopefully.destroy()
        community_service_page()

    cat = 0
    row = 2
    last_screen_hopefully = Frame(root)
    last_screen_hopefully.grid(row=0, column=0)
    # this makes the scalers for insterests
    t = Label(last_screen_hopefully, text="Interest:", font=("Helvetica", "18", "bold"))
    t.grid(row=0, column=0)
    # --------------------------
    scale_label(categories[cat], categories[cat], row)
    cat += 1
    row += 2
    sp = Scale(last_screen_hopefully, from_=0, to=100, orient=HORIZONTAL)
    sp.grid(row=row, column=0)
    row += 1
    # ------------------------
    scale_label(categories[cat], categories[cat], row)
    row += 2
    cat += 1
    sm = Scale(last_screen_hopefully, from_=0, to=100, orient=HORIZONTAL)
    sm.grid(row=row, column=0)
    row += 1
    # ----------------------------
    scale_label(categories[cat], categories[cat], row)
    cat += 1
    row += 2
    hf = Scale(last_screen_hopefully, from_=0, to=100, orient=HORIZONTAL)
    hf.grid(row=row, column=0)
    row += 1
    # -----------------------------
    scale_label(categories[cat], categories[cat], row)
    cat += 1
    row += 2
    ld = Scale(last_screen_hopefully, from_=0, to=100, orient=HORIZONTAL)
    ld.grid(row=row, column=0)
    row += 1
    # --------------------------------
    scale_label(categories[cat], categories[cat], row)
    row += 2
    cat += 1
    rb = Scale(last_screen_hopefully, from_=0, to=100, orient=HORIZONTAL)
    rb.grid(row=row, column=0)
    row += 1
    # --------------------------------------------
    scale_label(categories[cat], categories[cat], row)
    row += 2
    cat += 1
    cr = Scale(last_screen_hopefully, from_=0, to=100, orient=HORIZONTAL)
    cr.grid(row=row, column=0)
    row += 1
    # ----------------------------------------------
    v_space(last_screen_hopefully, row, 0)
    row += 1
    cont = Button(last_screen_hopefully, text="Continue")
    cont.grid(row=row, column=0)
    cont.config(command=scale_data)


def check_club():
    global c, clubs_screen, cl
    # this checks if the club is in the school
    l1 = 0
    w1 = 0
    l2 = 0
    repeat = int(amount.get())
    added_clubs = Frame(root)
    added_clubs.grid(row=2, column=1)
    cl = club.get()
    if cl in clubs_in_school:
        cs.append(cl)
        print(cs)
        added = Label(c, text=cs)
        added.grid(row=10, column=0)
    else:
        while w1 != len(clubs_in_school):
            if cl == clubs_in_school[w1]:
                print(clubs_in_school[w1])
                w1 += 1
            else:
                club_error()
                w1 += 1
                break
    if len(cs) == repeat:
        b = Button(added_clubs, text="Done", width=25, height=1)
        b.grid(row=1, column=0)
        b.config(command=interests_service)
        added_clubs.destroy()
        c.destroy()
        clubs_screen.destroy()
        interests_service()


def clubs():
    # if they clicked they are in 1 or more this would ask for which ones
    global amount, club, c
    club = StringVar()
    i = 0
    ex: int = 1
    ey: int = 0

    c = Frame(root)
    c.grid(row=2, column=0)

    v_space(c, 0, 0)

    instructions = Label(c, text="Enter Club Name:")
    instructions.grid(row=1, column=0)

    h_space(c, 1, 1)

    e = Entry(c, textvariable=club)
    e.grid(row=2, column=0)

    v_space(c, 3, ey)
    ex += 1
    ey += 1

    b = Button(c, text="Next")
    b.grid(row=4, column=0)
    b.config(command=check_club)

    h_space(c, 4, 1)


def clubs_amount():
    def in_club():
        r = int(amount.get())
        print(r)

        if r == 0:
            clubs_screen.destroy()
            interests_service()
        if r > 0:
            clubs()

    # this asks for the amount fo clubs their in.

    print("In new window")
    global clubs_screen

    clubs_screen = Frame(root)
    clubs_screen.grid(row=1, column=0)

    title = Label(clubs_screen, text="Clubs", font=("Helvetica", "18", "bold"))
    title.grid(row=0, column=0, sticky=W)

    amount_of_clubs = Label(clubs_screen, text="How many clubs are you in?")
    amount_of_clubs.grid(row=1, column=0)

    amount_entry = Entry(clubs_screen, textvariable=amount)
    amount_entry.grid(row=1, column=1)

    v_space(clubs_screen, 2, 0)
    v_space(clubs_screen, 2, 1)

    after_club_amount = Button(clubs_screen, text="Next")
    after_club_amount.grid(row=1, column=2)
    after_club_amount.config(command=in_club)

    pass


def next():
    global mathType, scienceType, ssType, litType
    i = 0
    clicked = 0
    print("Class Scores")

    # list of all check boxes
    mathSection = [mVar.get(), mVar1.get(), mVar2.get(), mVar3.get()]
    scienceSection = [sVar.get(), sVar1.get(), sVar2.get(), sVar3.get()]
    ssSection = [ssVar.get(), ssVar1.get(), ssVar2.get(), ssVar3.get()]
    lit_section = [litVar.get(), litVar1.get(), litVar2.get(), litVar3.get()]

    # this checks for each column if the user checked 1 box only per column
    while i < len(mathSection):
        if mathSection[i] == 1:
            mathType = i
            mathType += 1
            clicked -= 1
            i += 1
            print("Math Score: ", mathType)
        else:
            i += 1
            clicked += 1

    if clicked != 3 and mathType == 0:
        error()

    clicked = 0
    i = 0

    while i < len(scienceSection):
        if scienceSection[i] == 1:
            scienceType = i
            scienceType += 1
            i += 1
            clicked -= 1
            print("Science type: ", scienceType)
        else:
            i += 1
            clicked += 1

    if clicked != 3 and scienceType == 0:
        error()

    i = 0
    clicked = 0

    while i < len(ssSection):
        if ssSection[i] == 1:
            ssType = i
            ssType += 1
            clicked -= 0
            print("Social Studies: ", ssType)
            i += 1
        else:
            i += 1
            clicked += 1

    if clicked != 3 and ssType == 0:
        error()
    i = 0
    clicked = 0

    while i < len(lit_section):
        if lit_section[i] == 1:
            litType = i
            litType += 1
            clicked -= 1
            i += 1
            print("Language Arts: ", litType)
        else:
            i += 1
            clicked += 1

    if clicked != 3 and litType == 0:
        error()
    ctype = [mathType, scienceType, ssType, litType]
    smart = mathType + scienceType + ssType + litType / 4
    print(smart)
    if 0 in ctype:
        error()
    else:
        ClassWindow.destroy()
        InstructionsWindow.destroy()
        bottomWindow.destroy()
        print("Making new window...")
        clubs_amount()


# this is the set up of the first window
In = Label(InstructionsWindow, text=Instructions)
In.grid(row=0, column=0)

v_space(InstructionsWindow, 1, 0)

title = Label(InstructionsWindow, text="Classes: ", font=font)
title.grid(row=2, column=0)

v_space(InstructionsWindow, 3, 0)

m = Label(ClassWindow, text=classButtons[0], font=subt)
m.grid(row=0, column=0)
# the chunked lines a rows and each chunk is a column
m1 = Checkbutton(ClassWindow, text=difficulty[0], variable=mVar)
m1.grid(row=1, column=0, sticky=W)
m2 = Checkbutton(ClassWindow, text=difficulty[1], variable=mVar1)
m2.grid(row=2, column=0, sticky=W)
m3 = Checkbutton(ClassWindow, text=difficulty[2], variable=mVar2)
m3.grid(row=3, column=0, sticky=W)
m4 = Checkbutton(ClassWindow, text=difficulty[3], variable=mVar3)
m4.grid(row=4, column=0, sticky=W)

h_space(ClassWindow, 0, 1)

s = Label(ClassWindow, text=classButtons[1], font=subt)
s.grid(row=0, column=2)

s1 = Checkbutton(ClassWindow, text=difficulty[0], variable=sVar)
s1.grid(row=1, column=2, sticky=W)
s1 = Checkbutton(ClassWindow, text=difficulty[1], variable=sVar1)
s1.grid(row=2, column=2, sticky=W)
s1 = Checkbutton(ClassWindow, text=difficulty[2], variable=sVar2)
s1.grid(row=3, column=2, sticky=W)
s1 = Checkbutton(ClassWindow, text=difficulty[3], variable=sVar3)
s1.grid(row=4, column=2, sticky=W)

h_space(ClassWindow, 0, 3)

ss = Label(ClassWindow, text=classButtons[2], font=subt)
ss.grid(row=0, column=4)

ss1 = Checkbutton(ClassWindow, text=difficulty[0], variable=ssVar)
ss1.grid(row=1, column=4, sticky=W)
ss2 = Checkbutton(ClassWindow, text=difficulty[1], variable=ssVar1)
ss2.grid(row=2, column=4, sticky=W)
ss3 = Checkbutton(ClassWindow, text=difficulty[2], variable=ssVar2)
ss3.grid(row=3, column=4, sticky=W)
ss4 = Checkbutton(ClassWindow, text=difficulty[3], variable=ssVar3)
ss4.grid(row=4, column=4, sticky=W)

h_space(ClassWindow, 0, 5)

la = Label(ClassWindow, text=classButtons[3], font=subt)
la.grid(row=0, column=6)

la1 = Checkbutton(ClassWindow, text=difficulty[0], variable=litVar)
la1.grid(row=1, column=6, sticky=W)
la1 = Checkbutton(ClassWindow, text=difficulty[1], variable=litVar1)
la1.grid(row=2, column=6, sticky=W)
la1 = Checkbutton(ClassWindow, text=difficulty[2], variable=litVar2)
la1.grid(row=3, column=6, sticky=W)
la1 = Checkbutton(ClassWindow, text=difficulty[3], variable=litVar3)
la1.grid(row=4, column=6, sticky=W)

h_space(ClassWindow, 0, 7)

c = Label(ClassWindow, text=classButtons[4], font=subt)
c.grid(row=0, column=8)

c1 = Checkbutton(ClassWindow, text=ExtraClass[0])
c1.grid(row=1, column=8, sticky=W)
c1 = Checkbutton(ClassWindow, text=ExtraClass[1])
c1.grid(row=2, column=8, sticky=W)
c1 = Checkbutton(ClassWindow, text=ExtraClass[2])
c1.grid(row=3, column=8, sticky=W)
c1 = Checkbutton(ClassWindow, text=ExtraClass[3])
c1.grid(row=4, column=8, sticky=W)
c1 = Checkbutton(ClassWindow, text=ExtraClass[4])
c1.grid(row=1, column=9, sticky=W)
c1 = Checkbutton(ClassWindow, text=ExtraClass[5])
c1.grid(row=2, column=9, sticky=W)
c1 = Checkbutton(ClassWindow, text=ExtraClass[6])
c1.grid(row=3, column=9, sticky=W)
c1 = Checkbutton(ClassWindow, text=ExtraClass[7])
c1.grid(row=4, column=9, sticky=W)

v_space(bottomWindow, 0, 0)

nextButton = Button(bottomWindow, text="Next", width=9, height=1)
nextButton.grid(row=1, column=0)
nextButton.config(command=next)

root.mainloop()

