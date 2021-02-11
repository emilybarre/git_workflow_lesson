def interface():
    print("Blood Test Analysis")
    while True:
        print("\nOptions")
        print("1 - HDL")
        print("2 - LDL")
        print("3 - Cholesterol")
        print("9 - Quit")
        choice = input("Enter an option: ")
        if choice == "9":
            return
        elif choice == "3":
            test_driver("cholesterol")
        elif choice == "2":
            test_driver("LDL")
            return
        elif choice == "1":
            test_driver("HDL")
            return


def test_driver(test):
    test_num = get_input(test)
    
    if test == "HDL":
        test_result = analyze_HDL(test_num)
    elif test == "LDL":
        test_result = analyze_LDL(test_num)
    elif test == "cholesterol"
        test_result = analyze_cholesterol(test_num)
    
    output(test,test_num,test_result)


def get_input(test):
    test_num = input("\nWhat is your {}?\n".format(test))
    test_num = int(test_num)
    return test_num


def analyze_HDL(HDL):
    if HDL >= 60:
        result = "Normal"
    elif 40 <= HDL < 60:
        result = "Borderline Low"
    elif HDL < 40:
        result = "Low"
    else:
        result = "Error"
    return result


def analyze_LDL(LDL):
    if LDL < 130:
        result = "Normal"
    elif 130 <= LDL < 160:
        result = "Borderline High"
    elif 160 <= LDL < 190:
        result = "High"
    elif 190 <= LDL:
        result = "Very High"
    else:
        result = "Error"
    return result

def output(test,test_num,test_result):
    print("\nThe {} entered was {}".format(test, test_num))
    print("This {} level is {}".format(test, test_result))


if __name__ == "__main__":
    interface()
