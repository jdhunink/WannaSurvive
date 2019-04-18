from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import subprocess

from crontab import CronTab

backup_script = "backup.sh"
dir_folder_path = ''
destination_folder_path = ''

def backup_browse_button():
    global dir_folder_path
    filename = filedialog.askdirectory()
    dir_folder_path.set(filename)
    print(filename)

def destination_browse_button():
    global destination_folder_path
    destination_filename = filedialog.askdirectory()
    destination_folder_path.set(destination_filename)
    print(destination_filename)

def schedule_backup():
    cron = CronTab(user=True)
    job = cron.new(command='./mount.sh')

    if(frequency == "hourly"):
        job.hour.every(1)
        print("Cron job created.")

    elif(frequency == "daily"):
        job.daily.every(1)
        job.hour.on(time)
        print("Cron job created.")

    elif(frequency == "weekly"):
        job.weekly.every(1)
        job.day.on(day)
        print("Cron job created.")

    elif(frequency == "monthly"):
        job.monthly.every(1)
        job.day.on(day)
        print("Cron job created.")

    messagebox.showinfo("Backup Status", "Backup Scheduled")
    print("Backup Scheduled")

def backup_now():
    print("Backing Up Now")
    subprocess.call('chmod 775 mount.sh', shell=True)
    subprocess.call('chmod 775 backup.sh', shell=True)
    args = []
    args.append('./mount.sh')
    args.append(str(dir_folder_path.get()))
    args.append(str(destination_folder_path.get()))
    p = subprocess.Popen(args)
    tkMessageBox.showinfo("Backup Status", "The backup is complete")



class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("WannaSurvive")

        master.geometry("900x550")

        #Title Label
        title = Label(master, text="WannaSurvive", fg="Coral", bg="Gray24",anchor=W, padx=30, font=("Times 40 bold"))
        title.pack(fill=X, ipadx=10, ipady=10)

        #Left Frame
        leftFrame = Frame(master, borderwidth=1, relief=SOLID)

        #Left Tab Title
        tabtitle1 = Label(leftFrame, text="Home", fg="Coral", bg="Gray24", anchor=W, padx=15, font=("Times 34 bold"))
        tabtitle1.pack(fill=X, ipadx=10, ipady=5, side=TOP)

        T = Text(leftFrame, width=51, height=10, fg="Coral", bg="Gray24", font=("Times 16"), highlightthickness=0, padx= 15)
        T.pack(fill=X, ipady=10, side=TOP)
        T.insert(INSERT, "WannaSurvive is built to keep your data safe. We've developed a backup software built on the premise of protecting your \ninformation from unwanted encryption that may occur from a \na ransomware attack. Ransomware is built specifically to \nencrypt all of your personal and company data, and hold it \nhostage. Our software looks to combat that via a clever \nworkaround to how Ransomware virus' are designed. We \ncreate symbolic links to your attached storage drives only \nwhen a backup is about to begin. After the backup is complete we sever that connection and isolate your backup drive from \nany ransomware virus in the world.")

        tabtitle1 = Label(leftFrame, text="About", fg="Coral", bg="Gray24", anchor=W, padx=15, font=("Times 34 bold"))
        tabtitle1.pack(fill=X, ipadx=10, ipady=5, side=TOP)

        #Body Text
        #hometext = Label(leftFrame, width=49, anchor=W, fg="Coral", bg="Gray24", text = "WannaSurvive was created as a senior seminar project by \nJacob Hunink, Andrea Goode and Jesse Lippincot.")
        #hometext.pack(ipadx=2, ipady=10, side=TOP)

        T2= Text(leftFrame, width=49, height=3, fg="Coral", bg="Gray24", font=("Times 16"), highlightthickness=0, padx= 15)
        T2.pack(fill=X, ipadx=2, ipady=10, side=TOP)
        T2.insert(INSERT, "WannaSurvive was created as a Senior Seminar project by \nJacob Hunink, Andrea Goode and Jesse Lippincot for the \nspring semester 2019.")


        BackupNowFrame = Frame(leftFrame, bg="Gray24", padx=10)
        BackupButton = Button(BackupNowFrame, text="Backup Now", command=backup_now, foreground="Gray20", font=("Times 28 bold"), bg="Gray24", highlightbackground='Gray60', activeforeground="Coral")
        BackupButton.pack(ipadx=10, ipady=5, side=LEFT)

        BackupNowFrame.pack(fill=BOTH, expand=YES, ipadx=10, ipady=5, side=BOTTOM)

        #Packing Left Frame
        leftFrame.pack(fill=BOTH, expand=YES, side=LEFT)



        #Right Frame
        #Right Frame
        #Right Frame
        #Right Frame
        RightFrame = Frame(master, borderwidth=1, relief=SOLID)

        #Right Tab Title
        tabtitle2 = Label(RightFrame, width=24, anchor=W, padx=15, text="Schedule Backup",fg="Coral", bg="Gray24", font=("Times 34 bold"))
        tabtitle2.pack(ipadx=10, ipady=5, side=TOP)

        frequency = StringVar(root)
        weekday = StringVar(root)
        #Button Frame
        #Button Frame
        #Button Frame
        #Button Frame
        ButtonFrame = Frame(RightFrame, height=80, bg="Gray24", padx =60)
        #Radio Buttons
        hourly = Radiobutton(ButtonFrame, text="Hourly", anchor=W, font=("Times 16 bold"), foreground="Coral", bg="Gray24", variable=frequency, value="Hourly")
        hourly.pack(padx=3, ipady=5, side=LEFT)

        daily = Radiobutton(ButtonFrame, text="Daily", anchor=W, font=("Times 16 bold"), foreground="Coral", bg="Gray24", state=ACTIVE, variable=frequency, value="Daily")
        daily.pack(ipadx=3, ipady=5, side=LEFT)

        weekly = Radiobutton(ButtonFrame, text="Weekly", anchor=W, font=("Times 16 bold"), foreground="Coral", bg="Gray24", variable=frequency, value="Weekly")
        weekly.pack(ipadx=3, ipady=5, side=LEFT)

        Monthly = Radiobutton(ButtonFrame, text="Monthly", anchor=W, font=("Times 16 bold"), foreground="Coral", bg="Gray24", variable=frequency, value="Monthly")
        Monthly.pack(ipadx=3, ipady=5, side=LEFT)

        ButtonFrame.pack(fill=X, ipady=10, side=TOP)

        ButtonFrame2 = Frame(RightFrame, height=80, bg="Gray24", padx =10)
        #Radio Buttons
        Mon = Radiobutton(ButtonFrame2, text="Mon", anchor=W, font=("Times 16 bold"), foreground="Coral", bg="Gray24", state=ACTIVE, variable=weekday, value="Mon")
        Mon.pack(padx=3, ipady=5, side=LEFT)

        Tue = Radiobutton(ButtonFrame2, text="Tue", anchor=W, font=("Times 16 bold"), foreground="Coral", bg="Gray24", variable=weekday, value="Tue")
        Tue.pack(ipadx=3, ipady=5, side=LEFT)

        Wed = Radiobutton(ButtonFrame2, text="Wed", anchor=W, font=("Times 16 bold"), foreground="Coral", bg="Gray24", variable=weekday, value="Wed")
        Wed.pack(ipadx=3, ipady=5, side=LEFT)

        Thur = Radiobutton(ButtonFrame2, text="Thur", anchor=W, font=("Times 16 bold"), foreground="Coral", bg="Gray24", variable=weekday, value="Thur")
        Thur.pack(ipadx=3, ipady=5, side=LEFT)

        Fri = Radiobutton(ButtonFrame2, text="Fri", anchor=W, font=("Times 16 bold"), foreground="Coral", bg="Gray24", variable=weekday, value="Fri")
        Fri.pack(ipadx=3, ipady=5, side=LEFT)

        Sat = Radiobutton(ButtonFrame2, text="Sat", anchor=W, font=("Times 16 bold"), foreground="Coral", bg="Gray24", variable=weekday, value="Sat")
        Sat.pack(ipadx=3, ipady=5, side=LEFT)

        Sun = Radiobutton(ButtonFrame2, text="Sun", anchor=W, font=("Times 16 bold"), foreground="Coral", bg="Gray24", variable=weekday, value="Sun")
        Sun.pack(ipadx=3, ipady=5, side=LEFT)

        ButtonFrame2.pack(fill=X, ipady=10, side=TOP)

        #Time Selection Frame
        #Time Selection Frame
        #Time Selection Frame
        #Time Selection Frame

        TimeFrame = Frame(RightFrame, bg="Gray24", padx =20)
        time = StringVar(root)

        #Dictionary
        Times = {'0:00':1,'1:00':2,'2:00':3,'3:00':4,'4:00':5,'5:00':6,'6:00':7,'7:00':8,'8:00':9,'9:00':10,'10:00':11,'11:00':12,
        '12:00':13,'13:00':14,'14:00':15,'15:00':16,'16:00':17,'17:00':18,'18:00':19,'19:00':20,'20:00':21,'21:00':22,'22:00':23,'23:00':24}
        time.set('0:00')

        timetext = Label(TimeFrame, foreground="Coral", font=("Times 16 bold"), bg="Gray24", text="Backup Time:", anchor=W)
        timetext.pack(ipadx=5, ipady=5, side=LEFT)
        timeMenu = OptionMenu(TimeFrame,time, *Times)
        timeMenu.pack(ipadx=5, ipady=5, side=LEFT)
        timeMenu.config(foreground="Gray10", font=("Times 16 bold"), bg="Gray24")

        DayOfMonthFrame = Frame(TimeFrame, bg="Gray24", padx =20)
        DayOfMonth = StringVar(root)

        DaysOfMonth = {'1st':1, '2nd':2, '3rd':3, '4th':4, '5th':5, '6th':6, '7th':7, '8th':8, '9th':9, '10th':10, '11th':11, '12th':12, '13th':13, '14th':14, '15th':15,
        '16th':16, '17th':17, '18th':18, '19th':19, '20th':20, '21st':21, '22nd':22, '23th':23, '24th':24, '25th':25, '26th':26, '27th':27, '28th':28, '29th':29, '30th':30, '31st':31}

        DayOfMonth.set('1st')

        DayOfMonthMenu = OptionMenu(TimeFrame, DayOfMonth, *DaysOfMonth)
        DayOfMonthMenu.pack(ipadx=5, ipady=5, side=RIGHT)
        DayOfMonthMenu.config(foreground="Gray10", font=("Times 16 bold"), bg="Gray24")

        dayOfMonthText = Label(TimeFrame, foreground="Coral", font=("Times 16 bold"), bg="Gray24", text="Day of Month", anchor=W)
        dayOfMonthText.pack(ipadx=5, ipady=5, side=RIGHT)
        TimeFrame.pack(fill=X, ipadx=10, ipady=10, side=TOP)

        #Backup Directory Selection
        #Backup Directory Selection
        #Backup Directory Selection
        #Backup Directory Selection

        BackupDirFrame = Frame(RightFrame, height=140, bg="Gray24", padx =10)
        BackupDirText = Label(BackupDirFrame, foreground="Coral", font=("Times 16 bold"), bg="Gray24", text="Backup Directory: ", anchor=W)
        BackupDirText.pack(ipadx=1, ipady=2, side=LEFT)

        dir_folder_path.set("No Directory Selected")
        BackupDirText = Label(BackupDirFrame, foreground="Coral", font=("Times 16 bold"), bg="Gray24", textvariable=dir_folder_path, anchor=W)
        BackupDirText.pack(ipadx=2, ipady=2, side=LEFT)

        BackupDirFrame.pack(fill=X, ipadx=10, ipady=2)

        BackupButtonFrame = Frame(RightFrame, height=140, bg="Gray24", padx =10)

        button2 = Button(BackupButtonFrame, height=1, width=8, text="Browse", command=backup_browse_button, foreground="Gray20", font=("Times 16 bold"), bg="Gray24", highlightbackground='Gray60', activeforeground="Coral")
        button2.pack(ipadx=10, ipady=5, side=LEFT)

        BackupButtonFrame.pack(fill=X, ipadx=10, ipady=8)

        #Destination Directory Selection
        #Destination Directory Selection
        #Destination Directory Selection
        #Destination Directory Selection

        DestinationDirFrame = Frame(RightFrame, height=100, bg="Gray24", padx =10)
        DestinationDirText = Label(DestinationDirFrame, foreground="Coral", font=("Times 16 bold"), bg="Gray24", text="Destination Directory: ", anchor=W)
        DestinationDirText.pack(ipadx=1, ipady=2, side=LEFT)

        destination_folder_path.set("No Directory Selected")
        DestinationDirText = Label(DestinationDirFrame, foreground="Coral", font=("Times 16 bold"), bg="Gray24", textvariable=destination_folder_path, anchor=W)
        DestinationDirText.pack(ipadx=2, ipady=2, side=LEFT)

        DestinationDirFrame.pack(fill=X, ipadx=10, ipady=2)

        DestinationButtonFrame = Frame(RightFrame, height=100, bg="Gray24", padx =10)

        button2 = Button(DestinationButtonFrame, height=1, width=8, text="Browse", command=destination_browse_button, foreground="Gray20", font=("Times 16 bold"), bg="Gray24", highlightbackground='Gray60', activeforeground="Coral")
        button2.pack(ipadx=10, ipady=5, side=LEFT)

        DestinationButtonFrame.pack(fill=X, ipadx=10, ipady=8)

        #Schedule Backup Button
        #Schedule Backup Button
        #Schedule Backup Button
        #Schedule Backup Button

        ScheduleBackupFrame = Frame(RightFrame, bg="Gray24", padx=10)
        ScheduleBackupButton = Button(ScheduleBackupFrame, text="Schedule Backup", command=schedule_backup, foreground="Gray20", font=("Times 28 bold"), bg="Gray24", highlightbackground='Gray60', activeforeground="Coral")
        ScheduleBackupButton.pack(ipadx=10, ipady=5, side=LEFT)

        ScheduleBackupFrame.pack(fill=BOTH, expand=YES, ipadx=10, ipady=5)

        RightFrame.pack(fill=BOTH, expand=YES, side=LEFT)



root = Tk()
dir_folder_path = StringVar()
destination_folder_path = StringVar()
root.resizable(False, False)
my_gui = MyFirstGUI(root)
root.mainloop()
