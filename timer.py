# Set up jump rope timer

import time  

def individual_set_countdown(set_num, input_two, input_three):
    while input_two >= 0:
        print(f"SET {set_num}:", input_two, end= '\r')
        time.sleep(1)
        input_two -= 1
    print(f"Set {set_num} is completed")
    while input_three >= 0:
        print("BREAK TIME: ", input_three, end='\r')
        time.sleep(1)
        input_three -= 1

def jumrope_timer():
    input_one = (int(input("Let's start! How many sets do you want to do today?: ")))
    input_two = int(input("How long do you want each of your set to be? (in seconds): "))
    input_three = int(input("Break in between the sets (in seconds): "))
    for num in range(1, input_one + 1):
        individual_set_countdown(num, input_two, input_three)
    print(f"Congrats!!! All {input_one} sets completed")
    exit()
    
jumrope_timer()