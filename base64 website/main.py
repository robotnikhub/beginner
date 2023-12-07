'''
base 64 - kodowanie które jest uzywane do przesylania plików w internecie między serwerami
róznica między hashem a kodowaniem jest taka, ze w np. base 64 mozna odzyskac plik a w hash nie, 
hash działa na innej zasadzie niz kodowanie
'''

from flask import Flask, render_template, request, redirect
import base64
import os
from werkzeug.utils import secure_filename

upload_folder = "C:\\Users\\stahu\\Desktop\\oooo\\b64_website\\files"
app = Flask(__name__)
app.config['upload_folder'] = upload_folder


@app.route("/", methods = ["GET"])
def index1():
    return render_template("index.html")

@app.route("/", methods = ["POST"])
def index():
    file = request.files['file']
    print(file.filename)
    
    filename = secure_filename(file.filename)
    
    file.save(os.path.join(app.config['upload_folder'], filename))
    buf = b''
    with open(f'C:\\Users\\stahu\\Desktop\\oooo\\b64_website\\files\\{filename}', 'rb') as filee: # rb read bytes
        print(filee)
        for b in filee:
            buf += b
            print(b)
    f_b64 = base64.standard_b64encode(buf)
    print(f_b64)
    choose = input("czy chcesz zapisac plik w formie base64? ")
    if choose=="y":
        with open(f"C:\\Users\\stahu\\Desktop\\oooo\\b64_website\\files\\base64\\{filename}", "wb") as f:
            f.write(f_b64)
    else:
        pass
    choose2 = input("czy chcesz zapisac plik w normalnej formie? ")
    if choose2=="y":
        pass
    else:
        os.remove(f'C:\\Users\\stahu\\Desktop\\oooo\\b64_website\\files\\{filename}')
    return redirect('/')

@app.route("/wow", methods = ["GET"])
def index2():
    return render_template("look.html")

if __name__ == "__main__":
    app.run("127.0.0.1", "8080")

# przyciski zeby wygenerowalo hash i mozliwosc pobrania pliku