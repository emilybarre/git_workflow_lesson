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
	output(HDL_val,result)

def getdata():
	HDL = input("What is your HDL?")
	HDL = int(HDL)
	return HDL

def analyzedata(HDL):
	if HDL >= 60: 
		result = "Normal" 
	elif 40 <= HDL < 60:
		result = "Borderline Low"
	elif HDL < 40: 
		result = "Low"
	else:
		result = "Error"
		
	return result

def output(HDL,result):
	print("The HDL entered was {}".format(HDL))
	print("This HDL level is {}".format(result))
	
interface()