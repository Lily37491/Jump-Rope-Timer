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