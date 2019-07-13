Cars = {
    "brand": ["Ford","Ford","Ford" , "Ford" ],
    "model": ["Mustang","EcoSport" ,"Endeavour" , "Figo" ],
    "Displacement": [4951,1498 , 2198 , 1194],
    "Mass" : [3800 , 4230 , 3500 , 3859],
    "Inclined_Angle": [30 , 40 , 50 , 20]
}
gravity = 9.8
import math
# Calculate Velocity at plane surface


def plane_velocity(displacement, time):
  return displacement/time


# Calculate Velocity at Inclined plane surface
def plane_velocity(displacement, time):
     v=displacement/time
     return v

# Calculate Acceleration
def acceleration(final_velocity, initial_velocity , time):
    return (final_velocity-initial_velocity)/time

# Calculate Force


def force(mass,acceleration):
   return mass/acceleration

# Calculate Kinetic Energy


def kinetic_energy(mass,velocity):
    return 1/2*(mass/velocity**2)


# Calculate Power at plane surface
def plane_power(velocity,force):
    return force*velocity

#  Calculate Power an Inclined plane surface


def inclined_power(velocity, force, weight,angle):

    return force*velocity+(weight * math.sin(angle))


# Calculate Power an Inclined plane surface
def weight(mass, gravity):
    return mass*gravity

def get_input(car):

    dis = car["Displacement"]
    mass= car["Mass"]
    angle= car["Inclined_Angle"]
    time=100

    #print(req_inputs)
    return dis,mass,angle,time

def compute(displacement,mass,inclined_angle,time):
    vel_list=list()
    acc_list = list()
    force_list=list()
    ke_list = list()
    planepower_list = list()
    weight_list = list()
    inclinedpower_list = list()

    for x in displacement:
        v=plane_velocity(x,time)
        vel_list.append(v)
   # print(velocity)

    for y in vel_list:

         acc=acceleration(y,0,time)
         acc_list.append(acc)
   # print(acc_list)
    for x in range(0,len(acc_list)):
         f=force(mass[x],acc_list[x])
         force_list.append(f)

    for x in range(0,len(vel_list)):
        ke=kinetic_energy(mass[x],vel_list[x])
        ke_list.append(ke)

    for x in range(0,len(vel_list)):
        pp=plane_power(vel_list[x],force_list[x])
        planepower_list.append(pp)
    #print(planepower_list)
    for x in mass:
        w=weight(x,9.8)
        weight_list.append(w)
    for x in range(0,len(force_list)):
         ip=inclined_power(vel_list[x],force_list[x],weight_list[x],inclined_angle[x])
         inclinedpower_list.append(ip)
    #print(inclinedpower_list)

    return vel_list,acc_list,force_list,ke_list,planepower_list,weight_list,inclinedpower_list


def output(v,a,f,ke,pp,w,ip,Cars):

        Cars["Velocity"]=v
        Cars["Acceleration"]=a
        Cars["Force"]=f
        Cars["Kinetic Energy"]=ke
        Cars["Plane Power"] = pp
        Cars["Weight"] =w
        Cars["Inclined Power"] =ip
        print(Cars)



d,m,a,t=get_input(Cars)
vel,acc,f,ke,pp,w,ip=compute(d,m,a,t)
output(vel,acc,f,ke,pp,w,ip,Cars)
