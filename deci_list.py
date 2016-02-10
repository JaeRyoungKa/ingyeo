def deci_to_any(n,radix):
    converted_number = []
    quotient = 1
    remainder = 1
    while quotient != 0:
        remainder = n % radix
        converted_number.insert(0,str(remainder))
        quotient = n / radix
        n = quotient
    number = "".join(converted_number)
    return number

n = int(raw_input("Number?"))
radix = int(raw_input("radix?"))
if n > 0 and radix >= 2 and radix <= 16:
    result = int(deci_to_any(n,radix))
    print n,"in base 10 is %d in base" %result,radix
else:
    print "wrong input!"