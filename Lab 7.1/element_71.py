class Element(object):
    
    def __init__(prvek_object, number, name, symbol, boiling_point):
        prvek_object.number = number
        prvek_object.name = name
        prvek_object.symbol = symbol
        prvek_object.boiling_point = boiling_point
    
    def print_details(prvek_object):
        print('Number: {}'.format(prvek_object.number))
        print('Name: {}'.format(prvek_object.name))
        print('Symbol: {}'.format(prvek_object.symbol))
        print('Boiling point: {} K'.format(prvek_object.boiling_point))
        
def main():

    e1 = Element(1, 'Hydrogen', 'H', 20.3)
    e2 = Element(3, 'Lithium', 'Li', 1615)
    e3 = Element(11, 'Sodium', 'Na', 1156)
    e4 = Element(12, 'Magnesium', 'Mg', 1380)
    e5 = Element(79, 'Gold', 'Au', 3129)

    e1.print_details()
    e2.print_details()
    e3.print_details()
    e4.print_details()
    e5.print_details()

if __name__ == '__main__':
    main()
