 #First of all, assuming is free fall and ignoring air resistance, the only force acting on the object is gravity.
#I will start defining the variables.

time=float(input("Hi user, give me any time (in seconds) and I will tell you the position of the object at that instant."))
initial_position =float(input("Now give me (in meters) the value of the position from which the object falls"))
gravity=float(input("Finally, give me (in m/s^2) the value of gravity" ))
print ("Given this formula:y=y0-(g*t**2)/2, I will calculate the position of the object at the instant you have first gave me.")

#Since we have considered free fall, according to the formula y=y0+V0*t-(g*t**2)/2 , V0 is zero then the equation y=y0-(g*t**2)/2 remain

def formula (initial_position, gravity, time):
    position =initial_position-(gravity*time**2)/2
    return position

print ("The result is:", formula (initial_position, gravity, time),"meters.")         