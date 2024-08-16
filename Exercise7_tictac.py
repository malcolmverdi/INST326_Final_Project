from board import Board

#type() tells you what class an object belongs to

#isinstance() tells you whether an object is an instance of a particular class


class LoggingBoard(Board):

    def __init__(self):

        super().__init__()
        self.log = []

    def claim_square(self, player, index):

        super().claim_square(player, index)
        self.log.append(f"{player.name} selects square {index}")


    def get_winner(self):

        winner = super().get_winner()
        if winner != None:
            self.log.append(f"{winner.name} wins!")
        
        return winner


    def game_over(self):
        over = super().game_over()
        if over == True:
            print("/n".join(self.log))
        
        return over

