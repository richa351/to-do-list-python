from tkinter import *
import tkinter.messagebox
root = Tk()
root.geometry('600x500')
root.title("TO-DO-LIST")
root.config(bg="PaleVioletRed")
root.resizable(False, False)

# HEADING LABEL
lb1 = Label(root, text="TO-DO-LIST",
            font=("Comic Sans MS", 15), bg="PaleVioletRed").pack(side=TOP)
s = Scrollbar(root, orient=VERTICAL)
# LISTBOX storing tasks
tasks = Listbox(root, selectbackground='Gold', bg='Silver',
                font=('Helvetica', 12), height=12, width=25, yscrollcommand=s.set)
tasks.pack()


def entertask():
    input_txt = ""
    input_txt = newitem.get()
    print(input_txt)
    if input_txt == "":
        tkinter.messagebox.showwarning(
            title="Warning!", message="Please Enter some Text")
    else:
        tasks.insert(END, input_txt)
        newitem.delete(0, END)


# add item label
# This is because the place() method does not return the object it creates so always use it in next line when you want to extract the value from entry
newitem = Entry(root, width=21, font=2)
newitem.place(x=180, y=315)
btn1 = Button(root, text="Add-Item",
              font=("Comic Sans MS", 10), command=entertask).place(x=180, y=280)

# Creating a function and button to delete the item


def deletetask():
    select = tasks.curselection()
    tasks.delete(select[0])


btn2 = Button(root, text="Delete-Item",
              font=("Comic Sans MS", 10), command=deletetask).place(x=180, y=350)

# Creating a function and button to mark it complete the item


def markcomplete():
    # becomes a tuple containing the index of the selected item
    mark = tasks.curselection()
    # it assigns the first (and presumably only) index and assigned the index of the selected value can be 0,1,2...
    temp = mark[0]
    # store the text of the selected item in a string
    # it appears to store the selected task's text in the temp_marked variable.
    temp_marked = tasks.get(mark)
    temp_marked = temp_marked+" ✔"
    # delete it then insert it
    tasks.delete(temp)
    tasks.insert(temp, temp_marked)


btn3 = Button(root, text="Mark Complete", font=(
    "Comic Sans MS", 10), command=markcomplete).place(x=180, y=390)


mainloop()
