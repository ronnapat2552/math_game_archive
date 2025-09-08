import random
import time

print("""
Math Game by Ronnapat
Since 5 March 2023 
""")

while True :
    add_key = 0
    minus_key = 0
    muti_key = 0
    div_key = 0
    # Get user input
    noround = input("\nHow many round you gonna play?: ")
    ran_num1 = input("Select number from ")
    ran_num2 = input("to ")

    while True :
        add_key = input("\nDo you want addition ( Yes 1 | No 0 ) : ")
        minus_key = input("Do you want subtraction ( Yes 1 | No 0 ) : ")
        muti_key = input("Do you want multiplication ( Yes 1 | No 0 ) : ")
        div_key = input("Do you want division ( Yes 1 | No 0 ) : ")

        if add_key == "0" and minus_key == "0" and muti_key == "0" and div_key == "0" :
            print("\nError!! You didn\'t insert operation. Please insert operation again.")
        else :
            break

    # Set the variable
    correct = 0
    wrong = 0
    combo = 0
    hi_combo = 0

    # Set the list
    timestart = []
    timeend = []
    timestorage = []
    operation = []

    timestart.clear()
    timeend.clear()
    timestorage.clear()
    operation.clear()

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

    text_round = 0

    # Start the game 
    for i in range(int(noround)) :
        
        # Count number round every round end.
        text_round += 1
        
        # Random Phase
        num1 = random.randint(int(ran_num1),int(ran_num2))
        num2 = random.randint(int(ran_num1),int(ran_num2))
        ran_oper = random.choice(operation)
        
        # Ask Question Phase

        # Set respond
        cor_count = 0
        wrong_count = 0

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

        
        if str(ran_oper) == "3" :
            time_s = time.perf_counter()
            timestart.append(str(time_s))

            while num2 == 0 :
                num2 = random.randint(int(ran_num1),int(ran_num2))
                if num2 != 0 :
                    break

            while num1 < num2 :
                num1 = random.randint(int(ran_num1),int(ran_num2))
                num2 = random.randint(int(ran_num1),int(ran_num2))
                if num1 > num2 :
                    break

            
            ans = num1 / num2
            print(F"\nRound {text_round} :")
            text = F"{num1} ÷ {num2} = ?? : "
            in_ans = input(str(text))

            if in_ans == str(round(ans,3)) :
                print("Correct!!")
                correct += 1
                cor_count += 1

            if in_ans != str(round(ans,3)) :
                print("Wrong!!")
                wrong += 1
                wrong_count += 1

            time_e = time.perf_counter()
            timeend.append(str(time_e))
        
        # Combo System
        if cor_count == 1 :
            combo += 1
            print(F"Combo Streak x{combo}")

            if combo > hi_combo :
                hi_combo = combo

        if wrong_count == 1 :
            combo = 0
            print("Combo break! :(")
            
    
    # Loop until the round end.
    # Game End    
    
    # Stop the timer
    toc = time.perf_counter()

    round_count = 0
    time_count = -1
    print("\n========================================")
    print("                Result")
    for i in range(int(noround)) :
        round_count = round_count + 1
        time_count = time_count + 1
        text1 = F"\nTime Round {round_count}: "
        time_value = float(timeend[time_count]) - float(timestart[time_count])
        timestorage.append(float(time_value))
        value = f"    {time_value:0.3}s"
        text2 = value
        print(str(text1))
        print(str(text2))

    print("\n----------------------------------------")

    # Minute Convertion
    time_min = 0
    time_sec = toc - tic
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

    list_num = 0
    while True :
        comp_list = timestorage[int(list_num)]
        if min_num == comp_list :
            round_min = list_num
            break
        else :
            list_num += 1

    list_num = 0
    while True :
        comp_list = timestorage[int(list_num)]
        if max_num == comp_list :
            round_max = list_num
            break
        else :
            list_num += 1


    text_min = f"{min_num:0.3}s  Round {round_min + 1}"
    text_max = f"{max_num:0.3}s  Round {round_max + 1}"


    # Print Result
    print("\nTotal time :",timefinal_sec)
    print(f"Accuracy : {textaccu}%")
    print("Maximum time :",str(text_max))
    print("Mininum time :",str(text_min))
    print(f"Average time : {avgtime:0.3}s")
    print("Total correct :",correct)
    print("Total wrong :",wrong)
    print(F"\nHighest combo : x{hi_combo}")
    print("\n========================================")
    
    # Request for next round.
    key = 0
    while True:
        next_calculation = input("\nAnother one? (yes +/no -): ")
        if next_calculation == "no" or next_calculation == "n" or next_calculation == "-":
            print("\nBye!!")
            key += 1
            break
        elif next_calculation == "yes" or next_calculation == "y" or next_calculation == "+":
            break
        else :
            print("Invalid Input")
    
    # Key permission
    if key == 1 :
        break
