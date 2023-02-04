q1="""who sacrificed his/her life in avengers end game?
a)natasha
b)iron man
c)thor
d)both a&b"""
q2="""what is the last marvel  movie of phase3?
a)infinity war
b)end game
c)age of ultron
d)none of the above"""
q3="""who killed iron man father?
a)bucky
b)thor
c)iron man
d)nick fury"""
q4="""who is your favourite actress?
a)anupama
b)sai pallavi
c)samanta
d)kajal"""

questions={q1:"d" ,q2:"b" ,q3:"a" ,q4:"a"}

name=input("Hii what your name")
print("hello",name,"welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    x=input("do you want to skip this question?(yes/no):")
    if x=="yes":
        continue
    answer=input("enter your answer:")
    if answer==questions[i]:
        print("wow! you got one point")
        score=score+1
        print("your current score is:",score)
    else:
        print("wrong answer,you lost one point")
        score=score-1
        print("your current score is:",score)
    y=input("do you want to Quit? type (yes/n0)")
    if y=="yes":
        break
print("Your total score is:",score)





