#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 03
# Problem 1
# 204111 Sec 002

import math

def main():
    # get surface area from user input
    surface_area = float(input("input surface area: "))
    # calculate radius from surface area
    radius = find_r_from_surface_area(surface_area)
    # use radius to caculate volume
    volume = sphere_volume(radius)
    # display volume
    print("volume = {0:.2f}".format(volume))

def find_r_from_surface_area(surface_area):
	return (surface_area/(4*math.pi))**0.5

#function to compute volume of sphere from radius
def sphere_volume(radius):
	return 4/3*math.pi*radius**3

if __name__ == '__main__':
    main()