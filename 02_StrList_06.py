ux_vector =input().strip()
vx_vector =input().strip()

u_vector = ux_vector[1:-1]
u_vector = u_vector.split(",")

v_vector = vx_vector[1:-1]
v_vector = v_vector.split(",")

x_vector = float(u_vector[0]) + float(v_vector[0])
y_vector = float(u_vector[1]) + float(v_vector[1])
z_vector = float(u_vector[2]) + float(v_vector[2])

final_vector = [x_vector,y_vector,z_vector]
print(f'{ux_vector} + {vx_vector} = {final_vector}')

#[1, 2, 3] [2, 3, 4]

