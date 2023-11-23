class Besin():
    def __init__(self, ad, kalori, protein):
        self.ad = ad
        self.kalori = kalori
        self.protein = protein

    def goruntule(self):
        print("Besin Adı:", self.ad)
        print("Kalori:", self.kalori)
        print("Protein:", self.protein)

class Meyve(Besin):
    def __init__(self, ad, kalori, protein, vitamin):
        super().__init__(ad, kalori, protein)
        self.vitamin = vitamin

    def goruntule(self):
        super().goruntule()
        print("Vitamin:", self.vitamin)

m1 = Meyve("Elma", 52, 0.3, "C")
m1.goruntule()