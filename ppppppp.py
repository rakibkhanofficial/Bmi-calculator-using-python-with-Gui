from tkinter import*



root = Tk()
root.geometry("1350x650+0+0")
root.resizable(0,0)
root.title("BMI")
def BMI_cal():
    BHeight = float(var2.get())
    Bweight = float(var1.get())
    BMI = str('%.2f' %(Bweight / (BHeight * BHeight)))
    lblBMIResult. config(text=BMI)
       
var1 = DoubleVar()
var2 = DoubleVar()


Tops=Frame(root, width=1350, height=50, bd=8, relief="raise")
Tops.pack(side=TOP)
f1 = Frame(root, width = 600,height = 600, bd=8, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root, width = 300,height = 700, bd=8, relief="raise")
f2.pack(side=RIGHT)


fla = Frame(f1, width = 600,height = 200, bd=20, relief="raise")
fla.pack(side=TOP)
flb = Frame(f1, width = 600,height = 600, bd=20, relief="raise")
flb.pack(side=TOP)




lblTitle=Label(Tops, text= "      BODY MASS INDEX  " ,padx=16,pady=16, bd=16,
               fg="#000000", font=('times new roman',54,'bold'),
               bg="forestgreen",relief = 'raise',width = 32, height = 1)
lblTitle.pack()

lblweight=Label (fla, text = "SELECT WEIGHT IN KILOGRAMS ",font=('times new roman', 20, 'bold'), bd=20).grid(row = 0,column=0)
Bodyweight = Scale(fla, variable = var1, from_= 1, to=500, length=880,tickinterval=30,orient=HORIZONTAL)
Bodyweight.grid(row = 1,column=0)


lblheight=Label(flb, text = "ENTER HEIGHT IN METERS SQUARE",font=('times new roman',20,'bold'), bd=20).grid(row = 0,column=0)
txtheight = Entry(flb, textvariable = var2, font=('times new roman',16,'bold' ),bd=16, width=22,justify='center')
txtheight.grid(row = 1, column=0)




lblBMIResult = Label(flb, padx=16,pady=16, bd=16,
                     fg="#000000", font=('arial',30,'bold'),
                     bg="forestgreen", relief = 'sunk',width = 34, height = 1)
lblBMIResult.grid(row = 2, column=0)



lblBMITable=Label(f2,font=('times new roman',20,'bold'),text="BMI table").grid(row =0, column = 0)
txtlblBMITable = Text(f2, height = 12, width = 38,bd=16,font=('times new roman',12,'bold'))
txtlblBMITable.grid(row=1, column=0)


txtlblBMITable. insert(END,'meaning \t\t'+ "BMI \n\n")
txtlblBMITable. insert(END,'Normal weight \t\t'+ "19-24,9\n\n")
txtlblBMITable. insert(END,'overweight \t\t'+ "25-29,9\n\n")
txtlblBMITable. insert(END,'obesity level 1 \t\t' + "30-34,9\n\n")
txtlblBMITable. insert(END,'obesity level 2 \t\t' + "35-39,9\n\n")
txtlblBMITable. insert(END,'obesity level 3 \t\t' + ">,40\n\n")

btnBMI = Button(f2, text="Click to \nCheck your \nBMI",padx=8,pady=8,bd=12, width =21,
                font=('times new roman',20,'bold'), height=3, command =BMI_cal)
btnBMI. grid(row = 2,column=0)
root.mainloop()

