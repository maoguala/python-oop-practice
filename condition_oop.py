class Game:
    def __init__(self, round, p1_WTimes, p2_WTimes, player1, player2): # definite  
        self.__round = round 
        self.__p1_WTimes = p1_WTimes
        self.__p2_WTimes = p2_WTimes
        self.__player1 = player1
        self.__player2 = player2

    @property 
    def round(self):
        return self.__round 

    @round.setter
    def round(self, x):
        self.__round = x
    
    @property 
    def p1_WTimes(self):
        return self.__p1_WTimes 
    
    @p1_WTimes.setter
    def  p1_WTimes(self, x):
        self.__p1_WTimes = x

    @property 
    def p2_WTimes(self):
        return self.__p2_WTimes 
    
    @p2_WTimes.setter
    def  p2_WTimes(self, x):
        self.__p2_WTimes = x

    @property
    def player1(self):
        return self.__player1
    @player1.setter
    def player1(self, x):
        self.__player1 = x

    @property
    def player2(self):
        return self.__player2
    @player2.setter
    def player2(self, x):
        self.__player2 = x

    def check_winner(self):
        if self.__player1 > self.__player2:
            self.__p1_WTimes += 1
            return "Player 1 Wins"
        elif self.__player1 < self.__player2:
            self.__p2_WTimes += 1
            return "Player 2 Wins"
        else:
            return "Tie"
        
    def final_winner(self):
        if self.p1_WTimes == 3:
            print("\n\n GameOver!! Is player1 winning!\n\n")
            return True
        elif self.p2_WTimes == 3:
            print("\n\n GameOver!! Is player2 winning!\n\n")
            return True
        return False
    def __str__(self):
        return (
            f"Round(s): {self.__round}\n"
            f"Player1 winning times: {self.__p1_WTimes}\n"
            f"Player2 winning times: {self.__p2_WTimes}\n"
            f"Player1 current round input: {self.__player1}\n"
            f"Player2 current round input: {self.__player2}\n"
        )

start_round = 1
player1_winning = 0
player2_winning = 0

while True:
    p1 = int(input("Enter the player1's value: "))
    p2 = int(input("Enter the player2's value: "))

    print("\n")
    
    data = Game(start_round, player1_winning, player2_winning,p1,p2)
 
    result = data.check_winner()

    player1_winning = data.p1_WTimes
    player2_winning = data.p2_WTimes

    print(f"Round Result: {result}\n")
    print("\n\nNext Round...\n\n")

    print(data)

    GamEnd = data.final_winner()

    if GamEnd:
        break

    start_round += 1