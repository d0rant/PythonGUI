import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
import csv

from tkinter import filedialog, Label

idlist= []
timelist= []
courselist= []


class Courses(object):


    def __init__(self, root):
        FilePathLbl = Label(root,width=15)
        FilePathLbl.config(text="Provide data path", bg='white')
        FilePathLbl.grid(row=0, column=0, padx=(5,10), pady=(20,0))

        self.PathEntry = Entry(root)
        self.PathEntry.grid(row=0,column=1, padx=(0,0), pady=(20,0), columnspan=2, sticky=W + E)

        YrLbl = Label(root, width=15)
        YrLbl.config(text="Year", bg="white")
        YrLbl.grid(row=1, column=0, padx=(5,10), pady=(20,0), sticky=W+ E )
        n = tk.StringVar()
        self.YrBox = ttk.Combobox(root, width=5, textvariable=n)
        self.YrBox["values"] = ('1', '2','3','4','5','')
        self.YrBox.grid(column=1, row=1, padx=(5,10), pady=(20,0), sticky=W + E)
        self.YrBox.current()

        DepLbl = Label(root)
        DepLbl.config(text='Department', bg='white')
        DepLbl.grid(row=1, column=3, padx=(5,10), pady=(20,0), sticky=W + E)

        self.DpEntry= Entry(root)
        self.DpEntry.grid(row=1,column=4, padx=(5,10), pady=(20,0),sticky=W)

        DspBtn=Button(root)
        DspBtn.config(text="Display", bg='white', command=self.display)
        DspBtn.grid(row=2, column=0, sticky=E, padx=(0,10), pady=(50,0))

        ClrBtn=Button(root)
        ClrBtn.config(text="Clear",bg='white', command=self.clear)
        ClrBtn.grid(row=2, column=1, sticky=W + E,padx=(0,10), pady=(50,0))

        SvBtn=Button(root)
        SvBtn.config(text="Save", bg="white", command=self.save)
        SvBtn.grid(row=2, column=2, sticky=W + E, padx=(0,10), pady=(50,0))

        SelCrsLbl = Label(root)
        SelCrsLbl.config(text="Selected courses:",bg="white")
        SelCrsLbl.grid(row=5, column=0,columnspan=5, padx=(10,0), pady=(50,0), ipadx=5, sticky=W)

        self.SelCrsLbx = Listbox(root, width=20)
        self.SelCrsLbx.grid(row=6, column=0, columnspan=5, padx=(10,0), pady=(15,0), sticky=W)

        CrsLbl= Label(root)
        CrsLbl.config(text="Courses", bg="white")
        CrsLbl.grid(row=5, column=2, columnspan=10, padx=(0,0), pady=(50,0), sticky=W + E)

        self.CrsLbx = Listbox(root, width=50)
        self.CrsLbx.grid(row=6, column=2, columnspan=10,padx=(0,0), pady=(15,0), sticky=W + E)
        self.CrsLbx.bind('<Double-1>', self.onselect)



    def display(self):
        self.CrsLbx.delete(0,END)
        a = self.PathEntry.get()
        if not str(a).endswith(".csv"):
            messagebox.showinfo("Warning", "You have not choosen a csv file")
        else:
            a = open(str(a), 'r')
            courses = []
            for row in a:
                courses.append(row)

        year = self.YrBox.get()
        department = (self.DpEntry.get()).upper()
        for element in courses:
            if (element.split(' ')[1].startswith(str(year))) and (
                    element.split(' ')[0].startswith(str(department)) and (element.split(' ')[0].endswith(department))):
                self.CrsLbx.insert('end', element)

    def onselect(self, val):
        courses = []
        sender = val.widget
        idx = sender.curselection()
        scrs = []
        SelCrsList = []
        if idx:
            for item in idx:
                global value
                value = sender.get(item)
                print("the value is", value)

        if self.SelCrsLbx.size()>5:
            messagebox.showinfo("Warning", "You can choose up to six courses")
        else:
            idcrs= []
            k = value.split(',')
            idcrs.append(k[0])

            helplist = []
            if len(k) != 2:
                helplist.append(k[2:])
                str1= ''
                for element in helplist:
                    x = str1.join(element[0] + '' + element[1])
                    timecrs= x.split(' ')

        if len(self.SelCrsLbx.get(0,END))==0:
            self.SelCrsLbx.insert('end',idcrs[0])
            global idlist
            idlist.append(idcrs[0])
            global timelist
            timelist.append(timecrs)
            global courselist
            courselist.append(value)
        else:
            id = self.SelCrsLbx.get(0,END)
            idlist.clear()
            for element in id:
                idlist.append(element)
            y = False
            if idcrs[0] in idlist:
                messagebox.showinfo("Warning","You have already selected this course")
            else:
                x = True
                y  = True
                if x:
                    time=[]
                    if len(timecrs) == 2:
                        time = timecrs[0:2]
                    else:
                        if len(timecrs) == 4:
                            time = timecrs[0:4]
                        else:
                            if len(timecrs)== 6:
                                time = timecrs[0:6]
                    for row in timelist:
                        for element in time:
                            h = row
                            print
                            if element in row:
                                day = row
                                day2 = timecrs
                                n = day.index(element)
                                m = day2.index(element)
                                if len(day) == 2:
                                    y = n +1
                                if len(day) == 4:
                                    y = n+2
                                if len(day) == 6:
                                    y= n+ 3
                                if len(day2) == 2:
                                    x = m +1
                                if len(day2) == 4:
                                    x = m + 2
                                if len(day2) == 6:
                                    x= m + 3
                                if day[y] == day2[x]:
                                    messagebox.showinfo("Warning", "Courses are held in the same time")
                                    y = False
                                    x = False
                                    return x
                    else:
                        if y:
                            self.SelCrsLbx.insert('end', idcrs[0])
                            idlist.append(idcrs[0])
                            timelist.append(timecrs)
                            courselist.append(value)
                        return x
    def clear(self):
        self.SelCrsLbx.delete(0, END)
        timelist.clear()
        idlist.clear()

    def save(self):
        if self.SelCrsLbx.size() == 0:
            messagebox.showinfo("Warning", "You have not choosen any course")
        else:
            f = open('SavedCourses.csv', 'w')
            writer = csv.writer(f)
            for row in courselist:
                writer.writerow(row.split(','))
            f.close()

if __name__ =="__main__":
    root=Tk()
    root.resizable(0,0)
    root.geometry("520x500+400+200")
    root.wm_title("" * 50 + "Course Tool")
    root.configure(background='limegreen')
    Courses(root)
    root.mainloop()
