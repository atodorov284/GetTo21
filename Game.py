import math
import random
class GameSticks:
    def __init__(self, first_or_second):
        self.name = 'player'
        self.current_turn = 'ai' if first_or_second == 'second' else 'player'
        self.ai_first = True if self.current_turn=='ai' or self.current_turn == 'second' else False
        self.current_turn = 'ai' if self.ai_first else self.name
        self.sticks = 0
        self.limit = 21

    def Play(self,sticks, player):
        if(int(sticks) > 3):
            raise Exception("Sticks cannot be more than 3")
            return
        self.sticks += int(sticks)
        self.current_turn = self.name if self.current_turn == "ai" else "ai"

    def End(self):
        return False if self.sticks >= self.limit else True

    def Winner(self):
        return self.name if self.current_turn == "ai" else "ai"

    def ai(self):
        if(self.ai_first):
            self.ai_first = False
            return 1
        self.winning = [5,9,13,17, 21]
        if(self.sticks not in self.winning):
            for number in self.winning:
                if(self.sticks < number and number-self.sticks < 4):
                    return number-self.sticks
        return random.randint(1,3)