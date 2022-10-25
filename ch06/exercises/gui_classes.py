class Player:
  def_init_(self):
  self.player_num = 1
  self.is_large = True
  self.score = 0
  self.player_pos = (20, 10)

class Enemy:
  def_init_(self):
  self.color = 'brown'
  self.is_large = False
  self.active = True
  self.goomba_pos = (40, 0)

class Background:
  def_init_(self):
  self.color = 'blue'
  self.num_clouds = 2 
  self.num_hill = 1
  self.num_bush = 1
