import random
import sys

def generate_board():
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
  master_cube_list = [cube1, cube2, cube3, cube4,
                      cube5, cube6, cube7, cube8,
                      cube9, cube10, cube11, cube12,
                      cube13, cube14, cube15, cube16]

  return scramble_board(master_cube_list)

# take the cubes and scramble their order
def scramble_board(cube_list):
  cube_list = cube_list #arg is a list (mutable) so we have to create ref in scope
  scrambled_board = []
  remaining_cube_count = num_cubes = len(cube_list)
  for x in range(0, num_cubes):
    next_cube_idx = random.randint(0, remaining_cube_count-1)
    next_cube = cube_list.pop(next_cube_idx)
    scrambled_board.append(next_cube)
    remaining_cube_count-=1

  return scrambled_board

# print board to stdout
def print_board(board):
  row = ''
  cubes_picked = 0
  print '\r'
  for cube in board:
    cubes_picked += 1
    if len(row) == 0:
      row = cube.face()
    else:
      row = row + cube.face()

    if cubes_picked % 4 == 0:
      cubes_picked = 0
      print '\t' + row
      row = ''
  print '\r'

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

  playing = input[0] == 'y'

  if playing:
    player = Player("Chad")
    board = generate_board()
  while(playing):
    print_board(board)
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

  def face(self):
    letter = self.faces[self.chosen_face]
    if letter == 'Qu':
      return 'Qu '
    else:
      return letter + '  '

if __name__ == '__main__':
  main()

