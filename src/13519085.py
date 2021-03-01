def ambilKuliah(katastorage,semester,prequisite,currsem):
    # selama masih terdapat matkul yang dapat diambil dan semester tidak lebih dari 8
    if(len(katastorage) != 0 and currsem <= 8): 
        i = 0
        while(i<len(katastorage)):
            # menghapus semua matkul yang tidak punya prequisite dari daftar matkul dan menambahkannya di array semester
            if(prequisite[i] == 0): 
                semester[currsem-1].append(katastorage[i][0])
                katastorage.pop(i)
                prequisite.pop(i)
            else:
                i = i + 1
        # untuk setiap matkul di array semester,dihapus prequisite matkul yang mengandung matkul yang telah dihapus 
        for i in range(len(semester[currsem - 1])):
            for j in range(len(katastorage)):
                k = 0
                while(k<len(katastorage[j])):
                    if(semester[currsem - 1][i] == katastorage[j][k]):
                        katastorage[j].remove(semester[currsem -1][i])
                        prequisite[j] = prequisite[j] - 1
                        k = len(katastorage[j])
                    else:
                        k = k + 1
        # memanggil fungsi untuk menjalankan proses pengambilan matkul semester selanjutnya
        ambilKuliah(katastorage,semester,prequisite,currsem+1)
                

# katastorage sebagai tempat menyimpan daftar matkul beserta prequisitenya
katastorage = []
# semester sebagai tempat menyimpan matkul yang diambil per semester
semester = [[],[],[],[],[],[],[],[]]

# membaca masukan file
name = str(input("Masukkan nama file: "))
f = open("../test/" + name,"r")
for i in f:
    katastorage.append(i.rstrip().replace(' ','').replace('.','').rsplit(","))

# prequisite sebagai jumlah prequisite yang diperlukan setiap matkul (default = -1)
prequisite = [-1 for i in range(len(katastorage))]
for i in range(len(katastorage)):
    prequisite[i] = len(katastorage[i]) - 1

# memanggil fungsi untuk menjalankan proses pengambilan matkul semester pertama
ambilKuliah(katastorage,semester,prequisite,1)

# menulis keluaran matkul yang diambil setiap semester
print("\n")
print("Jadwal Pengambilan Matkul")
print("--------------------------")
for i in range(len(semester)):
    if(len(semester[i]) != 0):
        print("Semester ",i+1,": ",end="")
        print(semester[i][0],end="")
        for j in range(1,len(semester[i])):
            print(",",semester[i][j],end="")
        print("")

