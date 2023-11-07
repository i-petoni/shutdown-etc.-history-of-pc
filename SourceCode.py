import tkinter as tk
from PIL import ImageTk, Image
import subprocess
import datetime

root = tk.Tk()
root.iconphoto(False, tk.PhotoImage(file="files/images/dot.png"))
root.title("Sekure")
root.geometry('350x550')
root.resizable(False, False)
root.config(bg="#1b1b1b")
main_canvas = tk.Canvas(root, bg="#1b1b1b", bd=0, highlightthickness=0)
main_canvas.pack(fill="both", expand=True)

reboot_canvas = tk.Canvas(root, bg="#1b1b1b", bd=0, highlightthickness=0)
shutdown_canvas = tk.Canvas(root, bg="#1b1b1b", bd=0, highlightthickness=0)
login_canvas = tk.Canvas(root, bg="#1b1b1b", bd=0, highlightthickness=0)
logoff_canvas = tk.Canvas(root, bg="#1b1b1b", bd=0, highlightthickness=0)

dated_shutdown_canvas = tk.Canvas(root, bg="#1b1b1b", bd=0, highlightthickness=0)
dated_reboot_canvas = tk.Canvas(root, bg="#1b1b1b", bd=0, highlightthickness=0)
dated_logoff_canvas = tk.Canvas(root, bg="#1b1b1b", bd=0, highlightthickness=0)


class Labels:
    def __init__(self, txt):
        self.label = tk.Label(root, font=("Bahnschrift", 11), width=10, height=11, bg="#1b1b1b", fg="white", text=txt, anchor="w")
        self.countin = tk.Label(root, font=("Bahnschrift", 11), width=2, height=11, bg="#1b1b1b", fg="#00b7c3", text=txt,
                              anchor="w")


specified_dates_events = []
first_col_txt = ""
second_col_txt = ""
third_col_txt = ""
countin_ten_txt = ""
countin_twenty_txt = ""
countin_thirty_txt = ""
indexin = 1

todays_date = str(datetime.date.today())
current_month = datetime.datetime.now().month
previous_month = 0
current_year = datetime.datetime.now().year
get_utcoffset = subprocess.run(["powershell", "-Command", "Get-TimeZone"], capture_output=True, text=True).stdout.strip()
utcoffset = int(get_utcoffset.split("\n")[4].split(":")[1].strip())
previous_date = 0
given_date = 0
next_date = 0
time = 24
time2 = 0
this = {0:30, -1:29, -2:28,-3:27, -4:26, -5:25, -6:24, -7:23, -8:22, -9:21, -10:20, -11:19, -12:18, -13:17, -14:16}
dated_events_output = ""
actual_time = []
actual_date = []

first_col = Labels(txt=first_col_txt)
second_col = Labels(txt=second_col_txt)
third_col = Labels(txt=third_col_txt)
countin_ten = Labels(txt=countin_ten_txt)
countin_twenty = Labels(txt=countin_twenty_txt)
countin_thirty = Labels(txt=countin_thirty_txt)

# images
reboot_info_button_inactive_img = ImageTk.PhotoImage(Image.open("files/images/reboot_info_inactive.png"))
reboot_info_button_active_img = ImageTk.PhotoImage(Image.open("files/images/reboot_info_active.png"))
shutdown_info_button_inactive_img = ImageTk.PhotoImage(Image.open("files/images/shutdown_info_inactive.png"))
shutdown_info_button_active_img = ImageTk.PhotoImage(Image.open("files/images/shutdown_info_active.png"))
login_info_button_inactive_img = ImageTk.PhotoImage(Image.open("files/images/login_info_inactive.png"))
login_info_button_active_img = ImageTk.PhotoImage(Image.open("files/images/login_info_active.png"))
back_active = ImageTk.PhotoImage(Image.open("files/images/back_button_active.png"))
back_inactive = ImageTk.PhotoImage(Image.open("files/images/back_button_inactive.png"))
ok_inactive = ImageTk.PhotoImage(Image.open("files/images/ok_inactive.png"))
ok_active = ImageTk.PhotoImage(Image.open("files/images/ok_active.png"))
recent_active = ImageTk.PhotoImage(Image.open("files/images/recent active.png"))
recent_inactive = ImageTk.PhotoImage(Image.open("files/images/recent inactive.png"))
todays_history_active = ImageTk.PhotoImage(Image.open("files/images/todays history active.png"))
todays_history_inactive = ImageTk.PhotoImage(Image.open("files/images/todays history inactive.png"))


# main functions
def reboot_info_button_func():
    main_canvas.pack_forget()
    reboot_canvas.pack(expand=True, fill="both")
    reboot_back_button_frame.place(relx=0.03, rely=0.02)
    reboot_back_button.pack()
    restart_history_txt.place(relx=0.26, rely=0.06)
    blue_line.place(relx=0.278, rely=0.126)
    recent_reboot_frame.place(relx=0.28, rely=0.18)
    recent_reboot_button.pack()
    todays_reboot_history_frame.place(relx=0.28, rely=0.33)
    todays_reboot_history_button.pack()
    custom_reboot_history_btn_frame.place(relx=0.6, rely=0.5)
    custom_reboot_history_btn.pack()
    custom_date_history_txt.place(relx=0.28, rely=0.48)
    custom_date.place(relx=0.3, rely=0.55)
    custom_month.place(relx=0.4, rely=0.55)
    year_txt.place(relx=0.5, rely=0.547)
    date_txt.place(relx=0.3, rely=0.6)


def shutdown_info_button_func():
    main_canvas.pack_forget()
    shutdown_canvas.pack(expand=True, fill="both")
    shutdown_back_button_frame.place(relx=0.03, rely=0.02)
    shutdown_back_button.pack()
    shutdown_history_txt.place(relx=0.22, rely=0.06)
    blue_line.place(relx=0.278, rely=0.126)
    recent_shutdown_frame.place(relx=0.28, rely=0.18)
    recent_shutdown_button.pack()
    todays_SD_history_frame.place(relx=0.28, rely=0.33)
    todays_SD_history_button.pack()
    custom_sd_history_btn_frame.place(relx=0.6, rely=0.5)
    custom_sd_history_btn.pack()
    custom_date_history_txt.place(relx=0.28, rely=0.48)
    custom_date.place(relx=0.3, rely=0.55)
    custom_month.place(relx=0.4, rely=0.55)
    year_txt.place(relx=0.5, rely=0.547)
    date_txt.place(relx=0.3, rely=0.6)


def login_info_button_func():
    main_canvas.pack_forget()
    login_canvas.pack(expand=True, fill="both")
    login_back_button_frame.place(relx=0.03, rely=0.02)
    login_back_button.pack()
    login_history_txt.place(relx=0.26, rely=0.06)
    blue_line.place(relx=0.263, rely=0.126)
    recent_login_frame.place(relx=0.28, rely=0.2)
    recent_login_button.pack()
    logoff_history_frame.place(relx=0.28, rely=0.75)
    logoff_history_btn.pack()
    arrow_decoration.place(relx=0.65, rely=0.744)


def logoff_info_button_func():
    recent_login_ok_button.pack_forget()
    recent_login_ok_frame.place_forget()
    login_canvas.pack_forget()
    logoff_canvas.pack(expand=True, fill="both")
    logoff_history_txt.place(relx=0.25, rely=0.06)
    recent_logoff_frame.place(relx=0.28, rely=0.18)
    recent_logoff_button.pack()
    todays_logoff_history_frame.place(relx=0.28, rely=0.33)
    todays_logoff_history_button.pack()
    custom_logoff_history_btn_frame.place(relx=0.6, rely=0.5)
    custom_logoff_history_btn.pack()
    custom_date_history_txt.place(relx=0.28, rely=0.48)
    custom_date.place(relx=0.3, rely=0.55)
    custom_month.place(relx=0.4, rely=0.55)
    year_txt.place(relx=0.5, rely=0.547)
    date_txt.place(relx=0.3, rely=0.6)
    login_history_frame.place(relx=0.28, rely=0.75)
    login_history_btn.pack()
    arrow_decoration2.place(relx=0.24, rely=0.744)
    try:
        recent_login_info.pack_forget()
    except NameError:
        pass


def back_to_login_button_func():
    recent_logoff_ok_button.pack_forget()
    recent_logoff_ok_frame.place_forget()
    logoff_canvas.focus_set()
    logoff_canvas.pack_forget()
    custom_date_history_txt.place_forget()
    custom_date.delete(0, "end")
    custom_month.delete(0, "end")
    custom_date.place_forget()
    custom_month.place_forget()
    year_txt.place_forget()
    date_txt.place_forget()
    custom_logoff_history_btn_frame.place_forget()
    custom_logoff_history_btn.pack_forget()
    login_canvas.pack(expand=True, fill="both")
    recent_login_frame.place(relx=0.28, rely=0.2)
    recent_login_button.pack()
    try:
        recent_logoff_info.pack_forget()
    except NameError:
        pass


def reboot_back_button_func():
    reset()
    recent_reboot_ok_button.pack_forget()
    recent_reboot_ok_button_frame.place_forget()
    reboot_canvas.pack_forget()
    blue_line.place_forget()
    custom_date_history_txt.place_forget()
    custom_date.delete(0, "end")
    custom_month.delete(0, "end")
    reboot_canvas.focus_set()
    custom_date.place_forget()
    custom_month.place_forget()
    year_txt.place_forget()
    date_txt.place_forget()
    custom_reboot_history_btn_frame.place_forget()
    custom_reboot_history_btn.pack_forget()
    no_matches_found.place_forget()
    no_matches_found.config(font=("Berlin Sans FB", 17))
    main_canvas.pack(expand=True, fill="both")
    try:
        recent_reboot_info.pack_forget()
    except NameError:
        pass


def shutdown_back_button_func():
    reset()
    recent_shutdown_ok_button.pack_forget()
    recent_shutdown_ok_button_frame.place_forget()
    shutdown_canvas.pack_forget()
    blue_line.place_forget()
    custom_date_history_txt.place_forget()
    custom_date.delete(0, "end")
    custom_month.delete(0, "end")
    shutdown_canvas.focus_set()
    custom_date.place_forget()
    custom_month.place_forget()
    year_txt.place_forget()
    date_txt.place_forget()
    custom_sd_history_btn_frame.place_forget()
    custom_sd_history_btn.pack_forget()
    no_matches_found.place_forget()
    no_matches_found.config(font=("Berlin Sans FB", 17))
    main_canvas.pack(expand=True, fill="both")
    try:
        recent_shutdown_info.pack_forget()
    except NameError:
        pass


def login_back_button_func():
    recent_login_ok_button.pack_forget()
    recent_reboot_ok_button_frame.place_forget()
    login_canvas.pack_forget()
    blue_line.place_forget()
    main_canvas.pack(expand=True, fill="both")
    try:
        recent_login_info.pack_forget()
    except NameError:
        pass


def recent_reboot():
    global given_date, previous_date, next_date, current_month, previous_month, time, time2, dated_events_output, specified_dates_events, actual_time, recent_reboot_info
    global first_col_txt, second_col_txt, third_col_txt, countin_ten_txt, countin_twenty_txt, countin_thirty_txt, indexin, actual_date
    reset()
    given_date = int(todays_date[8:10])
    if given_date > 15:
        previous_date = given_date - 15
        if utcoffset > 0:
            time = time - utcoffset
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{previous_date}T{time}:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date}T{time}:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
        if utcoffset < 0:
            next_date = given_date + 1
            time2 = time2 - utcoffset
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{previous_date}T{time2}:00:00' and @SystemTime<'{current_year}-{current_month}-{next_date}T{time2}:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
        if utcoffset == 0:
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{previous_date}T00:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date + 1}T00:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
    elif given_date <= 15:
        previous_date = this[given_date - 15]
        previous_month = current_month - 1
        if utcoffset > 0:
            time = time - utcoffset
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{previous_month}-{previous_date}T{time}:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date}T{time}:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
        if utcoffset < 0:
            next_date = given_date + 1
            time2 = time2 - utcoffset
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{previous_month}-{previous_date}T{time2}:00:00' and @SystemTime<'{current_year}-{current_month}-{next_date}T{time2}:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
        if utcoffset == 0:
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{previous_month}-{previous_date}T00:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date + 1}T00:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
    if len(dated_events_output) <= 0:
        recent_reboot_button.pack_forget()
        no_matches_found.config(font=("Berlin Sans FB", 15))
        no_matches_found.place(relx=0.22, rely=0.2)
    elif len(dated_events_output) > 0:
        somethang = dated_events_output.strip().split("Comment:")
        somethang.pop(-1)
        for i in somethang:
            if "Shutdown Type: restart" in i:
                first = i.find("Date:")
                second = i.find("Z\n")
                third = i[first:second].find("T")
                actual_date.append(i[first:second][6:16])
                actual_time.append(i[first:second][third + 1:third + 9])
        try:
            for a in actual_time:
                if a[0:5] == actual_time[actual_time.index(a) + 1][0:5]:
                    actual_time.pop(actual_time.index(a))
        except IndexError:
            pass
        try:
            for j in actual_date:
                if j[8:10] == actual_date[actual_date.index(j)+1][8:10]:
                    actual_date.pop(actual_date.index(j))
        except IndexError:
            pass
        try:
            specified_dates_events = actual_time[-1]
            actual_date = actual_date[-1]
        except IndexError:
            pass
        if len(specified_dates_events) >= 1:
            recent_reboot_info = tk.Label(recent_reboot_frame,
                                          text=f'DATE: {actual_date}\nTIME: {specified_dates_events}',
                                          font=("Bahnschrift", 9), justify="left",
                                          bd=0, bg="#1b1b1b", fg="white")
            recent_reboot_button.pack_forget()
            recent_reboot_info.pack(ipadx=5, ipady=5)
            recent_reboot_ok_button_frame.place(relx=0.62, rely=0.183)
            recent_reboot_ok_button.pack()
        else:
            recent_reboot_button.pack_forget()
            no_matches_found.config(font=("Berlin Sans FB", 15))
            no_matches_found.place(relx=0.22, rely=0.2)


def recent_reboot_ok_button_func():
    reset()
    recent_reboot_info.pack_forget()
    recent_reboot_ok_button.pack_forget()
    recent_reboot_ok_button_frame.place_forget()
    recent_reboot_button.pack()


def todays_reboot_history_func():
    global given_date, previous_date, next_date, current_month, previous_month, time, time2, dated_events_output, specified_dates_events, actual_time, actual_date
    global first_col_txt, second_col_txt, third_col_txt, countin_ten_txt, countin_twenty_txt, countin_thirty_txt, indexin
    reset()
    given_date = int(todays_date[8:10])
    if utcoffset > 0:
        if given_date != 1:
            previous_date = given_date - 1
            time = time - utcoffset
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{previous_date}T{time}:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date}T{time}:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
        else:
            previous_date = given_date
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{previous_date}T00:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date+1}T00:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
    if utcoffset < 0:
        next_date = given_date + 1
        time2 = time2 - utcoffset
        dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{given_date}T{time2}:00:00' and @SystemTime<'{current_year}-{current_month}-{next_date}T{time2}:00:00']][(EventID=1074)]]" /f:text'''
        dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                             text=True).stdout
    if utcoffset == 0:
        dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{given_date}T00:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date + 1}T00:00:00']][(EventID=1074)]]" /f:text'''
        dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                             text=True).stdout
    if len(dated_events_output) == 0:
        no_matches_found.config(font=("Berlin Sans FB", 17))
        no_matches_found.place(relx=0.18, rely=0.3)
    elif len(dated_events_output) > 0:
        something = dated_events_output.strip().split("Comment:")
        something.pop(-1)
        for i in something:
            if "Shutdown Type: restart" in i:
                first = i.find("Date:")
                second = i.find("Z\n")
                third = i[first:second].find("T")
                actual_time.append(i[first:second][third + 1:third + 9])
        if len(actual_time) == 0:
            no_matches_found.config(font=("Berlin Sans FB", 17))
            no_matches_found.place(relx=0.18, rely=0.3)
        elif len(actual_time) > 0:
            try:
                for a in actual_time:
                    if a[0:5] == actual_time[actual_time.index(a) + 1][0:5]:
                        actual_time.pop(actual_time.index(a))
            except IndexError:
                pass
            specified_dates_events = actual_time
            for s in specified_dates_events:
                if specified_dates_events.index(s) < 10:
                    first_col_txt = first_col_txt + f"{s}\n"
                    countin_ten_txt = countin_ten_txt + f"{indexin}\n"
                    indexin = indexin + 1
                if 9 < specified_dates_events.index(s) < 20:
                    second_col_txt = second_col_txt + f"{s}\n"
                    countin_twenty_txt = countin_twenty_txt + f"{indexin}\n"
                    indexin = indexin + 1
                if specified_dates_events.index(s) > 19:
                    third_col_txt = third_col_txt + f"{s}\n"
                    countin_thirty_txt = countin_thirty_txt + f"{indexin}\n"
                    indexin = indexin + 1
            first_col.label.config(text=first_col_txt)
            second_col.label.config(text=second_col_txt)
            third_col.label.config(text=third_col_txt)
            countin_ten.countin.config(text=countin_ten_txt)
            countin_twenty.countin.config(text=countin_twenty_txt)
            countin_thirty.countin.config(text=countin_thirty_txt)
    first_col.label.place(relx=0.1, rely=0.3)
    second_col.label.place(relx=0.42, rely=0.3)
    third_col.label.place(relx=0.75, rely=0.3)
    countin_ten.countin.place(relx=0.001, rely=0.3)
    countin_twenty.countin.place(relx=0.318, rely=0.3)
    countin_thirty.countin.place(relx=0.642, rely=0.3)
    blue_line.place_forget()
    recent_reboot_ok_button_frame.place_forget()
    recent_reboot_ok_button.pack_forget()
    custom_date_history_txt.place_forget()
    custom_date.delete(0, "end")
    custom_month.delete(0, "end")
    reboot_canvas.focus_set()
    custom_date.place_forget()
    custom_month.place_forget()
    year_txt.place_forget()
    date_txt.place_forget()
    reboot_canvas.pack_forget()
    dated_reboot_canvas.pack(fill="both", expand=True)
    todays_reboot_back_btn_frame.place(relx=0.03, rely=0.02)
    todays_reboot_back_btn.pack()
    dated_reboot_history_txt.place(relx=0.03, rely=0.1)
    todays_date_txt.place(relx=0.04, rely=0.15)
    try:
        recent_reboot_info.pack_forget()
    except NameError:
        pass


def todays_reboot_back_btn_func():
    reset()
    todays_date_txt.place_forget()
    todays_reboot_back_btn_frame.place_forget()
    todays_reboot_back_btn.pack_forget()
    dated_reboot_canvas.pack_forget()
    reboot_canvas.pack(fill="both", expand=True)
    blue_line.place(relx=0.278, rely=0.126)
    custom_date_history_txt.place(relx=0.28, rely=0.48)
    custom_date.place(relx=0.3, rely=0.55)
    custom_month.place(relx=0.4, rely=0.55)
    year_txt.place(relx=0.5, rely=0.547)
    date_txt.place(relx=0.3, rely=0.6)
    recent_reboot_button.pack()
    try:
        no_matches_found.place_forget()
    except NameError:
        pass


def custom_reboot_history_func():
    global given_date, previous_date, next_date, current_month, previous_month, time, time2, dated_events_output, specified_dates_events, actual_time, actual_date
    global first_col_txt, second_col_txt, third_col_txt, countin_ten_txt, countin_twenty_txt, countin_thirty_txt, indexin
    reset()
    try:
        given_date = int(custom_date.get())
        current_month = int(custom_month.get())
    except ValueError:
        pass
    if utcoffset > 0:
        if given_date != 1:
            previous_date = given_date - 1
            time = time - utcoffset
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{previous_date}T{time}:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date}T{time}:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
        else:
            previous_date = given_date
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{previous_date}T00:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date+1}T00:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
    if utcoffset < 0:
        next_date = given_date + 1
        time2 = time2 - utcoffset
        dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{given_date}T{time2}:00:00' and @SystemTime<'{current_year}-{current_month}-{next_date}T{time2}:00:00']][(EventID=1074)]]" /f:text'''
        dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                             text=True).stdout
    if utcoffset == 0:
        dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{given_date}T00:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date + 1}T00:00:00']][(EventID=1074)]]" /f:text'''
        dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                             text=True).stdout
    if len(dated_events_output) == 0:
        no_matches_found.config(font=("Berlin Sans FB", 17))
        no_matches_found.place(relx=0.18, rely=0.3)
    elif len(dated_events_output) > 0:
        something = dated_events_output.strip().split("Comment:")
        something.pop(-1)
        for i in something:
            if "Shutdown Type: restart" in i:
                first = i.find("Date:")
                second = i.find("Z\n")
                third = i[first:second].find("T")
                actual_time.append(i[first:second][third + 1:third + 9])
        if len(actual_time) == 0:
            no_matches_found.config(font=("Berlin Sans FB", 17))
            no_matches_found.place(relx=0.18, rely=0.3)
        elif len(actual_time) > 0:
            try:
                for a in actual_time:
                    if a[0:5] == actual_time[actual_time.index(a) + 1][0:5]:
                        actual_time.pop(actual_time.index(a))
            except IndexError:
                pass
            specified_dates_events = actual_time
            for s in specified_dates_events:
                if specified_dates_events.index(s) < 10:
                    first_col_txt = first_col_txt + f"{s}\n"
                    countin_ten_txt = countin_ten_txt + f"{indexin}\n"
                    indexin = indexin + 1
                if 9 < specified_dates_events.index(s) < 20:
                    second_col_txt = second_col_txt + f"{s}\n"
                    countin_twenty_txt = countin_twenty_txt + f"{indexin}\n"
                    indexin = indexin + 1
                if specified_dates_events.index(s) > 19:
                    third_col_txt = third_col_txt + f"{s}\n"
                    countin_thirty_txt = countin_thirty_txt + f"{indexin}\n"
                    indexin = indexin + 1
            first_col.label.config(text=first_col_txt)
            second_col.label.config(text=second_col_txt)
            third_col.label.config(text=third_col_txt)
            countin_ten.countin.config(text=countin_ten_txt)
            countin_twenty.countin.config(text=countin_twenty_txt)
            countin_thirty.countin.config(text=countin_thirty_txt)
    if len(custom_date.get()) != 0 and len(custom_month.get()) !=0:
        custom_date_txt.config(text=f"{current_year}-{given_date}-{current_month}")
    first_col.label.place(relx=0.1, rely=0.3)
    second_col.label.place(relx=0.42, rely=0.3)
    third_col.label.place(relx=0.75, rely=0.3)
    countin_ten.countin.place(relx=0.001, rely=0.3)
    countin_twenty.countin.place(relx=0.318, rely=0.3)
    countin_thirty.countin.place(relx=0.642, rely=0.3)
    blue_line.place_forget()
    recent_reboot_ok_button_frame.place_forget()
    recent_reboot_ok_button.pack_forget()
    custom_date_history_txt.place_forget()
    custom_date.delete(0, "end")
    custom_month.delete(0, "end")
    reboot_canvas.focus_set()
    custom_date.place_forget()
    custom_month.place_forget()
    year_txt.place_forget()
    date_txt.place_forget()
    reboot_canvas.pack_forget()
    dated_reboot_canvas.pack(fill="both", expand=True)
    custom_reboot_history_back_btn_frame.place(relx=0.03, rely=0.02)
    custom_reboot_history_back_btn.pack()
    dated_reboot_history_txt.place(relx=0.03, rely=0.1)
    custom_date_txt.place(relx=0.04, rely=0.15)
    try:
        recent_reboot_info.pack_forget()
    except NameError:
        pass


def custom_reboot_history_back_func():
    reset()
    custom_date_txt.config(text=f"")
    custom_date_txt.place_forget()
    custom_reboot_history_back_btn_frame.place_forget()
    custom_reboot_history_back_btn.pack_forget()
    dated_reboot_canvas.pack_forget()
    reboot_canvas.pack(fill="both", expand=True)
    blue_line.place(relx=0.278, rely=0.126)
    custom_date_history_txt.place(relx=0.28, rely=0.48)
    custom_date.place(relx=0.3, rely=0.55)
    custom_month.place(relx=0.4, rely=0.55)
    year_txt.place(relx=0.5, rely=0.547)
    date_txt.place(relx=0.3, rely=0.6)
    recent_reboot_button.pack()
    try:
        no_matches_found.place_forget()
    except NameError:
        pass


def recent_shutdown_func():
    global given_date, previous_date, next_date, time, time2, current_month, previous_month, dated_events_output, specified_dates_events, actual_time, recent_shutdown_info
    global first_col_txt, second_col_txt, third_col_txt, countin_ten_txt, countin_twenty_txt, countin_thirty_txt, indexin, actual_date
    reset()
    given_date = int(todays_date[8:10])
    if given_date > 7:
        previous_date = given_date - 7
        if utcoffset > 0:
            time = time - utcoffset
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{previous_date}T{time}:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date}T{time}:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
        if utcoffset < 0:
            next_date = given_date + 1
            time2 = time2 - utcoffset
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{previous_date}T{time2}:00:00' and @SystemTime<'{current_year}-{current_month}-{next_date}T{time2}:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
        if utcoffset == 0:
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{[previous_date]}T00:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date + 1}T00:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
    elif given_date <= 7:
        previous_date = this[given_date-7]
        previous_month = current_month - 1
        if utcoffset > 0:
            time = time - utcoffset
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{previous_month}-{previous_date}T{time}:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date}T{time}:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
        if utcoffset < 0:
            next_date = given_date + 1
            time2 = time2 - utcoffset
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{previous_month}-{previous_date}T{time2}:00:00' and @SystemTime<'{current_year}-{current_month}-{next_date}T{time2}:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
        if utcoffset == 0:
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{previous_month}-{previous_date}T00:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date + 1}T00:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
    if len(dated_events_output) == 0:
        recent_shutdown_button.pack_forget()
        no_matches_found.config(font=("Berlin Sans FB", 15))
        no_matches_found.place(relx=0.22, rely=0.2)
    elif len(dated_events_output) > 0:
        somethang = dated_events_output.strip().split("Comment:")
        somethang.pop(-1)
        for i in somethang:
            if "Shutdown Type: power off" in i:
                first = i.find("Date:")
                second = i.find("Z\n")
                third = i[first:second].find("T")
                actual_date.append(i[first:second][6:16])
                actual_time.append(i[first:second][third + 1:third + 9])
        try:
            for a in actual_time:
                if a[0:5] == actual_time[actual_time.index(a) + 1][0:5]:
                    actual_time.pop(actual_time.index(a))
        except IndexError:
            pass
        try:
            for j in actual_date:
                if j[8:10] == actual_date[actual_date.index(j)+1][8:10]:
                    actual_date.pop(actual_date.index(j))
        except IndexError:
            pass
        try:
            specified_dates_events = actual_time[-1]
            actual_date = actual_date[-1]
        except IndexError:
            pass
    recent_shutdown_info = tk.Label(recent_shutdown_frame, text=f'DATE: {actual_date} \nTIME: {specified_dates_events} ', font=("Bahnschrift", 10),
                                    justify="left",
                                    bd=0, bg="#1b1b1b", fg="white")
    recent_shutdown_button.pack_forget()
    recent_shutdown_info.pack(ipadx=5, ipady=5)
    recent_shutdown_ok_button_frame.place(relx=0.65, rely=0.183)
    recent_shutdown_ok_button.pack()


def recent_shutdown_ok_button_func():
    reset()
    recent_shutdown_ok_button.pack_forget()
    recent_shutdown_ok_button_frame.place_forget()
    recent_shutdown_info.pack_forget()
    recent_shutdown_button.pack()


def todays_SD_history_func():
    global given_date, previous_date, next_date, current_month, previous_month, time, time2, dated_events_output, specified_dates_events, actual_time, actual_date
    global first_col_txt, second_col_txt, third_col_txt, countin_ten_txt, countin_twenty_txt, countin_thirty_txt, indexin
    reset()
    given_date = int(todays_date[8:10])
    if utcoffset > 0:
        if given_date != 1:
            previous_date = given_date - 1
            time = time - utcoffset
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{previous_date}T{time}:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date}T{time}:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
        else:
            previous_date = given_date
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{previous_date}T00:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date+1}T00:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
    if utcoffset < 0:
        next_date = given_date + 1
        time2 = time2 - utcoffset
        dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{given_date}T{time2}:00:00' and @SystemTime<'{current_year}-{current_month}-{next_date}T{time2}:00:00']][(EventID=1074)]]" /f:text'''
        dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                             text=True).stdout
    if utcoffset == 0:
        dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{given_date}T00:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date+1}T00:00:00']][(EventID=1074)]]" /f:text'''
        dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                             text=True).stdout
    if len(dated_events_output) == 0:
        no_matches_found.config(font=("Berlin Sans FB", 17))
        no_matches_found.place(relx=0.18, rely=0.3)
    elif len(dated_events_output) > 0:
        something = dated_events_output.strip().split("Comment:")
        something.pop(-1)
        for i in something:
            if "Shutdown Type: power off" in i:
                first = i.find("Date:")
                second = i.find("Z\n")
                third = i[first:second].find("T")
                actual_time.append(i[first:second][third + 1:third + 9])
        if len(actual_time) == 0:
            no_matches_found.config(font=("Berlin Sans FB", 17))
            no_matches_found.place(relx=0.18, rely=0.3)
        elif len(actual_time) > 0:
            try:
                for a in actual_time:
                    if a[0:5] == actual_time[actual_time.index(a) + 1][0:5]:
                        actual_time.pop(actual_time.index(a))
            except IndexError:
                pass
            specified_dates_events = actual_time
            for s in specified_dates_events:
                if specified_dates_events.index(s) < 10:
                    first_col_txt = first_col_txt + f"{s}\n"
                    countin_ten_txt = countin_ten_txt + f"{indexin}\n"
                    indexin = indexin + 1
                if 9 < specified_dates_events.index(s) < 20:
                    second_col_txt = second_col_txt + f"{s}\n"
                    countin_twenty_txt = countin_twenty_txt + f"{indexin}\n"
                    indexin = indexin + 1
                if specified_dates_events.index(s) > 19:
                    third_col_txt = third_col_txt + f"{s}\n"
                    countin_thirty_txt = countin_thirty_txt + f"{indexin}\n"
                    indexin = indexin + 1
            first_col.label.config(text=first_col_txt)
            second_col.label.config(text=second_col_txt)
            third_col.label.config(text=third_col_txt)
            countin_ten.countin.config(text=countin_ten_txt)
            countin_twenty.countin.config(text=countin_twenty_txt)
            countin_thirty.countin.config(text=countin_thirty_txt)
    first_col.label.place(relx=0.1, rely=0.3)
    second_col.label.place(relx=0.42, rely=0.3)
    third_col.label.place(relx=0.75, rely=0.3)
    countin_ten.countin.place(relx=0.001, rely=0.3)
    countin_twenty.countin.place(relx=0.318, rely=0.3)
    countin_thirty.countin.place(relx=0.642, rely=0.3)
    blue_line.place_forget()
    recent_shutdown_ok_button_frame.place_forget()
    recent_shutdown_ok_button.pack_forget()
    shutdown_canvas.pack_forget()
    custom_date_history_txt.place_forget()
    custom_date.delete(0, "end")
    custom_month.delete(0, "end")
    shutdown_canvas.focus_set()
    custom_date.place_forget()
    custom_month.place_forget()
    year_txt.place_forget()
    date_txt.place_forget()
    dated_shutdown_canvas.pack(fill="both", expand=True)
    todays_SD_back_frame.place(relx=0.03, rely=0.02)
    todays_SD_back_button.pack()
    dated_sd_history_txt.place(relx=0.03, rely=0.1)
    todays_date_txt.place(relx=0.04, rely=0.15)
    try:
        recent_shutdown_info.pack_forget()
    except NameError:
        pass


def todays_SD_back_func():
    reset()
    todays_date_txt.place_forget()
    todays_SD_back_frame.place_forget()
    todays_SD_back_button.pack_forget()
    dated_shutdown_canvas.pack_forget()
    shutdown_canvas.pack(fill="both", expand=True)
    blue_line.place(relx=0.278, rely=0.126)
    custom_date_history_txt.place(relx=0.28, rely=0.48)
    custom_date.place(relx=0.3, rely=0.55)
    custom_month.place(relx=0.4, rely=0.55)
    year_txt.place(relx=0.5, rely=0.547)
    date_txt.place(relx=0.3, rely=0.6)
    recent_shutdown_button.pack()
    try:
        no_matches_found.place_forget()
    except NameError:
        pass


def custom_sd_history_func():
    global given_date, previous_date, next_date, current_month, previous_month, time, time2, dated_events_output, specified_dates_events, actual_time, actual_date
    global first_col_txt, second_col_txt, third_col_txt, countin_ten_txt, countin_twenty_txt, countin_thirty_txt, indexin
    reset()
    try:
        given_date = int(custom_date.get())
        current_month = int(custom_month.get())
    except ValueError:
        pass
    if utcoffset > 0:
        if given_date != 1:
            previous_date = given_date - 1
            time = time - utcoffset
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{previous_date}T{time}:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date}T{time}:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
        else:
            previous_date = given_date
            dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{previous_date}T00:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date+1}T00:00:00']][(EventID=1074)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
    if utcoffset < 0:
        next_date = given_date + 1
        time2 = time2 - utcoffset
        dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{given_date}T{time2}:00:00' and @SystemTime<'{current_year}-{current_month}-{next_date}T{time2}:00:00']][(EventID=1074)]]" /f:text'''
        dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                             text=True).stdout
    if utcoffset == 0:
        dated_events_cmd = f'''wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{given_date}T00:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date + 1}T00:00:00']][(EventID=1074)]]" /f:text'''
        dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                             text=True).stdout
    if len(dated_events_output) == 0:
        no_matches_found.config(font=("Berlin Sans FB", 17))
        no_matches_found.place(relx=0.18, rely=0.3)
    elif len(dated_events_output) > 0:
        something = dated_events_output.strip().split("Comment:")
        something.pop(-1)
        for i in something:
            if "Shutdown Type: power off" in i:
                first = i.find("Date:")
                second = i.find("Z\n")
                third = i[first:second].find("T")
                actual_time.append(i[first:second][third + 1:third + 9])
        if len(actual_time) == 0:
            no_matches_found.config(font=("Berlin Sans FB", 17))
            no_matches_found.place(relx=0.18, rely=0.3)
        elif len(actual_time) > 0:
            try:
                for a in actual_time:
                    if a[0:5] == actual_time[actual_time.index(a) + 1][0:5]:
                        actual_time.pop(actual_time.index(a))
            except IndexError:
                pass
            specified_dates_events = actual_time
            for s in specified_dates_events:
                if specified_dates_events.index(s) < 10:
                    first_col_txt = first_col_txt + f"{s}\n"
                    countin_ten_txt = countin_ten_txt + f"{indexin}\n"
                    indexin = indexin + 1
                if 9 < specified_dates_events.index(s) < 20:
                    second_col_txt = second_col_txt + f"{s}\n"
                    countin_twenty_txt = countin_twenty_txt + f"{indexin}\n"
                    indexin = indexin + 1
                if specified_dates_events.index(s) > 19:
                    third_col_txt = third_col_txt + f"{s}\n"
                    countin_thirty_txt = countin_thirty_txt + f"{indexin}\n"
                    indexin = indexin + 1
            first_col.label.config(text=first_col_txt)
            second_col.label.config(text=second_col_txt)
            third_col.label.config(text=third_col_txt)
            countin_ten.countin.config(text=countin_ten_txt)
            countin_twenty.countin.config(text=countin_twenty_txt)
            countin_thirty.countin.config(text=countin_thirty_txt)
            if len(custom_date.get()) != 0 and len(custom_month.get()) !=0:
                custom_date_txt.config(text=f"{current_year}-{given_date}-{current_month}")
    first_col.label.place(relx=0.1, rely=0.3)
    second_col.label.place(relx=0.42, rely=0.3)
    third_col.label.place(relx=0.75, rely=0.3)
    countin_ten.countin.place(relx=0.001, rely=0.3)
    countin_twenty.countin.place(relx=0.318, rely=0.3)
    countin_thirty.countin.place(relx=0.642, rely=0.3)
    blue_line.place_forget()
    recent_shutdown_ok_button_frame.place_forget()
    recent_shutdown_ok_button.pack_forget()
    shutdown_canvas.pack_forget()
    custom_date_history_txt.place_forget()
    custom_date.delete(0, "end")
    custom_month.delete(0, "end")
    shutdown_canvas.focus_set()
    custom_date.place_forget()
    custom_month.place_forget()
    year_txt.place_forget()
    date_txt.place_forget()
    dated_shutdown_canvas.pack(fill="both", expand=True)
    custom_sd_history_back_btn_frame.place(relx=0.03, rely=0.02)
    custom_sd_history_back_btn.pack()
    dated_sd_history_txt.place(relx=0.03, rely=0.1)
    custom_date_txt.place(relx=0.04, rely=0.15)
    try:
        recent_shutdown_info.pack_forget()
    except NameError:
        pass


def custom_sd_history_back_func():
    reset()
    custom_date_txt.place_forget()
    custom_date_txt.config(text=f"")
    custom_sd_history_back_btn_frame.place_forget()
    custom_sd_history_back_btn.pack_forget()
    dated_shutdown_canvas.pack_forget()
    shutdown_canvas.pack(fill="both", expand=True)
    blue_line.place(relx=0.278, rely=0.126)
    custom_date_history_txt.place(relx=0.28, rely=0.48)
    custom_date.place(relx=0.3, rely=0.55)
    custom_month.place(relx=0.4, rely=0.55)
    year_txt.place(relx=0.5, rely=0.547)
    date_txt.place(relx=0.3, rely=0.6)
    recent_shutdown_button.pack()
    try:
        no_matches_found.place_forget()
    except NameError:
        pass


def recent_login_func():
    global recent_login_info
    recent_logoff_info_command = "Get-LocalUser | Select Name, LastLogon"
    a = str(subprocess.run(["powershell", "-Command", recent_logoff_info_command], capture_output=True, text=True).stdout.strip())
    recent_login_info = tk.Label(recent_login_frame, text=f'{a}',
                              font=("Banscrift", 9), justify="left",
                              bd=0, bg="#1b1b1b", fg="white")
    recent_login_button.pack_forget()
    recent_login_frame.place(relx=0.16, rely=0.17)
    recent_login_info.pack(ipadx=10, ipady=10)
    recent_login_ok_frame.place(relx=0.35, rely=0.65)
    recent_login_ok_button.pack()


def recent_login_ok_func():
    recent_login_ok_button.pack_forget()
    recent_login_ok_frame.place_forget()
    recent_login_info.pack_forget()
    recent_login_frame.place(relx=0.28, rely=0.2)
    recent_login_button.pack()


def recent_logoff_func():
    global recent_logoff_info
    recent_logoff_info_command = "Get-EventLog -LogName Security -InstanceId 4647 -Newest 1"
    output_of_command = str(subprocess.run(["powershell.exe", "-Command", recent_logoff_info_command], capture_output=True))
    actual_date_time = output_of_command[384:440].split(" ")[2:5]
    recent_logoff_info = tk.Label(recent_logoff_frame, text=f'DATE: {actual_date_time[0]} {actual_date_time[1]}\nTIME: {actual_date_time[2]}',
                                 font=("Banscrift", 9), justify="left",
                                 bd=0, bg="#1b1b1b", fg="white")
    recent_logoff_button.pack_forget()
    recent_logoff_info.pack(ipadx=5, ipady=5)
    recent_logoff_ok_frame.place(relx=0.6, rely=0.183)
    recent_logoff_ok_button.pack()



def recent_logoff_ok_func():
    recent_logoff_ok_button.pack_forget()
    recent_logoff_ok_frame.place_forget()
    recent_logoff_info.pack_forget()
    recent_logoff_button.pack()


def todays_logoff_history_func():
    global given_date, previous_date, next_date, time, time2, dated_events_output
    global first_col_txt, second_col_txt, third_col_txt, countin_ten_txt, countin_twenty_txt, countin_thirty_txt, indexin
    reset()
    given_date = int(todays_date[8:10])
    if utcoffset > 0:
        if given_date != 1:
            previous_date = given_date - 1
            time = time - utcoffset
            dated_events_cmd = f'''wevtutil qe Security /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{previous_date}T{time}:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date}T{time}:00:00']][(EventID=4647)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
        else:
            previous_date = given_date
            dated_events_cmd = f'''wevtutil qe Security /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{previous_date}T00:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date+1}T00:00:00']][(EventID=4647)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
    if utcoffset < 0:
        next_date = given_date + 1
        time2 = time2 - utcoffset
        dated_events_cmd = f'''wevtutil qe Security /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{given_date}T{time2}:00:00' and @SystemTime<'{current_year}-{current_month}-{next_date}T{time2}:00:00']][(EventID=4647)]]" /f:text'''
        dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                             text=True).stdout
    if utcoffset == 0:
        dated_events_cmd = f'''wevtutil qe Security /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{given_date}T00:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date+1}T00:00:00']][(EventID=4647)]]" /f:text'''
        dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                             text=True).stdout
    if len(dated_events_output) == 0:
        no_matches_found.config(font=("Berlin Sans FB", 17))
        no_matches_found.place(relx=0.18, rely=0.3)
    elif len(dated_events_output) > 0:
        something = dated_events_output.strip().split("User initiated logoff")
        something.pop(-1)
        for i in something:
            first = i.find("Date:")
            second = i.find("Z\n")
            specified_dates_events.append(i[first:second][6:-1][11:19])
        for s in specified_dates_events:
            if specified_dates_events.index(s) < 10:
                first_col_txt = first_col_txt + f"{s}\n"
                countin_ten_txt = countin_ten_txt + f"{indexin}\n"
                indexin = indexin + 1
            if 9 < specified_dates_events.index(s) < 20:
                second_col_txt = second_col_txt + f"{s}\n"
                countin_twenty_txt = countin_twenty_txt + f"{indexin}\n"
                indexin = indexin + 1
            if specified_dates_events.index(s) > 19:
                third_col_txt = third_col_txt + f"{s}\n"
                countin_thirty_txt = countin_thirty_txt + f"{indexin}\n"
                indexin = indexin + 1
        first_col.label.config(text=first_col_txt)
        second_col.label.config(text=second_col_txt)
        third_col.label.config(text=third_col_txt)
        countin_ten.countin.config(text=countin_ten_txt)
        countin_twenty.countin.config(text=countin_twenty_txt)
        countin_thirty.countin.config(text=countin_thirty_txt)
    first_col.label.place(relx=0.1, rely=0.3)
    second_col.label.place(relx=0.42, rely=0.3)
    third_col.label.place(relx=0.75, rely=0.3)
    countin_ten.countin.place(relx=0.001, rely=0.3)
    countin_twenty.countin.place(relx=0.318, rely=0.3)
    countin_thirty.countin.place(relx=0.642, rely=0.3)
    blue_line.place_forget()
    recent_logoff_ok_frame.place_forget()
    recent_logoff_ok_button.pack_forget()
    custom_date_history_txt.place_forget()
    custom_date.delete(0, "end")
    custom_month.delete(0, "end")
    logoff_canvas.focus_set()
    custom_date.place_forget()
    custom_month.place_forget()
    year_txt.place_forget()
    date_txt.place_forget()
    logoff_canvas.pack_forget()
    dated_logoff_canvas.pack(fill="both", expand=True)
    todays_logoff_back_btn_frame.place(relx=0.03, rely=0.02)
    todays_logoff_back_btn.pack()
    dated_logoff_history_txt.place(relx=0.03, rely=0.1)
    todays_date_txt.place(relx=0.04, rely=0.15)
    try:
        recent_logoff_info.pack_forget()
    except NameError:
        pass


def todays_logoff_back_btn_func():
    reset()
    todays_date_txt.place_forget()
    todays_logoff_back_btn_frame.place_forget()
    todays_logoff_back_btn.pack_forget()
    dated_logoff_canvas.pack_forget()
    logoff_canvas.pack(fill="both", expand=True)
    blue_line.place(relx=0.278, rely=0.126)
    custom_date_history_txt.place(relx=0.28, rely=0.48)
    custom_date.place(relx=0.3, rely=0.55)
    custom_month.place(relx=0.4, rely=0.55)
    year_txt.place(relx=0.5, rely=0.547)
    date_txt.place(relx=0.3, rely=0.6)
    recent_logoff_button.pack()
    try:
        no_matches_found.place_forget()
    except NameError:
        pass


def custom_logoff_history_func():
    global given_date, previous_date, next_date, current_month, previous_month, time, time2, dated_events_output, specified_dates_events, actual_time, actual_date
    global first_col_txt, second_col_txt, third_col_txt, countin_ten_txt, countin_twenty_txt, countin_thirty_txt, indexin
    reset()
    try:
        given_date = int(custom_date.get())
        current_month = int(custom_month.get())
    except ValueError:
        pass
    if utcoffset > 0:
        if given_date != 1:
            previous_date = given_date - 1
            time = time - utcoffset
            dated_events_cmd = f'''wevtutil qe Security /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{previous_date}T{time}:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date}T{time}:00:00']][(EventID=4647)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
        else:
            previous_date = given_date
            dated_events_cmd = f'''wevtutil qe Security /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{previous_date}T00:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date+1}T00:00:00']][(EventID=4647)]]" /f:text'''
            dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                                 text=True).stdout
    if utcoffset < 0:
        next_date = given_date + 1
        time2 = time2 - utcoffset
        dated_events_cmd = f'''wevtutil qe Security /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{given_date}T{time2}:00:00' and @SystemTime<'{current_year}-{current_month}-{next_date}T{time2}:00:00']][(EventID=4647)]]" /f:text'''
        dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                             text=True).stdout
    if utcoffset == 0:
        dated_events_cmd = f'''wevtutil qe Security /q:"*[System[TimeCreated[@SystemTime>='{current_year}-{current_month}-{given_date}T00:00:00' and @SystemTime<'{current_year}-{current_month}-{given_date+1}T00:00:00']][(EventID=4647)]]" /f:text'''
        dated_events_output = subprocess.run(["powershell", "-Command", dated_events_cmd], capture_output=True,
                                             text=True).stdout
    if len(dated_events_output) == 0:
        no_matches_found.config(font=("Berlin Sans FB", 17))
        no_matches_found.place(relx=0.18, rely=0.3)
    elif len(dated_events_output) > 0:
        something = dated_events_output.strip().split("User initiated logoff")
        something.pop(-1)
        for i in something:
            first = i.find("Date:")
            second = i.find("Z\n")
            specified_dates_events.append(i[first:second][6:-1][11:19])
        for s in specified_dates_events:
            if specified_dates_events.index(s) < 10:
                first_col_txt = first_col_txt + f"{s}\n"
                countin_ten_txt = countin_ten_txt + f"{indexin}\n"
                indexin = indexin + 1
            if 9 < specified_dates_events.index(s) < 20:
                second_col_txt = second_col_txt + f"{s}\n"
                countin_twenty_txt = countin_twenty_txt + f"{indexin}\n"
                indexin = indexin + 1
            if specified_dates_events.index(s) > 19:
                third_col_txt = third_col_txt + f"{s}\n"
                countin_thirty_txt = countin_thirty_txt + f"{indexin}\n"
                indexin = indexin + 1
        first_col.label.config(text=first_col_txt)
        second_col.label.config(text=second_col_txt)
        third_col.label.config(text=third_col_txt)
        countin_ten.countin.config(text=countin_ten_txt)
        countin_twenty.countin.config(text=countin_twenty_txt)
        countin_thirty.countin.config(text=countin_thirty_txt)
        if len(custom_date.get()) != 0 and len(custom_month.get()) != 0:
            custom_date_txt.config(text=f"{current_year}-{given_date}-{current_month}")
    first_col.label.place(relx=0.1, rely=0.3)
    second_col.label.place(relx=0.42, rely=0.3)
    third_col.label.place(relx=0.75, rely=0.3)
    countin_ten.countin.place(relx=0.001, rely=0.3)
    countin_twenty.countin.place(relx=0.318, rely=0.3)
    countin_thirty.countin.place(relx=0.642, rely=0.3)
    blue_line.place_forget()
    recent_logoff_ok_frame.place_forget()
    recent_logoff_ok_button.pack_forget()
    custom_date_history_txt.place_forget()
    custom_date.delete(0, "end")
    custom_month.delete(0, "end")
    logoff_canvas.focus_set()
    custom_date.place_forget()
    custom_month.place_forget()
    year_txt.place_forget()
    date_txt.place_forget()
    logoff_canvas.pack_forget()
    dated_logoff_canvas.pack(fill="both", expand=True)
    custom_logoff_history_back_btn_frame.place(relx=0.03, rely=0.02)
    custom_logoff_history_back_btn.pack()
    dated_logoff_history_txt.place(relx=0.03, rely=0.1)
    custom_date_txt.place(relx=0.04, rely=0.15)
    try:
        recent_logoff_info.pack_forget()
    except NameError:
        pass


def custom_logoff_history_back_func():
    reset()
    custom_date_txt.place_forget()
    custom_date_txt.config(text=f"")
    custom_logoff_history_back_btn_frame.place_forget()
    custom_logoff_history_back_btn.pack_forget()
    dated_logoff_canvas.pack_forget()
    logoff_canvas.pack(fill="both", expand=True)
    blue_line.place(relx=0.278, rely=0.126)
    custom_date_history_txt.place(relx=0.28, rely=0.48)
    custom_date.place(relx=0.3, rely=0.55)
    custom_month.place(relx=0.4, rely=0.55)
    year_txt.place(relx=0.5, rely=0.547)
    date_txt.place(relx=0.3, rely=0.6)
    recent_logoff_button.pack()
    try:
        no_matches_found.place_forget()
    except NameError:
        pass


# side functions
def reset():
    global given_date, previous_date, next_date, current_month, previous_month, time, time2, dated_events_output, specified_dates_events, actual_time, actual_date
    global first_col_txt, second_col_txt, third_col_txt, countin_ten_txt, countin_twenty_txt, countin_thirty_txt, indexin
    given_date = 0
    previous_date = 0
    next_date = 0
    current_month = datetime.datetime.now().month
    previous_month = 0
    time = 24
    time2 = 0
    dated_events_output = ""
    specified_dates_events = []
    actual_time = []
    actual_date = []
    first_col_txt = ""
    second_col_txt = ""
    third_col_txt = ""
    countin_ten_txt = ""
    countin_twenty_txt = ""
    countin_thirty_txt = ""
    indexin = 1
    first_col.label.config(text=first_col_txt)
    second_col.label.config(text=second_col_txt)
    third_col.label.config(text=third_col_txt)
    countin_ten.countin.config(text=countin_ten_txt)
    countin_twenty.countin.config(text=countin_twenty_txt)
    countin_thirty.countin.config(text=countin_thirty_txt)
    first_col.label.place_forget()
    second_col.label.place_forget()
    third_col.label.place_forget()
    countin_ten.countin.place_forget()
    countin_twenty.countin.place_forget()
    countin_thirty.countin.place_forget()


def reboot_info_button_active(i):
    reboot_info_button.config(image=reboot_info_button_active_img)


def reboot_info_button_inactive(i):
    reboot_info_button.config(image=reboot_info_button_inactive_img)


def shutdown_info_button_active(o):
    shutdown_info_button.config(image=shutdown_info_button_active_img)


def shutdown_info_button_inactive(o):
    shutdown_info_button.config(image=shutdown_info_button_inactive_img)


def login_info_button_inactive(i):
    login_info_button.config(image=login_info_button_inactive_img)


def login_info_button_active(i):
    login_info_button.config(image=login_info_button_active_img)


def reboot_back_button_active(i):
    reboot_back_button.config(image=back_active)


def reboot_back_button_inactive(i):
    reboot_back_button.config(image=back_inactive)


def shutdown_back_button_active(i):
    shutdown_back_button.config(image=back_active)


def shutdown_back_button_inactive(i):
    shutdown_back_button.config(image=back_inactive)


def login_back_button_active(i):
    login_back_button.config(image=back_active)


def login_back_button_inactive(i):
    login_back_button.config(image=back_inactive)


def recent_reboot_ok_button_active(i):
    recent_reboot_ok_button.config(image=ok_active)
    recent_reboot_frame.config(bg="#00b7c3")


def recent_reboot_ok_button_inactive(i):
    recent_reboot_ok_button.config(image=ok_inactive)
    recent_reboot_frame.config(bg="#1b1b1b")


def recent_shutdown_ok_button_active(i):
    recent_shutdown_ok_button.config(image=ok_active)
    recent_shutdown_frame.config(bg="#00b7c3")


def recent_shutdown_ok_button_inactive(i):
    recent_shutdown_ok_button.config(image=ok_inactive)
    recent_shutdown_frame.config(bg="#1b1b1b")


def recent_reboot_button_active(i):
    recent_reboot_button.config(image=recent_active)


def recent_reboot_button_inactive(i):
    recent_reboot_button.config(image=recent_inactive)


def todays_reboot_history_button_inactive(i):
    todays_reboot_history_button.config(image=todays_history_inactive)


def todays_reboot_history_button_active(i):
    todays_reboot_history_button.config(image=todays_history_active)


def todays_reboot_back_btn_active(i):
    todays_reboot_back_btn.config(image=back_active)


def todays_reboot_back_btn_inactive(i):
    todays_reboot_back_btn.config(image=back_inactive)


def custom_reboot_btn_active(i):
    custom_reboot_history_btn.config(fg="#00b7c3")


def custom_reboot_btn_inactive(i):
    custom_reboot_history_btn.config(fg="white")


def custom_reboot_back_btn_active(i):
    custom_reboot_history_back_btn.config(image=back_active)


def custom_reboot_back_btn_inactive(i):
    custom_reboot_history_back_btn.config(image=back_inactive)


def recent_shutdown_button_active(i):
    recent_shutdown_button.config(image=recent_active)


def recent_shutdown_button_inactive(i):
    recent_shutdown_button.config(image=recent_inactive)


def todays_SD_history_button_active(i):
    todays_SD_history_button.config(image=todays_history_active)


def todays_SD_history_button_inactive(i):
    todays_SD_history_button.config(image=todays_history_inactive)


def todays_SD_back_active(i):
    todays_SD_back_button.config(image=back_active)
    todays_SD_history_frame.config(bg="#00b7c3")

def todays_SD_back_inactive(i):
    todays_SD_back_button.config(image=back_inactive)
    todays_SD_history_frame.config(bg="#1b1b1b")


def custom_sd_btn_active(i):
    custom_sd_history_btn.config(fg="#00b7c3")


def custom_sd_btn_inactive(i):
    custom_sd_history_btn.config(fg="white")


def custom_sd_back_btn_active(i):
    custom_sd_history_back_btn.config(image=back_active)


def custom_sd_back_btn_inactive(i):
    custom_sd_history_back_btn.config(image=back_inactive)


def recent_login_button_active(i):
    recent_login_button.config(image=recent_active)


def recent_login_button_inactive(i):
    recent_login_button.config(image=recent_inactive)


def recent_login_ok_active(i):
    recent_login_ok_button.config(image=ok_active)
    recent_login_frame.config(bg="#00b7c3")


def recent_login_ok_inactive(i):
    recent_login_ok_button.config(image=ok_inactive)
    recent_login_frame.config(bg="#1b1b1b")


def logoff_btn_active(i):
    logoff_history_btn.config(fg="#00b7c3")
    arrow_decoration.config(fg="black")


def logoff_btn_inactive(i):
    logoff_history_btn.config(fg="black")
    arrow_decoration.config(fg="#00b7c3")


def login_btn_active(i):
    login_history_btn.config(fg="#00b7c3")
    arrow_decoration2.config(fg="black")


def login_btn_inactive(i):
    login_history_btn.config(fg="black")
    arrow_decoration2.config(fg="#00b7c3")


def recent_logoff_btn_active(i):
    recent_logoff_button.config(image=recent_active)


def recent_logoff_btn_inactive(i):
    recent_logoff_button.config(image=recent_inactive)


def todays_logoff_btn_active(i):
    todays_logoff_history_button.config(image=todays_history_active)


def todays_logoff_btn_inactive(i):
    todays_logoff_history_button.config(image=todays_history_inactive)


def recent_logoff_ok_active(i):
    recent_logoff_ok_button.config(image=ok_active)
    recent_logoff_frame.config(bg="#00b7c3")


def recent_logoff_ok_inactive(i):
    recent_logoff_ok_button.config(image=ok_inactive)
    recent_logoff_frame.config(bg="#1b1b1b")


def todays_logoff_back_btn_active(i):
    todays_logoff_back_btn.config(image=back_active)


def todays_logoff_back_btn_inactive(i):
    todays_logoff_back_btn.config(image=back_inactive)


def custom_logoff_btn_active(i):
    custom_logoff_history_btn.config(fg="#00b7c3")


def custom_logoff_btn_inactive(i):
    custom_logoff_history_btn.config(fg="white")


def custom_logoff_back_btn_active(i):
    custom_logoff_history_back_btn.config(image=back_active)


def custom_logoff_back_btn_inactive(i):
    custom_logoff_history_back_btn.config(image=back_inactive)


def custom_date_handle1(i):
    text = custom_date.get()
    try:
        val = int(text)
        if len(text) == 2:
            custom_date.delete(1)
    except ValueError:
        custom_date.delete(0, "end")


def custom_date_handle2(i):
    text = custom_date.get()
    try:
        val = int(text)
        if val > 32:
            custom_date.delete(1)
    except ValueError:
        custom_date.delete(0, "end")


def custom_month_handle1(i):
    text = custom_month.get()
    try:
        val = int(text)
        if len(text) == 2:
            custom_month.delete(1)
    except ValueError:
        custom_month.delete(0, "end")


def custom_month_handle2(i):
    text = custom_month.get()
    try:
        val = int(text)
        if val > 12:
            custom_month.delete(1)
    except ValueError:
        custom_month.delete(0, "end")


blue_line = tk.LabelFrame(root, bg="#00b7c3", width=130, height=2, bd=0)
restart_history_txt = tk.Label(reboot_canvas, text="Restart History", font=("Berlin Sans FB", 17), bg="#1b1b1b", fg="black")
shutdown_history_txt = tk.Label(shutdown_canvas, text="Shutdown History", font=("Berlin Sans FB", 17), bg="#1b1b1b", fg="black")
login_history_txt = tk.Label(login_canvas, text="Login History", font=("Berlin Sans FB", 17), bg="#1b1b1b", fg="black")
logoff_history_txt = tk.Label(logoff_canvas, text="Logoff History", font=("Berlin Sans FB", 17), bg="#1b1b1b", fg="black")
arrow_decoration = tk.Label(login_canvas, text=">", font=("Berlin Sans FB", 25), bg="#1b1b1b", fg="#00b7c3")
arrow_decoration2 = tk.Label(logoff_canvas, text="<", font=("Berlin Sans FB", 25), bg="#1b1b1b", fg="#00b7c3")
dated_sd_history_txt = tk.Label(dated_shutdown_canvas, text="ShutDown History of", font=("Berlin Sans FB", 17), bg="#1b1b1b", fg="black")
dated_reboot_history_txt = tk.Label(dated_reboot_canvas, text="Reboot History of", font=("Berlin Sans FB", 17), bg="#1b1b1b", fg="black")
dated_logoff_history_txt = tk.Label(dated_logoff_canvas, text="logoff History of", font=("Berlin Sans FB", 17), bg="#1b1b1b", fg="black")
todays_date_txt = tk.Label(root, text=f"{todays_date}", font=("Bahnschrift", 12), bg="#1b1b1b", fg="#00b7c3")
no_matches_found = tk.Label(root, text="No Matches Found", font=("Berlin Sans FB", 17), bg="#1b1b1b", fg="black")
custom_date_history_txt = tk.Label(root, text="Custom Date", font=("Berlin Sans FB", 17), bg="#1b1b1b", fg="white")
custom_date = tk.Entry(root, bg="#1b1b1b", fg="#00b7c3", bd=0, highlightcolor="#00b7c3", highlightthickness=2, font=("Berlin Sans FB", 13), width=2)
custom_month = tk.Entry(root, bg="#1b1b1b", fg="#00b7c3", bd=0, highlightcolor="#00b7c3", highlightthickness=2, font=("Berlin Sans FB", 13), width=2)
year_txt = tk.Label(root, text=f"{current_year}", font=("Berlin Sans FB", 14), bg="#1b1b1b", fg="#a6a6a5")
date_txt = tk.Label(root, text="DD      MM", font=("Berlin Sans FB", 10), bg="#1b1b1b", fg="white")
custom_date_txt = tk.Label(root, text=f"", font=("Bahnschrift", 12), bg="#1b1b1b", fg="#00b7c3")

# main buttons
reboot_info_button_frame = tk.LabelFrame(main_canvas, bg="#1b1b1b", bd=0)
reboot_info_button = tk.Button(reboot_info_button_frame, image=reboot_info_button_inactive_img, bg="#1b1b1b", bd=0,
                               relief="sunken", activebackground="#1b1b1b", command=reboot_info_button_func)
reboot_info_button_frame.place(relx=0.26, rely=0.188)
reboot_info_button.pack()

shutdown_info_button_frame = tk.LabelFrame(main_canvas, bd=0, bg="#1b1b1b")
shutdown_info_button = tk.Button(shutdown_info_button_frame, bd=0, bg="#1b1b1b", activebackground="#1b1b1b",
                                 relief="sunken", image=shutdown_info_button_inactive_img, command=shutdown_info_button_func)
shutdown_info_button_frame.place(relx=0.26, rely=0.407)
shutdown_info_button.pack()

login_info_button_frame = tk.LabelFrame(main_canvas, bg="#1b1b1b", bd=0)
login_info_button = tk.Button(login_info_button_frame, bg="#1b1b1b", bd=0, activebackground="#1b1b1b",
                              relief="sunken", image=login_info_button_inactive_img, command=login_info_button_func)
login_info_button_frame.place(relx=0.26, rely=0.6248)
login_info_button.pack()

# secondary buttons
reboot_back_button_frame = tk.LabelFrame(reboot_canvas, bg="#1b1b1b", bd=0)
reboot_back_button = tk.Button(reboot_back_button_frame, bd=0, bg="#1b1b1b", relief="sunken", activebackground="#1b1b1b",
                               image=back_inactive, command=reboot_back_button_func)

recent_reboot_frame = tk.LabelFrame(reboot_canvas, padx=1, pady=1, bd=0, bg="#1b1b1b")
recent_reboot_button = tk.Button(recent_reboot_frame, command=recent_reboot, bd=0, image=recent_inactive, bg="#1b1b1b",
                                 relief="sunken", activebackground="#1b1b1b")
recent_reboot_ok_button_frame = tk.LabelFrame(reboot_canvas, bd=0, bg="#1b1b1b")
recent_reboot_ok_button = tk.Button(recent_reboot_ok_button_frame, bg="#1b1b1b", image=ok_inactive, bd=0,
                                    relief="sunken", activebackground="#1b1b1b", command=recent_reboot_ok_button_func)

todays_reboot_history_frame = tk.LabelFrame(reboot_canvas, padx=1, pady=1, bd=0, bg="#1b1b1b")
todays_reboot_history_button = tk.Button(todays_reboot_history_frame, command=todays_reboot_history_func, bd=0, image=todays_history_inactive, bg="#1b1b1b", relief="sunken", activebackground="#1b1b1b")
todays_reboot_back_btn_frame = tk.LabelFrame(dated_reboot_canvas, bd=0, bg="#1b1b1b")
todays_reboot_back_btn = tk.Button(todays_reboot_back_btn_frame, bg="#1b1b1b", image=back_inactive, bd=0, relief="sunken", activebackground="#1b1b1b", command=todays_reboot_back_btn_func)

custom_reboot_history_btn_frame = tk.LabelFrame(reboot_canvas, padx=1, pady=1, bd=0, bg="#1b1b1b")
custom_reboot_history_btn = tk.Button(custom_reboot_history_btn_frame, command=custom_reboot_history_func, text=">", fg="white",
                                      font=("Berlin Sans FB", 30), bd=0, bg="#1b1b1b", relief="sunken", activebackground="#1b1b1b")
custom_reboot_history_back_btn_frame = tk.LabelFrame(dated_reboot_canvas, padx=1, pady=1, bd=0, bg="#1b1b1b")
custom_reboot_history_back_btn = tk.Button(custom_reboot_history_back_btn_frame, command=custom_reboot_history_back_func, fg="white", image=back_inactive,
                                      font=("Berlin Sans FB", 30), bd=0, bg="#1b1b1b", relief="sunken", activebackground="#1b1b1b")

shutdown_back_button_frame = tk.LabelFrame(shutdown_canvas, bg="#1b1b1b", bd=0)
shutdown_back_button = tk.Button(shutdown_back_button_frame, bd=0, bg="#1b1b1b", relief="sunken", activebackground="#1b1b1b", image=back_inactive, command=shutdown_back_button_func)

recent_shutdown_frame = tk.LabelFrame(shutdown_canvas, padx=1, pady=1, bd=0, bg="#1b1b1b")
recent_shutdown_button = tk.Button(recent_shutdown_frame, command=recent_shutdown_func, bd=0, image=recent_inactive, bg="#1b1b1b", activebackground="#1b1b1b", relief="sunken")
recent_shutdown_ok_button_frame = tk.LabelFrame(shutdown_canvas, bd=0, bg="#1b1b1b")
recent_shutdown_ok_button = tk.Button(recent_shutdown_ok_button_frame, bg="#1b1b1b", image=ok_inactive, bd=0, relief="sunken", activebackground="#1b1b1b", command=recent_shutdown_ok_button_func)

todays_SD_history_frame = tk.LabelFrame(shutdown_canvas, bd=0, bg="#1b1b1b", padx=1, pady=1)
todays_SD_history_button = tk.Button(todays_SD_history_frame, bd=0, bg="#1b1b1b", image=todays_history_inactive, relief="sunken", activebackground="#1b1b1b", command=todays_SD_history_func)
todays_SD_back_frame = tk.LabelFrame(dated_shutdown_canvas, bd=0, bg="#1b1b1b")
todays_SD_back_button = tk.Button(todays_SD_back_frame, bg="#1b1b1b", image=back_inactive, bd=0, relief="sunken", activebackground="#1b1b1b", command=todays_SD_back_func)

custom_sd_history_btn_frame = tk.LabelFrame(shutdown_canvas, padx=1, pady=1, bd=0, bg="#1b1b1b")
custom_sd_history_btn = tk.Button(custom_sd_history_btn_frame, command=custom_sd_history_func, text=">", fg="white",
                                      font=("Berlin Sans FB", 30), bd=0, bg="#1b1b1b", relief="sunken", activebackground="#1b1b1b")
custom_sd_history_back_btn_frame = tk.LabelFrame(dated_shutdown_canvas, padx=1, pady=1, bd=0, bg="#1b1b1b")
custom_sd_history_back_btn = tk.Button(custom_sd_history_back_btn_frame, command=custom_sd_history_back_func, fg="white", image=back_inactive,
                                      font=("Berlin Sans FB", 30), bd=0, bg="#1b1b1b", relief="sunken", activebackground="#1b1b1b")

login_back_button_frame = tk.LabelFrame(login_canvas, bg="#1b1b1b", bd=0)
login_back_button = tk.Button(login_back_button_frame, bd=0, bg="#1b1b1b", relief="sunken", activebackground="#1b1b1b", image=back_inactive, command=login_back_button_func)

recent_login_frame = tk.LabelFrame(login_canvas, bd=0, bg="#1b1b1b", padx=1, pady=1)
recent_login_button = tk.Button(recent_login_frame, bd=0, bg="#1b1b1b", image=recent_inactive, relief="sunken", activebackground="#1b1b1b", command=recent_login_func)
recent_login_ok_frame = tk.LabelFrame(login_canvas, bd=0, bg="#1b1b1b")
recent_login_ok_button = tk.Button(recent_login_ok_frame, bg="#1b1b1b", image=ok_inactive, bd=0, relief="sunken", activebackground="#1b1b1b", command=recent_login_ok_func)

recent_logoff_frame = tk.LabelFrame(logoff_canvas, bd=0, bg="#1b1b1b", padx=1, pady=1)
recent_logoff_button = tk.Button(recent_logoff_frame, bd=0, bg="#1b1b1b", image=recent_inactive, relief="sunken", activebackground="#1b1b1b", command=recent_logoff_func)
recent_logoff_ok_frame = tk.LabelFrame(logoff_canvas, bd=0, bg="#1b1b1b")
recent_logoff_ok_button = tk.Button(recent_logoff_ok_frame, bg="#1b1b1b", image=ok_inactive, bd=0, relief="sunken", activebackground="#1b1b1b", command=recent_logoff_ok_func)

todays_logoff_history_frame = tk.LabelFrame(logoff_canvas, bd=0, bg="#1b1b1b", padx=1, pady=1)
todays_logoff_history_button = tk.Button(todays_logoff_history_frame, bd=0, bg="#1b1b1b", image=todays_history_inactive, relief="sunken", activebackground="#1b1b1b", command=todays_logoff_history_func)
todays_logoff_back_btn_frame = tk.LabelFrame(dated_logoff_canvas, bd=0, bg="#1b1b1b")
todays_logoff_back_btn = tk.Button(todays_logoff_back_btn_frame, bg="#1b1b1b", image=back_inactive, bd=0, relief="sunken", activebackground="#1b1b1b", command=todays_logoff_back_btn_func)

custom_logoff_history_btn_frame = tk.LabelFrame(logoff_canvas, padx=1, pady=1, bd=0, bg="#1b1b1b")
custom_logoff_history_btn = tk.Button(custom_logoff_history_btn_frame, command=custom_logoff_history_func, text=">", fg="white",
                                      font=("Berlin Sans FB", 30), bd=0, bg="#1b1b1b", relief="sunken", activebackground="#1b1b1b")
custom_logoff_history_back_btn_frame = tk.LabelFrame(dated_logoff_canvas, padx=1, pady=1, bd=0, bg="#1b1b1b")
custom_logoff_history_back_btn = tk.Button(custom_logoff_history_back_btn_frame, command=custom_logoff_history_back_func, fg="white", image=back_inactive,
                                      font=("Berlin Sans FB", 30), bd=0, bg="#1b1b1b", relief="sunken", activebackground="#1b1b1b")

logoff_history_frame = tk.LabelFrame(login_canvas, bg="#1b1b1b", bd=0)
logoff_history_btn = tk.Button(logoff_history_frame, text="Logoff History", font=("Berlin Sans FB", 16), relief="sunken", activebackground="#1b1b1b", bg="#1b1b1b", bd=0, command=logoff_info_button_func)
login_history_frame = tk.LabelFrame(logoff_canvas, bg="#1b1b1b", bd=0)
login_history_btn = tk.Button(login_history_frame, text="Login History", font=("Berlin Sans FB", 16), relief="sunken", activebackground="#1b1b1b", bg="#1b1b1b", bd=0, command=back_to_login_button_func)

# binding functions
# Main buttons
reboot_info_button.bind("<Enter>", reboot_info_button_active)
reboot_info_button.bind("<Leave>", reboot_info_button_inactive)
shutdown_info_button.bind("<Enter>", shutdown_info_button_active)
shutdown_info_button.bind("<Leave>", shutdown_info_button_inactive)
login_info_button.bind("<Enter>", login_info_button_active)
login_info_button.bind("<Leave>", login_info_button_inactive)
logoff_history_btn.bind("<Enter>", logoff_btn_active)
logoff_history_btn.bind("<Leave>", logoff_btn_inactive)

#Main back buttons
reboot_back_button.bind("<Enter>", reboot_back_button_active)
reboot_back_button.bind("<Leave>", reboot_back_button_inactive)
shutdown_back_button.bind("<Enter>", shutdown_back_button_active)
shutdown_back_button.bind("<Leave>", shutdown_back_button_inactive)
login_back_button.bind("<Enter>", login_back_button_active)
login_back_button.bind("<Leave>", login_back_button_inactive)
login_history_btn.bind("<Enter>", login_btn_active)
login_history_btn.bind("<Leave>", login_btn_inactive)

#reboot functions btns
recent_reboot_button.bind("<Enter>", recent_reboot_button_active)
recent_reboot_button.bind("<Leave>", recent_reboot_button_inactive)
recent_reboot_ok_button.bind("<Enter>", recent_reboot_ok_button_active)
recent_reboot_ok_button.bind("<Leave>", recent_reboot_ok_button_inactive)
todays_reboot_history_button.bind("<Enter>", todays_reboot_history_button_active)
todays_reboot_history_button.bind("<Leave>", todays_reboot_history_button_inactive)
todays_reboot_back_btn.bind("<Enter>", todays_reboot_back_btn_active)
todays_reboot_back_btn.bind("<Leave>", todays_reboot_back_btn_inactive)
custom_reboot_history_btn.bind("<Enter>", custom_reboot_btn_active)
custom_reboot_history_btn.bind("<Leave>", custom_reboot_btn_inactive)
custom_reboot_history_back_btn.bind("<Enter>", custom_reboot_back_btn_active)
custom_reboot_history_back_btn.bind("<Leave>", custom_reboot_back_btn_inactive)

#shutdown functions btns
recent_shutdown_button.bind("<Enter>", recent_shutdown_button_active)
recent_shutdown_button.bind("<Leave>", recent_shutdown_button_inactive)
recent_shutdown_ok_button.bind("<Enter>", recent_shutdown_ok_button_active)
recent_shutdown_ok_button.bind("<Leave>", recent_shutdown_ok_button_inactive)
todays_SD_history_button.bind("<Enter>", todays_SD_history_button_active)
todays_SD_history_button.bind("<Leave>", todays_SD_history_button_inactive)
todays_SD_back_button.bind("<Enter>", todays_SD_back_active)
todays_SD_back_button.bind("<Leave>", todays_SD_back_inactive)
custom_sd_history_btn.bind("<Enter>", custom_sd_btn_active)
custom_sd_history_btn.bind("<Leave>", custom_sd_btn_inactive)
custom_sd_history_back_btn.bind("<Enter>", custom_sd_back_btn_active)
custom_sd_history_back_btn.bind("<Leave>", custom_sd_back_btn_inactive)

#login functions btns
recent_login_button.bind("<Enter>", recent_login_button_active)
recent_login_button.bind("<Leave>", recent_login_button_inactive)
recent_login_ok_button.bind("<Enter>", recent_login_ok_active)
recent_login_ok_button.bind("<Leave>", recent_login_ok_inactive)

#logoff functions btns
recent_logoff_button.bind("<Enter>", recent_logoff_btn_active)
recent_logoff_button.bind("<Leave>", recent_logoff_btn_inactive)
recent_logoff_ok_button.bind("<Enter>", recent_logoff_ok_active)
recent_logoff_ok_button.bind("<Leave>", recent_logoff_ok_inactive)
todays_logoff_history_button.bind("<Enter>", todays_logoff_btn_active)
todays_logoff_history_button.bind("<Leave>", todays_logoff_btn_inactive)
todays_logoff_back_btn.bind("<Enter>", todays_logoff_back_btn_active)
todays_logoff_back_btn.bind("<Leave>", todays_logoff_back_btn_inactive)
custom_logoff_history_btn.bind("<Enter>", custom_logoff_btn_active)
custom_logoff_history_btn.bind("<Leave>", custom_logoff_btn_inactive)
custom_logoff_history_back_btn.bind("<Enter>", custom_logoff_back_btn_active)
custom_logoff_history_back_btn.bind("<Leave>", custom_logoff_back_btn_inactive)

#Miscellaneous
arrow_decoration.bind("<Enter>", logoff_btn_active)
arrow_decoration.bind("<Leave>", logoff_btn_inactive)
arrow_decoration2.bind("<Enter>", login_btn_active)
arrow_decoration2.bind("<Leave>", login_btn_inactive)
custom_date.bind("<Key>", custom_date_handle1)
custom_date.bind("<KeyRelease>", custom_date_handle2)
custom_month.bind("<Key>", custom_month_handle1)
custom_month.bind("<KeyRelease>", custom_month_handle2)

root.mainloop()
