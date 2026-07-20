from vpython import *

# Constants
q = -1          # charge
m = 1           # mass

B = vector(0,0,1)   # magnetic field

dt = 0.01

# Particle
particle = sphere(
    pos=vector(2,0,0),
    radius=0.15,
    color=color.red,
    make_trail=True
)

# Initial velocity
v = vector(0,2,1)


# Magnetic field arrow
field = arrow(
    pos=vector(0,0,0),
    axis=vector(0,0,2),
    color=color.blue
)

# Show Information
info = label(
    pos=vector(0, 2, 0),
    text="",
    height= 15
)

while True:

    rate(100)

    # Lorentz force
    F = q * cross(v,B)

    # Acceleration
    a = F/m

    # Update velocity
    v += a*dt

    # Update position
    particle.pos += v*dt

    #Update Information
    info.text = (
    f"Velocity = {mag(v):.2f}\n"
    f"Force = {mag(F):.2f}\n"
    f"Kinetic Energy = {0.5*m*mag(v)**2:.2f}"
)
