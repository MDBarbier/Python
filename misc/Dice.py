from enum import Enum

class Hand:
    Rolls = []
    BestRank = null
    BestRankType1 = null
    BestRankType2 = null
    Kicker = null
    nines = 0
    tens = 0
    jacks = 0
    queens = 0
    kings = 0
    aces = 0

    def __init__(self, roll1, roll2, roll3, roll4, roll5):
        self.Rolls = self.Rolls + [roll1, roll2, roll3, roll4, roll5]
        self.Rolls.sort()
        self.BestRank = calculateBestRank()

    def calculateBestRank():

        for roll in rolls:
            if roll == 1:
                nines++
            elif roll == 2:
                tens++
            elif roll == 3:
                jacks++
            elif roll == 4:
                queens++
            elif roll == 5:
                kings++
            elif roll == 6:
                aces++

        #check 5 of a kind
        if aces == 5 or kings == 5 or queens == 5 or jacks == 5 or tens == 5 or nines == 5:
            BestRank = Ranks.FiveOfAKind
            if Rolls[0] == 6:
                BestRankType1 == Cards.Ace
            elif Rolls[0] == 5:
                BestRankType1 == Cards.King
            elif Rolls[0] == 4:
                BestRankType1 == Cards.Queen
            elif Rolls[0] == 3:
                BestRankType1 == Cards.Jack
            elif Rolls[0] == 2:
                BestRankType1 == Cards.Ten
            elif Rolls[0] == 1:
                BestRankType1 == Cards.Nine

        #check 4 of a kind
        if aces == 4:
            BestRank = Ranks.FourOfAKind
            BestRankType1 = Cards.Ace
            #find the other card
            for roll in rolls:
                if roll != 6:
                    if roll == 1:
                        Kicker = Cards.Nine
                    elif roll == 2:
                        Kicker = Cards.Ten
                    elif roll == 3:
                        Kicker = Cards.Jack
                    elif roll == 4:
                        Kicker = Cards.Queen
                    else roll == 5:
                        Kicker = Cards.King
        elif kings == 4:
            BestRank = Ranks.FourOfAKind
            BestRankType1 = Cards.King
            #find the other card
            for roll in rolls:
                if roll != 5:
                    if roll == 1:
                        Kicker = Cards.Nine
                    elif roll == 2:
                        Kicker = Cards.Ten
                    elif roll == 3:
                        Kicker = Cards.Jack
                    elif roll == 4:
                        Kicker = Cards.Queen
                    else roll == 6:
                        Kicker = Cards.Ace
        elif queens == 4:
            BestRank = Ranks.FourOfAKind
            BestRankType1 = Cards.Queen
            #find the other card
            for roll in rolls:
                if roll != 4:
                    if roll == 1:
                        Kicker = Cards.Nine
                    elif roll == 2:
                        Kicker = Cards.Ten
                    elif roll == 3:
                        Kicker = Cards.Jack
                    elif roll == 5:
                        Kicker = Cards.King
                    else roll == 6:
                        Kicker = Cards.Ace
        elif jacks == 4:
            BestRank = Ranks.FourOfAKind
            BestRankType1 = Cards.Jack
            #find the other card
            for roll in rolls:
                if roll != 3:
                    if roll == 1:
                        Kicker = Cards.Nine
                    elif roll == 2:
                        Kicker = Cards.Ten
                    elif roll == 4:
                        Kicker = Cards.Queen
                    elif roll == 5:
                        Kicker = Cards.King
                    else roll == 6:
                        Kicker = Cards.Ace
        elif tens == 4:
            BestRank = Ranks.FourOfAKind
            BestRankType1 = Cards.Ten
            #find the other card
            for roll in rolls:
                if roll != 2:
                    if roll == 1:
                        Kicker = Cards.Nine
                    elif roll == 3:
                        Kicker = Cards.Jack
                    elif roll == 4:
                        Kicker = Cards.Queen
                    elif roll == 5:
                        Kicker = Cards.King
                    else roll == 6:
                        Kicker = Cards.Ace
        elif nines == 4:
            BestRank = Ranks.FourOfAKind
            BestRankType1 = Cards.Nine
            #find the other card
            for roll in rolls:
                if roll != 1:
                    if roll == 2:
                        Kicker = Cards.Ten
                    elif roll == 3:
                        Kicker = Cards.Jack
                    elif roll == 4:
                        Kicker = Cards.Queen
                    elif roll == 5:
                        Kicker = Cards.King
                    else roll == 6:
                        Kicker = Cards.Ace

        #check full house
        if (aces == 3 or kings ==3 or queens == 3 or jacks == 3 or tens == 3 or nines == 3) and (aces == 2 or kings ==2 or queens == 2 or jacks == 2 or tens == 2 or nines == 2):
            
            BestRank = Ranks.FullHouse

            if aces == 3:
                BestRankType1 = Cards.Ace
            elif kings == 3:
                BestRankType1 = Cards.King
            elif queens == 3: 
                BestRankType1 = Cards.Queen
            elif jacks == 3:
                BestRankType1 = Cards.Jack
            elif tens == 3:
                BestRankType1 = Cards.Ten
            else
                BestRankType1 = Cards.Nine

            if aces == 2:
                BestRankType2 = Cards.Ace
            elif kings == 2:
                BestRankType2 = Cards.King
            elif queens == 2: 
                BestRankType2 = Cards.Queen
            elif jacks == 2:
                BestRankType2 = Cards.Jack
            elif tens == 2:
                BestRankType2 = Cards.Ten
            else
                BestRankType2 = Cards.Nine

        #check straight
        if aces == 1 and kings == 1 and queens == 1 and jacks == 1 and tens == 1 and nines == 1:
            BestRank = Ranks.Straight

        #check three of a kind


        #check two pair


        #check pair

    class Ranks(Enum):
        HighCard = 0
        Pair = 1
        TwoPair = 2
        ThreeOfAKind = 3
        FourOfAKind = 4
        FiveOfAKind = 5
        Straight = 6
        FullHouse = 7

    class Cards(Enum):
        Nine = 1
        Ten = 2
        Jack = 3
        Queen = 4
        King = 5
        Ace = 6
