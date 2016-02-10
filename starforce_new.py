import random
successrate1 = [95,90,85,80,75,70,65,60,55,45,35,30,30,30,30,30,30,30,30,30,30,30]
success_bonus = [4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5]
successrate = successrate1 + success_bonus
destroyrate = [0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,3,3,3,4,4,10,10]
costtable = [0.00136,0.00271,0.00406,0.00541,0.00676,0.00811,0.00946,0.01081,0.01216,0.01351,0.109407,0.138377,0.17175800,0.209802,0.252759,0.300872,0.354379,0.413514,0.3478506,0.549582,0.626964,0.710872]

cost = 0
star = 0
a = 0
ct = 0

while not a == "exit":
 a = raw_input()
 if a == "":
  if ct == 2:
   cost += costtable[star]
   star += 1
   ct = 0
   print "SUCCESS by a chance time!"
  else:
   if random.random() * 100 < successrate[star]:
    cost += costtable[star]
    star += 1
    print "SUCCESS"
    ct = 0
   elif random.random() * 100 < destroyrate[star]:
    cost += costtable[star]
    star = 0
    print "DESTROYED"
    ct = 0
   else:
    if star < 6:
     print "FAILED"
     cost += costtable[star]
     ct = 0
    elif star == 10:
     print "FAILED"
     cost += costtable[star]
     ct = 0
    elif star == 15:
     print "FAILED"
     cost += costtable[star]
     ct = 0
    elif star == 20:
     print "FAILED"
     cost += costtable[star]
     ct = 0
    else:
     print "FAILED"
     cost += costtable[star]
     star -= 1
     ct += 1
  print "Current" , star , "Stars", ", cost :", cost
  print "Mesos needed : ", int(round(costtable[star]*100000000,-2))