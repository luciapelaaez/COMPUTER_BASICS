mass =float(input ("Give me the mass: "))
velocity =float(input ("Give me the velocity so I can calculate the kynetic energy:"))
def formula (mass,velocity):
    resultado= 0.5 * mass * velocity ** 2
    return resultado
print ("The result is: ", formula (mass,velocity))
