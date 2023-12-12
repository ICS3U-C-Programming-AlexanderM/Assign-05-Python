#!/usr/bin/env python3
# Created by: Alex M
# Created on: Dec 6, 2023

# Creating a function called cube_area 
def cube_area(side):
    #assigning surface area formula 
    surface_area = 6*side**2
    return surface_area
#returning the value of surface area to function


def main():
    #inside def main, a do while loop so if you enter invalid input you dont have to run it again.  
    while True :
    #
        user_side  = input("Enter your side in cm  ")  # Get user input for the side 
        #try catch for the input 
        try :
            cube_side = float(user_side)
        except ValueError :
            print (f"{user_side} is not a valid input try again ")
        else:
            # check if user input is not a whole number  (below  0 )
            if cube_side < 0 :
                print (f"{cube_side} is an invalid input try again")
            else:
                surface_area = cube_area (cube_side)#assigning cube area to surface area and calling the function 
                #displaying the  output 
                print (f"The surface area of a cube with the side {cube_side}cm is {surface_area:.2f} cm^2 ")
                break # break statement 


if __name__ == "__main__":
    main()