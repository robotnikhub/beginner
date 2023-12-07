import customtkinter
# import qrcode
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=20,
#     border=4,
# )
# qr.add_data('Some data')
# qr.make(fit=True)

# img = qr.make_image(fill_color="black", back_color="white")
# img.save("test.png")

def button_callback():
    print("button pressed")

def hello(textbox):
    text = textbox.get("0.0", "end")

resolution_x = 250
resolution_y = 100
row_x = int(resolution_x/2)
column_y = int(resolution_y/2)

app = customtkinter.CTk()
app.title("generowanie kodu QR")
app.geometry(f'{resolution_x}x{resolution_y}')

app.grid_columnconfigure(0, weight=2)

textbox = customtkinter.CTkTextbox(app, width=resolution_x, height=50)
textbox.grid(row=1, column=2, padx=0, pady=0)
hello(textbox)

# hello(get_get)
button = customtkinter.CTkButton(app, text="Generuj kod QR", command=hello)
button.grid(row=2, column=2, padx=0, pady=0)
app.mainloop()
