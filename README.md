# Tugas Kecil 2 Strategi Algoritma: Decrease and Conquer
Program melakukan topological sorting dengan menerapkan algoritma decrease and conquer. Pada program terdapat prosedur rekursif yang berisi:
1. Jika terdapat simpul yang semua sisinya mengarah keluar (terdapat matkul yang prerequisite-nya berjumlah 0), maka simpul tersebut dihapus dan dimasukkan ke dalam array solusi (matkul dimasukkan ke dalam array semester)
2. Semua sisi dari setiap simpul yang memiliki sisi menuju simpul yang terhapus (matkul yang salah satu prerequisite-nya adalah matkul yang terhapus) akan dihapus
3. Prosedur akan dipanggil kembali dengan setiap pemanggilan prosedur akan mengubah jumlah semester untuk menentukan matkul-matkul yang diambil pada setiap semester. Prosedur akan terus dipanggil sampai array solusi sudah melebihi batas (jumlah semester mencapai 8) atau tidak ada simpul yang tersisa (seluruh matkul sudah dimasukkan ke dalam array solusi)  

## Requirements
Python 3.7.4 or higher

## How to Use
1. Buka terminal dan pastikan directory sudah berada di folder "src"
2. Jalankan program bernama "13519085.py" dengan memasukkan input "python3 13519085.py"
3. Masukkan input nama file dalam bentuk txt (contoh: "test1.txt"). Nama file txt dapat dilihat pada folder "test"
4. Tunggu sampai program mengeluarkan output

## Author
Nizamixavier Rafif Lutvie
(13519085)
