class BioData:
  def __init__(self, nama, kelas, umur, agama):
    self.nama = nama
    self.kelas = kelas
    self.umur = umur
    self.agama = agama
   
   def printNama(self):
    print("Nama anda: {self.nama}")
    
   def printKelas(self):
    print("Kelas anda: {kelas}")

   def printumur(self):
    print("Umur anda: {umur}")

   def printagama(self):
    print("Agama anda: {agama}")
   
Ahmad = BioData("Ahmad Borat", "12 IPA 1", "18 Tahun", "Islam")
Ahmad.printNama()
Ahmad.printKelas
