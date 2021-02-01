def interface(): 
	print("Blood Test Analysis")
	while True: 
		print("\nOptions")
		print("1 - HDL")
		print("9 - Quit")
		choice = input("Enter an option: ")
	if choice == "9": 
		return
	elif choice == "1":
		HDL_driver()

def HDL_driver():
	HDL_val = getdata()
	result = analyzedata(HDL_val)
	output(result)

def getdata():
	HDL = input("What is your HDL?")
	HDL = int(HDL)
	return HDL

interface()