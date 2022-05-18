from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# import msql.connector for connecting to mysql database
import mysql.connector
import datetime


class ApnaLibrary:
    # constructor
    # main page named as window
    def __init__(self, mainpage):
        self.mainpage=mainpage
        self.mainpage.title("ApnaLibrary (Library Management System)")
        self.mainpage.geometry("1366x768")
    
        heading = Label(self.mainpage, text="Welcome to ApnaLibrary Management Portal!",
                        bg="blue", fg="cyan", bd=20, relief=GROOVE, font=("Pristina", 36, "bold"))
        heading.pack(side=TOP, fill=X)

        # defining variables:
        self.designation=StringVar()
        self.id=StringVar()
        self.fname=StringVar()
        self.lname=StringVar()
        self.pin_addr=StringVar()
        self.mobile_no=StringVar()
        # single variable containing both class and division
        self.class_and_division=StringVar()
        self.address_line_1=StringVar()
        self.address_line_2=StringVar()
        self.book_id=StringVar()
        self.book_title=StringVar()
        self.author_name=StringVar()
        self.date_borrowed=StringVar()
        self.date_due=StringVar()
        self.days_on_book=StringVar()
        self.late_return_fine=StringVar()
        self.date_over_due=StringVar()
        self.actual_price=StringVar()

        # defining functions for CRUD operations:

        


        # setting frame for membership information ->

        frame1 = LabelFrame(self.mainpage, text="View Membership Information", bd=8, relief=GROOVE, font=("Pristina", 20, "bold"), padx=20, pady=5, bg="#3A8CF9")
        frame1.place(x=0, y=115, height=150, width=1355)

        # designation
        label_designation = Label(frame1, bg="#3A8CF9",
                             text="Designation", font=("Pristina", 15, "bold"))
        label_designation.grid(row=0, column=0, sticky=W)
        designation=ttk.Combobox(frame1, font=("arial", 10), width=18, height=15, state="readonly", textvariable=self.designation)
        designation['value']=("Undergraduate (B.E)", "Masters (M.E)")
        designation.grid(row=0, column=1, padx=20) 


        # ID number
        label_ID = Label(frame1, bg="#3A8CF9",
                             text="ID", font=("Pristina", 15, "bold"))
        label_ID.grid(row=1, column=0, sticky=W)

        text_ID = Entry(frame1, font=("arial", 10), width=21, textvariable=self.id)
        text_ID.grid(row=1, column=1)


        # first name
        label_fname = Label(frame1, bg="#3A8CF9",
                         text="First name", font=("Pristina", 15, "bold"))
        label_fname.grid(row=2, column=0, sticky=W)

        text_fname = Entry(frame1, font=("arial", 10), width=21, textvariable=self.fname)
        text_fname.grid(row=2, column=1)


        # last name
        label_lname = Label(frame1, bg="#3A8CF9",
                            text="Last name", font=("Pristina", 15, "bold"))
        label_lname.grid(row=0, column=2, sticky=W)

        text_lname = Entry(frame1, font=("arial", 10), width=21, textvariable=self.lname)
        text_lname.grid(row=0, column=3, padx=20)


        # PIN number
        label_PIN = Label(frame1, bg="#3A8CF9",
                           text="PIN Address", font=("Pristina", 15, "bold"))
        label_PIN.grid(row=1, column=2, sticky=W)

        text_PIN = Entry(frame1, font=("arial", 10), width=21, textvariable=self.pin_addr)
        text_PIN.grid(row=1, column=3, padx=20)

        # mobile number
        label_mobile = Label(frame1, bg="#3A8CF9",
                          text="Mobile No.", font=("Pristina", 15, "bold"))
        label_mobile.grid(row=2, column=2, sticky=W)

        text_mobile = Entry(frame1, font=("arial", 10), width=21, textvariable=self.mobile_no)
        text_mobile.grid(row=2, column=3, padx=20)

        # class and division
        label_class_and_division = Label(frame1, bg="#3A8CF9",
                                         text="Class and division (eg: TE 2) (Write in this format)", font=("Pristina", 15, "bold"), padx=20)
        label_class_and_division.grid(row=0, column=4, sticky=W)
        label_class_and_division = Entry(frame1, font=("arial", 10), width=21, textvariable=self.class_and_division)
        label_class_and_division.grid(row=0, column=5, sticky=W)

        # address line 1
        label_address_1 = Label(frame1, bg="#3A8CF9",
                                text="Address Line 1", font=("Pristina", 15, "bold"), padx=20)
        label_address_1.grid(row=1, column=4, sticky=N)
        text_address_1 = Entry(frame1, font=("arial", 10), width=40, textvariable=self.address_line_1)
        text_address_1.grid(row=1, column=5)

        # address line 2
        label_address_2 = Label(frame1, bg="#3A8CF9",
                                text="Address Line 2", font=("Pristina", 15, "bold"), padx=20)
        label_address_2.grid(row=2, column=4, sticky=N)

        text_address_2 = Entry(frame1, font=("arial", 10), width=40, textvariable=self.address_line_2)
        text_address_2.grid(row=2, column=5)


        # setting frame for book details->

        frame2 = LabelFrame(self.mainpage, text="View Book Details", bd=8, relief=GROOVE, font=(
            "Pristina", 20, "bold"), padx=20, pady=5, bg="#3A8CF9")
        frame2.place(x=0, y=270, height=150, width=700)

        label_book_ID = Label(frame2, bg="#3A8CF9",
                            text="Book ID", font=("Pristina", 15, "bold"), padx=10)
        label_book_ID.grid(row=0, column=0, sticky=N)

        text_book_ID = Entry(frame2, font=("arial", 10), width=10, textvariable=self.book_id)
        text_book_ID.grid(row=0, column=1)

        label_book_title = Label(frame2, bg="#3A8CF9",
                              text="Book Title", font=("Pristina", 15, "bold"), padx=10)
        label_book_title.grid(row=1, column=0, sticky=N)

        text_book_title = Entry(frame2, font=("arial", 10), width=15, textvariable=self.book_title)
        text_book_title.grid(row=1, column=1)

        label_author_name = Label(frame2, bg="#3A8CF9",
                                 text="Author name", font=("Pristina", 15, "bold"), padx=10)
        label_author_name.grid(row=2, column=0, sticky=N)

        text_author_name = Entry(frame2, font=("arial", 10), width=15, textvariable=self.author_name)
        text_author_name.grid(row=2, column=1)

        label_date_borrowed = Label(frame2, bg="#3A8CF9",
                              text="Date Borrowed", font=("Pristina", 15, "bold"), padx=10)
        label_date_borrowed.grid(row=0, column=2, sticky=N)
        text_date_borrowed = Entry(frame2, font=("arial", 10), width=10, textvariable=self.date_borrowed)
        text_date_borrowed.grid(row=0, column=3)

        label_due_date = Label(frame2, bg="#3A8CF9",
                              text="Date due", font=("Pristina", 15, "bold"), padx=10)
        label_due_date.grid(row=1, column=2, sticky=N)
        text_due_date = Entry(frame2, font=("arial", 10), width=10, textvariable=self.date_due)
        text_due_date.grid(row=1, column=3)

        label_days_on_book = Label(frame2, bg="#3A8CF9",
                              text="Days on book", font=("Pristina", 15, "bold"), padx=10)
        label_days_on_book.grid(row=2, column=2, sticky=N)
        text_days_on_book = Entry(frame2, font=("arial", 10), width=10, textvariable=self.days_on_book)
        text_days_on_book.grid(row=2, column=3)

        label_late_return_fine = Label(frame2, bg="#3A8CF9",
                              text="Late return fine", font=("Pristina", 15, "bold"), padx=10)
        label_late_return_fine.grid(row=0, column=4, sticky=N)
        text_late_return_fine = Entry(frame2, font=("arial", 10), width=10, textvariable=self.late_return_fine)
        text_late_return_fine.grid(row=0, column=5)

        label_date_over_due = Label(frame2, bg="#3A8CF9",
                              text="Date over due", font=("Pristina", 15, "bold"), padx=10)
        label_date_over_due.grid(row=1, column=4, sticky=N)
        text_date_over_due = Entry(frame2, font=("arial", 10), width=10, textvariable=self.date_over_due)
        text_date_over_due.grid(row=1, column=5)

        label_actual_price = Label(frame2, bg="#3A8CF9",
                              text="Actual Price", font=("Pristina", 15, "bold"), padx=10)
        label_actual_price.grid(row=2, column=4, sticky=N)
        text_actual_price = Entry(frame2, font=("arial", 10), width=10, textvariable=self.actual_price)
        text_actual_price.grid(row=2, column=5)

        frame2_sub = LabelFrame(self.mainpage, bd=8, relief=GROOVE, font=(
            "Pristina", 20, "bold"), padx=20, pady=5, bg="#3A8CF9")
        frame2_sub.place(x=700, y=270, height=150, width=680)

        self.textbox = Text(frame2_sub, font=("arial", 10),
                            width=45, height=7, padx=2, pady=5)
        self.textbox.grid(row=0, column=0, sticky=W)
        scrollb = Scrollbar(self.textbox, command=self.textbox.yview)
        self.textbox['yscrollcommand']=scrollb.set
        scrollb.place(x=300, y=0, anchor='ne', relheight=1)

        scrollBar=Scrollbar(frame2_sub)
        scrollBar.grid(row=0, column=4, sticky="ns")

        # list_books = ['To Kill a Mockingbird',
        #                'The Great Gatsby', 
        #                'Things Fall Apart', 
        #                'Harry Potter', 
        #                'Moby-Dick', 
        #                'The Color Purple',
        #                 'Catch-22', 
        #                 '1984', 
        #                 'The Hobbit and The Lord of the Rings', 
        #                 'Hamlet', 
        #                 'The Catcher in the Rye', 
        #                 'Invisible Man', 
        #                 'Watchmen', 
        #                 'Lord of the rings', 
        #                 'Frankenstein', 
        #                 'Wuthering Heights', 
        #                 'The Sound and the Fury', 
        #                 'The Brothers Karamazov', 
        #                 'Giovanni Room', 
        #                 'The Hate U Give', 
        #                 'Rich Dad Poor Dad', 
        #                 'Pride and Prejudice']
    
        list_books = ['To Kill a Mockingbird',
                        'The Great Gatsby', 
                        'Things Fall Apart',
                        'Harry Potter',
                        'Moby-Dick',
                        'The Color Purple',
                        'Catch-22',
                        '1984',
                        'The Hobbit and The Lord of the Rings',
                        'Hamlet',
                        'The Catcher in the Rye'
                        ]

        def select_book_and_display(event=""):
            print("Function called")
            value=str(listbox.get(ACTIVE))
            x=value
            if (x=='To Kill a Mockingbird'):
                self.book_id.set('1')
                self.book_title.set('To Kill a Mockingbird')
                self.author_name.set('Harper Lee')

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                print(type(d1))
                print(type(d2))
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set(10)
                self.late_return_fine.set("50")
                self.date_over_due.set("NO")
                self.actual_price.set("550")
            elif (x == 'The Great Gatsby'):
                self.book_id.set('2')
                self.book_title.set('The Great Gatsby')
                self.author_name.set('F. Scott Fitzgerald')

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                print(type(d1))
                print(type(d2))
                d3 = d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set(10)
                self.late_return_fine.set("100")
                self.date_over_due.set("NO")
                self.actual_price.set("550")
            elif (x == 'Things Fall Apart'):
                self.book_id.set('3')
                self.book_title.set('Things Fall Apart')
                self.author_name.set('Chinua Achebe')

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                print(type(d1))
                print(type(d2))
                d3 = d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set(10)
                self.late_return_fine.set("100")
                self.date_over_due.set("NO")
                self.actual_price.set("550")
            elif (x == 'Harry Potter'):
                self.book_id.set('4')
                self.book_title.set('Harry Potter')
                self.author_name.set('J.K Rowling')

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                print(type(d1))
                print(type(d2))
                d3 = d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set(10)
                self.late_return_fine.set("100")
                self.date_over_due.set("NO")
                self.actual_price.set("550")
            elif (x == 'Moby-Dick'):
                self.book_id.set('5')
                self.book_title.set('Moby-Dick')
                self.author_name.set('Herman Melville')

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                print(type(d1))
                print(type(d2))
                d3 = d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set(10)
                self.late_return_fine.set("100")
                self.date_over_due.set("NO")
                self.actual_price.set("550")
            elif (x == 'The Color Purple'):
                self.book_id.set('6')
                self.book_title.set('The Color Purple')
                self.author_name.set('Alice Walker')

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                print(type(d1))
                print(type(d2))
                d3 = d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set(10)
                self.late_return_fine.set("100")
                self.date_over_due.set("NO")
                self.actual_price.set("550")
            elif (x == 'Catch-22'):
                self.book_id.set('7')
                self.book_title.set('Catch-22')
                self.author_name.set('Joseph Heller')

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                print(type(d1))
                print(type(d2))
                d3 = d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set(10)
                self.late_return_fine.set("100")
                self.date_over_due.set("NO")
                self.actual_price.set("550")
            elif (x == '1984'):
                self.book_id.set('8')
                self.book_title.set('1984')
                self.author_name.set('George Orwell')

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                print(type(d1))
                print(type(d2))
                d3 = d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set(10)
                self.late_return_fine.set("100")
                self.date_over_due.set("NO")
                self.actual_price.set("550")
            elif (x == 'The Hobbit and The Lord of the Rings'):
                self.book_id.set('9')
                self.book_title.set('The Hobbit and The Lord of the Rings')
                self.author_name.set('J.R.R Tolkien')

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                print(type(d1))
                print(type(d2))
                d3 = d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set(10)
                self.late_return_fine.set("100")
                self.date_over_due.set("NO")
                self.actual_price.set("550")
            elif (x == 'Hamlet'):
                self.book_id.set('10')
                self.book_title.set('Hamlet')
                self.author_name.set('William Shakespeare')

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                print(type(d1))
                print(type(d2))
                d3 = d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set(10)
                self.late_return_fine.set("100")
                self.date_over_due.set("NO")
                self.actual_price.set("550")
            elif (x == 'The Catcher in the Rye'):
                self.book_id.set('11')
                self.book_title.set('The Catcher in the Rye')
                self.author_name.set('J.D Salinger')

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                print(type(d1))
                print(type(d2))
                d3 = d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set(10)
                self.late_return_fine.set("100")
                self.date_over_due.set("NO")
                self.actual_price.set("550")
            

        
        # def print_value():
        #     print("Hello world")
        
        listbox = Listbox(frame2_sub, font=("arial", 10), width=40, height=7)
        

        listbox.grid(row=0, column=3, padx=4)
        scrollBar.config(command=listbox.yview)

        # for book in list_books:
        #     listbox.insert(END, book)
        for i in range(len(list_books)):
            listbox.insert(i, list_books[i])
        listbox.bind("<<ListboxSelect>>", select_book_and_display)



        # frame for radio buttons to select one of the CRUD operations->
        operation_selection_frame = LabelFrame(
            self.mainpage, relief=RIDGE, bd=7, bg="#3A8CF9")
        operation_selection_frame.place(x=0, y=425, height=40, width=1355)

        self.v = StringVar(self.mainpage, "1")

        values = {"Add Record": "1",
                  "Display Records": "2",
                  "Update a Record": "3",
                  "Delete a Record": "4",
        }



        for (text, value) in values.items():
            Radiobutton(operation_selection_frame, text=text, font=("Pristina", 20, "bold"), variable = self.v,
                        value=value, bg="#3A8CF9").pack(anchor=W, side=LEFT, ipadx=5)

        

        submit_button = Button(operation_selection_frame, text="Execute Operation",
                               width=15, bg="green", font=("Pristina", 20, "bold"), command=self.execute_operation)
        submit_button.pack(anchor=W, side=LEFT, padx=20, ipadx=5)

        # frame to show the data from the database->

        database_info_frame = Frame(
            self.mainpage, relief=RIDGE, bd=7, bg="#3A8CF9", padx=15)
        database_info_frame.place(x=0, y=480, width=1355, height=200)

        table_frame = Frame(database_info_frame, bd=6,
                            relief=GROOVE, bg='#3A8CF9')
        table_frame.place(x=0, y=2, height=180, width=1315)  

        # creating treeview for displaying database columns

        xscroll=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(table_frame, orient=VERTICAL)


        self.database_table=ttk.Treeview(table_frame, column=["designation", "id", "fname", "lname", "pin_addr", "mobile_no", "class", "division", "address_line_1", "address_line_2", "book_id", "book_title", "author_name", "date_borrowed", "date_due", "days_on_book", "late_return_fine", "date_over_due", "actual_price"], xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)           
        
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.database_table.xview)
        yscroll.config(command=self.database_table.yview)

        self.database_table.heading("designation", text="Designation")
        self.database_table.heading("id", text="ID")
        self.database_table.heading("fname", text="First Name")
        self.database_table.heading("lname", text="Last Name")
        self.database_table.heading("pin_addr", text="PIN Address")
        self.database_table.heading("mobile_no", text="Mobile Number")
        self.database_table.heading("class", text="Class")
        self.database_table.heading("division", text="Division")
        self.database_table.heading("address_line_1", text="Address Line 1")
        self.database_table.heading("address_line_2", text="Address Line 2")
        self.database_table.heading("book_id", text="Book Id")
        self.database_table.heading("book_title", text="Book Title")
        self.database_table.heading("author_name", text="Author Name")
        self.database_table.heading("date_borrowed", text="Date Borrowed")
        self.database_table.heading("date_due", text="Date Due")
        self.database_table.heading("days_on_book", text="Days on book")
        self.database_table.heading(
            "late_return_fine", text="Late return fine")
        self.database_table.heading("date_over_due", text="Date over due")
        self.database_table.heading("actual_price", text="Actual Price")

        self.database_table['show']='headings'
        self.database_table.pack(fill=BOTH, expand=1)

        self.fetch()
        self.database_table.bind("<ButtonRelease-1>", self.get_cursor)
    
    def addData(self):
        print("Add operation started")
        connection = mysql.connector.connect(
            host="localhost", username="root", password="2001Pankaj@", database="dbmsl_mini_project")
        cursor = connection.cursor()
        
        cursor.execute(
            "insert into library_management values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (self.designation.get(), self.id.get(), self.fname.get(), self.lname.get(), self.pin_addr.get(), self.mobile_no.get(), self.class_and_division.get().split()[0], self.class_and_division.get().split()[1], self.address_line_1.get(
            ), self.address_line_2.get(), self.book_id.get(), self.book_title.get(), self.author_name.get(), self.date_borrowed.get(), self.date_due.get(), self.days_on_book.get(), self.late_return_fine.get(), self.date_over_due.get(), self.actual_price.get())
        )
        connection.commit()
        connection.close()

        messagebox.showinfo(
            "Success", "Information has been inserted successfully!")
    
    def fetch(self):
        print("fetch operation started")
        connection = mysql.connector.connect(
            host="localhost", username="root", password="2001Pankaj@", database="dbmsl_mini_project")
        cursor = connection.cursor()
        cursor.execute("select * from library_management")
        rows=cursor.fetchall()

        if len(rows)!=0:
            self.database_table.delete(*self.database_table.get_children())
            for i in rows:
                self.database_table.insert("", END, values=i)
            connection.commit()
        connection.close()
    
    def get_cursor(self, event=""):
        print("Get-cursor event started")
        cursor_row = self.database_table.focus()
        content = self.database_table.item(cursor_row)
        row=content['values']

        self.designation.set(row[0])
        self.id.set(row[1])
        self.fname.set(row[2])
        self.lname.set(row[3])
        self.pin_addr.set(row[4])
        self.mobile_no.set(row[5])
        # self.database_table.set(row[6])
        # self.database_table.set(row[7])
        self.class_and_division.set(str(row[6])+' '+str(row[7]))
        self.address_line_1.set(row[8])
        self.address_line_2.set(row[9])
        self.book_id.set(row[10])
        self.book_title.set(row[11])
        self.author_name.set(row[12])
        self.date_borrowed.set(row[13])
        self.date_due.set(row[14])
        self.days_on_book.set(row[15])
        self.late_return_fine.set(row[16])
        self.date_over_due.set(row[17])
        self.actual_price.set(row[18])

    def show(self):
        self.textbox.insert(END, "Designation: "+self.designation.get()+"\n")
        self.textbox.insert(END, "ID: "+self.id.get()+"\n")
        self.textbox.insert(END, "First name: "+self.fname.get()+"\n")
        self.textbox.insert(END, "Last name: "+self.lname.get()+"\n")
        self.textbox.insert(END, "PIN Address: "+self.pin_addr.get()+"\n")
        self.textbox.insert(END, "Mobile Number: "+self.mobile_no.get()+"\n")
        self.textbox.insert(
            END, "Class: "+self.class_and_division.get().split()[0]+"\n")
        self.textbox.insert(END, "Division: " +
                            self.class_and_division.get().split()[1]+"\n")
        self.textbox.insert(END, "Address Line 1: "+self.address_line_1.get()+"\n")
        self.textbox.insert(END, "Address Line 2: " +
                            self.address_line_2.get()+"\n")
        self.textbox.insert(END, "Book ID: "+self.book_id.get()+"\n")
        self.textbox.insert(END, "Book title: "+self.book_title.get()+"\n")
        self.textbox.insert(END, "Author Name: "+self.author_name.get()+"\n")
        self.textbox.insert(END, "Date Borrowed: "+self.date_borrowed.get()+"\n")
        self.textbox.insert(END, "Due Date: "+self.date_due.get()+"\n")
        self.textbox.insert(END, "Days on book: "+self.days_on_book.get()+"\n")
        self.textbox.insert(END, "Late Return Fine: "+self.late_return_fine.get()+"\n")
        self.textbox.insert(END, "Date Over Due?: "+self.date_over_due.get()+"\n")
        self.textbox.insert(END, "Actual Price: "+self.actual_price.get()+"\n")
        
    def delete_data(self):
        print("Delete operation started")
        print(type(self.id.get()))
        connection = mysql.connector.connect(
            host="localhost", username="root", password="2001Pankaj@", database="dbmsl_mini_project")
        cursor = connection.cursor()

        cursor.execute(
            "delete from library_management where id=%s"%(self.id.get())
        )
        connection.commit()
        connection.close()

        messagebox.showinfo(
            "Success", "Record has been deleted successfully!")

    def update_data(self):
        print("Update operation started")
        print(type(self.id.get()))
        connection = mysql.connector.connect(
            host="localhost", username="root", password="2001Pankaj@", database="dbmsl_mini_project")
        cursor = connection.cursor()

        cursor.execute(
            "update library_management set designation='%s', firstname='%s', lastname='%s', pin_address='%s', mobile_number='%s', class='%s', division ='%s', address_line_1='%s', address_line_2='%s', book_id='%s', book_title='%s', author_name='%s', date_borrowed='%s', due_date='%s', days_on_book='%s', late_return_fine='%s', date_over_due='%s', actual_price='%s' where id='%s'" % (self.designation.get(
            ), self.fname.get(), self.lname.get(), self.pin_addr.get(), self.mobile_no.get(), self.class_and_division.get().split()[0], self.class_and_division.get().split()[1], self.address_line_1.get(), self.address_line_2.get(), self.book_id.get(), self.book_title.get(), self.author_name.get(), self.date_borrowed.get(), self.date_due.get(), self.days_on_book.get(), self.late_return_fine.get(), self.date_over_due.get(), self.actual_price.get(),self.id.get())
        )
        connection.commit()
        connection.close()

        messagebox.showinfo(
            "Success", "Record has been updated successfully!")



    def execute_operation(self):
        print("Execution operation started")
        if self.v.get() == "1":
            self.addData()
            print("entered add")
        elif self.v.get() == "2":
            self.show()
            print("entered display")
        elif self.v.get() == "3":
            self.update_data()
            print("entered update")
        elif self.v.get() == "4":
            self.delete_data()
            print("entered delete")
        print("skipped")

if __name__=="__main__":
    mainpage = Tk()  # mainpage is the window name and Tk() displays the window
    obj=ApnaLibrary(mainpage)
    obj.mainpage.mainloop() # to make sure the Tkinter window keeps running.

    

