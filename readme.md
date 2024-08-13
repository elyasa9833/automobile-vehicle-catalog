## Tugas ini tentang membuat sebuah dealer mobil yang hanya menyajikan informasi katalog tentang kendaraan yang di dalam dealer

### Berikut adalah persyaratan tiap uraian kendaraan:
1. Kamu harus membuat merk mobil sebagai sebuah class
2. Dalam tiap merk mobil akan memiliki setidaknya 1 model dari merk tersebut dan harus disetel sebagai peranakan dari class merk mobil yang dipilih atau inheritance dari class merk mobil yang dipilih
3. Dalam tiap model merk mobil wajib memiliki 2 variabel global yang menyimpan informasi deskripsi model dan harga model tersebut
4. Dalam tiap model merk mobil wajib memiliki 2 method yang menyimpan informasi tentang spesifikasi dan fitur
5. Informasi tentang spesifikasi kendaraan harus mengembalikan nilai suatu Class yang terabstraksi atau dipasang interface agar definisi class spesifikasi tetap sama untuk seluruh kendaraan, dan wajib memiliki 1 method bernama `serialize` yang mengembalikan nilai dictionary, method ini digunakan untuk menyimpulkan seluruh nilai method dalam class spesifikasi ke dalam bentuk objek
6. Informasi tentang spesifikasi kendaraan adalah:
  - engine (ex. 3000 cc)
  - gas (ex. Petrol/Diesel)
  - power (ex. 300 hp)
  - transmission (ex. Automatic/Manual)
7. Informasi tentang fitur kendaraan juga harus mengembalikan nilai suatu Class yang terabstraksi atau dipasang interface agar definisi class fitur bisa digunakan Kembali dan memiliki aturan yang sama, dan juga wajib memiliki method `serialize` yang mengembalikan nilai dictionary dan menyimpulkan seluruh nilai pada method di class fitur tersebut
8. Informasi tentang fitur kendaraan adalah:
  - power outlet (ex. False)
  - cruise control (ex. True)
  - keyless (ex. True)
  - airbag (ex. True)
  - sunroof (ex. False)


### Setelah membuat setidaknya 2 merk mobil dan 1 model tiap merk, Langkah selanjutnya adalah membuat class Dealer.

Class Dealer ini digunakan sebagai kelas Utama setelah mengambil argument dari pengguna, class ini harus memiliki 3 method, diantaranya:
  - Show All Cars
  - Show All Car Models (only for 1 brand)
  - Show Car Model Detail (for 1 brand and 1 model)

### Ketentuan Dealer:
1. Class Dealer harus menerima 2 inputan pengguna yaitu merk dan model
2. Class Dealer harus memiliki pengecekan apabila merk atau model yang ditulis tidak ada
3. Method All Cars diperbolehkan print out seluruh merk dan model atau mengembalikan nilai untuk ditampilkan di file main.py
4. Method Show All Car Models tidak diperbolehkan print out hasil yang diminta, wajib mengembalikan nilai yang diminta karena print out harus dilakukan di fungsi main.py
5. Method Show Car Model Detail tidak diperbolehkan print out hasil yang diminta, wajib mengembalikan nilai yang diminta ke dalam bentuk Class yang terabstraksi atau dipasang interface agar definisi output dari method ini selalu sama dan dapat dipakai kembali


### Setelah 2 bisnis proses berhasil dibuat, Langkah terakhir adalah membangun file main.py

File Utama atau main.py harus berupa argument parser dari python, karena program ini akan dijalankan lewat terminal dan membaca input argument dari user. Parser pada file main.py harus memiliki 3 argument, diantaranya: 
1. Meminta menampilkan semua merk dan modelnya
2. Meminta menampilkan semua model mobil dari merk yang dipilih
3. Meminta menampilkan informasi detail dari merk dan model mobil yang dipilih, seperti deskripsi, Harga, spesifikasi dan fitur.


Referensi untuk mengambil data data kendaraan bisa diambil dari website https://www.oto.com