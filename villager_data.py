"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
  """
    species = set()

    data = open(filename)
    for line in data: 
        value = line.rstrip().split("|")[1]
        species.add(value)
    return species

def get_villagers_by_species(filename, species="All"):
    """Return a list of villagers' names by species.

    Arguments:
      - filename (str): the path to a data file
      - species (str): optional, the name of a species

    Return:
      - list[list]: a list of lists
    """

    villagers = []
    
    data = open(filename)
    for line in data: 
      name, species = line.rstrip().split('|')[0:2]
      
      if "All" in species:
        villagers.append(name)

    return sorted(villagers)

def all_names_by_hobby(filename):
    """Return a list that villagers' names, grouped by hobby.

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    # TODO: replace this with your code
    fitness = []
    nature = []
    education =[]
    music = []
    fashion = []
    play = []

    data= open(filename)
    for line in data: 
      name = line.rstrip().split("|")[0]
      hobby = line.rstrip().split("|")[3]
      if hobby == "Fitness":
        fitness.append(name)
      elif hobby == "Nature":
        nature.append(name)
      elif hobby == "Education":
        education.append(name)
      elif hobby == "Music":
        music.append(name)
      elif hobby == "Fashion":
        fashion.append(name)
      elif hobby == "Play":
        play.append(name)
    return [fitness, nature, education, music, fashion, play]

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []
    data = open(filename)
    for line in data: 
      all_data.append(tuple(line.rstrip().split("|")))
    return all_data

def find_motto(filename, name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """
    data = open(filename)
    for line in data:
      villager_name = line.rstrip().split('|')[0]
      motto = line.rstrip().split('|')[-1]
      if name == villager_name:
        return motto
    
            
def find_likeminded_villagers(filename, name):
    """Return a set of villagers with the same personality as the given villager."""

    # TODO: replace this with your code
    likeminded = set()
    data = open(filename)
    search_personality = None

    for line in data: 
      villager_name = line.rstrip().split('|')[0]
      if villager_name == name: 
        search_personality = line.rstrip().split('|')[2]
        break
    for line in data:
      villager_name = line.rstrip().split('|')[0]
      personality = line.rstrip().split('|')[2]
      if personality == search_personality:
          likeminded.add(villager_name)
        
    return likeminded
print(find_likeminded_villagers("villagers.csv", "Curt"))
