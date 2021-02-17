class BioData:
  def __init__(self, nama, kelas, umur, agama):
    self.nama = nama
    self.kelas = kelas
    self.umur = umur
    self.agama = agama
   
   def printNama(self):
    print(F"Nama anda: {self.nama}")
    
   def printKelas(kelas):
    print(F"Kelas anda: {kelas}")

 def printKelas(umur):
    print(f"Umur anda: {umur}")

 def printKelas(Agama):
    print(f"Kelas anda: {agama}")
   
Ahmad = BioData("Ahmad Borat", "12 IPA 1", "18 Tahun", "Islam")
Ahmad.printNama()
Ahmad.printKelas
