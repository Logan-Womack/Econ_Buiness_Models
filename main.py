rl_int = input("What is the intrest rate of a riskless borrower? ")
prob = input("What is the probibility of default? ")
princ = input("What is the principle Loan amount? ")
leng = input("what is the length of the debt in months? ")
rp = ((1 + float(rl_int)) * float(prob)) / (1.0 - float(prob))
rc = (1 + (float(rl_int)) + float(rp))
yrly_int = float(rl_int) + float(rp)
tc = (rc) * float(princ)
payment = tc / int(leng)
print(tc)
print("The clients total monthly payment will be", str(payment))





