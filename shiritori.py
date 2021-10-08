# class Shiritori:
#      words = []
#      game_over = False
     
#      def __init__(self,word):
#          self.words.append(word)
         
#      def print(self):
#          print(self.words)
    
#     def check_valid(word)
        
# a = Shiritori("Hello")
# a = Shiritori("Wow")
# a.print()
class Shiritori:
    def __init__(self):
        self.words = []
        self.game_over = False
    def play(self, word):
        if word not in self.words and self.game_over == False:
            if len(self.words) == 0 or word[0] == self.words[-1][-1]:
                self.words.append(word)
                return self.words
        self.game_over = True
        return 'game over'
    def restart(self):
        self.words = []
        self.game_over = False
        return 'Game Restarted'
    
game = Shiritori()
print(game.play('Pretty'))
print(game.play('yes'))
print(game.play('Tuxedo'))


        