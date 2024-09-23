from flask import Flask, request, jsonify

app = Flask(__name__)

data_list = []

@app.route('/send-data', methods=['POST'])
def sendData():
    nama = request.form.get('nama')
    nim = request.form.get('nim')
    alamat = request.form.get('alamat')

    new_data = {
        'nama': nama,
        'nim': nim,
        'alamat': alamat
    }

    data_list.append(new_data)
    return jsonify(new_data)

@app.route('/get-data', methods=['GET']) #untuk debug agar tau apakah data yang masuk sudah benar
def getData():
    return jsonify(data_list)

if __name__ == '__main__':
    app.run(debug=True, port=8081)
