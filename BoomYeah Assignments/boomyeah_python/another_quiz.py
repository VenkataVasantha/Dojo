#Create a program wherein the user will take a 5-question quiz with multiple choice.

#The quiz accepts answers in lower or uppercase. If the answer is not part of the choices, A comment of "Please enter a valid answer" will prompt.

#After answering the 5 questions, a score (in percentage) will be displayed.

def main():

    q1 = {
        'question': 'Who designed Python?',
        'choices': {
            'a': 'Guido Van Rossum',
            'b': 'Lasmus Lerdorf',
            'c': 'Matz Matsumoto'
        },
        'answer': 'a',
    }

    q2 = {
        'question': 'Python was released last?',
        'choices': {
            'a': '1995',
            'b': '2010',
            'c': '1991'
        },
        'answer': 'b',
    }

    q3 = {
        'question': 'Youtube is built in?',
        'choices': {
            'a': 'PHP',
            'b': 'Python',
            'c': 'Ruby'
        },
        'answer': 'b',
    }

    quiz  = [ q1, q2, q3 ]
    score = 0

    for q in quiz:

        # Print Question
        print q['question']

        # Print Choices
        for option in sorted( q['choices'].iterkeys() ):
            print option, '. ', q['choices'][option]

        # Take answer from the user
        choice = raw_input( 'Enter your choice: ' )
        choice = choice.lower()

        while choice not in q['choices'].keys():
            print "Invalid Choice, re-enter choice again"
            choice = raw_input( 'Enter your choice: ' )
            choice = choice.lower()

        if choice == q['answer']:
            score = score + 100
            continue

    print "Total Score: ", score, ' with percentage: ', float( score/len(quiz) ), ' %'

main()
