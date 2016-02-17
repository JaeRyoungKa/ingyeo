import random

# chance of result
hr = 1
out = 9
flyout = 5
foul = 4
h1 = 9
h2 = 3
h3 = 1
total = hr+out+h1+h2+h3

# initial game setting
team1 = 0
team2 = 0
inn = 1
sub = True


def batting():
    dice = random.randrange(0,total)
    if(dice<hr):
        return "hr"
    elif(dice<hr+out):
        return "out"
    elif(dice<hr+out+h1):
        return "h1"
    elif(dice<hr+out+h1+h2):
        return "h2"
    elif(dice<hr+out+h1+h2+h3):
        return "h3"
    elif(dice<hr+out+h1+h2+h3+foul):
        return "foul"
    else:
        return "flyout"

def score():
    global sub
    global team1
    global team2
    if sub:
        team1 += 1
    if not sub:
        team2 += 1


def process():
    while(inn<=9):
        out = strike = ball = 0
        global runnerlist
        global sub
        global inn
        global team1
        global team2
        runnerlist = []
        while(not(out>=3)):
            result = batting()
            if(result=="hr"):
                score()
                runnerlist = []
            if(result=="out"):
                out += 1
            if(result=="h1"):
                run(1)
            if(result=="h2"):
                run(2)
            if(result=="h3"):
                run(3)
            if(result=="hr"):
                run(4)
            if(result=="foul"):
                if(strike==2):
                    strike += 0
                else:
                    strike += 1
            if(result=="flyout"):
                out +=1
            print(inn,"회",runnerlist,out,"아웃",team1,":",team2,result)
        if not sub:
            inn += 1
        sub = not sub


def run(much):
    global runnerlist
    temp = []
    for runner in runnerlist:
        temp.append(runner+much)
    temp.append(much)
    for runner in temp:
        if(runner>=4):
            score()
            temp.remove(runner)
    for runner in temp:
        if(runner>=4):
            score()
            temp.remove(runner)
    runnerlist = temp
    runnerlist.sort()

process()