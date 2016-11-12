from tkinter import*


def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg = "powder blue")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


    
    


class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font','arial 20 bold')
        self.master.title('Calculator')
        self.pack(expand=YES, fill=BOTH)
        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display, justify='right', bd=30, bg='powder blue').pack(side=TOP,  expand=YES, fill=BOTH)

        for clearButton in (["CE"],["C"]):
            erase = iCalc(self, TOP)
            for element in clearButton:
                button(erase, LEFT, element,
                lambda storeObj = display, q = element: storeObj.set(''))


        for numberButton in ("789/","456*","123-","0.+"):
            number = iCalc(self, TOP)
            for element in numberButton:
                button(number, LEFT, element,
                lambda storeObj = display, q = element: storeObj.set(storeObj.get() + q))


        equal = iCalc(self,TOP)
        for element in ("="):
            if element == '=':
                buttonEquals = button(equal, LEFT, element)
                buttonEquals.bind('<ButtonRelease-1>',
                    lambda e, s=self, storeObj = display: s.calc(storeObj), '+')
            else:
                  buttonEquals = button(equal, LEFT, element,
                    lambda storeObj=display, s=' %s '%element: storeObj.set(storeObj.get()+s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set('Error...') 










if __name__ == '__main__':    
    app().mainloop()
    


       
    