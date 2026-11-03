# physics formulas

def calc_velocity(distance, time):
    # v = d/t
    return distance/time

def force(m, a):
    return m*a

def kineticEnergy(mass, velocity):
    # 1/2 m v^2
    return 0.5 * mass * (velocity * velocity)

def potentialEnergy(m, h):
    g = 9.81 # gravity
    return m * g * h

def energy(m):
    # e = mc^2
    c = 299792458
    return m * c * c

print("testing force:")
print(force(10, 9.81))
