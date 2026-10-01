username = str(input("masukkan Username : "))
password = str(input("masukkan Username : "))

if (username == "arfan" and password == "123"):

  saldo = 10000000000
  print("LOGIN BERHASIL")      
  print("------SELAMAT DATANG------")

while True :
  print("1.PEMBAYARAN")
  print("2. TRANSFER")
  print("3.TOP UP")
  transaksi = str(input("Pilih Transaksi : "))

  match transaksi :
    case "1" :
      print("-----Pilih Pembayaran------")
      print("1. Pulsa")
      print("2. PDAM")
      print("BPJS")
      pembayaran = str(input("Pilih Pembayaran : "))

      match pembayaran :
        case "1":
          pulsa = int(input("Jumlah Pembayaran Pulsa : "))
          print("Pembayaran Pulsa Sebesar :" +str(pulsa) + " Berhasil")
          sisasaldo = saldo - pulsa
          print("Sisa Saldo kamu : " + str(sisasaldo))

        case "2" :
          print("Halaman Transfer")
        case "3" :
          print("Halaman Transfer")
        case _:
          print("Transaksi Tidak Valid")
else:
  print("Login Gagal")
          