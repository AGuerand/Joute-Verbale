class Insult:
    def __init__(self,types):
        self.type= types
        if types == "Money":
            self.insultFinal=[",you six piece chicken Mcnobody","and remember your poor bruh", ",by the way I just bought your company and you'r fired", ",you absolute cretin"]
            self.sujet=["you","your car", "your job", "your bank account"]
            self.adjectives=["redneck","french","villain","prisoner","broke"]
            self.starter=["should", "smells like", "act like", "you should know that","I hope that"]
            self.complement=["tomorow", "today", "street", "hospital", "this morning", "tonight", "in a fight", "your room", "in the kitchen"]
            self.liaisons=["so","if","almost","then","it","like","a", "you", "are", "and", "the", "is", "your"]
            self.verb=["is", "will be", "eating", "eat", "fight","walking","walk","sleeping","sleep","fall","falling","move","moving","playing"] 
        if types == "Family":
            self.insultFinal=[",you donut", ",you man child", ",hope a creeper blow up your house", ",and also your mother is a hamster and your father smell of elderberries"]
            self.sujet=["your dog", "you", "your cat", "your MOM", "your sister", "your brother", "your uncle", "your aunt", "your family", "your dad"]
            self.adjectives=["redneck","french","lonely","villain","bad","crazy","childish","clown"]
            self.starter=["should", "smells like", "act like", "you should know that","I hope that"]
            self.complement=["tomorow", "today", "street", "hospital", "this morning", "tonight", "in a fight", "your room", "in the kitchen"]
            self.liaisons=["so","if","almost","then","it","like","a", "you", "are", "and", "the", "is", "your"]
            self.verb=["is", "will be", "eating", "eat", "fight","walking","walk","sleeping","sleep","fall","falling","move","moving","playing"] 
        if types == "Style":
            self.insultFinal=["like a gta character", "you meth-head",  "with your yeeyee haricut", ",and in wich garbage can you found your cloth friendo"]
            self.sujet=["your hair", "your dog", "you", "your car", "your job", "your cat", "your hat", "your outfit", "your face", "your beard", "your house"]
            self.adjectives=["fat","ugly","redneck","french","'beautiful'","clown"]
            self.starter=["should", "smells like", "act like", "you should know that","I hope that"]
            self.complement=["tomorow", "today", "street", "hospital", "this morning", "tonight", "in a fight", "your room", "in the kitchen"]
            self.liaisons=["so","if","almost","then","it","like","a", "you", "are", "and", "the", "is", "your"]
            self.verb=["is", "will be", "eating", "eat", "fight","walking","walk","sleeping","sleep","fall","falling","move","moving","playing"] 
        if types == "Action":
            self.insultFinal=["hope you get hit by a truck an survive", "like a gta character", "you donut", "you precious stuck up child", "you absolute cretin", "hope you step on a lego"]
            self.sujet=[ "you", "your job", "your family", "your bank account"]
            self.adjectives=["sad","redneck","french","retarded","blind","dumb","stupid","lonely","villain","bad","crazy","childish","deppresed"]
            self.starter=["should", "smells like", "act like", "you should know that","I hope that"]
            self.complement=["tomorow", "today", "street", "hospital", "this morning", "tonight", "in a fight", "your room", "in the kitchen"]
            self.liaisons=["so","if","almost","then","it","like","a", "you", "are", "and", "the", "is", "your"]
            self.verb=["is", "will be", "eating", "eat", "fight","walking","walk","sleeping","sleep","fall","falling","move","moving","playing"] 
        if types == "no":
            self.starter=["should", "smells like", "act like", "you should know that","I hope that"]
            self.complement=["tomorow", "today", "street", "hospital", "this morning", "tonight", "in a fight", "your room", "in the kitchen"]
            self.liaisons=["so","if","almost","then","it","like","a", "you", "are", "and", "the", "is", "your"]
            self.verb=["is", "will be", "eating", "eat", "fight","walking","walk","sleeping","sleep","fall","falling","move","moving","playing"] 