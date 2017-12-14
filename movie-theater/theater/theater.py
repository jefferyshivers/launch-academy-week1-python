class Theater:
  def __init__(self, seats):
    self._seats = seats
    self._patrons = 0

  def admit(self, num = 1):
    new_patrons_total = self._patrons + num
    if not new_patrons_total > self._seats:
      self._patrons = new_patrons_total
    else:
      print('Error: we do not have enough empty seats to fit this party!')

  def at_capacity(self):
    return self._seats == self._patrons

  def record_walk_outs(self, num = 1):
    new_patrons_total = self._patrons - num
    if new_patrons_total >= 0:
      self._patrons = new_patrons_total
    else:
      print('Error: there are not even this many patrons left in the theater!')

