from cs1media import *
from math import *

img = load_picture("C:\Users\jrk\Downloads/ra-men_collage.png")

def skew(img,direction,angle):
    width, height = img.size()
    if direction =="vertical":
        width_new = width + abs(int(tan(pi*int(angle)/180)*height))
        new_photo = create_picture(width_new, height)
        for j in range(height):
            for i in range(width):
                if angle>=0:
                    gap = int(tan(pi*angle/180)*(height-j))
                if angle<0:
                    gap = int(tan(pi*abs(angle)/180)*j)
                colour = img.get(i,j)
                new_photo.set(i+gap,j,colour)
    if direction =="horizontal":
        height_new = height + abs(int(tan(pi*int(angle)/180)*width))
        new_photo = create_picture(width,height_new)
        for i in range(width):
            for j in range(height):
                if angle>=0:
                    gap = int(tan(pi*angle/180)*(width-i))
                if angle<0:
                    gap = int(tan(pi*abs(angle)/180)*i)
                colour = img.get(i,j)
                new_photo.set(i,j+gap,colour)
                    
    return new_photo.show()
                
    

direction = raw_input("direction?")
angle = int(raw_input("angle?"))

skew(img,direction,angle)
