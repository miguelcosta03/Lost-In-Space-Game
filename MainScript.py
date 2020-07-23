from tkinter import *
import string
from random import choice

win = Tk()

img = PhotoImage(file="background.png")
Label(win, image=img, bg="grey").pack()
win.wm_attributes('-transparentcolor', 'grey')


def start_click():
    start = start_click
    if start == start_click:
        b_start.destroy()

        def level1_click():
            level1 = level1_click
            if level1 == level1_click:
                b_level_1.destroy()
                b_level_2.destroy()
                b_level_3.destroy()
                lp = ['space', 'ship', 'star']

                random_password = choice(lp)

                def try_password_click():
                    try_password = try_password_click
                    p = str(password.get())
                    if try_password == try_password_click:
                        c_random_password = [char for char in lp]
                        password_string = ''.join(map(str, c_random_password))  # Convert the ll list to string

                        letter_a_position = password_string.find('a')
                        letter_b_position = password_string.find('b')
                        letter_c_position = password_string.find('c')
                        letter_d_position = password_string.find('d')
                        letter_e_position = password_string.find('e')
                        letter_f_position = password_string.find('f')
                        letter_g_position = password_string.find('g')
                        letter_h_position = password_string.find('h')
                        letter_i_position = password_string.find('i')
                        letter_j_position = password_string.find('j')
                        letter_k_position = password_string.find('k')
                        letter_l_position = password_string.find('l')
                        letter_m_position = password_string.find('m')
                        letter_n_position = password_string.find('n')
                        letter_o_position = password_string.find('o')
                        letter_p_position = password_string.find('p')
                        letter_q_position = password_string.find('q')
                        letter_r_position = password_string.find('r')
                        letter_s_position = password_string.find('s')
                        letter_t_position = password_string.find('t')
                        letter_u_position = password_string.find('u')
                        letter_v_position = password_string.find('v')
                        letter_w_position = password_string.find('w')
                        letter_x_position = password_string.find('x')
                        letter_y_position = password_string.find('y')
                        letter_z_position = password_string.find('z')

                        # Position of letters in password attempt
                        c_password_attempt = [char for char in p]
                        password_attempt = ''.join(map(str, c_password_attempt))
                        letter_a_password_attempt_position = password_attempt.find('a')
                        letter_b_password_attempt_position = password_attempt.find('b')
                        letter_c_password_attempt_position = password_attempt.find('c')
                        letter_d_password_attempt_position = password_attempt.find('d')
                        letter_e_password_attempt_position = password_attempt.find('e')
                        letter_f_password_attempt_position = password_attempt.find('f')
                        letter_g_password_attempt_position = password_attempt.find('g')
                        letter_h_password_attempt_position = password_attempt.find('h')
                        letter_i_password_attempt_position = password_attempt.find('i')
                        letter_j_password_attempt_position = password_attempt.find('j')
                        letter_k_password_attempt_position = password_attempt.find('k')
                        letter_l_password_attempt_position = password_attempt.find('l')
                        letter_m_password_attempt_position = password_attempt.find('m')
                        letter_n_password_attempt_position = password_attempt.find('n')
                        letter_o_password_attempt_position = password_attempt.find('o')
                        letter_p_password_attempt_position = password_attempt.find('p')
                        letter_q_password_attempt_position = password_attempt.find('q')
                        letter_r_password_attempt_position = password_attempt.find('r')
                        letter_s_password_attempt_position = password_attempt.find('s')
                        letter_t_password_attempt_position = password_attempt.find('t')
                        letter_u_password_attempt_position = password_attempt.find('u')
                        letter_v_password_attempt_position = password_attempt.find('v')
                        letter_w_password_attempt_position = password_attempt.find('w')
                        letter_x_password_attempt_position = password_attempt.find('x')
                        letter_y_password_attempt_position = password_attempt.find('y')
                        letter_z_password_attempt_position = password_attempt.find('z')

                        if random_password == 'space':
                            lb_s['text'] = 'This password contains 5 letters. 2-Vowels and 3-Consoants'
                            if letter_s_position == letter_s_password_attempt_position:
                                lb_attempt['text'] = 'First Letter Succesfully Cracked'
                                if letter_p_position == letter_p_password_attempt_position:
                                    lb_attempt['text'] = 'Second Letter Succesfully Cracked'
                                    if letter_a_position == letter_a_password_attempt_position:
                                        lb_attempt['text'] = 'Third Letter Succesfully Cracked'
                                        if letter_c_position == letter_c_password_attempt_position:
                                            lb_attempt['text'] = 'Fourth Letter Succesfully Cracked'
                                            if letter_e_position == letter_e_password_attempt_position:
                                                lb_attempt['text'] = 'Fifth Letter Succesfully Cracked! Password Cracked'
                                            else:
                                                lb_attempt['text'] = 'Try again!'
                                        else:
                                            lb_attempt['text'] = 'Try again!'
                                    else:
                                        lb_attempt['text'] = 'Try again!'
                                else:
                                    lb_attempt['text'] = 'Try again!'
                            else:
                                lb_attempt['text'] = 'Try again!'

                        elif random_password == 'ship':
                            lb_s['text'] = 'This password contains 4 letters. 1-Vowel and 3-Consoants'
                            if letter_s_position == letter_s_password_attempt_position:
                                lb_attempt['text'] = 'First Letter Succesfully Cracked'
                                if letter_h_position == letter_h_password_attempt_position:
                                    lb_attempt['text'] = 'Second Letter Succesfully Cracked'
                                    if letter_i_position == letter_i_password_attempt_position:
                                        lb_attempt['text'] = 'Third Letter Succesfully Cracked'
                                        if letter_p_position == letter_p_password_attempt_position:
                                            lb_attempt['text'] = 'Fourth Letter Succesfully Cracked. Password Cracked'
                                        else:
                                            lb_attempt['text'] = 'Try again!'
                                    else:
                                        lb_attempt['text'] = 'Try again!'
                                else:
                                    lb_attempt['text'] = 'Try again!'
                            else:
                                lb_attempt['text'] = 'Try again!'

                        elif random_password == 'star':
                            lb_s['text'] = 'This password contains 4 letters. 1-Vowel and 3-Consoants'
                            if letter_s_position == letter_s_password_attempt_position:
                                lb_attempt['text'] = 'First Letter Succesfully Cracked'
                                if letter_t_position == letter_t_password_attempt_position:
                                    lb_attempt['text'] = 'Second Letter Succesfully Cracked'
                                    if letter_a_position == letter_a_password_attempt_position:
                                        lb_attempt['text'] = 'Third Letter Succesfully Cracked'
                                        if letter_a_position == letter_a_password_attempt_position:
                                            lb_attempt['text'] = 'Fourth Letter Succesfully Cracked. Password Cracked!'
                                        else:
                                            lb_attempt['text'] = 'Try again!'
                                    else:
                                        lb_attempt['text'] = 'Try again!'
                                else:
                                    lb_attempt['text'] = 'Try again!'
                            else:
                                lb_attempt['text'] = 'Try again!'
                # GUI for level 1
                password = Entry(win)
                password.place(x=350, y=250)

                lb_password_attempt = Label(win, text='Password Attempt: ')
                lb_password_attempt.place(x=200, y=250)

                b_try_password = Button(win, text='TRY', command=try_password_click)
                b_try_password.place(x=500, y=250)

                lb_attempt = Label(win, text='')
                lb_attempt.place(x=350, y=350)

                lb_s = Label(win, text='')
                lb_s.place(x=400, y=400)

        b_level_1 = Button(win, text='Level 1', command=level1_click)
        b_level_1.place(x=300, y=150)

        b_level_2 = Button(win, text='Level 2')
        b_level_2.place(x=400, y=150)

        b_level_3 = Button(win, text='Level 3')
        b_level_3.place(x=500, y=150)


# General GUI
b_start = Button(win, text='Start', command=start_click)
b_start.place(x=400, y=300)

win.geometry('800x600')
win.mainloop()
