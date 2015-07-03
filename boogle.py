import random
import sys

class Board(object):
  def __init__(self):
    self.board = self.generate_board()
    self.board = self.scramble()

  def generate_board(self):
    # letter distribution matches official game
    cube1 = Cube(['A', 'A', 'C', 'I', 'O', 'T'])
    cube2 = Cube(['D', 'E', 'N', 'O', 'S', 'W'])
    cube3 = Cube(['A', 'B', 'I', 'L', 'T', 'Y'])
    cube4 = Cube(['D', 'K', 'N', 'O', 'T', 'U'])
    cube5 = Cube(['A', 'B', 'J', 'M', 'O', 'Qu'])
    cube6 = Cube(['E', 'E', 'F', 'H', 'I', 'Y'])
    cube7 = Cube(['A', 'C', 'D', 'E', 'M', 'P'])
    cube8 = Cube(['E', 'G', 'I', 'N', 'T', 'V'])
    cube9 = Cube(['A', 'C', 'E', 'L', 'S', 'R'])
    cube10 = Cube(['E', 'G', 'K', 'L', 'U', 'Y'])
    cube11 = Cube(['A', 'D', 'E', 'N', 'V', 'Z'])
    cube12 = Cube(['E', 'H', 'I', 'N', 'P', 'S'])
    cube13 = Cube(['A', 'H', 'M', 'O', 'R', 'S'])
    cube14 = Cube(['E', 'L', 'P', 'S', 'T', 'U'])
    cube15 = Cube(['B', 'F', 'I', 'O', 'R', 'X'])
    cube16 = Cube(['G', 'I', 'L', 'R', 'U', 'W'])

    # list of available cubes
    return [cube1, cube2, cube3, cube4,
            cube5, cube6, cube7, cube8,
            cube9, cube10, cube11, cube12,
            cube13, cube14, cube15, cube16]

  def scramble(self):
    cube_list = self.board #arg is a list (mutable) so we have to create ref in scope
    scrambled_board = []
    remaining_cube_count = num_cubes = len(cube_list)
    for idx in range(0,4):
      row = []
      for x in [0,1,2,3]:
        next_cube_idx = random.randint(0, remaining_cube_count-1)
        next_cube = cube_list.pop(next_cube_idx)
        row.append(next_cube)
        remaining_cube_count-=1
      scrambled_board.append(row)

    return scrambled_board

  def reduce_row(self, row):
    output = "\t"
    for cube in row:
      output += cube.face()
    output += "\r"
    return output

  def display(self):
    output = ''
    print '\r'
    for row in self.board:
      #output = "\t" + reduce(lambda carry,el: carry + el.face(), row) + "\r"
      print self.reduce_row(row)
    print output

  def reset_cubes(self):
    for cube in self.board:
      cube.deactivate()

#calculate score of word
def score_word(word):
  length = len(word)
  if length == 3 or length == 4:
    return 1
  elif length == 5:
    return 2
  elif length == 6:
    return 3
  elif length == 7:
    return 5
  elif length > 7:
    return 11

# make sure word is valid
def check_word(word, player):
  #make sure word is on the board
  #make sure word is in the dictionary
  if word in player.wordList:
    return False
  if len(word) < 3:
    print "Your word is too short. A minimum of 3 letters is required."
    return False
  if word == 'quit':
    return False

  return True

def main():
  input = None
  options = ['y','n']

  input = raw_input("Would you like to play a game? (y/n): ").strip()
  while(input not in options):
    print "you typed %s. Please type 'y' or 'n'" % input
    input = None
    input = raw_input("Would you like to play a game? (y/n): ").strip()

  playing = input.lower().startswith('y')

  if playing:
    #game setup
    player = Player("Chad")
    board = Board()
  while(playing):
    board.display()
    # would be nice to highlight the letter(s) typed to go along with the user
    # input, and only allow letters that are on the board
    # so if there are multiple 'E's, then they are all highlighted when 'e' is typed
    # and if the next letter is 's', then only highlight the places on the board
    # where E-S are neighbours.
    # Then, if followed by another 'e', highlight only the E-S-E pattern (if it
    # exists) else do not allow another 'e' to be entered.
    word = raw_input("Enter a word you want to score: ").strip()
    if check_word(word, player):
      player.add_word(word, score_word(word) )
    else:
      print "You've already scored that word. Try again.\n"

    if player.num_words() == 5:
      break
  if playing:
    player.print_score()

  exit_message()


def exit_message():
  print "Thanks for playing Boogle.\nBye."

class Player(object):
  def __init__(self, name):
    self.name = name
    self.score = 0
    self.wordList = set()

  def num_words(self):
    return len(self.wordList)

  def add_word(self, word, points):
    self.wordList.add(word)
    self.inc_score(points)
    print "%s is worth %d points" %(word, points)

  def inc_score(self, amount):
    self.score += amount

  def print_score(self):
    print "You got %d points for %d words.\n" % (self.score, self.num_words())
    print "The words you found were:"
    for word in self.wordList:
      print word
    print "\n"

class Cube(object):
  def __init__(self, faces):
    self.faces = faces
    self.chosen_face = random.randint(0,5)
    self.active = False

  def face(self):
    letter = self.faces[self.chosen_face]
    ACTIVE = '\033[92m'
    INACTIVE = '\033[91m'
    END = '\033[0m'
    if self.active:
      output = ACTIVE
    else:
      output = INACTIVE
    if letter == 'Qu':
      output += 'Qu '
    else:
      output += letter + '  '

    return output + END

  def activate(self):
    self.active = True

  def deactivate(self):
    self.active = False

if __name__ == '__main__':
  main()

