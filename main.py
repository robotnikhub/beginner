'''
base 64 - kodowanie które jest uzywane do przesylania plików w internecie między serwerami
róznica między hashem a kodowaniem jest taka, ze w np. base 64 mozna odzyskac plik a w hash nie, 
hash działa na innej zasadzie niz kodowanie
'''

from flask import Flask, render_template, request, redirect
import base64

app = Flask(__name__)


@app.route("/", methods = ["GET"])
def index1():
    return render_template("index.html")

@app.route("/", methods = ["POST"])
def index():
    plik1 = request.form.get('plik')
    buf = b''
    with open(plik1, 'rb') as filee: # rb read bytes
        for b in filee:
            buf += b
            print(b)
    # f_b64 = base64.standard_b64encode(buf)
    # print(f_b64)
    print(plik1)
    return redirect('/wow')

@app.route("/wow", methods = ["GET"])
def index2():
    return render_template("index.html")


if __name__ == "__main__":
    app.run("127.0.0.1", "8080")

# przyciski zeby wygenerowalo hash i mozliwosc pobrania pliku