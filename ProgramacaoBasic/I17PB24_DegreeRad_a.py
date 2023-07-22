#################################################
#                   INPUT 17
#
# Programacao Basic 24
# BÚSSOLAS E RELÓGIOS
#
# Usage:
# > python I17PB24_DegreeRad_a.py
#
# v.3.027
# 20230719
#
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import math

# Convert degrees to radians
def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

# Convert radians to degrees
def radians_to_degrees(radians):
    degrees = radians * (180 / math.pi)
    return degrees

# main routine
def main():
    """ Main method """
    while True:
        option = input("Convert (1) Degree to Radian or (2) Radian to Degree? ")
        if option == "1":
            degree = input("Enter Degrees: ")
            print(f"{degree} Deg = {degrees_to_radians(float(degree)):.3f} Rad")
        elif option == "2":
            rad = input("Enter Radians: ")
            print(f"{rad} Rad = {radians_to_degrees(float(rad)):.3f} Deg")


# execute main
if __name__ == "__main__":
    main()