class character:
    def __init__(self,role):
        self.role = role
        if role == "The nice dude":
            self.strenght = "style"
            self.weakness = "family"
            self.point = 0
        if role == "The rich dude":
            self.strenght = ""
            self.weakness = ""
            self.point = 100
        if role == "The granny"
            self.strenght = ""
            self.weakness = ""
            self.point = 0
        if role == "The npc"
            self.strenght = ""
            self.weakness = ""
            self.point = 0
        if role == "Jeff":
            self.strenght = "style"
            self.weakness = "family"
            self.point = 0

    def __str__(self):
        return self.role

    def Achat(self,liste_achat):
        self.achats.append(liste_achat)