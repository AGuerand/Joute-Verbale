class Role:
    def __init__(self,role):
        self.role = role
        if role == "The cool dude":
            self.weakness = "Money"
            self.point = 0
        if role == "The rich dude":
            self.weakness = "Action"
            self.point = 100
        if role == "The granny":
            self.weakness = "Style"
            self.point = 0
        if role == "The Nice guy":
            self.weakness = "Family"
            self.point = 0
        if role == "Jeff":
            self.weakness = "no"
            self.point = -500

    def __str__(self):
        return self.role