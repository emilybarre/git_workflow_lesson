def interface():
    print("Blood Test Analysis")
    while True:
        print("\nOptions")
        print("1 - HDL")
        print("2 - LDL")
        print("9 - Quit")
        choice = input("Enter an option: ")
        if choice == "9":
            return
        if choice == "2":
            LDL_driver()
        if choice == "3":
            
        elif choice == "1":
            HDL_driver()
            return


def HDL_driver():
    HDL_val = getHDL()
    LDL_val = getLDL()
    resultHDL = analyze_HDL(HDL_val)
    resultLDL = analyze_LDL(LDL_val)
    output(HDL_val, LDL_val, resultHDL, resultLDL)

def LDL_driver():
    LDL_val = getLDL()
    resultLDL = analyze_LDL(LDL_val)
    output(LDL_val, resultLDL)

def getHDL():
    HDL = input("\nWhat is your HDL?\n")
    HDL = int(HDL)
    return HDL


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


def getLDL():
    LDL = input("\nWhat is your LDL?\n")
    LDL = int(LDL)
    return LDL


def analyze_LDL(LDL):
    if LDL < 130:
        result = "Normal"
    elif 130 <= LDL < 159:
        result = "Borderline High"
    elif 160 <= LDL < 189:
        result = "High"
    elif 190 < LDL:
        result = "Very High"
    else:
        result = "Error"
    return result

def output(HDL, LDL, result_HDL, result_LDL):
    print("\nThe HDL entered was {}".format(HDL))
    print("This HDL level is {}".format(result_HDL))
    print("\nThe LDL entered was {}.".format(LDL))
    print("This LDL level is {}".format(result_LDL))


if __name__ == "__main__":
    interface()
