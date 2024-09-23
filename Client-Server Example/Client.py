from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-data', methods=['POST'])
def sendData():
    nama = request.form.get('nama')
    nim = request.form.get('nim')
    alamat = request.form.get('alamat')

    form = {
        'nama': nama,
        'nim': nim,
        'alamat': alamat
    }
    kirim = requests.post('http://localhost:8081/send-data', data=form)
    return kirim.json()

if __name__ == '__main__':
    app.run(debug=True,port=8080)