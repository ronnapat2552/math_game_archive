import random
import time

print("""
Math Game by Ronnapat
Since 5 March 2023 
Version 2023.09.r3""")

while True :
    add_key = 0
    minus_key = 0
    muti_key = 0
    div_key = 0

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
    
    # New get user input
    while True :
        # Number round input
        while True :
            noround = input("\nHow many round you gonna play?: ")
            detectChar = noround.isnumeric()

            if detectChar == True :
                if int(noround) > 0 :
                    break
                else :
                    print("Error!! You insert number equal 0. Please insert number again.")
            elif detectChar == False :
                print("Error!! You insert letter or number below 0. Please insert number again.")
        
        # Range number input
        while True :
            ran_num1 = input("\nSelect number from : ")
            ran_num2 = input("to : ")
            detectNum1 = ran_num1.isdecimal()
            detectNum2 = ran_num2.isdecimal()
            find_NegNum1 = ran_num1.find("-", 1)
            find_NegNum2 = ran_num2.find("-", 1)

            try :
                if int(ran_num1) + 1 == int(ran_num1) + 1 and int(ran_num2) + 1 == int(ran_num2) + 1 :
                    break
            except :
                print("Error!! Please insert number again.")

        # Operator input
        while True :
            add_key = input("\nDo you want addition ( Yes 1 | No 0 ) : ")
            minus_key = input("Do you want subtraction ( Yes 1 | No 0 ) : ")
            muti_key = input("Do you want multiplication ( Yes 1 | No 0 ) : ")
            div_key = input("Do you want division ( Yes 1 | No 0 ) : ")

            if add_key == "0" and minus_key == "0" and muti_key == "0" and div_key == "0" :
                print("Error!! You didn\'t insert operation. Please insert operation again.") 
            elif add_key == "1" or minus_key == "1" or muti_key == "1" or div_key == "1" :
                break
            else :
                print("Error!! You didn\'t insert operation. Please insert operation again.") 

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

        info_text1 = F"\nTotal Round  : {noround}"
        info_text2 = F"Number Range : {ran_num1} - {ran_num2}"
        info_text3 = F"Mode :"
        info_text4 = F"  {add_check} - Plus (+)\n  {minus_check} - Minus (-)\n  {muti_check} - Mutipilcation (x)\n  {div_check} - Divide (÷)"

        print("\n======= Summary =======")
        print(str(info_text1))
        print(str(info_text2))
        print(str(info_text3))
        print(str(info_text4))
        print("\n=======================")

        # Confirmation
        key = 0
        while True :
            confirm = input("\nAre you sure (yes + | no -): ")

            # Check if input is valid
            if confirm == "y" or confirm == "yes" or confirm == "+" :
                    key += 1
                    break
            elif confirm == "n" or confirm == "no" or confirm == "-" :
                break
            else :
                print("Error!! Invalid Input")

        # Key permission
        if key == 1 :
            break

    # Set the variable
    correct = 0
    wrong = 0
    combo = 0
    hi_combo = 0
    text_round = 0
    score = 0

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
        if cor_count == 1 :
            combo += 1
            if combo > 5 :
                score += 5
            else :
                score += combo

            if combo > hi_combo :
                hi_combo = combo

        if wrong_count == 1 :
            combo = 0

    # Loop until the round end.
    # Game End    
    
    # Stop the timer
    toc = time.perf_counter()
    
    # Print round time
    round_count = 0
    time_count = -1
    print("\n=============== Result =================")
    for i in range(int(noround)) :
        round_count = round_count + 1
        time_count = time_count + 1

        text_t = F"\nRound {round_count} "

        oper_sign = ""
        if str(oper_storage[time_count]) == "0" :
            oper_sign = "+"
        elif str(oper_storage[time_count]) == "1" :
            oper_sign = "-"
        elif str(oper_storage[time_count]) == "2" :
            oper_sign = "x"
        elif str(oper_storage[time_count]) == "3" :
            oper_sign = "÷"

        text1 = f"{num1_storage[time_count]} {oper_sign} {num2_storage[time_count]} = ??"

        text2 = f"   Correct Ans : {correct_ans[time_count]}"
        text3 = f"   Your Answer : {input_answer[time_count]} [{check_storage[time_count]}]"

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

        value = f"   Time : {time_value:0.3}s"
        if time_value < 0.999 :
            value = f"   Time : {time_value:0.2}s"
        elif time_value > 9.99 :
            value = f"   Time : {time_value:0.4}s"

        value2 = f" ({time_per}%)"
        
        value3 = value + value2
        text4 = value3

        print(str(text_t))
        print(str(text1))
        print(str(text2))
        print(str(text3))
        print(str(text4))

    print("\n----------------------------------------")

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
    if accuracy == 100.00 :
        text_rank = "SX+"
    elif accuracy >= 97.50 :
        text_rank = "SX"
    elif accuracy >= 95.00 :
        text_rank = "EX+"
    elif accuracy >= 92.50 :
        text_rank = "EX"
    elif accuracy >= 90.00 :
        text_rank = "X+"
    elif accuracy >= 87.50 :
        text_rank = "X"
    elif accuracy >= 85.00 :
        text_rank = "S+"
    elif accuracy >= 82.50 :
        text_rank = "S"
    elif accuracy >= 80.00 :
        text_rank = "A+"
    elif accuracy >= 75.00 :
        text_rank = "A"
    elif accuracy >= 70.00 :
        text_rank = "B+"
    elif accuracy >= 65.00 :
        text_rank = "B"
    elif accuracy >= 60.00 :
        text_rank = "C"
    elif accuracy >= 50.00 :
        text_rank = "D"
    elif accuracy >= 25.00 :
        text_rank = "F"
    elif accuracy <= 24.99 :
        text_rank = "F-"

    # Maximum Score
    max_score = 0
    combo = 0
    for i in range(int(noround)) :
        combo += 1
        if combo > 5 :
            max_score += 5
        else :
            max_score += combo

    perfect_text = ""
    if accuracy == 100 :
        perfect_text = "Perfect!!"

    # Get date
    date = time.strftime("%a, %d %b %Y %X %z ", time.localtime())

    # Print Result
    print("\nTotal time :",timefinal_sec)
    print(f"Accuracy : {textaccu}%")
    print(f"Maximum time : {str(text_max)}")
    print(f"Median time  : {str(text_median)}")
    print(f"Mininum time : {str(text_min)}")
    print(f"Average time : {avgtime:0.3}s")
    print("Total correct :",correct)
    print("Total wrong :",wrong)
    print(F"\nHighest combo : x{hi_combo}")
    print(F"Score : {score}/{max_score} {perfect_text}")
    print(F"Rank : {text_rank}")
    print("\n------------- Session info -------------")
    print(f"\nDate : {date}")
    print(str(info_text1))
    print(str(info_text2))
    print(str(info_text3))
    print(str(info_text4))
    print("\n========================================")
    
    # Request for next round.
    key = 0
    while True:
        next_calculation = input("\nAnother one? (yes + | no -): ")
        if next_calculation == "no" or next_calculation == "n" or next_calculation == "-":
            print("\nBye!!\n")
            key += 1
            break
        elif next_calculation == "yes" or next_calculation == "y" or next_calculation == "+":
            break
        else :
            print("Invalid Input")
    
    # Key permission
    if key == 1 :
        break
