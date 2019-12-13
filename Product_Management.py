from tkinter import *
file= 'Info.csv'

root= Tk()

def New_user():
    global NewEntry1
    global NewEntry2
    global NewEntry3
    global roots


    roots = Tk()
    roots.title('Signup')
    newuser= Label(roots, text='Username:')
    password= Label(roots, text='Password:')
    confirm_password= Label(roots, text='Confirm Password:')
    NewEntry1= Entry(roots)
    NewEntry2= Entry(roots, show='*')
    NewEntry3= Entry(roots, show='*')
    newuser.grid(row=0, sticky=E)
    password.grid(row=1, sticky=E)
    confirm_password.grid(row=2)
    NewEntry1.grid(row=0, column=1)
    NewEntry2.grid(row=1, column=1)
    NewEntry3.grid(row=2, column=1)
    signupButton= Button(roots, text='Sign up', command= Sign_up)
    signupButton.grid(columnspan=3)


    roots.mainloop()

def Sign_up():

    if NewEntry2.get() == NewEntry3.get():
        import csv

        with open(file, 'a') as csv_file:
            csv_writer= csv.writer(csv_file,delimiter=' ')
            csv_writer.writerow([NewEntry1.get(),',',NewEntry2.get()])

        roots.destroy()
        LoginIsPressed()

    else:

        root_1 = Tk()
        label_3 = Label(root_1, text= 'Password did not match')
        label_3.pack()


def LoginIsPressed():
    global entry_1
    global entry_2
    global root1

    
    root1 = Tk()
    root1.title('Login')
    label_1= Label(root1, text='Username:')
    label_2= Label(root1,text='Password:')
    entry_1= Entry(root1)
    entry_2= Entry(root1, show='*')
    label_1.grid(row=0)
    label_2.grid(row=1)
    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)
    Login_1= Button(root1, text='Login', command= Login)
    Login_1.grid(columnspan=2)

    

    checkpoint_1= Checkbutton(root1, text='Keep me logged in')
    checkpoint_1.grid(columnspan=3)
    root1.mainloop()

def Login():
    global AddToCart
    global ShowCart
    global Entry_1
    global Entry_2
    global root4
    global Buy
    global addtocsv
    import csv


    Prod_uct=[]
    Quant_ity=[]
    list_price=[]
    Pri_ce=[]
    c=[]
    d=[]
    list_product=[]
    list_quantity=[]
    list_Price=[]
    flag=False
            
    
    
    with open(file,'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            c.append(line[0].strip())
            d.append(line[1].strip())

            

    for i in range(len(c)):
            

            if entry_1.get() == c[i] and entry_2.get() == d[i]:
                flag=True

                root4=Tk()
                root4.title('Buy')

                import csv

                with open('Products.csv','r') as f:
                    csv_reader= csv.reader(f)

                    list_Product= Listbox(root4, selectmode= EXTENDED)
                    list_Quantity= Listbox(root4, selectmode= EXTENDED)
                    list_price= Listbox(root4, selectmode= EXTENDED)

                    i=0
                    for line in csv_reader:
                        

                        i=i+1

                        list_product.append(line[0].strip())
                        list_quantity.append(line[1].strip())
                        list_Price.append(line[2].strip())

    
                        list_Product.insert(i,line[0])
                        list_Quantity.insert(i,line[1])
                        list_price.insert(i,line[2])

                        list_Product.grid(row=0, column=1)
                        list_Quantity.grid(row=0, column=2)
                        list_price.grid(row=0, column=3)

                
                        text= Label(root4 , text= 'Enter what you want to buy:')
                        text.grid(row=1, column=1)
                        Entry_1= Entry(root4)
                        Entry_1.grid(row=1, column=2)


                        text_Amount= Label(root4 , text= 'Quantity:')
                        text_Amount.grid(row=2, column=1, sticky= E)
                        Entry_2= Entry(root4)
                        Entry_2.grid(row=2, column=2)

                        def Buy():
                            AddToCart()
                            addtocsv()
                            root_5= Tk()

                            with open('Cart.csv', 'r') as csv_file:
                                csv_reader= csv.reader(csv_file)

                                Show_product= Listbox(root_5, selectmode= EXTENDED)
                                Show_quantity= Listbox(root_5, selectmode= EXTENDED)
                                Show_price= Listbox(root_5, selectmode= EXTENDED)

                                i_2=0
                                for line in csv_reader:
                                    i_2= i_2+1
                                    Show_product.insert(i_2,line[0])
                                    Show_quantity.insert(i_2,line[1])
                                    Show_price.insert(i_2,line[2])

                                Show_product.grid(row=0, column=1)
                                Show_quantity.grid(row=0, column=2)
                                Show_price.grid(row=0, column=3)

                                label_3= Label(root_5, text='Total:')
                                label_3.grid(row=1, column=2, sticky=E)

                                t=0
                                for i_3 in Pri_ce:
                                    t= t+ float(i_3)

                                label_4= Label(root_5, text =t)
                                label_4.grid(row=1, column=3, sticky=W)


                            root_5.mainloop()

                    Buy_1= Button(root4, text='Buy', command= Buy)
                    Buy_1.grid(row=3, columnspan=4)
                            


                    del(list_Price[0])
                    del(list_product[0])
                    del(list_quantity[0])

                    def AddToCart():
                        flag_2=False

                

                        if Entry_1.get() in list_product:
                            Prod_uct.append(Entry_1.get())
                    

                        else:
                            root_1=Tk()
                            l_1= Label(root_1, text='Wrong Product')
                            l_1.pack()
                            root_1.mainloop()

                        for z in range(len(list_product)):
                            
                            if Entry_1.get()== list_product[z] and int(Entry_2.get())<=int(list_quantity[z]):
                                flag_2=True
   
                                Quant_ity.append(str(Entry_2.get()))
                            

                        if not flag_2:
                                root_2= Tk()
                                l_2= Label(root_2, text='Wrong Quantity')
                                l_2.pack()
                                root_2.mainloop()

                        for z_1 in range(len(list_product)):

                            if Entry_1.get()== list_product[z_1]:

                                y= int(Entry_2.get()) * float(list_Price[(z_1)])
                                Pri_ce.append(str(y))

                            else:
                                pass
                        Entry_1.delete(0, 'end')
                        Entry_2.delete(0, 'end')
 
                    def addtocsv():
                        with open('Cart.csv','w') as csv_file:
                            csv_writer= csv.writer(csv_file, delimiter=' ')
                            csv_writer.writerow(['Product',',','Quantity',',','Price'])
                            csv_writer.writerow(['',',','',',',''])

                            for i,j,z_2 in zip(Prod_uct,Quant_ity,Pri_ce):
                                csv_writer.writerow([i,',',j,',',z_2])

                    
                        

                    Addto_cart = Button(root4, text='Add To Cart', command=AddToCart)
                    Addto_cart.grid(row=4, columnspan=4)
                    
    
                    def Sh_cart():


                        addtocsv()
                        root5= Tk()
                        with open('Cart.csv', 'r') as csv_file:
                            csv_reader= csv.reader(csv_file)

                            Show_product= Listbox(root5, selectmode= EXTENDED)
                            Show_quantity= Listbox(root5, selectmode= EXTENDED)

                            i_1=0
                            
                            for line in csv_reader:
                                i_1= i_1+1
                                Show_product.insert(i_1,line[0])
                                Show_quantity.insert(i_1,line[1])

                            Show_product.grid(row=0, column=1)
                            Show_quantity.grid(row=0, column=2)

                        Buy_again= Button(root5, text='Buy', command= Buy)
                        Buy_again.grid(columnspan=2)
                                

                        root5.mainloop()

                    Show_Cart= Button(root4, text='Show Cart', command= Sh_cart)
                    Show_Cart.grid(row=2, column= 3)

                    root4.mainloop()

    if not flag:
                    root3= Tk()
                    label_3= Label(root3, text='invalid login')
                    label_3.grid(columnspan=2)
                    root3. mainloop()
                
    
   
button_1= Button(root, text='Login', command= LoginIsPressed)
button_1.grid(columnspan=2)


New_User= Button(root, text= 'New User', command=New_user)
New_User.grid(columnspan=3)
