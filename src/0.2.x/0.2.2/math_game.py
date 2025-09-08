import random
import time
import platform
import re

version = "0.2.2"
stage = "Alpha"

#print(f"""
#Math Game by Ronnapat            5 Mar 2023
#===========================================
#V.{version} {stage}""")

# Default value
noround = 10
ran_num1 = 0
ran_num2 = 10

add_key = "1"
minus_key = "0"
muti_key = "0"
div_key = "0"

# Functions Area
def check_if_num(n : str) :
    match_text = re.findall("^[0-9]",n)
    if match_text :
        return True
    else :
        return False
    
def isfloatzero(string : str):
    match_txt = re.findall("0$", string)
    if match_txt :
        return True
    else :
        return False

def check_f_letter(letter : str, num : bool, text : str) :
    if num == True :
        match_text = re.findall(f"^{letter}[0-9]$",text)
    else :
        match_text = re.findall(f"^{letter}",text)
    if match_text :
        return True
    else :
        return False

# ===============

# Interal setting
setting = {
    "Max Combo Score" : 5,
    "Persentage Torrance" : 25,
    "Pause After Finish Duration" : 1.5,
    "Options Item Display" : 6,
    "Developer Mode" : False,
}

# Default random options value
# r_min_range = 5
# r_max_range = 10
# r_min_num1 = -5
# r_max_num1 = 0
# r_min_num2 = 10
# r_max_num2 = 15
# r_key_add = "1"
# r_key_min = "1"
# r_key_mut = "0"
# r_key_div = "0"

# Title Screen Tag
title_screen = 1

while True :

    # Old Get user input
    #while True :
    #    noround = input("\nHow many round you gonna play?: ")
    #    detectChar = noround.isnumeric()
    #    
    #    if detectChar == True :
    #        if int(noround) > 0 :
    #            break
    #        else :
    #            print("\nError!! You insert number equal 0. Please insert number again.")
    #    elif detectChar == False :
    #        print("\nError!! You insert letter or number below 0. Please insert number again.")
    #
    #ran_num1 = input("Select number from ")
    #ran_num2 = input("to ")
    
    start_key = 0
    exit_key = 0

    while True :
        while title_screen == 1 : # Title Screen
            print("\nMath Game by Ronnapat            5 Mar 2023")
            print("===========================================")
            print("(s , +) - Play")
            print("(o , /) - Options")
            print("(a , *) - About")
            print("(x , -) - Exit")
            print("")
            print(f"V.{version} {stage}")
            print("===========================================")
            title_options = input(">> ")

            if title_options == "s" or title_options == "+" : # Start
                title_screen = 0
                break
            elif title_options == "o" or title_options == "/" : # Options
                page = 1
                total_page = (page % 2) + 1
                start_i = 0
                while True :
                    # Setting ,You can change in the program.
                    page_item = int(setting.get("Options Item Display"))

                    total_page = (int(len(setting)) // int(setting.get("Options Item Display"))) + 1
                    if int(len(setting)) % int(setting.get("Options Item Display")) == 0 :
                        total_page = 1

                    if page > total_page :
                        page = total_page

                    if page == 1 :
                        start_i = 0
                    elif page >= 2 :
                        start_i = page_item * (page - 1)
                    
                    # Display Side
                    print(f"\nOptions")
                    print("===========================================")
                    value = setting.keys()
                    for i in range(start_i, page_item * page) :
                        # Label
                        if i == 0 :
                            print("+ Gameplay +")
                        elif i == 3 :
                            print("+ GUI +")
                        elif i == 4 :
                            print("+ Other +")
                            
                        # Catch Error
                        try :
                            print(f"({i + 1}) {list(value)[i]}",end="")

                            # Shorter Spacer Program
                            value_len = len(list(value)[i])
                            if value_len < 30 :
                                for j in range(30 - value_len) :
                                    print(" ",end="")
                            print(" ",end="")

                            # Unit Placer
                            if i == 1 :
                                print(f"[ {setting.get(list(value)[i])}% ]")
                            elif i == 2 :
                                print(f"[ {setting.get(list(value)[i])}s ]")
                            else :
                                print(f"[ {setting.get(list(value)[i])} ]")
                        except IndexError :
                            print("")
                    print(f"\nPage {page} / {total_page} | {len(setting)} Items")
                    print("(< , +) - Previous Page")
                    print("(> , -) - Next Page")
                    print("(x , /) - Exit")
                    print("===========================================")
                    
                    # Input Side
                    setting_options = input(">> ")
                    if setting_options == "x"or setting_options == "/"  : # Exit
                        break
                    elif setting_options == ">" or setting_options == "+" : # Next Page
                        if page + 1 == total_page + 1 :
                            print("[Error!] Out of range")
                        else :
                            page += 1
                    elif setting_options == "<" or setting_options == "-" : # Previous Page
                        if page - 1 == 0 :
                            print("[Error!] Out of range")
                        else :
                            page -= 1
                    elif check_if_num(setting_options) == True and int(setting_options) <= len(setting) : # Change
                        print(f"({setting_options}) {list(value)[int(setting_options) - 1]} [ {setting.get(list(value)[int(setting_options) - 1])} ]")
                        if type(setting.get(list(value)[int(setting_options) - 1])) == bool :
                            new = input("Change Vaule to (boolean): ")
                            if new == "x" :
                                None
                            else :
                                if new == "t" or new == "True" or new == "true" :
                                    setting.update({list(value)[int(setting_options) - 1] : True})
                                elif new == "f" or new == "False" or new == "false" :
                                    setting.update({list(value)[int(setting_options) - 1] : False})
                        elif type(setting.get(list(value)[int(setting_options) - 1])) == int :
                            new = input("Change Vaule to (int): ")
                            if new == "x" :
                                None
                            else :
                                setting.update({list(value)[int(setting_options) - 1] : int(new)})      
                        elif type(setting.get(list(value)[int(setting_options) - 1])) == float :
                            new = input("Change Vaule to (float): ")
                            if new == "x" :
                                None
                            else :
                                setting.update({list(value)[int(setting_options) - 1] : float(new)})           
                    
            elif title_options == "a" or title_options == "*" : # About
                print("\nAbout")
                print("===========================================")
                print("")
                print("Math Game by Ronnapat            5 Mar 2023")
                print(f"V.{version} {stage}")
                if bool(setting.get("Developer Mode")) == True :
                    print(f"\nPython V.{platform.python_version()}")
                else :
                    None
                print("\nThis program is a main project of ")
                print("all of my Python project.")
                print("")
                print("===========================================")
                input("Press enter key to exit. ")
            elif title_options == "x" or title_options == "-" : # Exit
                exit_key = 1
                break
            else :
                print("[Error] Invalid Input")

        if exit_key == 1 :
            print("\nBye!!\n")
            break
    
        # Newer get user input
        while True :
            # Summary info
            add_check = "x"
            minus_check = "x"
            muti_check = "x"
            div_check = "x"

            if add_key == "1" :
                add_check = "/"
        
            if minus_key == "1" :
                minus_check = "/"

            if muti_key == "1" :
                muti_check = "/"

            if div_key == "1" :
                div_check = "/"

            print("\nGame Options")
            print("===========================================")
            print(f"(1) - Total Round  : {noround}")
            print(f"(2) - Number Range : {ran_num1} - {ran_num2}")
            print("(3) - Mode :")
            print(f"    {add_check} - Plus (+)")
            print(f"    {minus_check} - Minus (-)")
            print(f"    {muti_check} - Mutipilcation (x)")
            print(f"    {div_check} - Divide (÷)")
            print("")
            print("(  ,  ) - Ranked Game (Coming Soon)")
            print("(  ,  ) - Save Slot (Coming Soon)")
            print("(s , +) - Start")
            print("(x , -) - Back to title screen")
            print("===========================================")
            options = input(">> ")

            if options == "1" :
                while True :  # Number round input
                    old_noround = noround
                    noround = input(f"\nInsert round number ({old_noround}) : ")

                    if noround == "x" :
                        noround = old_noround
                        break 
                    
                    detectChar = noround.isnumeric()

                    if detectChar == True :
                        if int(noround) > 0 :
                            break
                        else :
                            print("[Error] You insert number equal 0. Please insert number again.")
                    elif detectChar == False :
                        print("[Error] You insert letter or number below 0. Please insert number again.")
            elif options == "2" :
                while True :  # Range number input
                    old_rannum1 = ran_num1
                    old_rannum2 = ran_num2
                    ran_num1 = input(f"\nInsert number from ({old_rannum1}) : ")

                    if ran_num1 == "x" :
                        ran_num1 = old_rannum1
                        ran_num2 = old_rannum2
                        break 

                    ran_num2 = input(f"Insert number to   ({old_rannum2}) : ")

                    if ran_num2 == "x" :
                        ran_num1 = old_rannum1
                        ran_num2 = old_rannum2
                        break 

                    detectNum1 = ran_num1.isdecimal()
                    detectNum2 = ran_num2.isdecimal()
                    find_NegNum1 = ran_num1.find("-", 1)
                    find_NegNum2 = ran_num2.find("-", 1)

                    try :
                        if int(ran_num1) + 1 == int(ran_num1) + 1 and int(ran_num2) + 1 == int(ran_num2) + 1 :
                            break
                    except :
                        print("[Error] Please insert number again.")
            elif options == "3" : 
                while True :  # Operator input
                    add_key = input("\nDo you want add (+) ( Yes 1 | No 0 ) : ")
                    minus_key = input("Do you want sub (-) ( Yes 1 | No 0 ) : ")
                    muti_key = input("Do you want mul (x) ( Yes 1 | No 0 ) : ")
                    div_key = input("Do you want div (÷) ( Yes 1 | No 0 ) : ")

                    if add_key == "0" and minus_key == "0" and muti_key == "0" and div_key == "0" :
                        print("[Error] You didn\'t insert operation. Please insert operation again.") 
                    elif add_key == "1" or minus_key == "1" or muti_key == "1" or div_key == "1" :
                        if add_key == "1" :
                            add_check = "/"
        
                        if minus_key == "1" :
                            minus_check = "/"

                        if muti_key == "1" :
                            muti_check = "/"

                        if div_key == "1" :
                            div_check = "/"
                        break
                    else :
                        print("[Error] You didn\'t insert operation. Please insert operation again.")
            elif options == "r" or options == "10" : # Random Options
                break
                while True :
                    print("\nRandom Options")
                    print("===========================================")
                    print("(1) - Round Range :")
                    print("(2) - Number Range :")
                    print("(3) - Operation :")
                    print("\n(s , +) - Random!")
                    print("(x , -) - Back")
                    print("===========================================")
                    options_r = input("Type an option here : ")
                    if options_r == "s" or options_r == "+" :
                        None
                    elif options_r == "x" or options_r == "-" :
                        break
                    else :
                        print("[Error] Invalid Input")
            elif options == "s" or options == "+" : # Start Game
                if add_key == "0" and minus_key == "0" and muti_key == "0" and div_key == "0" :
                    print("[Error] You didn\'t insert operation. Please insert operation again.") 
                elif add_key == "1" or minus_key == "1" or muti_key == "1" or div_key == "1" :
                    start_key = 1
                    break
                else :
                    print("[Error] You didn\'t insert operation. Please insert operation again.") 
            elif options == "x" or options == "-" : # Exit Game
                title_screen = 1
                break
            elif check_f_letter("q",False,options) == True :
                short_cut = options
                short_cut = short_cut.rsplit(" ")
                if short_cut[0] == "q1":
                    try :
                        noround = int(short_cut[1])
                    except Exception :
                        print("[Error] Invalid Input")
                elif short_cut[0] == "q2":
                    try :
                        ran_num1 = int(short_cut[1])
                        ran_num2 = int(short_cut[2])
                    except Exception :
                        print("[Error] Invalid Input")
                elif short_cut[0] == "q3":
                    try :
                        if str(short_cut[1]) == "1" or str(short_cut[2]) == "1" or str(short_cut[3]) == "1" or str(short_cut[4]) == "1" :
                            add_key = str(short_cut[1])
                            minus_key = str(short_cut[2])
                            muti_key = str(short_cut[3])
                            div_key = str(short_cut[4])
                        else :
                            print("[Error] Invalid Input")
                    except Exception :
                        print("[Error] Invalid Input")
                else :
                    print("[Error] Invalid Input")
            else :
                print("[Error] Invalid Input")

        if start_key == 1 :
            break

    if exit_key == 1 :
        break

    info_text1 = F"\nTotal Round  : {noround}"
    info_text2 = F"Number Range : {ran_num1} - {ran_num2}"
    info_text3 = F"Mode :"
    info_text4 = F"  {add_check} - Plus (+)\n  {minus_check} - Minus (-)\n  {muti_check} - Mutipilcation (x)\n  {div_check} - Divide (÷)"

    # Set the variable
    correct = 0
    wrong = 0
    combo = 0
    hi_combo = 0
    text_round = 0
    score = 0

    real_accu = 100.00

    # Set the list
    timestart = []
    timeend = []
    timestorage = []
    operation = []
    num1_storage = []
    num2_storage = []
    oper_storage = []
    check_storage = []
    input_answer = []
    correct_ans = []
    time_per_store = []

    # Clear the list
    timestart.clear()
    timeend.clear()
    timestorage.clear()
    operation.clear()
    num1_storage.clear()
    num2_storage.clear()
    oper_storage.clear()
    check_storage.clear()
    input_answer.clear()
    correct_ans.clear()
    time_per_store.clear()

    if add_key == "1" :
        operation.append("0")

    if minus_key == "1" :
        operation.append("1")

    if muti_key == "1" :
        operation.append("2")

    if div_key == "1" :
        operation.append("3")
    
    print("\nGet ready")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("GO!!")
    
    # Start the timer
    tic = time.perf_counter()

    # Start the game 
    for i in range(int(noround)) :
        
        # Count number round every round end.
        text_round += 1
        
        # Random Phase
        num1 = random.randint(int(ran_num1),int(ran_num2))
        num2 = random.randint(int(ran_num1),int(ran_num2))
        ran_oper = random.choice(operation)

        # Store number and operator
        num1_storage.append(str(num1))
        num2_storage.append(str(num2))
        oper_storage.append(str(ran_oper))
        
        # Ask Question Phase

        # Set respond
        cor_count = 0
        wrong_count = 0

        # Status bar
        print(f"\n{round(real_accu,2)}%  {correct} | {wrong}  x{combo}  Score : {score}")

        # Addition
        if str(ran_oper) == "0" :
            time_s = time.perf_counter()
            timestart.append(str(time_s))
            ans = num1 + num2
            print(F"\nRound {text_round} :")
            text = F"{num1} + {num2} = ?? : "
            in_ans = input(str(text))

            if in_ans == str(ans) :
                print("Correct!!")
                correct += 1
                cor_count += 1

            if in_ans != str(ans) :
                print("Wrong!!")
                wrong += 1
                wrong_count +=1

            time_e = time.perf_counter()
            timeend.append(str(time_e))

        # Subtraction
        if str(ran_oper) == "1" :
            time_s = time.perf_counter()
            timestart.append(str(time_s))
            ans = num1 - num2
            print(F"\nRound {text_round} :")
            text = F"{num1} - {num2} = ?? : "
            in_ans = input(str(text))

            if in_ans == str(ans) :
                print("Correct!!")
                correct += 1
                cor_count += 1

            if in_ans != str(ans) :
                print("Wrong!!")
                wrong += 1
                wrong_count += 1

            time_e = time.perf_counter()
            timeend.append(str(time_e))

        # Mutiplication
        if str(ran_oper) == "2" :
            time_s = time.perf_counter()
            timestart.append(str(time_s))
            ans = num1 * num2
            print(F"\nRound {text_round} :")
            text = F"{num1} x {num2} = ?? : "
            in_ans = input(str(text))

            if in_ans == str(ans) :
                print("Correct!!")
                correct += 1
                cor_count += 1

            if in_ans != str(ans) :
                print("Wrong!!")
                wrong += 1
                wrong_count += 1

            time_e = time.perf_counter()
            timeend.append(str(time_e))

        # Division
        if str(ran_oper) == "3" :
            time_s = time.perf_counter()
            timestart.append(str(time_s))
            
            # Make number is divisionable
            while True :
                # If number 2 is zero
                while num2 == 0 :
                    num2 = random.randint(int(ran_num1),int(ran_num2))
                    if num2 != 0 :
                        break

                ans = num1 / num2

                len_num = len(str(round(ans,5)))
                if len_num < 6 :
                    break
                else :
                    num1 = random.randint(int(ran_num1),int(ran_num2))
                    num2 = random.randint(int(ran_num1),int(ran_num2))

            print(F"\nRound {text_round} :")
            text = F"{num1} ÷ {num2} = ?? : "
            in_ans = input(str(text))

            if float(in_ans) == round(ans,5) :
                print("Correct!!")
                correct += 1
                cor_count += 1

            if float(in_ans) != round(ans,5) :
                print("Wrong!!")
                wrong += 1
                wrong_count += 1

            time_e = time.perf_counter()
            timeend.append(str(time_e))

        # Collect info
        input_answer.append(str(in_ans))
        correct_ans.append(str(ans))
        if cor_count == 1 :
            check_storage.append(str("Correct"))
        
        if wrong_count == 1 :
            check_storage.append(str("Wrong"))
        
        # Combo System and Score System Phase
        persentage_torrance = int(setting.get("Persentage Torrance")) # Setting
        empty_per = 100 - real_accu
        if cor_count == 1 :
            if real_accu != 100.00 :
                real_accu = real_accu + ((persentage_torrance / 100) * empty_per)

            combo += 1
            if combo > int(setting.get("Max Combo Score")) :
                score += int(setting.get("Max Combo Score"))
            else :
                score += combo

            if combo > hi_combo :
                hi_combo = combo

        if wrong_count == 1 :
            real_accu = real_accu - (real_accu * (persentage_torrance / 100))
            combo = 0

    # Loop until the round end.
    # Game End    
    
    # Stop the timer
    toc = time.perf_counter()

    # Print Last Status Bar
    print(f"\n{round(real_accu,2)}%  {correct} | {wrong}  x{combo}  Score : {score}")

    # Wait
    time.sleep(float(setting.get("Pause After Finish Duration")))
    
    # Print round time
    round_count = 0
    time_count = -1
    print("\nResult")
    print("===========================================")
    for i in range(int(noround)) :
        round_count = round_count + 1
        time_count = time_count + 1

        check_box = " "
        if check_storage[time_count] == "Correct" :
            check_box = "/"
        if check_storage[time_count] == "Wrong" :
            check_box = "x"

        text_t = F"\n{check_box} - Round {round_count} "

        oper_sign = ""
        if str(oper_storage[time_count]) == "0" :
            oper_sign = "+"
        elif str(oper_storage[time_count]) == "1" :
            oper_sign = "-"
        elif str(oper_storage[time_count]) == "2" :
            oper_sign = "x"
        elif str(oper_storage[time_count]) == "3" :
            oper_sign = "÷"

        text1 = f"Questions   : {num1_storage[time_count]} {oper_sign} {num2_storage[time_count]} = ??"

        text2 = f"Correct Ans : {correct_ans[time_count]}"
        text3 = f"Your Answer : {input_answer[time_count]} [{check_storage[time_count]}]"

        time_value = float(timeend[time_count]) - float(timestart[time_count])
        timestorage.append(float(time_value))
        total_time = toc - tic

        time_per = (time_value / total_time) * 100
        
        if time_per < 0.999 :
            time_per = f"{time_per:0.2}"
        elif time_per > 9.99 :
            time_per = f"{time_per:0.4}"
        else :
            time_per = f"{time_per:0.3}"

        time_per_store.append(float(time_per))

        value = f"Time        : {time_value:0.3}s"
        if time_value < 0.999 :
            value = f"Time        : {time_value:0.2}s"
        elif time_value > 9.99 :
            value = f"Time        : {time_value:0.4}s"

        value2 = f" ({time_per}%)"
        
        value3 = value + value2
        text4 = value3

        print(str(text_t))
        print(str(text1))
        print(str(text4))
        print(str(text2))
        print(str(text3))

    # Do some calculation result
    # Minute Convertion
    time_sec = total_time
    time_min = 0
    while time_sec > 60 :
        time_sec -= 60
        time_min += 1
        if time_sec < 60 :
            break

    timefinal_sec = f"{time_min}m {time_sec:0.3}s"

    if time_sec > 10 :
        timefinal_sec = f"{time_min}m {time_sec:0.4}s"

    # Calculate Avg
    avgtime = sum(timestorage) / len(timestorage)

    # Calculate Accuracy
    accuracy = (int(correct) / int(noround)) * 100
    if accuracy > 9.99 :
        textaccu = f"{accuracy:0.4}"
    else :
        textaccu = f"{accuracy:0.3}"

    # Wrong Accuracy
    wrong_accu = (int(wrong) / int(noround)) * 100
    if wrong_accu > 9.99 :
        text_wrong_accu = f"{wrong_accu:0.4}"
    else :
        text_wrong_accu = f"{wrong_accu:0.3}"

    text_real_accu = ""
    # Decimal placer for real accuracy
    if real_accu < 0.999 :
        text_real_accu = f"{real_accu:0.2}"
    elif real_accu > 9.99 :
        text_real_accu = f"{real_accu:0.4}"
    else :
        text_real_accu = f"{real_accu:0.3}"

    # Calculate Min and Max
    min_num = min(timestorage)
    max_num = max(timestorage)

    # Find the round for min and max
 
    count_numlist = 0
    while True :
        comp_list = timestorage[int(count_numlist)] 
        if min_num == comp_list :
            rou_min = count_numlist
            break
        else :
            count_numlist += 1
    
    count_numlist = 0
    while True :
        comp_list = timestorage[int(count_numlist)]
        if max_num == comp_list :
            rou_max = count_numlist
            break
        else :
            count_numlist += 1

    # Decimal placer for min max
    if min_num < 0.999 :
        min_num = f"{min_num:0.2}"
    elif min_num > 9.99 :
        min_num = f"{min_num:0.4}"
    else :
        min_num = f"{min_num:0.3}"

    if max_num < 0.999 :
        max_num = f"{max_num:0.2}"
    elif max_num > 9.99 :
        max_num = f"{max_num:0.4}"
    else :
        max_num = f"{max_num:0.3}"

    # Time Persentage
    min_time_per = min(time_per_store)
    max_time_per = max(time_per_store)

    sorted_time_per_store = sorted(time_per_store)
    no_time_per = (len(sorted_time_per_store) + 1) / 2
    med_time_per = sorted_time_per_store[int(no_time_per - 1)]

    text_min = f"{min_num}s ({min_time_per}%) Round {rou_min + 1}"
    text_max = f"{max_num}s ({max_time_per}%) Round {rou_max + 1}"

    # Calculate median

    sorted_timestorage = sorted(timestorage)
    
    # Find the middle list
    no_timemedian = (len(sorted_timestorage) + 1) / 2

    median = sorted_timestorage[int(no_timemedian - 1)]

    list_num = 0
    while True :
        comp_list = timestorage[int(list_num)]
        if median == comp_list :
            round_median = list_num
            break
        else :
            list_num += 1

    # Decimal placer for median
    if median < 0.999 :
        median = f"{median:0.2}"
    elif median > 9.99 :
        median = f"{median:0.4}"
    else :
        median = f"{median:0.3}"

    text_median = f"{median}s ({med_time_per}%) Round {round_median + 1}"

    # Ranking System
    text_rank = ""
    if real_accu == 100.00 :
        text_rank = "SX+"
    elif real_accu >= 97.50 :
        text_rank = "SX"
    elif real_accu >= 95.00 :
        text_rank = "EX+"
    elif real_accu >= 92.50 :
        text_rank = "EX"
    elif real_accu >= 90.00 :
        text_rank = "X+"
    elif real_accu >= 87.50 :
        text_rank = "X"
    elif real_accu >= 85.00 :
        text_rank = "S+"
    elif real_accu >= 82.50 :
        text_rank = "S"
    elif real_accu >= 80.00 :
        text_rank = "A+"
    elif real_accu >= 75.00 :
        text_rank = "A"
    elif real_accu >= 70.00 :
        text_rank = "B+"
    elif real_accu >= 65.00 :
        text_rank = "B"
    elif real_accu >= 60.00 :
        text_rank = "C"
    elif real_accu >= 50.00 :
        text_rank = "D"
    elif real_accu >= 25.00 :
        text_rank = "F"
    elif real_accu <= 24.99 :
        text_rank = "F-"

    # Maximum Score
    max_score = 0
    combo = 0
    for i in range(int(noround)) :
        combo += 1
        if combo > int(setting.get("Max Combo Score")) :
            max_score += int(setting.get("Max Combo Score"))
        else :
            max_score += combo

    perfect_text = ""
    if real_accu == 100 :
        perfect_text = "Perfect!!"

    # Get date
    date = time.strftime("%a, %d %b %Y %X %z ", time.localtime())

    # Old Print Result
    # print("\nTotal time    :",timefinal_sec)
    # print(f"Maximum time  : {str(text_max)}")
    # print(f"Median time   : {str(text_median)}")
    # print(f"Mininum time  : {str(text_min)}")
    # print(f"Average time  : {avgtime:0.3}s")
    # print("Total correct :",correct,f"({textaccu}%)")
    # print("Total wrong   :",wrong,f"({text_wrong_accu}%)")
    # print(F"\nHighest combo : x{hi_combo}")
    # print(F"Score         : {score}/{max_score} {perfect_text}")
    # print(f"Accuracy      : {text_real_accu}%")
    # print(F"Rank          : {text_rank}")
    # print("\nSession info")
    # print("-------------------------------------------")
    # print(f"\nDate : {date}")
    # print(f"Math Game V.{version} {stage}")
    # print(f"Python V.{platform.python_version()}")
    # print(str(info_text1))
    # print(str(info_text2))
    # print(str(info_text3))
    # print(str(info_text4))
    # print("\n===========================================")
    
    # Request for next round.
    while True:
        # Print Result
        print("")
        print("===========================================")
        print(f"Total time    : {timefinal_sec}")
        print(f"Accuracy      : {text_real_accu}%")
        print(f"Rank          : {text_rank}")
        print(F"Score         : {score}/{max_score} {perfect_text}")
        print(F"Highest combo : x{hi_combo}")
        print(f"\nMaximum time  : {str(text_max)}")
        print(f"Median time   : {str(text_median)}")
        print(f"Mininum time  : {str(text_min)}")
        print(f"Average time  : {avgtime:0.3}s")
        print("\nTotal correct :",correct,f"({textaccu}%)")
        print("Total wrong   :",wrong,f"({text_wrong_accu}%)")
        print("\n(s , *) - Session info")
        print("(n , +) - Next Game")
        print("(x , -) - Back to title screen")
        print("===========================================")
        options_end = input(">> ")
        if options_end == "s" or options_end == "*" : # Session info
            print("\nSession info")
            print("===========================================")
            print(f"Date : {date}")
            print(f"Math Game V.{version} {stage}")
            if bool(setting.get("Developer Mode")) == True :
                print(f"\nPython V.{platform.python_version()}")
            else :
                None
            print(str(info_text1))
            print(str(info_text2))
            print(str(info_text3))
            print(str(info_text4))
            print("===========================================")
            input("Press enter key to exit. ")
        elif options_end == "n" or options_end == "+" : # Next Game
            break
        elif options_end == "x" or options_end == "-" : # Back
            title_screen = 1
            break
        else :
            print("[Error] Invalid Input")

        # Old Input
        # next_calculation = input("Another one? (yes + | no -): ")
        # if next_calculation == "no" or next_calculation == "n" or next_calculation == "-":
        #     print("\nBye!!\n")
        #     key += 1
        #     break
        # elif next_calculation == "yes" or next_calculation == "y" or next_calculation == "+":
        #     break
        # else :
        #     print("[Error] Invalid Input")
    
    # Key permission
    # if key == 1 :
    #     break
