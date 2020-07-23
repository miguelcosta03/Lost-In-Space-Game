from tkinter import *
from random import choice
from pygame import mixer

win = Tk()

img = PhotoImage(file="background.png")
Label(win, image=img, bg="grey").pack()
win.wm_attributes('-transparentcolor', 'grey')


def start_click():
    start = start_click
    if start == start_click:
        b_start.destroy()
        mixer.init()
        mixer.music.load('music.mp3')
        mixer.music.play()

        def level1_click():
            level1 = level1_click
            if level1 == level1_click:
                b_level_1.destroy()
                b_level_2.destroy()
                b_level_3.destroy()
                lb_levels.destroy()
                lp = ['space', 'ship', 'star']

                random_password = choice(lp)

                def try_password_click():
                    try_password = try_password_click
                    p = str(password.get())
                    if try_password == try_password_click:
                        c_random_password = [char for char in lp]
                        password_string = ''.join(map(str, c_random_password))  # Convert the ll list to string
                        if random_password == 'space':
                            if p == 'space':
                                lb_attempt['text'] = 'Password Succesfully Cracked!'
                            else:
                                lb_attempt['text'] = 'Password Not Cracked!'

                        if random_password == 'ship':
                            if p == 'ship':
                                lb_attempt['text'] = 'Password Succesfully Cracked!'
                            else:
                                lb_attempt['text'] = 'Password Not Cracked!'

                        if random_password == 'star':
                            if p == 'star':
                                lb_attempt['text'] = 'Password Succesfully Cracked!'
                            else:
                                lb_attempt['text'] = 'Password Not Cracked!'

                def possible_passwords_click():
                    possible_passwords = possible_passwords_click
                    if possible_passwords == possible_passwords_click:
                        lb_possible_passwords_list['text'] = 'space \nship \nstar'

                def tip_click():
                    tip = tip_click
                    if tip == tip_click and random_password == 'space':
                        lb_tip[
                            'text'] = "This password contains 5 letters. 2-Vowels and 3-Consonants. That's where everything is "
                    elif tip == tip_click and random_password == 'spaceship':
                        lb_tip['text'] = "This password contains 9 letters. 3-Vowel and 6-Consonants. It's a transport " \
                                         "used in space"
                    elif tip == tip_click and random_password == 'star':
                        lb_tip['text'] = "This password contains 4 letters. 1-Vowel and 3-Consonants. It's a large and " \
                                         "luminous plasma sphere"

                # GUI for level 1
                # --------------------------- PASSWORD ATTEMPTS GUI ---------------------------
                password = Entry(win)
                password.place(x=350, y=250)

                lb_password_attempt = Label(win, text='Password Attempt: ')
                lb_password_attempt.place(x=200, y=250)

                b_try_password = Button(win, text='TRY', command=try_password_click)
                b_try_password.place(x=500, y=250)

                lb_attempt = Label(win, text='')
                lb_attempt.place(x=350, y=350)

                # --------------------------- END OF PASSWORD ATTEMPTS GUI ----------------------

                # --------------------------- TIPS GUI -----------------------------
                b_tip = Button(win, text='Click here for one password tip', command=tip_click)
                b_tip.place(x=100, y=150)

                lb_tip = Label(win, text='')
                lb_tip.place(x=100, y=180)

                # --------------------------- END OF TIPS GUI -----------------------

                # --------------------------- POSSIBLE PASSWORDS GUI ---------------------------
                b_possible_passwords = Button(win, text='Possible Passwords: ', command=possible_passwords_click)
                b_possible_passwords.place(x=550, y=150)

                lb_possible_passwords_list = Label(win, text='')
                lb_possible_passwords_list.place(x=680, y=150)

                # --------------------------- END OF POSSIBLE PASSWORDS GUI ---------------------

        # --------------------------- END OF LEVELS GUI --------------------
        def level2_click():
            level2 = level2_click
            if level2 == level2_click:
                b_level_1.destroy()
                b_level_2.destroy()
                b_level_3.destroy()
                lb_levels.destroy()
                lp = ['meteorite', 'Milky Way']

                random_password = choice(lp)

                def try_password_click():
                    try_password = try_password_click
                    p = str(password.get())
                    if try_password == try_password_click:
                        c_random_password = [char for char in lp]
                        password_string = ''.join(map(str, c_random_password))  # Convert the ll list to string
                        if random_password == 'meteorite':
                            if p == 'meteorite':
                                lb_attempt['text'] = 'Password Succesfully Cracked!'
                            else:
                                lb_attempt['text'] = 'Password Not Cracked!'

                        if random_password == 'milky Way':
                            if p == 'milky Way':
                                lb_attempt['text'] = 'Password Succesfully Cracked!'
                            else:
                                lb_attempt['text'] = 'Password Not Cracked!'

                def possible_passwords_click():
                    possible_passwords = possible_passwords_click
                    if possible_passwords == possible_passwords_click:
                        lb_possible_passwords_list['text'] = 'meteorite \nmilky way'

                def tip_click():
                    tip = tip_click
                    if tip == tip_click and random_password == 'meteorite':
                        lb_tip['text'] = "This password contains 9 letters. 5-Vowels and 4-Consonants. It's formed by " \
                                         "space garbage"
                    elif tip == tip_click and random_password == 'milky way':
                        lb_tip['text'] = "This password contains 8 letters. 4-Vowel and 4-Consonants. It has got a " \
                                         "drink name. "

                # GUI for level 1
                # --------------------------- PASSWORD ATTEMPTS GUI ---------------------------
                password = Entry(win)
                password.place(x=350, y=250)

                lb_password_attempt = Label(win, text='Password Attempt: ')
                lb_password_attempt.place(x=200, y=250)

                b_try_password = Button(win, text='TRY', command=try_password_click)
                b_try_password.place(x=500, y=250)

                lb_attempt = Label(win, text='')
                lb_attempt.place(x=350, y=350)

                # --------------------------- END OF PASSWORD ATTEMPTS GUI ----------------------

                # --------------------------- TIPS GUI -----------------------------
                b_tip = Button(win, text='Click here for one password tip', command=tip_click)
                b_tip.place(x=100, y=150)

                lb_tip = Label(win, text='')
                lb_tip.place(x=100, y=180)

                # --------------------------- END OF TIPS GUI -----------------------

                # --------------------------- POSSIBLE PASSWORDS GUI ---------------------------
                b_possible_passwords = Button(win, text='Possible Passwords: ', command=possible_passwords_click)
                b_possible_passwords.place(x=550, y=150)

                lb_possible_passwords_list = Label(win, text='')
                lb_possible_passwords_list.place(x=680, y=150)

                # --------------------------- END OF POSSIBLE PASSWORDS GUI ---------------------

        # --------------------------- LEVELS GUI ---------------------------
        b_level_1 = Button(win, text='Level 1', command=level1_click)
        b_level_1.place(x=300, y=150)

        b_level_2 = Button(win, text='Level 2', command=level2_click)
        b_level_2.place(x=400, y=150)

        b_level_3 = Button(win, text='Level 3')
        b_level_3.place(x=500, y=150)

        lb_levels = Label(win, text='LEVELS')
        lb_levels.place(x=400, y=100)

        # --------------------------- END OF LEVELS GUI --------------------


def close_click():
    close = close_click
    if close == close_click:
        win.destroy()


# --------------------------- GENERAL GUI ---------------------------
b_close = Button(win, text='Quit Game', command=close_click)
b_close.place(x=700, y=550)

b_start = Button(win, text='Start', command=start_click)
b_start.place(x=380, y=250)

win.geometry('800x600')
win.mainloop()
# --------------------------- END OF GENERAL GUI ---------------------------
