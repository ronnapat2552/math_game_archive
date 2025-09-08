import random
import time
import platform
import re
import os
import json

# 042024r3 Last Snapshot
version = "0.3.4"
stage = "Alpha"
snapshot = False

if snapshot == True :
    stage = "Snapshot"

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

# Functions Area ==========
# Check is number
def check_if_num(n : str) :
    match_text = re.findall("^[0-9]",n)
    if match_text :
        return True
    else :
        return False

# Check zero
def isfloatzero(string : str) :
    match_txt = re.findall("0$", string)
    if match_txt :
        return True
    else :
        return False

# Check fornt letter
def check_f_letter(letter : str, num : bool, text : str) :
    if num == True :
        match_text = re.findall(f"^{letter}[0-9]$",text)
    else :
        match_text = re.findall(f"^{letter}",text)
    if match_text :
        return True
    else :
        return False
    
def current_path() : 
    return os.getcwd() 

def neg_num(Number) :
    if re.findall(r"^-",str(Number)) == True :
        return "1"
    else :
        return "0"

# Spacer Program
def spacer(String : str,Space : int) :
    name_len = len(String)        # Count how many letter
    #  v------------------------------- Total available space
    if Space - name_len < Space :        # If blank space is greater than space
        space = Space - name_len         # Find a space
        box = f"{String}"
        for j in range(space) :
            box = f"{box} " # Add a space
    else :
        box = f"{String} "
    return box

# Color Text
def col(text : str ,fg : str = None ,bg : str = None) :
    fg_text = ""
    bg_text = ""
    try :
        fg_arg = fg.split(" ")
    except Exception:
        None
    try :
        bg_arg = bg.split(" ")
    except Exception:
        None

    # Background
    try :
        if bg_arg[0] == "rgb" :
            bg_text = f"\N{ESC}[48;2;{str(bg_arg[1])}m"
        elif bg_arg[0] == "256" :
            bg_text = f"\N{ESC}[48;5;{str(bg_arg[1])}m"
    except Exception :
        None
    # Foreground
    try :
        if fg_arg[0] == "rgb" :
            fg_text = f"\N{ESC}[38;2;{str(fg_arg[1])}m"
        elif fg_arg[0] == "256" :
            fg_text = f"\N{ESC}[38;5;{str(fg_arg[1])}m"
    except Exception :
        None
        
    return f"{fg_text}{bg_text}{text}\N{ESC}[0m"

def exit_symbol() :
    return f"{col("(x,-)",fg=col_red)}"

def randomnum() :
    global ran_num1, ran_num2
    return random.randint(int(ran_num1),int(ran_num2))

# ========================

# Interal setting

# - JSON Reader
jsonreader = open("data\\setting.json","r")
jsons = jsonreader.read()
jsonreader.close()

jsonsetting = json.loads(jsons)

setting = {
    "CheckNum1IsGreaterNum2": jsonsetting["CheckNum1IsGreaterNum2"],
    "CheckNum2IsGreaterNum1": jsonsetting["CheckNum2IsGreaterNum1"],
    "CheckAnsIs1": jsonsetting["CheckAnsIs1"],
    "MaxComboScore": jsonsetting["MaxComboScore"],
    "PersentTorrance": jsonsetting["PersentTorrance"], # %
    "PauseFinishDur": jsonsetting["PauseFinishDur"], # s
    "OptionsItemDis": jsonsetting["OptionsItemDis"],
    "PathData": f"{current_path()}\\data",
    "ConfirmExit": jsonsetting["ConfirmExit"],
    "DevMode": jsonsetting["DevMode"],
}
setting_default = [
    True,
    False,
    True,
    5,
    25, # %
    1.5,# s
    6,
    f"{current_path()}\\data",
    True,
    False,
]
setting_name = [
    #         10        20        30        40
    #1234567890123456789012345678901234567890
    #----------------------------------------  == 40 Letter ==
    "Check Num1 is Greater than Num2",
    "Check Num2 is Greater than Num1",
    "Check Answer is 1",
    "Max Combo Score",
    "Persentage Torrance",
    "Pause After Finish Duration",
    "Options Item Display",
    "Path to data files",
    "Confirmation Exit",
    "Developer Mode",
]
setting_unit = [
    "",
    "",
    "",
    "",
    "%",
    "s",
    "",
    "",
    "",
    "",
]

code_normal = [
    "Q",
    "T",
    "U",
    "N",
    "F",
    "M",
    "Z",
    "W",
    "X",
    "P",
]
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

# Basic Color Code
col_red = "256 196"
col_orange = "256 208"
col_yellow = "256 226"
col_lime = "256 46"
col_green = "256 28"
col_skyblue = "256 45"
col_blue = "256 20"
col_purple = "256 56"
col_pink = "256 207"
col_grey = "256 8"
col_white = "256 15"

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
            print("\nMath Game by Ronnapat           05 Mar 2023")
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
                    page_item = int(setting.get("OptionsItemDis"))

                    total_page = (int(len(setting)) // int(setting.get("OptionsItemDis"))) + 1
                    if int(len(setting)) % int(setting.get("OptionsItemDis")) == 0 :
                        total_page = 1

                    if page > total_page :
                        page = total_page

                    if page == 1 :
                        start_i = 0
                    elif page >= 2 :
                        start_i = page_item * (page - 1)
                    
                    # Display Side
                    print(f"\nOptions                               {exit_symbol()}")
                    print("===========================================")
                    value = setting.keys()
                    for i in range(start_i, page_item * page) :
                        # Label
                        if i == 1 - 1 :
                            print("+ Gameplay +")
                            print("  - Division")
                        elif i == 4 - 1 :
                            print("  - Modifier")
                        elif i == 6 - 1 :
                            print("  - Other")
                        elif i == 7 - 1 :
                            print("+ GUI +")
                        elif i == 10 - 1 :
                            print("+ Other +")
                            
                        # Catch Error
                        try :
                            if i > 8 :
                                print(f"({i + 1}) {setting_name[i]}",end="")
                            else :
                                print(f"({i + 1})  {setting_name[i]}",end="")

                            # Shorter Spacer Program
                            value_len = len(setting_name[i])
                            if value_len < 40 :
                                for j in range(40 - value_len) :
                                    print(" ",end="")
                            print(" ",end="")

                            # Unit Placer
                            print(f"[ {setting.get(list(value)[i])}{setting_unit[i]} ]")
                        except IndexError :
                            print("")
                    print(f"\n(-) < Page {page} / {total_page} > (+) | {len(setting)} Items")
                    print("(s) - Save Change | (r) - Reset to default")
                    print("===========================================")
                    
                    # Input Side
                    setting_options = input(">> ")
                    if setting_options == "x"or setting_options == "/"  : # Back
                        break
                    elif setting_options == ">" or setting_options == "+" : # Next Page
                        if page + 1 == total_page + 1 :
                            print("[Error] Out of range")
                        else :
                            page += 1
                    elif setting_options == "<" or setting_options == "-" : # Previous Page
                        if page - 1 == 0 :
                            print("[Error] Out of range")
                        else :
                            page -= 1
                    elif setting_options.rsplit(" ")[0] == "p" : # Page jumping shortcut
                        if int(setting_options.rsplit(" ")[1]) <= 0 :
                            print("[Error] Out of range")
                        elif int(setting_options.rsplit(" ")[1]) > total_page :
                            print("[Error] Out of range")
                        else :
                            page = int(setting_options.rsplit(" ")[1])
                    elif setting_options == "s" : # Save Change
                        setting_options = input("Are you sure want to save setting? ( Yes 1 | No 0 ): ")
                        if setting_options == "y" or setting_options == "1" :
                            with open("data\\setting.json","w") as file :
                                jsonsetting = None
                                jsonsetting = json.dumps(setting)
                                file.write(jsonsetting)
                            print("Save Setting Complete!")
                            input("Press enter key to exit. ")
                        else :
                            continue
                    elif setting_options == "r" : # Reset to default
                        setting_options = input("Are you sure want to reset? ( Yes 1 | No 0 ): ")
                        if setting_options == "y" or setting_options == "1" :
                            loop = 0
                            for i in setting_default :
                                setting.update({list(value)[loop] : setting_default[loop]})
                                loop += 1
                            print("Reset Setting Complete!")
                            input("Press enter key to exit. ")
                        else :
                            continue
                    elif check_if_num(setting_options) == True and int(setting_options) <= len(setting) : # Change Value
                        print(f"({setting_options}) {setting_name[int(setting_options) - 1]} [ {setting.get(list(value)[int(setting_options) - 1])}{setting_unit[int(setting_options) - 1]} ]")
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
                        elif type(setting.get(list(value)[int(setting_options) - 1])) == str :
                            new = input("Change Vaule to (str): ")
                            if new == "x" :
                                None
                            else :
                                setting.update({list(value)[int(setting_options) - 1] : str(new)})
                    else :
                        print("[Error!] Invalid Option")         
                    
            elif title_options == "a" or title_options == "*" : # About
                print("\nAbout")
                print("===========================================")
                print("Math Game                       05 Mar 2023")
                print("Create by Ronnapat Phawaphootanon")
                print(f"\nV.{version} {stage}")
                if bool(setting.get("DevMode")) == True :
                    print(f"Python V.{platform.python_version()}")
                else :
                    None
                print("\nThis program is a main project of ")
                print("all of my Python project and expand")
                print("my programming skill.")
                print("\nLink to Project")
                print("https://sites.google.com/view/tete-page/project/math-game")
                print("===========================================")
                input("Press enter key to exit. ")
            elif title_options == "x" or title_options == "-" : # Exit
                if setting.get("ConfirmExit") == True :
                    while True :
                        print("\nConfirmation")
                        print("===========================================")
                        print("        Are you sure want to quit?")
                        print("              Yes 1 | No 0 ")
                        print("===========================================")
                        title_options = input(">> ")
        
                        if title_options.lower() == "y" or title_options == "1" or title_options == "x" :
                            print("Bye!")
                            exit()
                        elif title_options.lower() == "n" or title_options == "0" :
                            exit_key = 0
                            break
                        print("[Error] Invalid Input")
                else :
                    print("Bye!")
                    exit()
            else :
                print("[Error] Invalid Input")
    
        # Newer get user input
        while True :
            # Summary info
            add_check = f"{col('x',fg=col_red)}"
            minus_check = f"{col('x',fg=col_red)}"
            muti_check = f"{col('x',fg=col_red)}"
            div_check = f"{col('x',fg=col_red)}"

            if add_key == "1" :
                add_check = f"{col('/',fg=col_lime)}"
        
            if minus_key == "1" :
                minus_check = f"{col('/',fg=col_lime)}"

            if muti_key == "1" :
                muti_check = f"{col('/',fg=col_lime)}"

            if div_key == "1" :
                div_check = f"{col('/',fg=col_lime)}"

            print(f"\nGame Options                          {exit_symbol()}")
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
            print("(a , *) - Save Slot")
            print("(s , +) - Start")
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
            elif options == "a" or options == "*" : # Save Slot

                while True :
                    save = []
                    file_save = open(f"data\\preset_data.txt","r") # f"data\\preset_data.txt"   Playtesting\\math_game\\data\\preset_data.txt
                    save = file_save.readlines()
                    file_save.close()
                    # Linebreak symbol removal
                    #loop = 0
                    #for i in range(len(save)) :
                    #    save[loop] = save[loop].replace("\n","")
                    #    loop += 1

                    print(f"\nSave Slot                             {exit_symbol()}")
                    print("===========================================")
                    print("Slot N    Round    Range    Mode")
                    for i in range(5) :
                        if save[i] == "E\n" or save[i] == "E" :
                            print(f"Slot {i + 1} -  {col('[ Empty ]',fg=col_grey)}")
                        else :
                            hot_text_save = []
                            hot_text_save = save[i].rsplit(" ") 
                            if hot_text_save[1] == "1" :  # ran_num1 Negative Sign
                                ran_num1_negsign = "-"
                            else :
                                ran_num1_negsign = ""
                            
                            if hot_text_save[3] == "3" :  # ran_num2 Negative Sign
                                ran_num2_negsign = "-"
                            else :
                                ran_num2_negsign = ""

                            if hot_text_save[5] == "1" :
                                add_sign = "A"
                            else :
                                add_sign = f"{col('-',fg=col_grey)}"

                            if hot_text_save[6] == "1" :
                                min_sign = "S"
                            else :
                                min_sign = f"{col('-',fg=col_grey)}"

                            if hot_text_save[7] == "1" :
                                mut_sign = "M"
                            else :
                                mut_sign = f"{col('-',fg=col_grey)}"

                            # Linebreak Removal
                            hot_text_save[8] = hot_text_save[8].replace("\n","")

                            if hot_text_save[8] == "1" :
                                div_sign = "D"
                            else :
                                div_sign = f"{col('-',fg=col_grey)}"
                            
                            print(f"Slot {i + 1} -  {spacer(hot_text_save[0],5)}    {spacer(f"{ran_num1_negsign}{hot_text_save[2]} - {ran_num2_negsign}{hot_text_save[4]}",8)} {add_sign} {min_sign} {mut_sign} {div_sign}")
                    print("\n(c , +) - Create Slot")
                    print("(u , *) - Use Slot")
                    print("(e , /) - Erase Slot")
                    print("(s) - Share Preset | (n) - Enter Code")
                    print("\n>> (Action) (SlotNumber)")
                    print("===========================================")
                    save_options = input(">> ")
                    if check_f_letter("c",False,save_options) == True : # Create
                        try :
                            save[int(save_options.rsplit(" ")[1]) - 1] = f"{noround} {neg_num(ran_num1)} {ran_num1} {neg_num(ran_num2)} {ran_num2} {add_key} {minus_key} {muti_key} {div_key}\n"
                            with open(f"data\\preset_data.txt","w") as file_save :
                                file_save.writelines(save)
                        except Exception :
                            print("[Error] Invalid Input")
                    elif check_f_letter("u",False,save_options) == True : # Use
                        if save[int(save_options.rsplit(" ")[1]) - 1] == "E\n" :
                            print("[Error] You can't use the empty slot")
                            continue
                        hot_text_save = []
                        hot_text_save = save[int(save_options.rsplit(" ")[1]) - 1]
                        hot_text_save = hot_text_save.rsplit(" ")
                        noround = int(hot_text_save[0])
                        ran_num1 = int(f"{hot_text_save[1]}{hot_text_save[2]}")
                        ran_num2 = int(f"{hot_text_save[3]}{hot_text_save[4]}")
                        add_key = str(hot_text_save[5])
                        minus_key = str(hot_text_save[6])
                        muti_key = str(hot_text_save[7])
                        
                        # Linebreak Removal
                        hot_text_save[8] = hot_text_save[8].replace("\n","")

                        div_key = str(hot_text_save[8])
                        break
                    elif check_f_letter("e",False,save_options) == True : # Erase
                        try :
                            save[int(save_options.rsplit(" ")[1]) - 1] = "E\n"
                            with open(f"data\\preset_data.txt","w") as file_save :
                                file_save.writelines(save)
                        except Exception :
                            print("[Error] Invalid Input")
                    elif check_f_letter("s",False,save_options) == True : # Share
                        try :         
                            code = []
                            code = save[int(save_options.rsplit(" ")[1]) - 1].rsplit(" ")
    
                            # code_round = ["",""]
                            # code_num1 = ["",""]
                            # code_num2 = ["",""]
    
                            # Round
                            code_round = code[0].replace(""," ")[1:-1]
                            code_round = code_round.rsplit(" ")
                            if len(code_round) == 2 :
                                code_round[0] = code_normal[int(code_round[0])]
                                code_round[1] = code_normal[int(code_round[1])]
                            else :
                                code_round.append("")
                                code_round[1] = code_normal[int(code_round[0])]
                                code_round[0] = code_normal[0]
    
                            # ran_num1
                            code_num1 = code[2].replace(""," ")[1:-1]
                            code_num1 = code_num1.rsplit(" ")
                            if len(code_num1) == 2 :
                                code_num1[0] = code_normal[int(code_num1[0])]
                                code_num1[1] = code_normal[int(code_num1[1])]
                            else :
                                code_num1.append("")
                                code_num1[1] = code_normal[int(code_num1[0])]
                                code_num1[0] = code_normal[0]
    
                            # ran_num2
                            code_num2 = code[4].replace(""," ")[1:-1]
                            code_num2 = code_num2.rsplit(" ")
                            if len(code_num2) == 2 :
                                code_num2[0] = code_normal[int(code_num2[0])]
                                code_num2[1] = code_normal[int(code_num2[1])]
                            else :
                                code_num2.append("")
                                code_num2[1] = code_normal[int(code_num2[0])]
                                code_num2[0] = code_normal[0]
                            
                            code_n1n = 0
                            code_n2n = 0
                            code_add = 0
                            code_min = 0
                            code_mul = 0
                            code_div = 0
                            
                            if code[1] == "1" :
                                code_n1n = code_normal[random.randint(5,9)] 
                            elif code[1] == "0" :
                                code_n1n = code_normal[random.randint(0,4)]
                            
                            if code[3] == "1" :
                                code_n2n = code_normal[random.randint(5,9)] 
                            elif code[3] == "0" :
                                code_n2n = code_normal[random.randint(0,4)]
                            
                            if code[5] == "1" :
                                code_add = code_normal[random.randint(5,9)] 
                            elif code[5] == "0" :
                                code_add = code_normal[random.randint(0,4)]
                            
                            if code[6] == "1" :
                                code_min = code_normal[random.randint(5,9)] 
                            elif code[6] == "0" :
                                code_min = code_normal[random.randint(0,4)]
                            
                            if code[7] == "1" :
                                code_mul = code_normal[random.randint(5,9)] 
                            elif code[7] == "0" :
                                code_mul = code_normal[random.randint(0,4)]
                            
                            # Linebreak Removal
                            code[8] = code[8].replace("\n","")
    
                            if code[8] == "1" :
                                code_div = code_normal[random.randint(5,9)] 
                            elif code[8] == "0" :
                                code_div = code_normal[random.randint(0,4)]
                            
                            print(f"\nCode : {code_round[0]}{code_round[1]}{code_n1n}{code_num1[0]}-{code_num1[1]}{code_n2n}{code_num2[0]}{code_num2[1]}-{code_add}{code_min}{code_mul}{code_div}")
                            input("Press enter key to exit. ")
                        except Exception :
                            print("[Error] Can't encode number")
                    elif check_f_letter("n",False,save_options) == True : # Enter Code
                        try :
                            if save[int(save_options.rsplit(" ")[1]) - 1] != "E\n" :
                                print("[Error] This slot is occupied")
                                continue
                            code = input("Input the code here (must include dash) >> ")
                            code = code.replace("-","")

                            code_decode = ""

                            for i in range(len(code_normal)) :
                                if code_normal[i] == code[0] :
                                    code_decode = f"{code_decode}{i}"
                                    break
                            for i in range(len(code_normal)) :
                                if code_normal[i] == code[1] :
                                    code_decode = f"{code_decode}{i}"
                                    break

                            for i in range(len(code_normal)) :
                                if code_normal[i] == code[2] :
                                    for j in range(0,5) :
                                        if i == j :
                                            code_decode = f"{code_decode} 0 "
                                            break
                                    for j in range(5,10) :
                                        if i == j :
                                            code_decode = f"{code_decode} 1 "
                                            break
                                    break

                            for i in range(len(code_normal)) :
                                if code_normal[i] == code[3] :
                                    code_decode = f"{code_decode}{i}"
                                    break
                            if code[3] != code_normal[0] :
                                for i in range(len(code_normal)) :
                                    if code_normal[i] == code[4] :
                                        code_decode = f"{code_decode}{i}"
                                        break

                            for i in range(len(code_normal)) :
                                if code_normal[i] == code[5] :
                                    for j in range(0,5) :
                                        if i == j :
                                            code_decode = f"{code_decode} 0 "
                                            break
                                    for j in range(5,10) :
                                        if i == j :
                                            code_decode = f"{code_decode} 1 "
                                            break
                                    break

                            for i in range(len(code_normal)) :
                                if code_normal[i] == code[6] :
                                    code_decode = f"{code_decode}{i}"
                                    break
                            if code[6] != code_normal[0] :
                                for i in range(len(code_normal)) :
                                    if code_normal[i] == code[7] :
                                        code_decode = f"{code_decode}{i}"
                                        break

                            for i in range(len(code_normal)) :
                                if code_normal[i] == code[8] :
                                    for j in range(0,5) :
                                        if i == j :
                                            code_decode = f"{code_decode} 0"
                                            break
                                    for j in range(5,10) :
                                        if i == j :
                                            code_decode = f"{code_decode} 1"
                                            break
                                    break

                            for i in range(len(code_normal)) :
                                if code_normal[i] == code[9] :
                                    for j in range(0,5) :
                                        if i == j :
                                            code_decode = f"{code_decode} 0"
                                            break
                                    for j in range(5,10) :
                                        if i == j :
                                            code_decode = f"{code_decode} 1"
                                            break
                                    break

                            for i in range(len(code_normal)) :
                                if code_normal[i] == code[10] :
                                    for j in range(0,5) :
                                        if i == j :
                                            code_decode = f"{code_decode} 0"
                                            break
                                    for j in range(5,10) :
                                        if i == j :
                                            code_decode = f"{code_decode} 1"
                                            break
                                    break

                            for i in range(len(code_normal)) :
                                if code_normal[i] == code[11] :
                                    for j in range(0,5) :
                                        if i == j :
                                            code_decode = f"{code_decode} 0"
                                            break
                                    for j in range(5,10) :
                                        if i == j :
                                            code_decode = f"{code_decode} 1"
                                            break
                                    break  

                            save[int(save_options.rsplit(" ")[1]) - 1] = f"{code_decode}\n"
                            with open(f"data\\preset_data.txt","w") as file_save :
                                file_save.writelines(save)
                        except Exception :
                            print("[Error] Can't decode the code")
                    elif save_options == "x" or save_options == "-" : # Back
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
            elif check_f_letter("q",False,options) == True : # Shortcut
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
    round_stat = []

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
    round_stat.clear()

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
    print(f"{col('3',fg=col_red)}")
    time.sleep(1)
    print(f"{col('2',fg=col_orange)}")
    time.sleep(1)
    print(f"{col('1',fg=col_yellow)}")
    time.sleep(1)
    print(f"{col('GO!!',fg=col_lime)}")
    
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
        print(f"\n{col(f'{round(real_accu,2)}%',fg=col_skyblue)}  {col(f'{correct}',fg=col_lime)} | {col(f'{wrong}',fg=col_red)}  x{combo}  {col(f'Score :',fg=col_grey)} {score}")

        # Addition
        if str(ran_oper) == "0" :
            time_s = time.perf_counter()
            timestart.append(str(time_s))
            ans = num1 + num2
            print(F"\nRound {text_round} :")
            text = F"{num1} + {num2} = ?? : "
            in_ans = input(str(text))

            if in_ans == str(ans) :
                print(f"{col('Correct!!',fg=col_lime)}")
                correct += 1
                cor_count += 1

            if in_ans != str(ans) :
                print(f"{col('Wrong!!',fg=col_red)}")
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
                print(f"{col('Correct!!',fg=col_lime)}")
                correct += 1
                cor_count += 1

            if in_ans != str(ans) :
                print(f"{col('Wrong!!',fg=col_red)}")
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
                print(f"{col('Correct!!',fg=col_lime)}")
                correct += 1
                cor_count += 1

            if in_ans != str(ans) :
                print(f"{col('Wrong!!',fg=col_red)}")
                wrong += 1
                wrong_count += 1

            time_e = time.perf_counter()
            timeend.append(str(time_e))

        # Division
        if str(ran_oper) == "3" :
            # Make number is divisionable
            # while True :
            #     # If number 2 is zero
            #     while num2 == 0 :
            #         num2 = random.randint(int(ran_num1),int(ran_num2))
            #         if num2 != 0 :
            #             break

            #     ans = num1 / num2

            #     len_num = len(str(round(ans,5)))
            #     if len_num < 6 :
            #         break
            #     else :
            #         num1 = random.randint(int(ran_num1),int(ran_num2))
            #         num2 = random.randint(int(ran_num1),int(ran_num2))

            def isfloatzero_regex(string):
                # We have defined a pattern for float value
                # Find the match and convert to boolean
                match_txt = re.findall(r"\.0$", string)
                if match_txt :
                    return True
                else :
                    return False

            # while True :
            #     def isfloatzero_regex(string):
            #         # We have defined a pattern for float value
            #         # Find the match and convert to boolean
            #         match_txt = re.findall(r"\.0$", string)
            #         if match_txt :
            #             return True
            #         else :
            #             return False
            #         
            #     if num2 != 0 :
            #         if num1 > num2 and num1 != 1 and num2 != 1 :
            #             ans = num1 / num2
            #             if isfloatzero_regex(str(ans)) == True :
            #                 ans = int(ans)
            #                 break
            #             else :
            #                 num1 = random.randint(ran_num1, ran_num2)
            #                 num2 = random.randint(ran_num1, ran_num2)
            #         else :
            #             num1 = random.randint(ran_num1, ran_num2)
            #             num2 = random.randint(ran_num1, ran_num2)
            #     else :
            #         num2 = random.randint(ran_num1, ran_num2)

            while True :

                if num2 == 0 :
                    num2 = random.randint(ran_num1, ran_num2)
                    continue
            
                if bool(setting.get("CheckNum2IsGreaterNum1")) == True :
                    if num1 > num2 :
                        num1 = random.randint(ran_num1, ran_num2)
                        num2 = random.randint(ran_num1, ran_num2)
                        continue
            
                if bool(setting.get("CheckNum1IsGreaterNum2")) == True :
                    if num1 < num2 :
                        num1 = random.randint(ran_num1, ran_num2)
                        num2 = random.randint(ran_num1, ran_num2)
                        continue
            
                if num1 == 1 or num2 == 1 :
                    num1 = random.randint(ran_num1, ran_num2)
                    num2 = random.randint(ran_num1, ran_num2)
                    continue
            
                ans = num1 / num2
            
                if isfloatzero_regex(str(ans)) == False :
                    num1 = random.randint(ran_num1, ran_num2)
                    num2 = random.randint(ran_num1, ran_num2)
                    continue
                
                if bool(setting.get("CheckAnsIs1")) == True :
                    if ans == 1 :
                        num1 = random.randint(ran_num1, ran_num2)
                        num2 = random.randint(ran_num1, ran_num2)
                        continue
            
                ans = int(ans)
                break

            time_s = time.perf_counter()
            timestart.append(str(time_s))

            print(F"\nRound {text_round} :")
            text = F"{num1} ÷ {num2} = ?? : "
            in_ans = input(str(text))

            if float(in_ans) == round(ans,5) :
                print(f"{col('Correct!!',fg=col_lime)}")
                correct += 1
                cor_count += 1

            if float(in_ans) != round(ans,5) :
                print(f"{col('Wrong!!',fg=col_red)}")
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
        persentage_torrance = int(setting.get("PersentTorrance"))                                                # Setting
        empty_per = 100 - real_accu
        if cor_count == 1 :
            if real_accu != 100.00 :
                real_accu = real_accu + ((persentage_torrance / 100) * empty_per)

            combo += 1
            if combo > int(setting.get("MaxComboScore")) :
                score += int(setting.get("MaxComboScore"))
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
    print(f"\n{col(f'{round(real_accu,2)}%',fg=col_skyblue)}  {col(f'{correct}',fg=col_lime)} | {col(f'{wrong}',fg=col_red)}  x{combo}  {col(f'Score :',fg=col_grey)} {score}")

    # Wait
    time.sleep(float(setting.get("PauseFinishDur")))
    
    # Print round time
    round_count = 0
    time_count = -1
    # print("\nResult")
    # print("===========================================")
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

        if time_value < 0.999 :
            time_value = f"{time_value:0.2}"
        elif time_value > 9.99 :
            time_value = f"{time_value:0.4}"
        else :
            time_value = f"{time_value:0.3}"

        timestorage.append(float(time_value))
        time_value = float(time_value)
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

        # print(str(text_t))
        # print(str(text1))
        # print(str(text4))
        # print(str(text2))
        # print(str(text3))

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

    round_stat.append(rou_min + 1)
    round_stat.append(rou_max + 1)
    round_stat.append(round_median + 1)

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
        if combo > int(setting.get("MaxComboScore")) :
            max_score += int(setting.get("MaxComboScore"))
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
        print(f"\nResult                                {exit_symbol()}")
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
        print("\n(i , /) - Session info")
        print("(d ,++) - Detail info")
        print("\n(s , *) - Save Game")
        print("(n , +) - Next Game")
        print("===========================================")
        end_options = input(">> ")
        if end_options == "i" or end_options == "/" : # Session info
            print("\nSession info")
            print("===========================================")
            print(f"Date : {date}")
            print(f"Math Game V.{version} {stage}")
            if bool(setting.get("DevMode")) == True :
                print(f"\nPython V.{platform.python_version()}")
            else :
                None
            print(str(info_text1))
            print(str(info_text2))
            print(str(info_text3))
            print(str(info_text4))
            print("===========================================")
            input("Press enter key to exit. ")
        elif end_options == "d" or end_options == "++" : # Detail info
            while True :
                print("\nDetail info")
                print("===========================================")
                print("View as")
                print("(1) - Time")
                print("(2) - Questions & Answer")
                print("\n(x , -) - Back")
                print("===========================================")
                detail_options = input(">> ")

                if detail_options == "1" :
                    print("\nTime info")
                    print("===========================================")
                    for i in range(int(noround)) :
                        stat = ""
                        if str(round_stat[0]) == str(i + 1) :
                            stat = "Min Time"
                        elif str(round_stat[1]) == str(i + 1) :
                            stat = "Max Time"
                        elif str(round_stat[2]) == str(i + 1) :
                            stat = "Med Time"
                        
                        print(f"Round {i + 1} : {timestorage[i]}s ({time_per_store[i]}%) {stat}")
                    print(f"\nAvg Time : {avgtime:0.3}s")
                    print("===========================================")
                    input("Press enter key to exit. ")
                elif detail_options == "2" :
                    print("\nQuestions & Answer info")
                    print("===========================================")
                    for i in range(int(noround)) :
                        oper_stat = ""
                        if oper_storage[i] == "0" :
                            oper_stat = "+"
                        elif oper_storage[i] == "1" :
                            oper_stat = "-"
                        elif oper_storage[i] == "2" :
                            oper_stat = "x"
                        elif oper_storage[i] == "3" :
                            oper_stat = "÷"

                        print(f"Round {i + 1} :")
                        print(f"{num1_storage[i]} {oper_stat} {num2_storage[i]} = ??")
                        if i == int(noround) - 1 :
                            print(f"{input_answer[i]} | {correct_ans[i]} [{check_storage[i]}]")
                        else :
                            print(f"{input_answer[i]} | {correct_ans[i]} [{check_storage[i]}]\n")
                    print("===========================================")
                    input("Press enter key to exit. ")
                elif detail_options == "x" or detail_options == "-" :
                    break
                else :
                    print("[Error] Invalid Input")
        elif end_options == "s" or end_options == "*" : # Save Game
            file_format = "txt"
            file_save_name = f"{time.strftime('%H%M%S%d%m%Y%z_save', time.localtime())}"
            os.chdir("saves\\")
            while True :
                print("\nSave Game")
                print("===========================================")
                print(f"(1) - Save as       : {file_save_name}.{file_format}")
                print(f"(2) - File Location : {current_path()}")
                print("(3) - Change File Format")
                print("\n(s , +) - Save")
                print("(x , -) - Back")
                print("===========================================")
                save_options = input(">> ")
                
                if save_options == "1" : # Save as
                    while True :
                        new = input(f"Change file name as ({file_save_name}): ")
                        if new == "x" :
                            break
                        else :
                            file_save_name = new
                            break
                elif save_options == "2" : # File Location
                    while True :
                        new = input(f"Change file location as ({current_path()}): ")
                        if new == "x" :
                            break
                        else :
                            if bool(os.path.isdir(new)) == True :
                                os.chdir(new)
                                break
                            else :
                                print("[Error] Invaild Location Path")
                elif save_options == "3" : # Change file fomat
                    while True :
                        print("\nChange fomat to")
                        print("===========================================")
                        print("(1) - Text File  (.txt)")
                        print("(2) - Javascript Object Notation  (.json)")
                        # print("( ) - Comma-separated values  (.csv) (Coming Soon)")
                        # print("( ) - Tom's Obvious, Minimal Language  (.toml) (Coming Soon)")
                        print("More format will coming soon...")
                        print("\n(x , -) - Back")
                        print("===========================================")
                        new = input(">> ")
                        if new == "x" or new == "-" :
                            break
                        elif new == "1" :
                            file_format = "txt"
                            break
                        elif new == "2" :
                            file_format = "json"
                            break
                        else :
                            print("[Error] Invaild Input")
                elif save_options == "s" or save_options == "+" : # Save
                    print("Saving....")
                    if file_format == "txt" : # Text File Format
                        save_file = open(f"{file_save_name}.txt","x")
                        save_file.write(f"{time_min} {time_sec:0.4} {text_real_accu} {score} {hi_combo} {correct} {wrong}\n")
                        save_file.write(f"\n")
                        for i in range(noround) :
                            text_save_box = f"{num1_storage[i]} {oper_storage[i]} {num2_storage[i]} {timestorage[i]:0.4} {input_answer[i]}\n"
                            save_file.write(text_save_box)
                        save_file.write(f"\n{time.strftime('%H %M %S %d %m %Y %z',time.localtime())}\n")
                        save_file.write(f"{noround} {ran_num1} {ran_num2} {add_key} {minus_key} {muti_key} {div_key}")
                        save_file.write(f"\n{version}")
                        save_file.close()
                    elif file_format == "json" :
                        save_file = {
                            "time_min": time_min,
                            "time_sec": f"{time_sec:0.4}",
                            "accu": text_real_accu,
                            "score": score,
                            "hi_combo": hi_combo,
                            "correct": correct,
                            "wrong": wrong,
                            "gameround": {},
                            "time": f"{time.strftime('%H %M %S %d %m %Y %z',time.localtime())}",
                            "round": noround,
                            "ran_num1": ran_num1,
                            "ran_num2": ran_num2,
                            "add": add_key,
                            "minus": minus_key,
                            "multi": muti_key,
                            "div": div_key,
                            "version": version,
                        }

                        for i in range(noround) :
                            new_time = {
                                f"{i + 1}": {
                                    "num1": num1_storage[i],
                                    "oper": oper_storage[i],
                                    "num2": num2_storage[i],
                                    "time": f"{timestorage[i]:0.4}",
                                    "input": input_answer[i]
                                }
                            }
                            save_file["gameround"].update(new_time)

                        with open(f"{file_save_name}.json","x") as file :
                            json.dump(save_file,file)

                    print("Save Complete")
                    os.chdir("..\\")
                    input("Press enter key to exit. ")
                    break
                elif save_options == "x" or save_options == "-" : # Exit
                    os.chdir("..\\")
                    break
                else :
                    print("[Error] Invalid Input")
        elif end_options == "n" or end_options == "+" : # Next Game
            break
        elif end_options == "x" or end_options == "-" : # Back
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
