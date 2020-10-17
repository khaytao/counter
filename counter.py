import keyboard

"""
this script maintains a counter in a txt file
"""
FILE_PATH = "counter.txt"


def uptick_counter():
    textfile = open(FILE_PATH, 'r+')
    cur_value = textfile.read()

    try:
        counter_value = int(cur_value) + 1
    except ValueError:
        counter_value = 0

    textfile.seek(0)
    textfile.write(str(counter_value))
    textfile.truncate()
    textfile.close()


def reset_counter():
    pass
# call function


keyboard.add_hotkey('ctrl+shift+1', uptick_counter)
keyboard.wait('esc')

