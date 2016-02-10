import random
star = 0
cost = 0
e_price = 10000


s1 = 0.98
r1 = 0.02
d1 = 0.000
b1 = 0.000

s2 = 0.93
r2 = 0.07
d2 = 0.000
b2 = 0.000

s3 = 0.88
r3 = 0.15
d3 = 0
b3 = 0

s4 = 0.88
r4 = 0.15
d4 = 0
b4 = 0

s5 = 0.83
r5 = 0.2
d5 = 0
b5 = 0

s6 = 0.78
r6 = 0.25
d6 = 0
b6 = 0

s7 = 0.73
r7 = 0
d7 = 0.3
b7 = 0

s8 = 0.68
r8 = 0
d8 = 0.35
b8 = 0

s9 = 0.63
r9 = 0
d9 = 0.4
b9 = 0

s10 = 0.58
r10 = 0
d10 = 0.45
b10 = 0

s11 = 0.48
r11 = 0.55
d11 = 0
b11 = 0

s12 = 0.38
r12 = 0
d12 = 0.65
b12 = 0

s13 = 0.30*1.1
r13 = 0
d13 = 0.693/70*67
b13 = 0.007/70*67

s14 = 0.30*1.1
r14 = 0
d14 = 0.686/70*67
b14 = 0.014/70*67

s15 = 0.30*1.1
r15 = 0
d15 = 0.686/70*67
b15 = 0.014/70*67

s16 = 0.30
r16 = 0.679/70*67
d16 = 0
b16 = 0.021/70*67

s17 = 0.30*1.1
r17 = 0
d17 = 0.679/70*67
b17 = 0.021/70*67

s18 = 0.30*1.1
r18 = 0
d18 = 0.679/70*67
b18 = 0.021/70*67

s19 = 0.30*1.1
r19 = 0
d19 = 0.672/70*67
b19 = 0.028/70*67

s20 = 0.30*1.1
r20 = 0
d20 = 0.672/70*67
b20 = 0.028/70*67

s21 = 0.30*1.1
r21 = 0.63/70*67
d21 = 0
b21 = 0.070/70*67

s22 = 0.30*1.1
r22 = 0
d22 = 0.63/70*67
b22 = 0.070/70*67

cost1 = 13.6
cost2 = 27.1
cost3 = 40.6
cost4 = 54.1
cost5 = 67.6
cost6 = 81.1
cost7 = 94.6
cost8 = 108.1
cost9 = 121.6
cost10 = 135.1
cost11 = 1094.07
cost12 = 1383.77
cost13 = 1717.58
cost14 = 2098.02
cost15 = 2527.59
cost16 = 3008.72
cost17 = 3543.79
cost18 = 4135.14
cost19 = 4785.06
cost20 = 5495.82
cost21 = 6269.64
cost22 = 7108.72

counter = 0
tries = 10000
cul_cost = 0
max_cost = 0
min_cost = 0
goal = 22
ct = 0
ctr = 0
des = 0
star = 0
testrecord = 0

while counter < tries:
	while star < goal:
		if star == 0:
			jujak = random.randint(1,1000)
			cost += cost1
			if jujak < s1*1000 + 1:
				star += 1
				ct = 0
			if s1*1000 < jujak < s1*1000 + r1*1000 + 1:
				star += 0
			if s1*1000 + r1*1000 < jujak < s1*1000 + r1*1000 + d1*1000 + 1:
				star -= 1
			if s1*1000 + r1*1000 + d1*1000 < jujak:
				star = 0
			# print(star)
			if star == goal:
				break

		if star == 1:
			jujak = random.randint(1,1000)
			cost += cost2
			if jujak < s2*1000 + 1:
				star += 1
			if s2*1000 < jujak < s2*1000 + r2*1000 + 1:
				star += 0
			if s2*1000 + r2*1000 < jujak < s2*1000 + r2*1000 + d2*1000 + 1:
				star -= 1
			if s2*1000 + r2*1000 + d2*1000 < jujak:
				star = 0
			# print(star)
			if star == goal:
				break
		if star == 2:
			jujak = random.randint(1,1000)
			cost += cost3
			if jujak < s3*1000 + 1:
				star += 1
			if s3*1000 < jujak < s3*1000 + r3*1000 + 1:
				star += 0	
			if s3*1000 + r3*1000 < jujak < s3*1000 + r3*1000 + d3*1000 + 1:
				star -= 1
			if s3*1000 + r3*1000 + d3*1000 < jujak:
				star = 0
			# print(star)
			if star == goal:
				break
		if star == 3:
			jujak = random.randint(1,1000)
			cost += cost4
			if jujak < s4*1000 + 1:
				star += 1
			if s4*1000 < jujak < s4*1000 + r4*1000 + 1:
				star += 0
			if s4*1000 + r4*1000 < jujak < s4*1000 + r4*1000 + d4*1000 + 1:
				star -= 1
			if s4*1000 + r4*1000 + d4*1000 < jujak:
				star = 0
			# print(star)
			if star == goal:
				break
		if star == 4:
			jujak = random.randint(1,1000)
			cost += cost5
			if jujak < s5*1000 + 1:
				star += 1
			if s5*1000 < jujak < s5*1000 + r5*1000 + 1:
				star += 0
			if s5*1000 + r5*1000 < jujak < s5*1000 + r5*1000 + d5*1000 + 1:
				star -= 1
			if s5*1000 + r5*1000 + d5*1000 < jujak:
				star = 0
			# print(star)
			if star == goal:
				break
		if star == 5:
			jujak = random.randint(1,1000)
			cost += cost6
			if ct == 2:
				star += 1
				ctr += 1
			if jujak < s6*1000 + 1:
				if ct != 2:
					star += 1
					ct = 0
			if s6*1000 < jujak < s6*1000 + r6*1000 + 1:
				if ct != 2:
					star += 0
					ct = 0
			if s6*1000 + r6*1000 < jujak < s6*1000 + r6*1000 + d6*1000 + 1:
				if ct != 2:
					star -= 1
					ct += 1
			if s6*1000 + r6*1000 + d6*1000 < jujak:
				if ct != 2:
					star = 0
					cost += e_price
					des += 1
			if ctr == 1:
				ct = 0
				ctr = 0
			# print(star)
			if star == goal:
				break

		if star == 6:
			jujak = random.randint(1,1000)
			cost += cost7
			if ct == 2:
				star += 1
				ctr += 1
			if jujak < s7*1000 + 1:
				if ct != 2:
					star += 1
					ct = 0
			if s7*1000 < jujak < s7*1000 + r7*1000 + 1:
				if ct != 2:
					star += 0
					ct = 0
			if s7*1000 + r7*1000 < jujak < s7*1000 + r7*1000 + d7*1000 + 1:
				if ct != 2:
					star -= 1
					ct += 1
			if s7*1000 + r7*1000 + d7*1000 < jujak:
				if ct != 2:
					star = 0
					cost += e_price
					des += 1
			if ctr == 1:
				ct = 0
				ctr = 0
			# print(star)
			if star == goal:
				break

		if star == 7:
			jujak = random.randint(1,1000)
			cost += cost8
			if ct == 2:
				star += 1
				ctr += 1
			if jujak < s8*1000 + 1:
				if ct != 2:
					star += 1
					ct = 0
			if s8*1000 < jujak < s8*1000 + r8*1000 + 1:
				if ct != 2:
					star += 0
					ct = 0
			if s8*1000 + r8*1000 < jujak < s8*1000 + r8*1000 + d8*1000 + 1:
				if ct != 2:
					star -= 1
					ct += 1
			if s8*1000 + r8*1000 + d8*1000 < jujak:
				if ct != 2:
					star = 0
					cost += e_price
					des += 1
			if ctr == 1:
				ct = 0
				ctr = 0
			# print(star)
			if star == goal:
				break

		if star == 8:
			jujak = random.randint(1,1000)
			cost += cost9
			if ct == 2:
				star += 1
				ctr += 1
			if jujak < s9*1000 + 1:
				if ct != 2:
					star += 1
					ct = 0
			if s9*1000 < jujak < s9*1000 + r9*1000 + 1:
				if ct != 2:
					star += 0
					ct = 0
			if s9*1000 + r9*1000 < jujak < s9*1000 + r9*1000 + d9*1000 + 1:
				if ct != 2:
					star -= 1
					ct += 1
			if s9*1000 + r9*1000 + d9*1000 < jujak:
				if ct != 2:
					star = 0
					cost += e_price
					des += 1
			if ctr == 1:
				ct = 0
				ctr = 0
			# print(star)
			if star == goal:
				break

		if star == 9:
			jujak = random.randint(1,1000)
			cost += cost10
			if ct == 2:
				star += 1
				ctr += 1
			if jujak < s10*1000 + 1:
				if ct != 2:
					star += 1
					ct = 0
			if s10*1000 < jujak < s10*1000 + r10*1000 + 1:
				if ct != 2:
					star += 0
					ct = 0
			if s10*1000 + r10*1000 < jujak < s10*1000 + r10*1000 + d10*1000 + 1:
				if ct != 2:
					star -= 1
					ct += 1
			if s10*1000 + r10*1000 + d10*1000 < jujak:
				if ct != 2:
					star = 0
					cost += e_price
					des += 1
			if ctr == 1:
				ct = 0
				ctr = 0
			# print(star)
			if star == goal:
				break

		if star == 10:
			jujak = random.randint(1,1000)
			cost += cost11
			if ct == 2:
				star += 1
				ctr += 1
			if jujak < s11*1000 + 1:
				if ct != 2:
					star += 1
					ct = 0
			if s11*1000 < jujak < s11*1000 + r11*1000 + 1:
				if ct != 2:
					star += 0
					ct = 0
			if s11*1000 + r11*1000 < jujak < s11*1000 + r11*1000 + d11*1000 + 1:
				if ct != 2:
					star -= 1
					ct += 1
			if s11*1000 + r11*1000 + d11*1000 < jujak:
				if ct != 2:
					star = 0
					cost += e_price
					des += 1
			if ctr == 1:
				ct = 0
				ctr = 0
			# print(star)
			# print(ct)
			if star == goal:
				break

		if star == 11:
			jujak = random.randint(1,1000)
			cost += cost12
			if ct == 2:
				star += 1
				ctr += 1
			if jujak < s12*1000 + 1:
				if ct != 2:
					star += 1
					ct = 0
			if s12*1000 < jujak < s12*1000 + r12*1000 + 1:
				if ct != 2:
					star += 0
					ct = 0
			if s12*1000 + r12*1000 < jujak < s12*1000 + r12*1000 + d12*1000 + 1:
				if ct != 2:
					star -= 1
					ct += 1
			if s12*1000 + r12*1000 + d12*1000 < jujak:
				if ct != 2:
					star = 0
					cost += e_price
					des += 1
			if ctr == 1:
				ct = 0
				ctr = 0
			# print(star)
			# print(ct)
			if star == goal:
				break

		if star == 12:
			jujak = random.randint(1,1000)
			cost += cost13
			if ct == 2:
				star += 1
				ctr += 1
			if jujak < s13*1000 + 1:
				if ct != 2:
					star += 1
					ct = 0
			if s13*1000 < jujak < s13*1000 + r13*1000 + 1:
				if ct != 2:
					star += 0
					ct = 0
			if s13*1000 + r13*1000 < jujak < s13*1000 + r13*1000 + d13*1000 + 1:
				if ct != 2:
					star -= 1
					ct += 1
			if s13*1000 + r13*1000 + d13*1000 < jujak:
				if ct != 2:
					star = 0
					cost += e_price
					des += 1
			if ctr == 1:
				ct = 0
				ctr = 0
			# print(star)
			# print(ct)
			if star == goal:
				break

		if star == 13:
			jujak = random.randint(1,1000)
			cost += cost14
			if ct == 2:
				star += 1
				ctr += 1
			if jujak < s14*1000 + 1:
				if ct != 2:
					star += 1
					ct = 0
			if s14*1000 < jujak < s14*1000 + r14*1000 + 1:
				if ct != 2:
					star += 0
					ct = 0
			if s14*1000 + r14*1000 < jujak < s14*1000 + r14*1000 + d14*1000 + 1:
				if ct != 2:
					star -= 1
					ct += 1
			if s14*1000 + r14*1000 + d14*1000 < jujak:
				if ct != 2:
					star = 0
					cost += e_price
					des += 1
			if ctr == 1:
				ct = 0
				ctr = 0
			# print(star)
			# print(ct)
			if star == goal:
				break

		if star == 14:
			jujak = random.randint(1,1000)
			cost += cost15
			if ct == 2:
				star += 1
				ctr += 1
			if jujak < s15*1000 + 1:
				if ct != 2:
					star += 1
					ct = 0
			if s15*1000 < jujak < s15*1000 + r15*1000 + 1:
				if ct != 2:
					star += 0
					ct = 0
			if s15*1000 + r15*1000 < jujak < s15*1000 + r15*1000 + d15*1000 + 1:
				if ct != 2:
					star -= 1
					ct += 1
			if s15*1000 + r15*1000 + d15*1000 < jujak:
				if ct != 2:
					star = 0
					cost += e_price
					des += 1
			if ctr == 1:
				ct = 0
				ctr = 0
			# print(star)
			# print(ct)
			if star == goal:
				break

		if star == 15:
			jujak = random.randint(1,1000)
			cost += cost16
			if ct == 2:
				star += 1
				ctr += 1
			if jujak < s16*1000 + 1:
				if ct != 2:
					star += 1
					ct = 0
			if s16*1000 < jujak < s16*1000 + r16*1000 + 1:
				if ct != 2:
					star += 0
					ct = 0
			if s16*1000 + r16*1000 < jujak < s16*1000 + r16*1000 + d16*1000 + 1:
				if ct != 2:
					star -= 1
					ct += 1
			if s16*1000 + r16*1000 + d16*1000 < jujak:
				if ct != 2:
					star = 0
					cost += e_price
					des += 1
			if ctr == 1:
				ct = 0
				ctr = 0
			# print(star)
			# print(ct)
			if star == goal:
				break

		if star == 16:
			jujak = random.randint(1,1000)
			cost += cost17
			if ct == 2:
				star += 1
				ctr += 1
			if jujak < s17*1000 + 1:
				if ct != 2:
					star += 1
					ct = 0
			if s17*1000 < jujak < s17*1000 + r17*1000 + 1:
				if ct != 2:
					star += 0
					ct = 0
			if s17*1000 + r17*1000 < jujak < s17*1000 + r17*1000 + d17*1000 + 1:
				if ct != 2:
					star -= 1
					ct += 1
			if s17*1000 + r17*1000 + d17*1000 < jujak:
				if ct != 2:
					star = 0
					cost += e_price
					des += 1
			if ctr == 1:
				ct = 0
				ctr = 0
			# print(star)
			# print(ct)
			if star == goal:
				break

		if star == 17:
			jujak = random.randint(1,1000)
			cost += cost18
			if ct == 2:
				star += 1
				ctr += 1
			if jujak < s18*1000 + 1:
				if ct != 2:
					star += 1
					ct = 0
			if s18*1000 < jujak < s18*1000 + r18*1000 + 1:
				if ct != 2:
					star += 0
					ct = 0
			if s18*1000 + r18*1000 < jujak < s18*1000 + r18*1000 + d18*1000 + 1:
				if ct != 2:
					star -= 1
					ct += 1
			if s18*1000 + r18*1000 + d18*1000 < jujak:
				if ct != 2:
					star = 0
					cost += e_price
					des += 1
			if ctr == 1:
				ct = 0
				ctr = 0
			# print(star)
			# print(ct)
			if star == goal:
				break

		if star == 18:
			jujak = random.randint(1,1000)
			cost += cost19
			if ct == 2:
				star += 1
				ctr += 1
			if jujak < s19*1000 + 1:
				if ct != 2:
					star += 1
					ct = 0
			if s19*1000 < jujak < s19*1000 + r19*1000 + 1:
				if ct != 2:
					star += 0
					ct = 0
			if s19*1000 + r19*1000 < jujak < s19*1000 + r19*1000 + d19*1000 + 1:
				if ct != 2:
					star -= 1
					ct += 1
			if s19*1000 + r19*1000 + d19*1000 < jujak:
				if ct != 2:
					star = 0
					cost += e_price
					des += 1
			if ctr == 1:
				ct = 0
				ctr = 0
			# print(star)
			# print(ct)
			if star == goal:
				break

		if star == 19:
			jujak = random.randint(1,1000)
			cost += cost20
			if ct == 2:
				star += 1
				ctr += 1
			if jujak < s20*1000 + 1:
				if ct != 2:
					star += 1
					ct = 0
			if s20*1000 < jujak < s20*1000 + r20*1000 + 1:
				if ct != 2:
					star += 0
					ct = 0
			if s20*1000 + r20*1000 < jujak < s20*1000 + r20*1000 + d20*1000 + 1:
				if ct != 2:
					star -= 1
					ct += 1
			if s20*1000 + r20*1000 + d20*1000 < jujak:
				if ct != 2:
					star = 0
					cost += e_price
					des += 1
			if ctr == 1:
				ct = 0
				ctr = 0
			# print(star)
			# print(ct)
			if star == goal:
				break

		if star == 20:
			jujak = random.randint(1,1000)
			cost += cost21
			if ct == 2:
				star += 1
				ctr += 1
			if jujak < s21*1000 + 1:
				if ct != 2:
					star += 1
					ct = 0
			if s21*1000 < jujak < s21*1000 + r21*1000 + 1:
				if ct != 2:
					star += 0
					ct = 0
			if s21*1000 + r21*1000 < jujak < s21*1000 + r21*1000 + d21*1000 + 1:
				if ct != 2:
					star -= 1
					ct += 1
			if s21*1000 + r21*1000 + d21*1000 < jujak:
				if ct != 2:
					star = 0
					cost += e_price
					des += 1
			if ctr == 1:
				ct = 0
				ctr = 0
			# print(star)
			# print(ct)
			if star == goal:
				break

		if star == 21:
			jujak = random.randint(1,1000)
			cost += cost22
			if ct == 2:
				star += 1
				ctr += 1
			if jujak < s22*1000 + 1:
				if ct != 2:
					star += 1
					ct = 0
			if s22*1000 < jujak < s22*1000 + r22*1000 + 1:
				if ct != 2:
					star += 0
					ct = 0
			if s22*1000 + r22*1000 < jujak < s22*1000 + r22*1000 + d22*1000 + 1:
				if ct != 2:
					star -= 1
					ct += 1
			if s22*1000 + r22*1000 + d22*1000 < jujak:
				if ct != 2:
					star = 0
					cost += e_price
					des += 1
			if ctr == 1:
				ct = 0
				ctr = 0
			# print(star)
			# print(ct)
			if star == goal:
				break

	if cost > max_cost:
		max_cost = cost
	if cost < min_cost or min_cost == 0:
		min_cost = cost


	if cost < 1500000:
		testrecord += 1

	counter += 1
	cul_cost += cost
	star = 0
	cost = 0
	
print(round(cul_cost/tries/10000,4))
print("max cost is..")
print(round(max_cost/10000,4))
print("min cost is..")
print(round(min_cost/10000,4))
print("goal was..")
print(goal)
print("des_count was..")
print(round(des/tries,3))
print("test record!")
print(round(testrecord/tries,4))