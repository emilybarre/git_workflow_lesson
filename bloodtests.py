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

interface()