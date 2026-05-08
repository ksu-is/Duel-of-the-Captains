
class Enemy:
  def __init__(self, decision):
    self.decision = decision
    self.loaded = True
    self.bowsprit = True
    self.health = 100

  def enemy_turn(self):
    if self.decision == 1 and self.loaded == True:
      print("The enemy ship has fired their cannons!")
    if self.decision == 2 and self.loaded == True:
        print("The enemy blundered!")
    elif self.decision == 2 and self.loaded == False:
      print("The enemy ship has reloaded their cannons.")
      self.loaded = True
    if self.decision == 3 and self.bowsprit == True:
      print("The enemy has evaded your attack!")
    if self.decision == 4 and self.bowsprit == True:
      print("The enemy charged their ship at you!")

  
