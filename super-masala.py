# class Obuna:
#     def __init__(self, foydalanuvchi, asosiy_narx):
#         self.foydalanuvchi = foydalanuvchi
#         self.asosiy_narx = asosiy_narx
#
#     def oylik_tolov(self):
#         """Oddiy tarif: hech qanday chegirmasiz."""
#         return self.asosiy_narx
#
#     def tavsif(self):
#         return f"Foydalanuvchi: {self.foydalanuvchi}, Tarif: Oddiy, Oylik to'lov: {self.oylik_tolov()} so'm"
#
#
# class TalabaObunasi(Obuna):
#     def __init__(self, foydalanuvchi, asosiy_narx, talaba_id):
#         super().__init__(foydalanuvchi, asosiy_narx)
#         self.talaba_id = talaba_id
#
#     def oylik_tolov(self):
#         """Talabalar uchun 30% chegirma."""
#         baza = super().oylik_tolov()
#         chegirma = baza * 0.30
#         return int(baza - chegirma)
#
#     def tavsif(self):
#         return (
#             f"Foydalanuvchi: {self.foydalanuvchi}, "
#             f"Tarif: Talaba, Talaba ID: {self.talaba_id}, "
#             f"Oylik to'lov: {self.oylik_tolov()} so'm"
#         )
#
#
# class OilaviyObuna(Obuna):
#     def __init__(self, foydalanuvchi, asosiy_narx, ekranlar_soni):
#         super().__init__(foydalanuvchi, asosiy_narx)
#         self.ekranlar_soni = ekranlar_soni
#
#     def oylik_tolov(self):
#         """
#         1 ta ekran – oddiy narx.
#         Har bir qo'shimcha ekran uchun +20% qo'shimcha to'lov.
#         """
#         baza = super().oylik_tolov()
#         if self.ekranlar_soni <= 1:
#             return baza
#         # (ekranlar_soni - 1) ta qo'shimcha ekran
#         koeff = 1 + 0.2 * (self.ekranlar_soni - 1)
#         return int(baza * koeff)
#
#     def tavsif(self):
#         return (
#             f"Foydalanuvchi: {self.foydalanuvchi}, "
#             f"Tarif: Oilaviy, Ekranlar: {self.ekranlar_soni}, "
#             f"Oylik to'lov: {self.oylik_tolov()} so'm"
#         )
#
#
# def umumiy_oylik(obunalar):
#     """Polimorfizm: har bir obuna turining o'z oylik_tolov() metodi chaqiriladi."""
#     jami = 0
#     for obuna in obunalar:
#         jami += obuna.oylik_tolov()
#     return jami
#
#
# if __name__ == "__main__":
#     o1 = Obuna("Ali", 100_000)
#     o2 = TalabaObunasi("Olim", 100_000, "T-001")
#     o3 = OilaviyObuna("Ibrohim", 100_000, 3)
#
#     print(o1.tavsif())
#     print(o2.tavsif())
#     print(o3.tavsif())
#
#     obunalar = [o1, o2, o3]
#     print("Umumiy oylik to'lov:", umumiy_oylik(obunalar))





























