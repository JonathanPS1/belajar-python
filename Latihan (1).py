#-------------------------------------------------------------------------------
#
# NAMA   : Jonathan Putra Satria
# NIM    : 672021179
#
#-------------------------------------------------------------------------------

def main():
    fruitTuple = ('mango', 'apple', 'orange', 'watermelon', 'grape')
    priceTuple = (13000, 9000, 8000, 9000, 16000)

    #Soal1
    fruitDict = {'mango': 13000, 'apple': 9000, 'orange': 8000, 'watermelon': 9000, 'grape': 16000}
    print("Soal 1 :", fruitDict)

    #Soal2
    totalHarga = 0
    for harga in fruitDict.values():
        totalHarga += harga

    jumlahBuah = len(fruitDict)
    rataHarga = totalHarga / jumlahBuah

    print("Soal 2 : Rata-rata harga buah adalah", rataHarga)

    #Soal3
    test_list = [4, 1, {'tiga': 3, 'tujuh': 7}, (9, 8, [2, 5]), 6]
    arrayKosong = []

    for angka in test_list:
        if isinstance(angka, int):
            arrayKosong.append(angka)
        elif isinstance(angka, dict):
            arrayKosong.extend(angka.values())
        elif isinstance(angka, tuple):
            for nestAngka in angka:
                if isinstance(nestAngka, int):
                    arrayKosong.append(nestAngka)
                elif isinstance(nestAngka, list):
                    arrayKosong.extend(nestAngka)

    hasilSorting = ' '.join(map(str, sorted(arrayKosong)))
    print("Soal 3 :", hasilSorting)

    #Soal4
    strProdi = "teknik informatika fakultas teknologi informasi universitas kristen satya wacana "
    listMahasiswa = ['DEVA', 'ABI', 'IVAN']
    dictKelas = {'IF001': 'Kapita Selekta', 'IF002': 'Matematika Diskrit', 'IF003': 'Pemrograman Web'}

    string1 = (f'Hari ini {listMahasiswa[0].title()} tidak mengikuti mata kuliah {dictKelas["IF001"]}')
    string2 = (f'{dictKelas["IF002"]} {list(dictKelas.keys())[2]} adalah salah satu mata kuliah di progdi {strProdi.title()}')

    print('Soal 4 :',string1)
    print('\t\t',string2)

    #Soal5
    listNum = [3, 11, 7, 9, 1, 13, 5, 2, 8, 14, 10, 12, 4, 6, 15]

    jumlahAngka = len(listNum)

    for i in range(jumlahAngka):
        for j in range(0, jumlahAngka-i-1):
            if listNum[j] > listNum[j+1]:
                listNum[j], listNum[j+1] = listNum[j+1], listNum[j]

    print("Soal 5 :", listNum)

if __name__ == '__main__':
    main()
