class CasillaDeVotacion:
  def __init__(self, identifier, country):
    self._identifier = identifier
    self._country = country
    self._region = None

  @property
  def region(self):
    return self._region

  @region.setter
  def region(self, region):
    if region in self._country:
      self._region = region
    else:
      raise ValueError(f'Region {region} is not in the list')


casilla = CasillaDeVotacion(123, ['Honduras', 'Morelos'])
print(casilla.region)
casilla.region = 'Honduras'
print(casilla.region)
