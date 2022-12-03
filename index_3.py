from tkinter import *
class costumer:
    def __init__(self,acc_type,username,name,adress,loan_duration,phone,email,balance) -> None:
        self.name = name
        self.adress = adress
        self.loan_duration = loan_duration
        self.phone = phone
        self.email = email
        self.acc_type = acc_type
        self.username = username
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount

Window = Tk()
Window.title('Bank mangement system')
Window.geometry('400x400')
Window.minsize(width=400,height=400)
Window.maxsize(width=400,height=1080)

# Master password used for all costumers and manager
master_password = 'admin123'
# default savings acc
accounts = {}
accounts['saving_aamir067'] = costumer('saving','aamir067','Aamir Khan','surrani bannu','None','03441259408' , 'aamirkhan@engineer.com',10000)
accounts['saving_rafay6969'] = costumer('saving','rafay6969','Hassan Rafay','fatma khel','None','03333333333' , 'rafay69@hacker.com',10000)

# default loan acc
accounts['loan_tawab95'] = costumer('loan','tawab95','tawab  khan','bannu surrani','120 days','03498789876' , 'tawabkhan95@engineer.com',10000)
accounts['loan_hamza321'] = costumer('loan','hamza321','Humza Khan','nourang','180 days','03489765678','hamza@gmail.com',10000)
def home():
    def clear_home():
        welcome_label.destroy()
        costumer_btn.destroy()
        manager_btn.destroy()
        quit_btn.destroy()
    welcome_label = Label(Window,text='WELCOME',font=('italic',25),bg='#999')
    welcome_label.pack(fill=X)
    def one():
        clear_home()
        def clear_one():
            saving_accs.destroy()
            loan_accs.destroy()
            back.destroy()
            exit.destroy()
        def one_a(type_of_acc):
            def clear_one_a():
                user_name_label.destroy()
                user_name_entry.destroy()
                pass_word_label.destroy()
                pass_word_entry.destroy()
                back.destroy()
                register.destroy()
                login_btn.destroy()
            clear_one()

            user_name_label = Label(Window,text='username : ',font=14)
            user_name_label.place(x=50,y=100)
            user_name_entry = Entry(Window,width=30)
            user_name_entry.place(x=140,y=105)

            pass_word_label = Label(Window,text='password : ',font=14)
            pass_word_label.place(x=50,y=150)
            pass_word_entry = Entry(Window,width=30)
            pass_word_entry.place(x=140,y=155)
            pass_word_entry.insert(0,master_password)

            # btns
            def back_function():
                clear_one_a()
                one()
            back = Button(Window,text='Back',padx=5,pady=5,command=back_function)
            back.place(x=80,y=200)
            def new_costumer():
                clear_one_a()
                u_name = Label(Window,text='Username : ',font=('sans serifs',14))
                u_name.place(x=70 ,y = 40)
                u_name_entry = Entry(Window,width=30)
                u_name_entry.place(x = 180 , y=45)

                name = Label(Window,text='Name : ',font=('sans serifs',14))
                name.place(x= 70 , y=80)
                name_entry=Entry(Window,width=30)
                name_entry.place(x = 150,y=85)

                adress = Label(Window,text='Adress : ',font=('sans serifs',14))
                adress.place(x = 70, y=120)
                adress_entry = Entry(Window,width=30)
                adress_entry.place(x= 150,y=125)

                phone = Label(Window,text='Phone : ',font=('sans serifs',14))
                phone.place(x=70,y=160)
                phone_entry = Entry(Window,width=30)
                phone_entry.place(x=150,y=165)

                mail = Label(Window,text='Email : ', font=('sans serifs',14))
                mail.place(x=70,y=200)
                mail_entry = Entry(Window,width=30)
                mail_entry.place(x=150,y=205)

                balance = Label(Window,text='Balance : ',font=('sans serifs',14))
                balance.place(x=70,y=240)
                balance_entry = Entry(Window,width=30)
                balance_entry.place(x=160,y=245)

                loan_duration = Label(Window,text='Loan duration : ',font=('sans serifs',14))
                loan_duration.place(x=70,y=280)
                loan_duration_entry = Entry(Window,width=20)
                loan_duration_entry.place(x=210,y=285)

                # btns
                def back_or_save(is_save):
                    if is_save == True:
                        accounts[f'{type_of_acc}_{u_name_entry.get()}'] = costumer(type_of_acc,u_name_entry.get(),name_entry.get(),adress_entry.get(),loan_duration_entry.get(),phone_entry.get(),mail_entry.get(),int(balance_entry.get()))
                    u_name.destroy()
                    u_name_entry.destroy()
                    name.destroy()
                    name_entry.destroy()
                    adress.destroy()
                    adress_entry.destroy()
                    phone.destroy()
                    phone_entry.destroy()
                    mail.destroy()
                    mail_entry.destroy()
                    balance.destroy()
                    balance_entry.destroy()
                    loan_duration.destroy()
                    loan_duration_entry.destroy()
                    back_btn.destroy()
                    save_btn.destroy()
                    one_a(type_of_acc)
                back_btn = Button(Window,text='Back',padx=5,pady=5,command=lambda:back_or_save(False))
                back_btn.place(x=70,y=320)
                save_btn = Button(Window,text='Save',padx=5,pady=5,command=lambda:back_or_save(True))
                save_btn.place(x=200,y=320)

            register = Button(Window,text='Reister new',padx=5,pady=5,command=new_costumer)
            register.place(x=160,y=200)
            def one_aa(user_name,pass_word):
                clear_one_a()
                def clear_one_aa():
                    acc_title.destroy()
                    acc_title_value.destroy()
                    acc_type.destroy()
                    acc_type_value.destroy()
                    acc_balance.destroy()
                    acc_balance_value.destroy()
                    withdraw_money.destroy()
                    deposit_money.destroy()
                    loan_duration.destroy()
                    loan_duration_value.destroy()
                    back_btn.destroy()
                    exit_btn.destroy()
                if f'{type_of_acc}_{user_name}' not in accounts.keys():
                    one_a(type_of_acc)
                else:
                    if pass_word != master_password:
                        one_a(type_of_acc)
                    else:
                        ...
                        acc_title = Label(Window,text='Account Title :  ',font=('sans serifs',14))
                        acc_title.place(x=50,y=40)
                        acc_title_value = Label(Window,text=accounts[f'{type_of_acc}_{user_name}'].name,font=('sans serifs',14))
                        acc_title_value.place(x=200,y=40)
                        acc_type = Label(Window,text='Account Type :  ',font=('sans serifs',14))
                        acc_type.place(x=50,y=80)
                        acc_type_value = Label(Window,text=accounts[f'{type_of_acc}_{user_name}'].acc_type,font=('sans serifs',14))
                        acc_type_value.place(x= 200,y=80)
                        acc_balance = Label(Window,text='Available Amount :',font=('sans serifs',16))
                        acc_balance.place(x=50,y=160)
                        acc_balance_value = Label(Window,text=accounts[f'{type_of_acc}_{user_name}'].balance,font=('sans serifs',16),bg='#aaa')
                        acc_balance_value.place(x=230,y=160)

                        loan_duration = Label(Window,text='Loan duration :',font=('sans serifs',14))
                        loan_duration.place(x=50,y=120)
                        loan_duration_value = Label(Window,text=accounts[f'{type_of_acc}_{user_name}'].loan_duration,font=('sans serifs',14))
                        loan_duration_value.place(x=200,y=120)

                        # btns
                        def money_opration(is_withdraw):
                            def clear_m_op():
                                money.destroy()
                                money_entry.destroy()
                                btn_back.destroy()
                                btn_conform.destroy()
                            clear_one_aa()
                            money = Label(Window,text='Enter Amount :',font=('sans serifs',12))
                            money.place(x=50,y=70)
                            money_entry = Entry(Window,width=20)
                            money_entry.place(x= 160,y=75)

                            # btns
                            def back_n_conform(is_conform,amount_entered):
                                if is_conform == True:
                                    if is_withdraw == True:
                                        accounts[f'{type_of_acc}_{user_name}'].withdraw(int(amount_entered))
                                    else:
                                        accounts[f'{type_of_acc}_{user_name}'].deposit(int(amount_entered))
                                clear_m_op()
                                one_aa(user_name,pass_word)

                            btn_back = Button(Window,text='Back',padx=5,pady=5,command= lambda: back_n_conform(False,money_entry.get()))
                            btn_back.place(x = 100,y=150)
                            btn_conform = Button(Window,text='Conform Opration',padx=5,pady=5,command= lambda: back_n_conform(True,money_entry.get()))
                            btn_conform.place(x=240,y=150)

                        if type_of_acc == 'loan':
                            deposit_money = Button(Window,text='Take Loan',padx=5,pady=5,command = lambda:money_opration(False))
                            deposit_money.place(x=100,y=250)
                        else:
                            deposit_money = Button(Window,text='Deposit Money',padx=5,pady=5,command = lambda:money_opration(False))
                            deposit_money.place(x=100,y=250)
                        withdraw_money = Button(Window,text='Withdraw Money',padx=5,pady=5,command=lambda:money_opration(True))
                        withdraw_money.place(x=230,y=250)
                        def back():
                            clear_one_aa()
                            one_a(type_of_acc)
                        back_btn = Button(Window,text="Back",command=back)
                        back_btn.place(x=120,y=310)
                        exit_btn = Button(Window,text='Quit',command=Window.quit)
                        exit_btn.place(x=260,y=310)

            login_btn= Button(Window,text='Login',padx=5,pady=5,command=lambda:one_aa(user_name_entry.get(),pass_word_entry.get()))
            login_btn.place(x=280,y=200)

        saving_accs = Button(Window,text='Saving accounts',padx=5,pady=5,command=lambda: one_a('saving'))
        saving_accs.place(x=160,y=130)
        loan_accs = Button(Window,text='Loan accounts',padx=5,pady=5,command=lambda: one_a('loan'))
        loan_accs.place(x=160,y=180)
        def backk():
            clear_one()
            home()
        back = Button(Window,text='Back' , padx=5,pady=5,command=backk)
        back.place(x=100,y=240)
        exit = Button(Window,text='Exit' , padx=5,pady=5,command=Window.quit)
        exit.place(x=250,y=240)

    costumer_btn = Button(Window,text='Enter as a Costumer',padx=5,pady=5,command=one)
    costumer_btn.place(x=140,y=150)

    def two():
        clear_home()
        def clear_two():
            saving_acc.destroy()
            loan_acc.destroy()
            back.destroy()
            exit.destroy()
        def show_accs(acc_type):
            clear_two()
            col = 30
            row = 30
            u_name = Label(Window,text='username',font=('sans serifs',12))
            u_name.place(x=col,y=row)
            acc_type = Label(Window,text='acc type',font=('sans serifs',12))
            acc_type.place(x=col+90,y=row)
            balance = Label(Window,text='balance',font=('sans serifs',12))
            balance.place(x=col+180,y=row)
            loan_duration = Label(Window,text='loan duration',font=('sans serifs',12))
            loan_duration.place(x=col+270,y=row)
            row = 70
            for keys in accounts:
                ...
                u_name_value = Label(Window,text=accounts[keys].name)
                u_name_value.place(x=col,y=row)
                acc_type_value = Label(Window,text=accounts[keys].acc_type)
                acc_type_value.place(x=col+90,y=row)
                balance_value = Label(Window,text=accounts[keys].balance)
                balance_value.place(x=col+180,y=row)
                loan_duration_value = Label(Window,text=accounts[keys].loan_duration)
                loan_duration_value.place(x=col+270,y=row)
                row += 40
                col=30

        saving_acc = Button(Window,text='Saving accounts',padx=5,pady=5,command=lambda: show_accs('saving'))
        saving_acc.place(x=160,y=130)
        loan_acc = Button(Window,text='Loan accounts',padx=5,pady=5,command=lambda: show_accs('loan'))
        loan_acc.place(x=160,y=180)
        def backk():
            clear_two()
            home()
        back = Button(Window,text='Back' , padx=5,pady=5,command=backk)
        back.place(x=100,y=240)
        exit = Button(Window,text='Exit' , padx=5,pady=5,command=Window.quit)
        exit.place(x=250,y=240)

    manager_btn = Button(Window,text='Enter as a Manager',padx=5,pady=5,command=two)
    manager_btn.place(x=140,y=200)
    quit_btn = Button(Window,text='Quit',padx=5,pady=5,command=Window.quit)
    quit_btn.place(x=180,y=250)

home()
Window.mainloop()