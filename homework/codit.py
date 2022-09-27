orig = 250
cur = 300
incre = (cur - orig)
perce_incre = (incre / orig * 100)
if perce_incre >= 20:
    print("SELL WEAK HANDS")
elif perce_incre <= -20:
    print("BUY THE DIP")
elif perce_incre <= 10:
    print("DIAMOND HANDS")