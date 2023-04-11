hidden = ""
pre_obs = input("ezpz> ")
salt = "salt"
for i in pre_obs + salt:
	for j in i:
		outn = ord(j) ^ 2
		outn1 = ord(j) >> 3 
		hidden = hidden + str(outn) + str(outn1)

print(hidden)

if hidden == "811073991114757496787496784755464865065061131499121101311814":
	print("good..")

