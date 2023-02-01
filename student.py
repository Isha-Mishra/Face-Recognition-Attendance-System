from email import message
from logging import exception
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Attendance Monitoring System")

        #============variable=============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar() 
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
       




        #first image
        img=Image.open(r"C:\Users\FO\Desktop\Attendance Monitering System\college_image\college.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second  
        img1=Image.open(r"C:\Users\FO\Desktop\Attendance Monitering System\college_image\ssipmt.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third
        img2=Image.open(r"C:\Users\FO\Desktop\Attendance Monitering System\college_image\inner-banner.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=450,height=130)

        #bg image 
        img3=Image.open(r"C:\Users\FO\Desktop\Attendance Monitering System\college_image\unnamed.png")
        img3=img3.resize((1350,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_image=Label(self.root,image=self.photoimg3)
        bg_image.place(x=0,y=130,width=1350,height=710)

        title_lbl=Label(bg_image,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1350,height=45)

        main_frame=Frame(bg_image,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1350,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold" ))
        Left_frame.place(x=5,y=5,width=660,height=500)

        img_left=Image.open(r"C:\Users\FO\Desktop\Attendance Monitering System\college_image\inner-banner.jpg")
        img_left=img_left.resize((650,100),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=650,height=100)
 
        #current cousre
        course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Course Information",font=("times new roman",12,"bold" ))
        course_frame.place(x=0,y=105,width=655,height=100)
        
        #department
        dep_label=Label(course_frame,text="Department",font=("times new roman",11,"bold" ))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(course_frame,textvariable=self.var_dep,font=("times new roman",11,"bold" ),state="readonly",width=20)
        dep_combo["values"]=("Select Department","CSE","IT","ETNT","EEE","Civil","ME")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(course_frame,text="Course",font=("times new roman",11,"bold" ))
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(course_frame,textvariable=self.var_course,font=("times new roman",11,"bold" ),state="readonly",width=20)
        course_combo["values"]=("Select Course","BE","B.TECH","M.TECH","BBA","MBA","B.COM","M.COM","BA","MA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(course_frame,text="Year",font=("times new roman",11,"bold" ))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(course_frame,textvariable=self.var_year,font=("times new roman",11,"bold" ),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        sem_label=Label(course_frame,text="Semester",font=("times new roman",11,"bold" ))
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(course_frame,textvariable=self.var_semester,font=("times new roman",11,"bold" ),state="readonly",width=20)
        sem_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #CLASS STUDENT INFORMATION 
        std_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text=" Class Student Information",font=("times new roman",12,"bold" ))
        std_frame.place(x=0,y=205,width=655,height=270)
  
        #student id 
        stdid_label=Label(std_frame,text="Student Id:",font=("times new roman",11,"bold" ))
        stdid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        stdid_entry=ttk.Entry(std_frame,width=20,textvariable=self.var_std_id,font=("times new roman",11,"bold" ))
        stdid_entry.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #student name
        stdname_label=Label(std_frame,text="Student Name:",font=("times new roman",11,"bold" ))
        stdname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        stdname_entry=ttk.Entry(std_frame,width=20,textvariable=self.var_std_name,font=("times new roman",11,"bold" ))
        stdname_entry.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        #class div 
        stddiv_label=Label(std_frame,text="Class Division:",font=("times new roman",11,"bold" ))
        stddiv_label.grid(row=1,column=0,padx=10,sticky=W)

        #stddiv_entry=ttk.Entry(std_frame,width=20,textvariable=self.var_div,font=("times new roman",11,"bold" ))
        #stddiv_entry.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        div_combo=ttk.Combobox(std_frame,textvariable=self.var_div,font=("times new roman",11,"bold" ),state="readonly",width=20)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W) 

        #roll no.
        stdroll_label=Label(std_frame,text="Roll no.:",font=("times new roman",11,"bold" ))
        stdroll_label.grid(row=1,column=2,padx=10,sticky=W)

        stdroll_entry=ttk.Entry(std_frame,width=20,textvariable=self.var_roll,font=("times new roman",11,"bold" ))
        stdroll_entry.grid(row=1,column=3,padx=2,pady=5,sticky=W)


        #gender
        stdgender_label=Label(std_frame,text="Gender:",font=("times new roman",11,"bold" ))
        stdgender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #stdgender_entry=ttk.Entry(std_frame,width=20,textvariable=self.var_gender,font=("times new roman",11,"bold" ))
        #stdgender_entry.grid(row=2,column=1,padx=2,pady=5,sticky=W)

        gender_combo=ttk.Combobox(std_frame,textvariable=self.var_gender,font=("times new roman",11,"bold" ),state="readonly",width=20)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)  

        #Dob
        stddob_label=Label(std_frame,text="Dob:",font=("times new roman",11,"bold" ))
        stddob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        stddob_entry=ttk.Entry(std_frame,width=20,textvariable=self.var_dob,font=("times new roman",11,"bold" ))
        stddob_entry.grid(row=2,column=3,padx=2,pady=5,sticky=W)

        #email
        stdmail_label=Label(std_frame,text="E-mail:",font=("times new roman",11,"bold" ))
        stdmail_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        stdmail_entry=ttk.Entry(std_frame,width=20,textvariable=self.var_email,font=("times new roman",11,"bold" ))
        stdmail_entry.grid(row=3,column=1,padx=2,pady=5,sticky=W)

        #phone no.
        stdph_label=Label(std_frame,text="Phone no.:",font=("times new roman",11,"bold" ))
        stdph_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        stdph_entry=ttk.Entry(std_frame,width=20,textvariable=self.var_phone,font=("times new roman",11,"bold" ))
        stdph_entry.grid(row=3,column=3,padx=2,pady=5,sticky=W)

        #Address
        stdadd_label=Label(std_frame,text="Address:",font=("times new roman",11,"bold" ))
        stdadd_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        stdadd_entry=ttk.Entry(std_frame,width=20,textvariable=self.var_address,font=("times new roman",11,"bold" ))
        stdadd_entry.grid(row=4,column=1,padx=2,pady=5,sticky=W)

        #teacher name
        teacher_label=Label(std_frame,text="Teacher Name:",font=("times new roman",11,"bold" ))
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(std_frame,width=20,textvariable=self.var_teacher,font=("times new roman",11,"bold" ))
        teacher_entry.grid(row=4,column=3,padx=2,pady=5,sticky=W)

        #buttons
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(std_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobutton1.grid(row=5,column=0)
        
        radiobutton2=ttk.Radiobutton(std_frame,variable=self.var_radio1,text="No Photo Sample",value="NO")
        radiobutton2.grid(row=5,column=1)

        #BUTTONS FRAME
        BTN_frame=LabelFrame(std_frame,bd=2,relief=RIDGE)
        BTN_frame.place(x=0,y=190,width=650,height=25)

        save_btn=Button(BTN_frame,text="SAVE",command=self.add_data,width=17,font=("times new roman",11,"bold" ),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(BTN_frame,text="UPDATE",command=self.update_data,width=17,font=("times new roman",11,"bold" ),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(BTN_frame,text="DELETE",command=self.delete_data,width=17,font=("times new roman",11,"bold" ),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(BTN_frame,text="RESET",command=self.reset_data,width=17,font=("times new roman",11,"bold" ),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #BUTTONS FRAME
        BTN_frame1=LabelFrame(std_frame,bd=2,relief=RIDGE)
        BTN_frame1.place(x=0,y=215,width=650,height=25)

        TAKE_PHOTO_btn=Button(BTN_frame1,command=self.generate_dataset,text="TAKE PHOTO SAMPLE",width=35,font=("times new roman",11,"bold" ),bg="blue",fg="white")
        TAKE_PHOTO_btn.grid(row=0,column=0)

        UPDATE_PHOTO_btn=Button(BTN_frame1,text="UPDATE PHOTO SAMPLE",width=35,font=("times new roman",11,"bold" ),bg="blue",fg="white")
        UPDATE_PHOTO_btn.grid(row=0,column=1)



        
        #right frame
        RIGHT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold" ))
        RIGHT_frame.place(x=670,y=5,width=660,height=500)
 
        img_right=Image.open(r"C:\Users\FO\Desktop\Attendance Monitering System\college_image\kv_04.jpg")
        img_right=img_right.resize((650,100),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(RIGHT_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=650,height=100)

        #search system
        search_frame=LabelFrame(RIGHT_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold" ))
        search_frame.place(x=0,y=105,width=650,height=70)

        srch_label=Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="black",fg="white")
        srch_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        srch_combo=ttk.Combobox(search_frame,font=("times new roman",11,"bold" ),state="readonly",width=15)
        srch_combo["values"]=("Select ","Roll No.","Phone No.")
        srch_combo.current(0)
        srch_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        srch_entry=ttk.Entry(search_frame,width=20,font=("times new roman",11,"bold" ))
        srch_entry.grid(row=0,column=2,padx=2,pady=5,sticky=W)          

        search_btn=Button(search_frame,text="SEARCH",width=10,font=("times new roman",11,"bold" ),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(search_frame,text="SHOW ALL",width=10,font=("times new roman",11,"bold" ),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)

        #table
        table_frame=Frame(RIGHT_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=0,y=175,width=650,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone no.","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")    
        self.student_table.heading("id",text=" StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone no.",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="photos")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100) 
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone no.",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #=========== function declaration ========

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
           messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                
                 conn = mysql.connector.connect(host="localhost",user="root",passwd="Isha@3002",database="attendance_system")
                 my_cursor = conn.cursor()
                 my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                self.var_dep.get(),
                                                self.var_course.get(),
                                                self.var_year.get(),
                                                self.var_semester.get(),
                                                self.var_std_id.get(),
                                                self.var_std_name.get(),
                                                self.var_div.get(),
                                                self.var_roll.get(),
                                                self.var_gender.get(),
                                                self.var_dob.get(),
                                                self.var_email.get(),
                                                self.var_phone.get(),
                                                self.var_address.get(),
                                                self.var_teacher.get(),
                                                self.var_radio1.get()
                                            ))
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                 messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)    
    

    #fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",passwd="Isha@3002",database="attendance_system")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
              self.student_table.delete(*self.student_table.get_children())
              for i in data:
                  self.student_table.insert("",END,values=i)
              conn.commit()
        conn.close()
    
    #get cursor
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
         
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
           messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Upadte","Do you want to update this student details",parent=self.root)
                if Upadate>0:
                    conn = mysql.connector.connect(host="localhost",user="root",passwd="Isha@3002",database="attendance_system")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (
                                                self.var_dep.get(),
                                                self.var_course.get(),
                                                self.var_year.get(),
                                                self.var_semester.get(),
                                                self.var_std_name.get(),
                                                self.var_div.get(),
                                                self.var_roll.get(),
                                                self.var_gender.get(),
                                                self.var_dob.get(),
                                                self.var_email.get(),
                                                self.var_phone.get(),
                                                self.var_address.get(),
                                                self.var_teacher.get(),
                                                self.var_radio1.get(),
                                                self.var_std_id.get()
                    ))
                else:
                    if not Upadate:
                        return  
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()   
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent =self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do yo want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",user="root",passwd="Isha@3002",database="attendance_system")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 
                conn.commit()   
                self.fetch_data()
                conn.close()  
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)      
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course") 
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")     
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #Take photo samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
           messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                    conn = mysql.connector.connect(host="localhost",user="root",passwd="Isha@3002",database="attendance_system")
                    my_cursor = conn.cursor()
                    my_cursor.execute("select * from student")
                    my_result = my_cursor.fetchall()
                    id=0
                    for x in my_result:
                        id+=1
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (
                                                self.var_dep.get(),
                                                self.var_course.get(),
                                                self.var_year.get(),
                                                self.var_semester.get(),
                                                self.var_std_name.get(),
                                                self.var_div.get(),
                                                self.var_roll.get(),
                                                self.var_gender.get(),
                                                self.var_dob.get(),
                                                self.var_email.get(),
                                                self.var_phone.get(),
                                                self.var_address.get(),
                                                self.var_teacher.get(),
                                                self.var_radio1.get(),
                                                self.var_std_id.get()==id+1
                    ))   
                    conn.commit() 
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    # Load predefined data on face frontals from opencv
                    
                    face_classifier = cv2.CascadeClassifier("C:\\Program Files\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
                        #scaling factor=1.3
                        #Minimum Neighbour=5

                        for(x,y,w,h) in faces:
                            face_cropped = img[y:y+h,x:x+w]
                            return face_cropped
                    cap=cv2.VideoCapture(0)
                    img_id = 0
                    while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face = cv2.resize(face_cropped(my_frame),(450,450))
                            face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)  
                            file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Cropped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()  
                    cv2.destroyAllWindows()  
                    
                    messagebox.showinfo("Result","Generating data sets completed!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)











if __name__ == "__main__":
   root=Tk()
   obj=Student(root)
   root.mainloop()