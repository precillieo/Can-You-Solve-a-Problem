from tkinter import *

class PizzaApp(Frame):
    
    def __init__(self, master):
        super(PizzaApp, self).__init__(master)
        self.grid()
        self.size=StringVar()
        self.toppings = ['Sausage', 'Pepperoni', 'Chicken',
                         'Mushroom', 'Black Olive', 'Green Pepper', 'Red Pepper', 'Onion']
        
        self.prices = {'medium': 3200, 'large': 5200, 'xlarge': 7000, 'm_toppings': 0.03, 'l_toppings': 0.05, 'xl_toppings': 0.07}
        self.chk = list(self.toppings)
        self.chkVar= list(self.toppings)
        self.create_widgets()
        
    def create_widgets(self):
        self.lbl_ss = Label(self, text='Select Size: ')
        self.lbl_ss.grid(row=0, column=0, sticky=W)
        
        
        self.rad_medium = (Radiobutton(self, text='Medium', variable = self.size, value='Medium'))
        self.rad_medium.grid(row=1, column=0, sticky=W)
        
        self.rad_large = (Radiobutton(self, text='Large', variable = self.size, value='Large'))
        self.rad_large.grid(row=1, column=1, sticky=W)
        
        self.rad_xlarge = (Radiobutton(self, text='Extra Large', variable = self.size, value='X-Large'))
        self.rad_xlarge.grid(row=1, column=2, sticky=W)
        self.rad_medium.select()
        
        self.lbl_empty = Label(self, text='').grid(row=2, column=0)
        
        self.lbl_st = Label(self, text='Select Toppings: ')
        self.lbl_st.grid(row=3, column=0, sticky=W)
        
        
        self.lbl_empty = Label(self, text='').grid(row=14, column=0)
        
        self.ent_total = Entry(self)
        self.ent_total.grid(row= 15, column=1, sticky=W)
        
        position = 3
        for i in range(len(self.toppings)):
            self.chkVar[i] = BooleanVar()
            self.chk[i] = Checkbutton(self, text=self.toppings[i], variable=self.chkVar[i])
            self.chk[i].grid(row=position, column=1, sticky=W)
            position += 1
        
        self.btn_reset = Button(self, text='Reset', width=10, command=self.reset)
        self.btn_reset.grid(row=position, column=0, sticky=E)
        
    
        self.btn_calculate = Button(self, text='Calculate Price', command=self.calculate)
        self.btn_calculate.grid(row=position, column=1, columnspan=2, sticky=W)
        

    def reset(self):
        self.rad_medium.select()
        for i in range(len(self.toppings)):
            self.chk[i].deselect()
        self.ent_total.delete(0,END)
        
    def calculate(self):
        self.ent_total.delete(0,END)
        total_toppings = 0
        
        for i in range(len(self.toppings)):
            if self.chkVar[i].get():
                total_toppings += 1
            
            if(self.size.get() == 'Medium'):
                total_price = self.prices['medium'] +(total_toppings * self.prices['medium'] * self.prices['m_toppings'])
            elif(self.size.get() == 'Large'):
                total_price = self.prices['large'] +(total_toppings * self.prices['large'] * self.prices['l_toppings'])
            elif(self.size.get() == 'X-Large'):
                total_price = self.prices['xlarge'] +(total_toppings * self.prices['xlarge'] * self.prices['xl_toppings'])
      
        self.ent_total.insert(END, total_price)
    
    
window = Tk()
window.title('Python Pizza Calculator')
window.geometry('300x400')
app = PizzaApp(window)
app.mainloop()