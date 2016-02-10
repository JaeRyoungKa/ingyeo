from cs1graphics import *
from time import *
import random

life = Canvas()
life.setBackgroundColor((0,178,232))
life.setWidth(800)
life.setHeight(500)
life.setTitle('Life of KAISTAN')

bg_darkness = Rectangle(400,500)
life.add(bg_darkness)
bg_darkness.moveTo(600,250)
bg_darkness.setFillColor("black")
bg_darkness.setDepth(2)

def setBGColor():
    r1 = 0
    r2 = 180
    r3 = 230
    for _ in range(130):
        if not r2 == 0:
            if random.randrange(1,256) < 181:
                r2 -= 2
        if not r3 == 0:
            if random.randrange(1,256) < 231:
                r3 -= 2
        life.setBackgroundColor((r1,r2,r3))
    r2 = 0
    r3 = 0
    for _ in range(130):
        if not r2 == 180:
            if random.randrange(1,256) < 181:
                r2 += 2
        if not r3 == 230:
            if random.randrange(1,256) < 231:
                r3 += 2
        life.setBackgroundColor((r1,r2,r3))

student = Layer()   
test1 = Circle(30)
test1.moveTo(150,200)
test1.setFillColor("White")

test2 = Rectangle(60,100)
test2.moveTo(150,280)
test2.setFillColor("Darkgreen")
test2.setDepth(3)

test3 = Rectangle(12,50)
test3.moveTo(134,355)
test3.setFillColor("yellow")

test4 = Rectangle(12,50)
test4.moveTo(166,355)
test4.setFillColor("yellow")

test5 = Rectangle(70,12)
test5.moveTo(205,280)
test5.rotate(30)
test5.adjustReference(-70,0)
test5.setDepth(3)
test5.setFillColor("orange")

test6 = Text("CAMPUS")
test6.setFontColor("white")
test6.moveTo(200,30)

test7 = Text("DORM")
test7.setFontColor("white")
test7.moveTo(600,30)
test7.setDepth(1)
student.add(test1)
student.add(test2)
student.add(test3)
student.add(test4)
student.add(test5)

test8 = Text("Year 1")
test8.setFontColor('White')
test8.setDepth(1)
test8.moveTo(200,80)

life.add(test8)
life.add(test6)
life.add(test7)
life.add(student)

def student_move():
    for _ in range(150):
        student.move(2,0)
        test5.flip(75)
        sleep(0.01)
    for _ in range(150):
        student.move(-2,0)
        test5.flip(75)
        sleep(0.01)

def show_animation():
    bachelor = 4
    master = 2
    phd = 6
    i = 1
    setBGColor()
    student_move()    
    while i < bachelor + master + phd:        
        i += 1
        global test8
        life.remove(test8)
        test8 = Text("Year " + str(i))
        life.add(test8)
        test8.setFontColor('White')
        test8.setDepth(1)
        test8.moveTo(200,80)
        setBGColor()
        student_move()         

show_animation()