initial_position =float (input ("Please give me the initial position xº in metre"))
initial_velocity =float (input("Give me the initial velocity vº in metre per second"))
initial_time =float(input("Give me the time in second at which your object stops the movement"))

def final_position (initial_position, initial_velocity,initial_time):
    position= initial_position + initial_velocity*initial_time
    return position
print ("The result of the final position based on your values is:", final_position (initial_position, initial_velocity,initial_time))

final_pos = final_position(initial_position, initial_velocity, initial_time)

def formula_velocity (initial_position,final_pos,initial_time):
    velocity= (final_pos-initial_position)/initial_time 
    return velocity
print ("Also, given those values I have calculated the final velocity, which is:", formula_velocity (initial_position,final_pos,initial_time))

velocityy=formula_velocity (initial_position,final_pos,initial_time)
       
       

def formula_acceleration (initial_velocity,initial_time,velocityy):
    acceleration= (velocityy-initial_velocity)/initial_time
    return acceleration
print ("And of course, I have calculated the acceleration, which is:",formula_acceleration (initial_velocity,initial_time,velocityy))





