import random
import math
upcount = 8
df_uc = upcount
success = 0
inno_price = 0.50 # which has 50% success rate
st_price = 0.000065*470 # 1 spell trace costs 20,000 mesos. needs 570 sts per one try.
gh_price = 0.0 # which has 50% success rate
cs_price = 0.22 # which has 10% success rate
total_price = 0
rate = 15+10+10+4

sigma = 0
tries = 50000
cul_price = 0
max_cost = 0
min_cost = 0
mean = 30.01
stdv = 0

while sigma < tries:
	# applies golden hammer 50%. if fails, try 2 15% scrolls and just one fail leads to using innocent scroll(s).
	gh_success = random.randint(1,2)
	total_price += gh_price # apllies golden hammer 50%
	while gh_success == 2:  #if failed,
		total_price += st_price #try to resuscitate
		if random.randint(1,100) < rate+1: # if sucesses
				total_price += st_price
				if random.randint(1,100) <rate+1: # and once again
					upcount = upcount - 1
					success = success + 2
					gh_success = 1
		if gh_success == 2:
			inno_s = 2
			total_price += gh_price
			while inno_s == 2: # otherwise, use innocent
				total_price += inno_price
				inno_s = random.randint(1,2)

	if upcount == df_uc:
		upcount += 1

	while upcount > 0 or success < df_uc + 1: #golden hammer
		while upcount > 0:
			upcount -= 1
			total_price += st_price
			rand = random.randint(1,100)
			if rand < rate+1:
				success += 1
			if rand > rate and random.randint(1,100) < 5:
				upcount += 1
		while upcount < df_uc + 1 - success:
			total_price += cs_price
			if random.randint(1,10) == 1:
				upcount += 1
	
	sigma += 1
	cul_price += total_price

	if max_cost < total_price:
		max_cost = total_price

	if min_cost > total_price or min_cost == 0:
		min_cost = total_price

	stdv += (mean - total_price)**2
	total_price = 0
	upcount = df_uc
	success = 0
	

print(round(cul_price/tries,4))
print(round(max_cost,4))
print(round(min_cost,4))
print(round(math.sqrt(stdv/tries),4))