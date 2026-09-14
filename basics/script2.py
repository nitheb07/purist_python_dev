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
    logf = open_log()
    logf.writelines(message)
    logf.close()

# we make sure the script runs only when executed directly, not when imported
if __name__ == "__main__":
    time_start = datetime.datetime.now()
    log_mesage.append("Script started at: %s\n" % time_start)
    a = int(input("Enter an integer: "))
    sum_list = [i for i in range(0,a,5)]
    loop_through_sum_list(sum_list)
    decrement_until_zero(a)
    # time_end = datetime.datetime.now()
    # log_mesage.append("Script ended at: %s\n" % time_end)
    write_log(log_mesage)
    sys.exit()
    