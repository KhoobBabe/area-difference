
def show_difference(l, w):
    def areas_calc(l, w):
        
        a_o_e = 3.14159 * (l/2) * (w/2)         #area of ellipse
        
        rad = (((l/2)**2) + ((w/2)**2))**0.5
    
        a_o_c = 3.14159 * (rad**2)              #area of circle
        areas_diff = a_o_c - a_o_e
        print("the difference in areas is", areas_diff)


    areas_calc(l, w)                    
   

l = int(input("Enter the length: "))
w = int(input("Enter the width: "))

show_difference(l, w)

