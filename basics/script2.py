import traceback
from typing import List
import sys
import tkinter.messagebox as messagebox
import datetime

log_mesage = []

def loop_through_sum_list(v_list: List[int]):
    """
    This function loops through a list of integers and prints the index 
    and value of elements that are divisible by 10.

    :param v_list: List of integers to be checked for divisibility by 10.
    :return: None

    ex:
        loop_through_sum_list([10, 15, 20])
    """
    try:
        for index, value in enumerate(v_list):
            if (value % 10 == 0):
                print("index = %d, value = %d" % (index, value))
    except Exception as e:
        error_log = traceback.format_exc()
        log_mesage.append(error_log)
        messagebox.showerror("Error", "An error occurred: %s" % e)

def decrement_until_zero(value: int):
    """
    This function decrements the given integer until it reaches zero.

    :param value: The integer to be decremented.
    :return: None

    ex:
        decrement_until_zero(5)
    """
    try:
        while value > 0:
            print("current value = %d" % value)
            value -= 1
    except Exception as e:
        error_log = traceback.format_exc()
        log_mesage.append(error_log)
        messagebox.showerror("Error", "An error occurred: %s" % e)

def open_log():
    logf = open("log.txt", "a")
    return logf

def write_log(message: List[str]):
    """
    This function writes a list of messages to the log file.

    :param message: List of strings to be written to the log file.
    :return: None
    """
    logf = open_log()
    logf.writelines(message)
    # time_end = datetime.datetime.now()
    # logf.write("Script ended at: %s\n" % time_end)
    logf.write("\n")
    logf.close()

# we make sure the script runs only when executed directly, not when imported
if __name__ == "__main__":
    # record the start time of the script
    time_start = datetime.datetime.now()
    log_mesage.append("============================================\n\nScript started at: %s\n" % time_start)
    # now we get the final value from the user to build a list with step values of 5 beginning from 0
    final_value = int(input("Enter an integer: "))
    # This below syntax is called a list comprehension, which is a concise way to create lists in Python
    sum_list = [step_value for step_value in range(0,final_value,5)]
    loop_through_sum_list(sum_list)
    decrement_until_zero(final_value)
    write_log(log_mesage)
    sys.exit()
    