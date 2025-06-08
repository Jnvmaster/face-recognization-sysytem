from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from frame1 import Student  # Make sure the class is 'student'

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1930x1005+0+0")
        self.root.title("Face Recognition System")

        # First image
        img = Image.open(r"C:\Users\Admin\Downloads\pes.jpg")
        img = img.resize((643, 150), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        lbl = Label(self.root, image=self.photoimg)
        lbl.place(x=0, y=0, width=643, height=150)
        # Second image
        img1 = Image.open(r"C:\Users\Admin\Downloads\logo.jfif")
        img1 = img1.resize((643, 150), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl1 = Label(self.root, image=self.photoimg1)
        lbl1.place(x=643, y=0, width=633, height=150)

        # Third image
        img2 = Image.open(r"C:\Users\Admin\Downloads\pes.jpg")
        img2 = img2.resize((644, 150), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl2 = Label(self.root, image=self.photoimg2)
        lbl2.place(x=1280, y=0, width=644, height=150)

        # Background image
        img3 = Image.open(r"C:\Users\Admin\Downloads\face.jpg")
        img3 = img3.resize((1930, 1005), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg3 = Label(self.root, image=self.photoimg3)
        bg3.place(x=0, y=150, width=1930, height=1005)

        title_lbl = Label(bg3, text="FACE RECOGNITION ATTENDENCE SYSTEM", font=("time new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1930, height=45)

        # === Buttons ===

        # Student Button
        img4 = Image.open(r"C:\Users\Admin\Downloads\student2.jfif")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        self.btn_student_img = Button(bg3, image=self.photoimg4, command=self.student_details)
        self.btn_student_img.place(x=200, y=120, width=220, height=220)
        self.btn_student = Button(bg3, text="STUDENT DETAILS", command=self.student_details, font=("time new roman", 15, "bold"), bg="blue", fg="white")
        self.btn_student.place(x=200, y=300, width=220, height=40)

        # Admin Button
        img5 = Image.open(r"C:\Users\Admin\Downloads\admin2.jpg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        self.btn_admin_img = Button(bg3, image=self.photoimg5)
        self.btn_admin_img.place(x=600, y=120, width=220, height=220)
        self.btn_admin = Button(bg3, text="ADMIN", font=("time new roman", 15, "bold"), bg="blue", fg="white")
        self.btn_admin.place(x=600, y=300, width=220, height=40)

        # Face Detector
        img6 = Image.open(r"C:\Users\Admin\Downloads\face detector.jpg")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        self.btn_face_img = Button(bg3, image=self.photoimg6)
        self.btn_face_img.place(x=1000, y=120, width=220, height=220)
        self.btn_face = Button(bg3, text="FACE DETECTOR", font=("time new roman", 15, "bold"), bg="blue", fg="white")
        self.btn_face.place(x=1000, y=300, width=220, height=40)

        # Attendance
        img7 = Image.open(r"C:\Users\Admin\Downloads\attendence.png")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        self.btn_attend_img = Button(bg3, image=self.photoimg7)
        self.btn_attend_img.place(x=1400, y=120, width=220, height=220)
        self.btn_attend = Button(bg3, text="ATTENDANCE", font=("time new roman", 15, "bold"), bg="blue", fg="white")
        self.btn_attend.place(x=1400, y=300, width=220, height=40)

        # Train Data
        img8 = Image.open(r"C:\Users\Admin\Downloads\traindata.jpg")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        self.btn_train_img = Button(bg3, image=self.photoimg8)
        self.btn_train_img.place(x=200, y=500, width=220, height=220)
        self.btn_train = Button(bg3, text="TRAIN DATA", font=("time new roman", 15, "bold"), bg="blue", fg="white")
        self.btn_train.place(x=200, y=680, width=220, height=40)

        # Photos
        img9 = Image.open(r"C:\Users\Admin\Downloads\photos.jpg")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        self.btn_photos_img = Button(bg3, image=self.photoimg9)
        self.btn_photos_img.place(x=600, y=500, width=220, height=220)
        self.btn_photos = Button(bg3, text="PHOTOS", font=("time new roman", 15, "bold"), bg="blue", fg="white")
        self.btn_photos.place(x=600, y=680, width=220, height=40)

        # Help Desk
        img10 = Image.open(r"C:\Users\Admin\Downloads\help desk.jpg")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        self.btn_help_img = Button(bg3, image=self.photoimg10)
        self.btn_help_img.place(x=1000, y=500, width=220, height=220)
        self.btn_help = Button(bg3, text="HELP DESK", font=("time new roman", 15, "bold"), bg="blue", fg="white")
        self.btn_help.place(x=1000, y=680, width=220, height=40)

        # Exit
        img11 = Image.open(r"C:\Users\Admin\Downloads\exit.jpg")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        self.btn_exit_img = Button(bg3, image=self.photoimg11, command=self.exit_system)
        self.btn_exit_img.place(x=1400, y=500, width=220, height=220)
        self.btn_exit = Button(bg3, text="EXIT", command=self.exit_system, font=("time new roman", 15, "bold"), bg="blue", fg="white")
        self.btn_exit.place(x=1400, y=680, width=220, height=40)

    # === Methods ===

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def exit_system(self):
        self.root.destroy()

# === Main ===
if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
