from tkinter import*
import random
import time
import datetime
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
import winsound

winsound.PlaySound('SmoothJazz.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
# Importing and setting up the background music--------------------------------------------------

root = Tk()
root.geometry("1450x1150+0+0")
root.title("Flamin' Damon's")
root.configure(background='#000000')
root.resizable(width=True, height=True)
#Naming The GUI and Sizing it

Tops = Frame (root, width = 1450, height = 100, bd = 12, relief = "raise")
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=('arial', 75, 'bold'), background='#FFA500', text= "\tFlamin' Damon's\t\t\t")
lblTitle.grid(row =0, column=0,)
BottomMainFrame = Frame (root,background='#000000', width = 1350, height = 950, bd = 12, relief = "raise")
BottomMainFrame.pack(side=BOTTOM, fill="both", expand=True)

F1 = Frame (BottomMainFrame, background='#e88215', width = 450, height = 1050, bd = 12, relief = "raise")
F1.pack(side=LEFT, fill="both", expand=True)

F2 = Frame (BottomMainFrame,  background='#e88215', width = 450, height = 950, bd = 12, relief = "raise")
F2.pack(side=LEFT)
F2Top = Frame (F2,  background='#e88215', width = 450, height = 350, bd = 4, relief = "raise")
F2Top.pack(side=TOP)
F2Bottom = Frame (F2, width = 450, height = 300, background='#e88215', bd = 4, relief = "raise")
F2Bottom.pack(side=BOTTOM)

F3 = Frame (BottomMainFrame,background='#808080', width = 950, height = 950, bd = 12, relief = "raise")
F3.pack(side=RIGHT, fill="both", expand=True)
# Creating the 3 Frames

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11= IntVar()
var12= IntVar()
var13 = IntVar()
var14 = IntVar()
var15= IntVar()
var16 = IntVar()
var17= IntVar()
var18= IntVar() 
var19= IntVar()
var20= IntVar()
var21= IntVar()
var22= IntVar()
var23= IntVar()
var24= IntVar()
var25= IntVar()
var26= IntVar()
var27= IntVar()
var28= IntVar()
var29= IntVar()
var30= IntVar()
var31= IntVar()
var32 = IntVar()
var33 = StringVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set(0)
var23.set(0)
var24.set(0)
var25.set(0)
var26.set(0)
var27.set(0)
var28.set(0)
var29.set(0)
var30.set(0)
var31.set(0)
var32.set(0)
var33.set("")

varYams = StringVar()
varYams.set("0")
varMac = StringVar()
varMac.set("0")
varGreens= StringVar()
varGreens.set("0")
varButterBeans= StringVar()
varButterBeans.set("0")
varBakedBeans= StringVar()
varBakedBeans.set("0")
varBlackEyed= StringVar()
varBlackEyed.set("0")
varCorn= StringVar()
varCorn.set("0")
varString=StringVar()
varString.set("0")
varCornBread=StringVar()
varCornBread.set("0")
varOkra=StringVar()
varOkra.set("0")
varBiscuits=StringVar()
varBiscuits.set("0")
varStuffing=StringVar()
varStuffing.set("0")
varChicken=StringVar()
varChicken.set("0")
varBreast=StringVar()
varBreast.set("0")
varPorkChops=StringVar()
varPorkChops.set("0")
varPig=StringVar()
varPig.set("0")
varFrog=StringVar()
varFrog.set("0")
varOxtails=StringVar()
varOxtails.set("0")
varFish=StringVar()
varFish.set("0")
varPeas=StringVar()
varPeas.set("0")
varPeach=StringVar()
varPeach.set("0")
varCranberry=StringVar()
varCranberry.set("0")
varTurkey=StringVar()
varTurkey.set("0")
varMeatlessChickn=StringVar()
varMeatlessChickn.set("0")
varVeganGum=StringVar()
varVeganGum.set("0")
varVeganMac=StringVar()
varVeganMac.set("0")
varSweetPotatoFritters=StringVar()
varSweetPotatoFritters.set("0")
varSeitan=StringVar()
varSeitan.set("0")
varChange=StringVar()
varChange.set("0")
varTotal=StringVar()
varTotal.set("0")
varSubTotal=StringVar()
varSubTotal.set("0")
varTip=StringVar()
varTip.set("0")
varPayment=IntVar()
varPayment.set("0")
varVAT=StringVar()
varVAT.set("")
varWater=StringVar()
varWater.set("0")
varSoda=StringVar()
varSoda.set("0")
varIT=StringVar()
varIT.set("0")
varST=StringVar()
varST.set("0")
varLemon=StringVar()
varLemon.set("0")
# The Varibles

def iExit() :
    qExit= messagebox.askyesno("Flamin' Damon's","Are you sure you want to quit?")
    if qExit > 0:
        root.destroy()
        return
# Exiting the GUI

def Reset():

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    var30.set(0)
    var31.set(0)
    var32.set(0)
    
    varYams.set("0")
    varMac.set("0")
    varGreens.set("0")
    varButterBeans.set("0")
    varBakedBeans.set("0")
    varBlackEyed.set("0")
    varCorn.set("0")
    varString.set("0")
    varCornBread.set("0")
    varOkra.set("0")
    varBiscuits.set("0")
    varStuffing.set("0")
    varChicken.set("0")
    varBreast.set("0")
    varPorkChops.set("0")
    varPig.set("0")
    varFrog.set("0")
    varOxtails.set("0")
    varFish.set("0")
    varPeas.set("0")
    varPeach.set("0")
    varCranberry.set("0")
    varTurkey.set("0")
    varMeatlessChickn.set("0")
    varVeganGum.set("0")
    varVeganMac.set("0")
    varSweetPotatoFritters.set("0")
    varSeitan.set("0")
    varChange.set(" ")
    varTotal.set("0")
    varTip.set("0")
    varSubTotal.set("0")
    varVAT.set("")
    varPayment.set(" ")
    
    txtYams.configure(state = DISABLED)
    txtMac.configure(state = DISABLED)
    txtGreens.configure(state = DISABLED)
    txtButterBeans.configure(state = DISABLED)
    txtBakedBeans.configure(state = DISABLED)
    txtBlackEyed.configure(state = DISABLED)
    txtCorn.configure(state = DISABLED)
    txtString.configure(state = DISABLED)
    txtCornBread.configure(state = DISABLED)
    txtOkra.configure(state = DISABLED)
    txtBiscuits.configure(state = DISABLED)
    txtPeas.configure(state = DISABLED)
    txtPeach.configure(state = DISABLED)
    txtCranberry.configure(state = DISABLED)
    txtWater.configure(state = DISABLED) 
    txtSoda.configure(state = DISABLED)
    txtST.configure(state = DISABLED)
    txtIT.configure(state = DISABLED)
    txtLemon.configure(state = DISABLED)
    txtChicken.configure(state = DISABLED)
    txtBreast.configure(state = DISABLED)
    txtPorkChops.configure(state = DISABLED)
    txtFish.configure(state = DISABLED)
    txtOxtails.configure(state = DISABLED)
    txtFrog.configure(state = DISABLED)
    txtPig.configure(state = DISABLED)
    txtTurkey.configure(state = DISABLED)
    txtMeatlessChickn.configure(state = DISABLED)
    txtSeitan.configure(state = DISABLED)
    txtVeganGum.configure(state = DISABLED)
    #txtChange.configure(state = DISABLED)
    txtTip.configure(state = DISABLED)
    #txtPayment.configure(state = DISABLED)
    txtSubTotal.configure(state = DISABLED)
    txtTotal.configure(state = DISABLED)

#Programming the Reset button. Change for right now is disabled as I could not get the Cash option to work correctly. Will be fixed in the future.
def chkYams():
    if (var1.get() == 1):
        txtYams.configure(state = NORMAL)
        varYams.set("")
    elif(var1.get() == 0):
            txtYams.configure(state = DISABLED)
            varYams.set("0")

def chkMac():
    if (var2.get() == 1):
        txtMac.configure(state = NORMAL)
        varMac.set("")
    elif(var2.get() == 0):
            txtMac.configure(state = DISABLED)
            varMac.set("0")
def chkGreens():
    if (var3.get() == 1):
        txtGreens.configure(state = NORMAL)
        varGreens.set("")
    elif(var3.get() == 0):
            txtGreens.configure(state = DISABLED)
            varGreens.set("0")
def chkButterBeans():
    if (var4.get() == 1):
        txtButterBeans.configure(state = NORMAL)
        varButterBeans.set("")
    elif(var4.get() == 0):
            txtButterBeans.configure(state = DISABLED)
            varButterBeans.set("0")
def chkBakedBeans():
    if (var5.get() == 1):
        txtBakedBeans.configure(state = NORMAL)
        varBakedBeans.set("")
    elif(var5.get() == 0):
            txtBakedBeans.configure(state = DISABLED)
            varBakedBeans.set("0")
def chkBlackEyed():
    if (var6.get() == 1):
        txtBlackEyed.configure(state = NORMAL)
        varBlackEyed.set("")
    elif(var6.get() == 0):
            txtBlackEyed.configure(state = DISABLED)
            varBlackEyed.set("0")

def chkCorn():
    if (var7.get() == 1):
        txtCorn.configure(state = NORMAL)
        varCorn.set("")
    elif(var7.get() == 0):
            txtCorn.configure(state = DISABLED)
            varCorn.set("0")

def chkStringBeans():
    if (var8.get() == 1):
        txtString.configure(state = NORMAL)
        varString.set("")
    elif(var8.get() == 0):
            txtString.configure(state = DISABLED)
            varString.set("0")


def chkCornBread():
    if (var9.get() == 1):
        txtCornBread.configure(state = NORMAL)
        varCornBread.set("")
    elif(var9.get() == 0):
            txtCornBread.configure(state = DISABLED)
            varCornBread.set("0")

def chkOkra():
    if (var10.get() == 1):
        txtOkra.configure(state = NORMAL)
        varOkra.set("")
    elif(var10.get() == 0):
            txtOkra.configure(state = DISABLED)
            varOkra.set("0")


def chkBiscuits():
    if (var11.get() == 1):
        txtBiscuits.configure(state = NORMAL)
        varBiscuits.set("")
    elif(var11.get() == 0):
            txtBiscuits.configure(state = DISABLED)
            varBiscuits.set("0")

def chkPeas():
    if (var19.get() == 1):
        txtPeas.configure(state = NORMAL)
        varPeas.set("")
    elif(var19.get() == 0):
            txtPeas.configure(state = DISABLED)
            varPeas.set("0")

def chkPeach():
    if (var30.get() == 1):
        txtPeach.configure(state = NORMAL)
        varPeach.set("")
    elif(var30.get() == 0):
            txtPeach.configure(state = DISABLED)
            varPeach.set("0")

def chkCranberry():
    if (var31.get() == 1):
        txtCranberry.configure(state = NORMAL)
        varCranberry.set("")
    elif(var31.get() == 0):
            txtCranberry.configure(state = DISABLED)
            varCranberry.set("0")
def chkWater():
    if (var23.get() == 1):
        txtWater.configure(state = NORMAL)
        varWater.set("")
    elif(var23.get() == 0):
            txtWater.configure(state = DISABLED)
            varWater.set("0")

def chkSoda():
    if (var24.get() == 1):
        txtSoda.configure(state = NORMAL)
        varSoda.set("")
    elif(var24.get() == 0):
            txtSoda.configure(state = DISABLED)
            varSoda.set("0")

def chkST():
    if (var26.get() == 1):
        txtST.configure(state = NORMAL)
        varST.set("")
    elif(var26.get() == 0):
            txtST.configure(state = DISABLED)
            varST.set("0")

def chkIT():
    if (var27.get() == 1):
        txtIT.configure(state = NORMAL)
        varIT.set("")
    elif(var27.get() == 0):
            txtIT.configure(state = DISABLED)
            varIT.set("0")

def chkLemon():
    if (var28.get() == 1):
        txtLemon.configure(state = NORMAL)
        varLemon.set("")
    elif(var28.get() == 0):
            txtLemon.configure(state = DISABLED)
            varLemon.set("0")
def chkChicken():
    if (var12.get() == 1):
        txtChicken.configure(state = NORMAL)
        varChicken.set("")
    elif(var12.get() == 0):
            txtChicken.configure(state = DISABLED)
            varChicken.set("0")

def chkBreast():
    if (var13.get() == 1):
        txtBreast.configure(state = NORMAL)
        varBreast.set("")
    elif(var13.get() == 0):
            txtBreast.configure(state = DISABLED)
            varBreast.set("0")

def chkPorkChops():
    if (var14.get() == 1):
        txtPorkChops.configure(state = NORMAL)
        varPorkChops.set("")
    elif(var14.get() == 0):
            txtPorkChops.configure(state = DISABLED)
            varPorkChops.set("0")

def chkFish():
    if (var15.get() == 1):
        txtFish.configure(state = NORMAL)
        varFish.set("")
    elif(var15.get() == 0):
            txtFish.configure(state = DISABLED)
            varFish.set("0")

def chkOxtails():
    if (var16.get() == 1):
        txtOxtails.configure(state = NORMAL)
        varOxtails.set("")
    elif(var16.get() == 0):
            txtOxtails.configure(state = DISABLED)
            varOxtails.set("0")

def chkFrog():
    if (var17.get() == 1):
        txtFrog.configure(state = NORMAL)
        varFrog.set("")
    elif(var17.get() == 0):
            txtFrog.configure(state = DISABLED)
            varFrog.set("0")

def chkPig():
    if (var18.get() == 1):
        txtPig.configure(state = NORMAL)
        varPig.set("")
    elif(var18.get() == 0):
            txtPig.configure(state = DISABLED)
            varPig.set("0")

def chkTurkey():
    if (var19.get() == 1):
        txtTurkey.configure(state = NORMAL)
        varTurkey.set("")
    elif(var19.get() == 0):
            txtTurkey.configure(state = DISABLED)
            varTurkey.set("0")

def chkMeatlessChickn():
    if (var21.get() == 1):
        txtMeatlessChickn.configure(state = NORMAL)
        varMeatlessChickn.set("")
    elif(var21.get() == 0):
            txtMeatlessChickn.configure(state = DISABLED)
            varMeatlessChickn.set("0")

def chkSeitan():
    if (var22.get() == 1):
        txtSeitan.configure(state = NORMAL)
        varSeitan.set("")
    elif(var22.get() == 0):
            txtSeitan.configure(state = DISABLED)
            varSeitan.set("0")

def chkVeganGum():
    if (var25.get() == 1):
        txtVeganGum.configure(state = NORMAL)
        varVeganGum.set("")
    elif(var25.get() == 0):
            txtVeganGum.configure(state = DISABLED)
            varVeganGum.set("0")

#Giving the Food items the ENABLE and DISABLE feature -------------------------------------------
            
def foodTotal():
    meal1 = float(varYams.get())
    meal2 = float(varMac.get())
    meal3 = float(varGreens.get())
    meal4 = float(varButterBeans.get())
    meal5 = float(varBakedBeans.get())
    meal6 = float(varBlackEyed.get())
    meal7 = float(varCorn.get())
    meal8 = float(varString.get())
    meal9 = float(varCornBread.get())
    meal10 = float(varOkra.get())
    meal11 = float(varBiscuits.get())
    meal12 = float(varChicken.get())
    meal13 = float(varBreast.get())
    meal14 = float(varPorkChops.get())
    meal15 = float(varPig.get())
    meal16 = float(varFrog.get())
    meal17 = float(varOxtails.get())
    meal18 = float(varFish.get())
    meal19 = float(varPeas.get())
    meal20 = float(varPeach.get())
    meal21 = float(varCranberry.get())
    meal22 = float(varTurkey.get())
    meal23= float(varMeatlessChickn.get())
    meal24 = float(varVeganGum.get())
   # meal25 = float(varVeganMac.get()) Was removed 
   # meal26 = float(varSweetPotatoFritters.get()) Was removed 
    meal27= float(varSeitan.get())
    meal28= float(varWater.get())
    meal29 = float(varSoda.get())
    meal30 = float(varIT.get())
    meal31 = float(varST.get())
    meal32 = float(varLemon.get())

    iTotal1 = ((meal1 * 3.50) + (meal2 * 3.50) + (meal3 * 3.50) + (meal4 * 3.50) + (meal5 * 3.50 ) + (meal6 * 2.50)) 
    iTotal2 = ((meal7 * 3.50) + (meal8 * 3.50) + (meal9 * 2.50) + (meal10 * 3.50) + (meal11 * 2.50 ) + (meal12 * 6.50)) 
    iTotal3 = ((meal13 * 6.50) + (meal14 * 6.50) + (meal15 * 6.50) + (meal16 * 6.50) + (meal17 * 6.50 ) + (meal18 * 6.50))
    iTotal4 = ((meal19 * 2.50) + (meal20 * 2.50) + (meal21 * 2.50) + (meal22 * 6.50) + (meal23 * 6.25 ) + (meal24 * 6.53))
    iTotal5 = ((meal27 * 6.56) + (meal28 * 0.50) + (meal29 * 1.50) + (meal30 * 1.25) + (meal31 * 1.50 ) + (meal32 * 1.50))
#Setting the food items to Meal in order to calculate the cost of the full meal ---------------------------------------------------------------
    
#iCost =(iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
#iTip = (iCost * 15)/100
#varTip.set(iTip)
#varSubTotal.set(iCost)
#varTotal.set(iCost + iTip)

#if (var33.get() == "Cash"):
#iChange = float(varPayment.get())
#iCost =(iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
#iTip = (iCost * 15)/100
#iTipq = "$", str('%.2f'%(iTip))
#varTip.set(iTipq)

#iCostq =  "$", str('%.2f'%(iCost))
#  varSubTotal.set(iCostq)
# iTotalq = "$", str('%.2f'%(iCost + iTip))
# cChange = (iChange - (iCost + iTip))
# cChangeq = "$", str('%.2f'%(cChange))
# varChange.set(cChangeq)

# Originally was the change feautre using Cash. Where the user will type in how much cash they want to spend and the change from Cash minus Cost but I had to disable this feature until I get it right

    if(var33.get() == "Credit" or "Debit Card"):
        varPayment.set("")
        iCost =(iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
        iTip = (iCost * 15)/100
        iTipq = F"${'%.2f'% iTip}"
        varTip.set(iTipq)
        iCostq = F"${'%.2f'%iCost}"
        varSubTotal.set(iCostq)
        iTotalq =str("$" '%.2f'%((iCost + iTip)))
        varTotal.set(iTotalq)
        varChange.set("")


# Using Credit or Debit transaction------------------------------------------

lblSide = Label(F1, background='#e88215', font = ('arial', 18, 'bold'), text="\t Sides\t\t\t")
lblSide.grid(row =0, column=0)
Yams = Checkbutton(F1,background='#e88215', text="Candied Yams\t\t$3.50", variable = var1, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkYams).grid(row=1, column=0, sticky=W)

txtYams = Entry(F1,font=('arial', 18,'bold'), textvariable = varYams, width =6 , justify ='left', state = DISABLED)
txtYams.grid(row = 1, column = 1)

Mac = Checkbutton(F1,background='#e88215', text="Mac'n Cheese\t\t$3.50", variable = var2, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkMac).grid(row=2, column=0, sticky=W)

txtMac = Entry(F1,font=('arial', 18,'bold'), textvariable = varMac, width =6 , justify ='left', state = DISABLED)
txtMac.grid(row = 2, column = 1)

Greens = Checkbutton(F1,background='#e88215', text="Collard Greens\t\t$3.50", variable = var3, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkGreens).grid(row=3, column=0, sticky=W)

txtGreens = Entry(F1,font=('arial', 18,'bold'), textvariable = varGreens, width =6 , justify ='left', state = DISABLED)
txtGreens.grid(row = 3, column = 1)

ButterBeans = Checkbutton(F1, background='#e88215', text="Southern Butter Bean\t$3.50", variable = var4, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkButterBeans).grid(row=4, column=0, sticky=W)

txtButterBeans = Entry(F1,font=('arial', 18,'bold'), textvariable = varButterBeans, width =6 , justify ='left', state = DISABLED)
txtButterBeans.grid(row = 4, column = 1)

BakedBeans = Checkbutton(F1,background='#e88215', text="Baked Bean\t\t$3.50", variable = var5, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkBakedBeans).grid(row=5, column=0, sticky=W)

txtBakedBeans = Entry(F1,font=('arial', 18,'bold'), textvariable = varBakedBeans, width =6 , justify ='left', state = DISABLED)
txtBakedBeans.grid(row = 5, column = 1)

BlackEyed = Checkbutton(F1,background='#e88215', text="Black-Eyed Peas\t\t$2.50", variable = var6, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkBlackEyed).grid(row=6, column=0, sticky=W)

txtBlackEyed = Entry(F1,font=('arial', 18,'bold'), textvariable = varBlackEyed, width =6 , justify ='left', state = DISABLED)
txtBlackEyed.grid(row = 6, column = 1)

Corn = Checkbutton(F1,background='#e88215', text="Corn(Cob Or No Cob)\t$3.50", variable = var7, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkCorn).grid(row=7, column=0, sticky=W)

txtCorn = Entry(F1,font=('arial', 18,'bold'), textvariable = varCorn, width =6 , justify ='left', state = DISABLED)
txtCorn.grid(row = 7, column = 1)

StringBeans = Checkbutton(F1, background='#e88215', text="String Beans\t\t$3.50", variable = var8, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkStringBeans).grid(row=8, column=0, sticky=W)

txtString = Entry(F1,font=('arial', 18,'bold'), textvariable = varString, width =6 , justify ='left', state = DISABLED)
txtString.grid(row = 8, column = 1)

CornBread = Checkbutton(F1,background='#e88215', text="Cornbread\t\t$2.50", variable = var9, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkCornBread).grid(row=9, column=0, sticky=W)

txtCornBread  = Entry(F1,font=('arial', 18,'bold'), textvariable = varCornBread, width =6 , justify ='left', state = DISABLED)
txtCornBread .grid(row = 9, column = 1)

Okra = Checkbutton(F1,background='#e88215', text="Southern Fried Okra\t$3.50", variable = var10, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkOkra).grid(row=10, column=0, sticky=W)

txtOkra = Entry(F1,font=('arial', 18,'bold'), textvariable = varOkra, width =6 , justify ='left', state = DISABLED)
txtOkra.grid(row = 10, column = 1)


Biscuits = Checkbutton(F1,background='#e88215', text="Biscuits\t\t\t$2.50", variable = var11, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkBiscuits).grid(row=11, column=0, sticky=W)

txtBiscuits = Entry(F1,background='#e88215',font=('arial', 18,'bold'), textvariable = varBiscuits, width =6 , justify ='left', state = DISABLED)
txtBiscuits.grid(row = 11, column = 1)

Peas = Checkbutton(F1,background='#e88215', text="Peas\t\t\t$2.50", variable = var19, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkPeas).grid(row=12, column=0, sticky=W)

txtPeas = Entry(F1,font=('arial', 18,'bold'), textvariable = varPeas, width =6 , justify ='left', state = DISABLED)
txtPeas.grid(row = 12, column = 1)

Peach = Checkbutton(F1,background='#e88215', text="Peach Cobbler\t\t$2.50", variable = var30, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkPeach).grid(row=13, column=0, sticky=W)

txtPeach = Entry(F1,font=('arial', 18,'bold'), textvariable = varPeach, width =6 , justify ='left', state = DISABLED)
txtPeach.grid(row = 13, column = 1)

Cranberry = Checkbutton(F1,background='#e88215', text="Canned Cranberry\t$2.50", variable = var31, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkCranberry).grid(row=14, column=0, sticky=W)

txtCranberry = Entry(F1,font=('arial', 18,'bold'), textvariable = varCranberry, width =6 , justify ='left', state = DISABLED)
txtCranberry.grid(row = 14, column = 1)

lblDrink = Label(F1, background='#e88215', font = ('arial', 18, 'bold'), text="\t Drinks \t\t\t")
lblDrink.grid(row =15, column=0)

Water = Checkbutton(F1,background='#e88215', text="Water\t\t$0.50", variable = var23, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkWater).grid(row=16, column=0, sticky=W)

txtWater = Entry(F1,font=('arial', 18,'bold'), textvariable = varWater, width =6 , justify ='left', state = DISABLED)
txtWater.grid(row = 16, column = 1)

Soda = Checkbutton(F1,background='#e88215', text="Coke Products\t$1.50", variable = var24, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkSoda).grid(row=17, column=0, sticky=W)

txtSoda = Entry(F1,font=('arial', 18,'bold'), textvariable = varSoda, width =6 , justify ='left', state = DISABLED)
txtSoda.grid(row = 17, column = 1)

ST = Checkbutton(F1,background='#e88215', text="Sweet Tea\t$1.50", variable = var26, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkST).grid(row=18, column=0, sticky=W)

txtST = Entry(F1,font=('arial', 18,'bold'), textvariable = varST, width =6 , justify ='left', state = DISABLED)
txtST.grid(row = 18, column = 1)

IT = Checkbutton(F1,background='#e88215', text="Iced Tea\t\t$1.50", variable = var27, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkIT).grid(row=19, column=0, sticky=W)

txtIT = Entry(F1,font=('arial', 18,'bold'), textvariable = varIT, width =6 , justify ='left', state = DISABLED)
txtIT.grid(row = 19, column = 1)

Lemon = Checkbutton(F1,background='#e88215', text="Lemonade\t$1.50", variable = var28, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkLemon).grid(row=20, column=0, sticky=W)

txtLemon = Entry(F1,font=('arial', 18,'bold'), textvariable = varLemon, width =6 , justify ='left', state = DISABLED)
txtLemon.grid(row = 20, column = 1)

# Creating the Sides and Drinks---------------------------------------------------------------------------------

lblSide = Label(F2Top, background='#e88215', font = ('arial', 18, 'bold'), text="\t Main Entrée\t\t\t")
lblSide.grid(row =0, column=0)

ChickenWings = Checkbutton(F2Top, background='#e88215', text=" 3 Chicken Wings(Baked or Fried)\t$6.50", variable = var12, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkChicken).grid(row=1, column=0, sticky=W)

txtChicken = Entry(F2Top,font=('arial', 18,'bold'), textvariable = varChicken, width =6 , justify ='left', state = DISABLED)
txtChicken.grid(row = 1, column = 1)

Breast = Checkbutton(F2Top, background='#e88215', text="Breast(Baked or Fried)\t\t$6.50", variable = var13, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkBreast).grid(row=2, column=0, sticky=W)

txtBreast = Entry(F2Top,font=('arial', 18,'bold'), textvariable = varBreast, width =6 , justify ='left', state = DISABLED)
txtBreast.grid(row = 2, column = 1)

PorkChops= Checkbutton(F2Top, background='#e88215', text="Pork Chops\t\t\t$6.50", variable = var14, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkPorkChops).grid(row=3, column=0, sticky=W)

txtPorkChops = Entry(F2Top,font=('arial', 18,'bold'), textvariable = varPorkChops, width =6 , justify ='left', state = DISABLED)
txtPorkChops.grid(row = 3, column = 1)

Fish = Checkbutton(F2Top, background='#e88215', text="Fish(Baked or Fried)\t\t$6.50", variable = var15, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkFish).grid(row=4, column=0, sticky=W)

txtFish = Entry(F2Top,font=('arial', 18,'bold'), textvariable = varFish, width =6 , justify ='left', state = DISABLED)
txtFish.grid(row = 4, column = 1)

Oxtails = Checkbutton(F2Top, background='#e88215',text="Oxtails\t\t\t\t$6.50", variable = var16, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkOxtails).grid(row=5, column=0, sticky=W)

txtOxtails = Entry(F2Top,font=('arial', 18,'bold'), textvariable = varOxtails, width =6 , justify ='left', state = DISABLED)
txtOxtails.grid(row = 5, column = 1)

Frog = Checkbutton(F2Top, background='#e88215', text="4 Frog Legs(Baked or Fried)\t$6.50", variable = var17, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkFrog).grid(row=6, column=0, sticky=W)

txtFrog = Entry(F2Top,font=('arial', 18,'bold'), textvariable = varFrog, width =6 , justify ='left', state = DISABLED)
txtFrog.grid(row = 6, column = 1)

Pig = Checkbutton(F2Top,  background='#e88215', text="Pig's Feet\t\t\t$6.50", variable = var18, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkPig).grid(row=7, column=0, sticky=W)

txtPig = Entry(F2Top,background='#e88215',font=('arial', 18,'bold'), textvariable = varPig, width =6 , justify ='left', state = DISABLED)
txtPig.grid(row = 7, column = 1)


Turkey = Checkbutton(F2Top, background='#e88215', text="3 Turkey Wings(Baked or Fried)\t$6.50", variable = var19, onvalue = 1, offvalue =0,

                                    font=('arial', 18,'bold'),command=chkTurkey).grid(row=8, column=0, sticky=W)

txtTurkey = Entry(F2Top,font=('arial', 18,'bold'), textvariable = varTurkey, width =6 , justify ='left', state = DISABLED)
txtTurkey.grid(row = 8, column = 1)

meatlessChickn  = Checkbutton(F2Top,  background='#e88215',text="Meatless Chick’n(Baked or Fried)\t$7.25", variable = var21, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkMeatlessChickn).grid(row=9, column=0, sticky=W)

txtMeatlessChickn = Entry(F2Top,font=('arial', 18,'bold'), textvariable = varMeatlessChickn, width =6 , justify ='left', state = DISABLED)
txtMeatlessChickn.grid(row = 9, column = 1)

Seitan  = Checkbutton(F2Top,  background='#e88215',text="Country Fried Seitan\t\t$6.56", variable = var22, onvalue = 1, offvalue =0,
                                    font=('arial', 18,'bold'),command=chkSeitan).grid(row=10, column=0, sticky=W)

txtSeitan= Entry(F2Top,font=('arial', 18,'bold'), textvariable = varSeitan, width =6 , justify ='left', state = DISABLED)
txtSeitan.grid(row = 10, column = 1)

VeganGum  = Checkbutton(F2Top,  background='#e88215', text="Vegan Gumbo\t\t\t$6.53", variable = var25, onvalue = 1, offvalue =0, font=('arial', 18,'bold'),command=chkVeganGum).grid(row=11, column=0, sticky=W)

txtVeganGum = Entry(F2Top,font=('arial', 18,'bold'), textvariable = varVeganGum, width =6 , justify ='left', state = DISABLED)
txtVeganGum.grid(row = 11, column = 1)
#Making the Main Entrees---------------------------------------------------------------


lblPay = Label(F2Bottom, background='#e88215', font = ('arial', 18, 'bold'), text="\tPayment\t\t\t", bd=10, width = 16, anchor = 'w')
lblPay.grid(row =0, column=0)

#lblChange = Label(F2Bottom, background='#e88215', font = ('arial', 18, 'bold'), text="\tChange\t\t\t", bd=10,  anchor = 'w')
#lblChange.grid(row =0, column=1)
#txtChange = Entry(F2Bottom, font =('arial', 18, 'bold'), textvariable = varChange, width =6, state = DISABLED)
#txtChange.grid(row = 0, column = 2)

cmbPaymentMethod = ttk.Combobox(F2Bottom, textvariable = var33, state = 'Readonly', font =('ariral',10,'bold'), width = 20)
cmbPaymentMethod['value']=('Credit', 'Debit')
cmbPaymentMethod.current(0)
cmbPaymentMethod.grid(row=1, column =0)

lblTip = Label(F2Bottom, background='#e88215', font = ('arial', 18, 'bold'), text="\t Tip\t\t\t", bd=10,  anchor = 'w')
lblTip.grid(row=1,column=1)
txtTip = Entry(F2Bottom, font =('arial', 18, 'bold'), textvariable = varTip, width =6, state = DISABLED)
txtTip.grid(row = 1, column = 2)
txtPayment = Entry(F2Bottom, font =('arial', 18, 'bold'), textvariable = varChange, width =6, #state = DISABLED)
)
txtPayment.grid(row=2,column=0)
lblSubTotal = Label(F2Bottom, background='#e88215', font = ('arial', 18, 'bold'), text="\t Sub Total\t\t\t", bd=10,  anchor = 'w')
lblSubTotal.grid(row=2,column=1)
txtSubTotal = Entry(F2Bottom, font =('arial', 18, 'bold'), textvariable = varSubTotal, width =6, state = DISABLED)
txtSubTotal.grid(row=2,column=2)

lblTotal = Label(F2Bottom, background='#e88215', font = ('arial', 18, 'bold'), text="\t Total \t\t\t", bd=10,  anchor = 'w')
lblTotal.grid(row=3,column=1)
txtTotal = Entry(F2Bottom, font =('arial', 18, 'bold'), textvariable = varTotal, width =6, state = DISABLED)
txtTotal.grid(row=3,column=2)

#------------------------
btnTotal = Button(F2Bottom, padx=16, pady=1, bd=4, fg="red", font=('arial', 16, 'bold'), width = 5, text ="Total  ",command=foodTotal).grid(row=4, column = 0)
btnReset = Button(F2Bottom, padx=16, pady=1, bd=4, fg="red", font=('arial', 16, 'bold'), width = 5, text ="Reset  ",command=Reset).grid(row=4, column = 1)
btnExit = Button(F2Bottom, padx=16, pady=1, bd=4, fg="red", font=('arial', 16, 'bold'), width = 5, text ="Exit", command=lambda: iExit()).grid(row=4, column = 2)
lblSpace = Label(F2Bottom, text = "\n\n\n\n\n\n\n")
lblSpace.grid(row =5, column = 0)
    


root.mainloop()

