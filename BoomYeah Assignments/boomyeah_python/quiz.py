#Create a program wherein the user will take a 5-question quiz with multiple choice.

#The quiz accepts answers in lower or uppercase. If the answer is not part of the choices, A comment of "Please enter a valid answer" will prompt.

#After answering the 5 questions, a score (in percentage) will be displayed.

def main():
    questions = ['1.    Who designed Python?', '2. Python was released last',
                '3.YouTube is built in']

    options =[ 'a.  Guido Van Rossum, b. Lasmus Lerdorf, c. Matz Matsumoto',
                'a. 1995, b. 2010, c.1991', 'a. PHP, b.Python, c.Ruby']

    answers =['A', 'B', 'C']



    #This prints option1 questions and takes input from the user
    print questions[0],'\n',options[0]
    choice = raw_input("Enter your answer:")
    choice = choice.upper()
    if choice == answers[0]:
       count1 = 100
    elif choice == answers[1] or choice == answers[2]:
        count1 =0

    while choice not in answers:
        print 'Insufficient data'
        choice = raw_input("Enter your answer:")
        choice = choice.upper()
        if choice == answers[0]:
            count1=100
        elif choice == answers[1] or choice == answers[2]:
            count1=0
    #This ends option1
    print
    print
    #This begin option2
    print questions[1],'\n',options[1]
    choice = raw_input("Enter your answer:")
    choice = choice.upper()
    if choice == answers[1]:
        count2=100
    elif choice == answers[0] or choice == answers[2]:
        count2=0

    while choice not in answers:
        print 'Insufficient data'
        choice = raw_input("Enter your answer:")
        choice = choice.upper()
        if choice == answers[1]:
            count2=100
        elif choice == answers[0] or choice == answers[2]:
             count2=0
    print
    print
    #This begins option3

    print questions[2],'\n',options[2]
    choice = raw_input("Enter your answer:")
    choice = choice.upper()
    if choice == answers[1]:
        count3=100
    elif choice == answers[0] or choice == answers[2]:
        count3=0

    while choice not in answers:
        print 'Insufficient data'
        choice = raw_input("Enter your answer:")
        choice = choice.upper()
        if choice == answers[1]:
            count3=100
        elif choice == answers[0] or choice == answers[2]:
             count3=0
    print
    print 'Now! Am counting your score'
    total = count1+ count2+ count3
    score =total/3
    print "Your score is ", score



main()
