import customtkinter
from PIL import Image
import qrcode
from tkinter import messagebox

def button_callback():
    print("button pressed")

def hello():
    text = textbox.get("0.0", "end").strip()
    if len(text) == 0:
        messagebox.showwarning(title="QR CODE ERROR [0X01]", message="No data was provided")
        raise Exception('No data was provided')
        
    print(text)
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("test.png")
    my_image = customtkinter.CTkImage(light_image=Image.open(".\\test.png"),
                                  dark_image=Image.open(".\\test.png"),
                                  size=(100, 100))
    image_label = customtkinter.CTkLabel(master=app, image=my_image, text="")  # display image with a CTkLabel 
    image_label.place(x=70, y=100)
    print(my_image)



resolution_x = 250
resolution_y = 220
row_x = int(resolution_x/2)
column_y = int(resolution_y/2)

app = customtkinter.CTk()
app.title("generowanie kodu QR")
app.geometry(f'{resolution_x}x{resolution_y}')
app.resizable(False, False)

textbox = customtkinter.CTkTextbox(master=app, width=resolution_x, height=50)
textbox.pack(anchor='s')

button = customtkinter.CTkButton(master=app, text="Generuj kod QR", command=hello)
button.pack(anchor='n')


app.mainloop()
