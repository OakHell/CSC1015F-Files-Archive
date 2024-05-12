"""Abdul-Kader Jainoodien
27 March 2024
Extract information of a place from given raw input"""

def location(block):
    """Isolates the location that was backwards found between ' ' and ' '"""
    return block[block.find(" END")-1:block[6:].find(" ")+6:-1].title()


def temperature(block):
    """Isolates the pressure found between ' ' and '_', converts to a number"""
    return float(block[block.find(" ")+1:block.find("_")])


def y_coordinate(block):
    """Isolates the y coordinate found between ',' and ' '"""
    return block[block.find(",")+1:block[6:].find(" ")+6]


def x_coordinate(block):
    """Isolates the x coordinate found between ':' and ','"""
    return block[block.find(":")+1:block.find(",")]


def pressure(block):
    """Isolates the pressure found between '_' and ':', converts to a number"""
    return float(block[block.find("_")+1:block.find(":")])


def get_block(data):
    """Cleans raw data"""
    return data[data.find("BEGIN"):data.find("END")+3]


def main():
    """Main function that takes in thr raw data, and prints out the clean seperated data"""
    data = input('Enter the raw data:\n')
    block = get_block(data)
    print('Site information:')
    print('Location:', location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(temperature(block)))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))

if __name__=='__main__':
    main()
    