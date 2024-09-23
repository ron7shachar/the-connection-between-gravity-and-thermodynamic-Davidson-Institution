from visual import *
from visual.graph import *


################# Change  ##################### 
g=6                                          # gravity
p=3                                           # viscosity
###############  CONSTANTS  ###################
m=1                  
n = 300                                       # Number of disks representing the MUMAS                                         # Mass of disks
L = vector(80,80,0)                                      # Dimensions of the table
R = 0.6                                       # Disk radius
c1=30                                      # Force magnitude of disk-ball interaction                                       # Initial velocities
dt = 0.01                                   # Time step

###############  SYSTEM CREATION   ############

table = box(size = (L.x,L.y,0), opacity = 0.2)    # Table

#____________________  Graph _________________#

gdisplay(x=430, y=0, width=430, height=450, xtitle='x', ytitle='N')
density_x = ghistogram(bins=arange(0,L.y,L.y/20))

#_______________  Disks List   _______________#

disks = []                                    # Define "disks" as list variable  
i=0
while i < n:                                  # Creating the list: "disks" with n MUMAS disks distributed randomely on the table
    onedisk = cylinder(pos = (random.uniform(-L.x/2+R,L.x/2-R),random.uniform(-L.y/2+R,L.y/2-R),0), radius = 2*R, axis = (0,0,0.5), color=color.magenta)
    disks.append(onedisk)
    i = i + 1


    #______________  Velocities List   ___________#

v = []                                        # Define "v" as list variable 
i=0
while i <n:                                   # Creating the velocities list with n random initial velocity vectors in the range [-vo,v0]
    velocity = vector(0,0,0)
    v.append(velocity)
    i = i + 1
c = []                                        # Define "v" as list variable 
i=0
while i <n:                                   # Creating the velocities list with n random initial velocity vectors in the range [-vo,v0]
    velocity1 = random.uniform(1,c1)
    c.append(velocity1)
    i = i + 1



    #_____ Density - Position Monitor List  ______#

q=0
positions=[]
while q < n:            
    positions.append(0)
    q = q + 1 

    ###############  TIME EVOLUTION  ##############

t = 0
while t < 50:
    rate(100)

    counter = 0                               # Reset Density-time monitor variable

    i = 0
    while i < n:
            

            #_________ Disk - Wall Collisions _____#

        if disks[i].pos.y - R < -L.y/2:ff=vector(0,1000,0)
        else:ff=vector(0,0,0)
            

            #______________ Dynamics _____________#
        ad=p*-v[i]*c[i]
        F_net =     ad+m*vector(0,-g,0)+ff            # Net force 
        v[i] = v[i] + (F_net)*dt                        # Calculate the velocity of each disk 
        disks[i].pos = disks[i].pos + v[i]*dt             # Calculate the position of each disk 

            #______________ Monitors _____________#
            
            
        positions[i] = disks[i].pos.y+L.y/2                 # Density - position monitor
        i=i+1
        #________ Graph _________#
            
    density_x.plot(data = (positions))  
        
        
    t = t + dt



   
