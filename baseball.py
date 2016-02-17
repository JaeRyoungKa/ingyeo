import random

# chance of result
hr = 1
out = 9
flyout = 4
foul = 3
h1 = 8
h2 = 3
h3 = 1
total = hr+out+h1+h2+h3+flyout+foul

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
    global inn
    global runnerlist
    global sub
    global team1
    global team2
    while(inn<=9):
        out = strike = ball = 0
        runnerlist = []
        while(not(out>=3)):
            temp = input('입력? (h for hitting, n for not hitting)')
            if temp == 'h':
                if random.randrange(0,100)<= 40:
                    global result
                    result = batting()
                    if(result=="hr"):
                        score()
                        strike = ball = 0
                    if(result=="out"):
                        out += 1
                        strike = ball = 0
                    if(result=="h1"):
                        run(1)
                        strike = ball = 0
                    if(result=="h2"):
                        run(2)
                        strike = ball = 0
                    if(result=="h3"):
                        run(3)
                        strike = ball = 0
                    if(result=="hr"):
                        if sub:
                            team1 += len(runnerlist)
                        if not sub:
                            team2 += len(runnerlist)
                        runnerlist = []
                        strike = ball = 0
                    if(result=="foul"):
                        if(strike==2):
                            strike += 0
                        else:
                            strike += 1
                    if(result=="flyout"):
                        out +=1
                        if not (out==3):
                            flyrun()
                        strike = ball = 0
                else:
                    strike += 1
                    result="헛스윙"
                    if strike == 3:
                        out +=1
                        strike = ball = 0
                        result="스트라이크 아웃"

            if temp == 'n':
                if random.randrange(0,100)<=60:
                    ball += 1
                    result='볼'
                    if ball == 4:
                        run(1)
                        strike = ball = 0
                        result="볼넷"
                else:
                    strike += 1
                    result="스트라이크"
                    if strike == 3:
                        out +=1
                        strike = ball = 0
                        result='스트라이크 아웃'
            print(result,ball,"볼",strike,"스트라이크",inn,"회",sub,runnerlist,out,"아웃",team1,":",team2)
        if not sub:
            inn += 1
        sub = not sub
        print("===========이닝교체=============")


def run(much):
    global runnerlist
    temp = []
    for runner in runnerlist:
        temp.append(runner+much)
    temp.append(much)
    for i in range(0,4):
        for runner in temp:
            if(runner >= 4):
                score()
                temp.remove(runner)
    runnerlist = temp
    runnerlist.sort()

def flyrun():
    global runnerlist
    temp = []
    for runner in runnerlist:
        if not (runner==1):
            temp.append(runner+1)
    for i in range(0,4):
        for runner in temp:
            if(runner >= 4):
                score()
                temp.remove(runner)
    runnerlist = temp
    runnerlist.sort()

process()