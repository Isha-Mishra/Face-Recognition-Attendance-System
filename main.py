from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x750+0+0")
        self.root.title("Attendance Monitoring System")

    
        
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
        img3=img3.resize((1400,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_image=Label(self.root,image=self.photoimg3)
        bg_image.place(x=0,y=130,width=1400,height=710)

        title_lbl=Label(bg_image,text="ATTENDANCE MONITORING SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        #student button
        img4=Image.open(r"C:\Users\FO\Desktop\Attendance Monitering System\college_image\electronics-500x500.jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_image,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=100,width=200,height=200)

        b1_1=Button(bg_image,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=150,y=200,width=200,height=40)


        #face detect button
        img5=Image.open(r"C:\Users\FO\Desktop\Attendance Monitering System\college_image\facedetect.png")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_image,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=450,y=100,width=200,height=200)

        b1_1=Button(bg_image,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=450,y=200,width=200,height=40)


        #Attendance button
        img6=Image.open(r"C:\Users\FO\Desktop\Attendance Monitering System\college_image\attendance.jpg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_image,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=750,y=100,width=200,height=200)

        b1_1=Button(bg_image,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=750,y=200,width=200,height=40)


        #help button
        img7=Image.open(r"C:\Users\FO\Desktop\Attendance Monitering System\college_image\help.jpg")
        img7=img7.resize((200,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_image,image=self.photoimg7,cursor="hand2")
        b1.place(x=1050,y=100,width=200,height=200)

        b1_1=Button(bg_image,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=1050,y=200,width=200,height=40)


        #train button
        img8=Image.open(r"C:\Users\FO\Desktop\Attendance Monitering System\college_image\machine-learning-icon-23.jpg")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_image,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=150,y=320,width=200,height=200)

        b1_1=Button(bg_image,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=150,y=420,width=200,height=40)


        #photos button
        img9=Image.open(r"C:\Users\FO\Desktop\Attendance Monitering System\college_image\nec_co_002.jpg")
        img9=img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_image,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=450,y=320,width=200,height=200)

        b1_1=Button(bg_image,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=450,y=420,width=200,height=40)


        #developer button
        img10=Image.open(r"C:\Users\FO\Desktop\Attendance Monitering System\college_image\pexels-photo-3184339.jpeg")
        img10=img10.resize((200,200),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_image,image=self.photoimg10,cursor="hand2")
        b1.place(x=750,y=320,width=200,height=200)

        b1_1=Button(bg_image,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=750,y=420,width=200,height=40)


        #exit button
        img11=Image.open(r"C:\Users\FO\Desktop\Attendance Monitering System\college_image\images (1).jpg")
        img11=img11.resize((200,200),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_image,image=self.photoimg11,cursor="hand2")
        b1.place(x=1050,y=320,width=200,height=200)

        b1_1=Button(bg_image,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=1050,y=420,width=200,height=40)

    def open_img(self):
        os.startfile("data")

        # =========== function button ============
 
    def student_details(self):
         self.new_window=Toplevel(self.root)
         self.app=Student(self.new_window)

    def train_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Train(self.new_window)
            
    def face_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Attendance(self.new_window)

 


        





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()        

        




