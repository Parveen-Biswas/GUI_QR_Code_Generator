import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode

root = tk.Tk()
root.geometry("325x450+400+200")
root.title("QR_Code Generator")
root.resizable(False,False)
window_icon = ImageTk.PhotoImage(Image.open("logo.png"))
root.iconphoto(True, window_icon)
root.configure(bg="lightblue")

# Label for identify Box
data_enter = tk.Label(root, text="Enter your data", font=("Arial 10 bold"), bg="lightblue")
data_enter.place(x=25, y=20)
version_enter = tk.Label(root, text="Enter your version (Complexity)", font=("Arial 10 bold"), bg="lightblue")
version_enter.place(x=25, y=65)
box_size_enter = tk.Label(root, text="Enter your box size", font=("Arial 10 bold"), bg="lightblue")
box_size_enter.place(x=25, y=115)
box_color_enter = tk.Label(root, text="Enter your box color", font=("Arial 10 bold"), bg="lightblue")
box_color_enter.place(x=25, y=165)
bg_color_enter = tk.Label(root, text="Enter your background color", font=("Arial 10 bold"), bg="lightblue")
bg_color_enter.place(x=25, y=215)
file_name_enter = tk.Label(root, text="Enter File Name", font=("Arial 10 bold"), bg="lightblue")
file_name_enter.place(x=25, y=265)

# about owner
about_label = tk.Label(root, text="Ⓒ Copyright 2024 Made by Parveen Biswas", bg="lightblue", font=("Arial 10"))
about_label.place(x=30, y=420)


# Entry for data
e1 = tk.Entry(root, width=45, border=2)
e1.place(x=25, y=45)
e2 = tk.Entry(root, width=45, border=2)
e2.place(x=25, y=90)
e3 = tk.Entry(root, width=45, border=2)
e3.place(x=25, y=140)
e4 = tk.Entry(root, width=45, border=2)
e4.place(x=25, y=190)
e5 = tk.Entry(root, width=45, border=2)
e5.place(x=25, y=240)
e6 = tk.Entry(root, width=45, border=2)
e6.place(x=25, y=290)

# function logic
def save_pic(format):
    # print(f"{e1.get()}")
    t1=int(e2.get())
    t2=int(e3.get())

    generate_qrcode = qrcode.QRCode(
    version=t1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=t2,
    border=4,
    )

    generate_qrcode.add_data(f"{e1.get()}")
    generate_qrcode.make(fit=True)

    img = generate_qrcode.make_image(fill_color=(f"{e4.get()}"), back_color=(f"{e5.get()}"))
    img.save(f'{e6.get()}.{format}')
    messagebox.showinfo("Success!","File has been saved.")
    root.destroy()

save_file = tk.Button(root, text='Save QR Code', command=lambda: save_pic('png'), width=26, font=("Arial 12 bold"), fg="red", bg="white", activeforeground="white", activebackground="red", border=3)
save_file.place(x=28, y=330)

root.mainloop()