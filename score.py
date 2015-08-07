#prompt score and change it to float
scr=raw_input("Please enter your score")
score=float(scr)
#grading logic
if (score <0 or score >1):
    print "Invalid score: please enter a valid score."
else:
    if score < 0.6:
        print "Your grade is : F"
    elif (score >=0.6 and score <0.7):
        print "Your grade is : D"
    elif (score>=0.7 and score <0.8):
        print "Your grade is : C"
    elif (score >=0.8 and score<0.9):
        print "Your grade is : B"
    else:
       print "Your grade is : A"
