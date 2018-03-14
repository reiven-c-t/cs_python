def chooseDice(self):
    choices = []
    while True:
        b = self.choose(["Die 1", "Die 2", "Die 3", "Die 4", "Die 5",

                         "Roll Dice", "Score"])

    if b[0] == "D":  # User clicked a die button
        i = eval(b[4]) - 1
        if i in choices:
            choices.remove(i)
            self.dice[i].setColor("black")
        else:
            choices.append(i)
            self.dice[i].setColor("gray")
    else:
        for d in self.dice:
            d.setColor("black")
        if b == "Score":
            return []
        elif choices != []:
            return choices
