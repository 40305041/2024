import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Dynamical system:
# dz/dt = f(t, z)   <---state space representation

# x' = v * cos(θ)
# y' = v * sin(θ)
# θ' = v * tan(u) / L

# State: z = [x, y, θ]
# Input: u

v = 5.0  # 5m/s
L = 2.3   # 2.3m
u = -2. * np.pi / 180.   # -2 degrees (in rad)
def system_dynamics(t, z):
    theta= z[2]
    # Bicycle model
    return [v * np.cos(theta),
            v * np.sin(theta),
            v * np.tan(u) / L]

t_final = 2
# the initial condition is:
# z(0) = [x(0), y(0), theta(0)]
z_initial = [0., 0.3, 5.]
solution = solve_ivp(system_dynamics,
                     [0, t_final],
                     z_initial,
                     t_eval=np.linspace(0, t_final, 2))

times = solution.t
x_trajectory = solution.y[0]
y_trajectory = solution.y[1]
theta_trajectory = solution.y[2]

plt.plot(times, y_trajectory)
plt.show()
