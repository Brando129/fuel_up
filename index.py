"""A vehicle needs 10 times the amount of fuel than the distance it travels.
However, it must always carry a minimum of 100 fuel before setting off.
Create a function which calculates the amount of fuel it needs, given the distance"""

def fueling(distance):
    fuel = distance * 10
    if fuel < 100:
        print(int(fuel))
        return "We need more petrol!"
    else:
        print(int(fuel))
        return "We've got all the requirements for this drive!"

print(fueling(9))