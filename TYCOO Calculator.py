from tkinter import* #import all

def tCalc(mainWin, side):
       storeObj  = Frame(mainWin, borderwidth = 1, bd= 5, bg= 'lavender')
       storeObj.pack(side=side, expand=YES, fill=BOTH)
       return storeObj

def buttons (mainWin, side, text, command = None):
       storeObj = Button(mainWin, text = text, command = command)
       storeObj.pack(side=side, expand=YES, fill=BOTH)
       return storeObj

class app(Frame):
       def __init__(self):
              Frame.__init__(self)
              self.option_add('*Font' , 'ariel 25')
              self.pack(expand = YES, fill = BOTH)
              self.master.title("TY COO's - Calculator")

              display = StringVar()
              Entry(self, relief=FLAT, textvariable=display, justify= 'right', bd=15, bg='lavender').pack(side=TOP, expand=YES, fill=BOTH)
              #for releif you can have SUNKEN, GROOVE, RAISED, RIDGE, FLAT, as interface suggestions

              for clearButtons in (['CE'] , ['C']): #these are for the clear buttons
                     erase = tCalc(self, TOP)
                     for tExpand in clearButtons:
                            buttons (erase, LEFT, tExpand, lambda storeObj=display, q=tExpand: storeObj.set(''))

              for numberButtons in ('789*', '456/', '321-' , '0.+'): #These are the numbers and operators
                     functionNumber = tCalc(self, TOP)
                     for char in numberButtons:
                                   buttons (functionNumber, LEFT, char, lambda storeObj=display, q=char: storeObj.set(storeObj.get() + q))

              equalAll = tCalc(self, TOP)                 
              for char in '=': #this is for the equal button
                     if char == '=':
                            equalsBut = buttons (equalAll, TOP, char)
                            equalsBut .bind('<ButtonRelease-1>', lambda e, s=self, storeObj=display: s.calc(storeObj), '+' )
                     else:
                            equalsBut = buttons(equalAll, LEFT, char, lambda storeObj=display, s ='%s ' %char: storeObj.set(storeObj.get() + s))

       def calc(self, display):
              try:
                     display.set(eval(display.get()))
              except:
                     display.set('ERROR')
                     
if __name__ == '__main__':
       app().mainloop ()
              
       
