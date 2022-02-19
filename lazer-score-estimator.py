import argparse

class Score:
    maxScore = 1000000
    accuracyPortion = 0.3
    comboPortion = 0.7
    scoreMultipliers = {"HD": 1.06, "HR": 1.06, "DT": 1.12, "FL": 1.12, "NF": 0.5, "EZ": 0.5, "HT": 0.3}
    
    def __init__(self, maxCombo, accuracy = 100.0, combo = False, modString = False):
        self.scoreMultiplier = 1.0
        self.maxCombo = maxCombo
        self.accuracyRatio = accuracy / 100.0

        if(not combo):
            self.comboRatio = 1.0
        else:
            self.comboRatio = combo / maxCombo
        if(modString):
            self.modString = modString
            self.doMultiplier()

        self.calculateStandardized()
        self.calculateClassic()

    def doMultiplier(self):
        for mod in Score.scoreMultipliers:
            if mod in self.modString:
                self.scoreMultiplier *= Score.scoreMultipliers[mod]
    
    def calculateStandardized(self):
        self.standardizedScore = round((Score.maxScore * (Score.accuracyPortion * self.accuracyRatio + Score.comboPortion * self.comboRatio)) * self.scoreMultiplier)

    def calculateClassic(self):
        self.classicScore = round(18 * pow((self.standardizedScore / Score.maxScore) * (self.maxCombo + 1), 2))

class CommandLine:
    def __init__(self):
        parser = argparse.ArgumentParser(description = "Description for my parser")
        parser.add_argument("-M", "--MaxCombo", help = "(int) maximum combo of a beatmap.", required = False)
        parser.add_argument("-a", "--accuracy", help = "(float) accuracy of a given play.", required = False, default = 100.0)
        parser.add_argument("-c", "--combo", help = "(int) combo achieved in a given play.", required = False, default = False)
        parser.add_argument("-m", "--mods", help = "(str) string of mods, using two char shorthand.", required = False, default = False)
        
        argument = parser.parse_args()
        if(argument.MaxCombo is not None):
            play = Score(int(argument.MaxCombo), float(argument.accuracy), int(argument.combo), argument.mods)
            print("Standardized: {0:,}\nClassic: {1:,}".format(play.standardizedScore, play.classicScore))
        else:
            self.runApplication()

    def runApplication(self):
        maxCombo = int(input("Max Combo: "))
        accuracy = float(input("Accuracy: "))
        combo = int(input("Combo: "))
        modList = input("Mods: ")
        play = Score(maxCombo, accuracy, combo, modList)

if __name__ == '__main__':
    app = CommandLine()