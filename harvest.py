############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_bestseller = is_bestseller
        self.is_seedless = is_seedless
        self.name =name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    musk = MelonType('musk',1998,'green',True,True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    casaba = MelonType('cas', 2003, 'orange', False , False, 'casaba') 
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', False, False, "Crenshaw")
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_water_melon= MelonType('yw',2013, "yelllow", False , True, 'Yellow Watermelon')
    yellow_water_melon.add_pairing('ice cream')
    all_melon_types.append(yellow_water_melon)

    print (len(all_melon_types))


    # Fill in the rest
    
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for type in melon_types:
        pairs = type.pairings
        print (f'{type.name} pairs with')
        for pair in pairs:
            print(f' -{pair}')
            
        
        
def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_dict = {}
    for melon_type in melon_types:
        melon_dict[melon_type.code] = melon_type.pairings
    print(melon_dict)
    return melon_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



melons = make_melon_types()
print_pairing_info(melons)
make_melon_type_lookup(melons)