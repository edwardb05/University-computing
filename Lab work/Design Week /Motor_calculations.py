import numpy as np
import matplotlib.pyplot as plt
# Insert values for you motor - example values for RS-555PC-25110

Vnom = 20 #Nominal voltage

# No load values

NLspeedrpm = 3600 #No load speed in rpm
NLcurrent =0.07 #No load current in Amps

# Stall values

Storque = 186e-3 #Stall torque in Nm e.g. this is 186mNm
Scurrent = 3.82 #Stall current in amps

###Plotting code - don't change###

# Evaluating the torque, speed, current all asumed linear equations
NLspeed = (NLspeedrpm/60)*2*np.pi #Converts from RPM to rad/s
Torquevals = np.linspace(0,Storque,1000) #Takes 1000 values of torque between 0 and max torque
Speedvals = NLspeed + Torquevals*(0-NLspeed/Storque) #Gives a linear increas of speed vals between NLspeed and stall
Currentvals =NLcurrent+ Torquevals*((Scurrent-NLcurrent)/Storque) #Gives current vals between NL current and stall

# Evaluating power and efficiency curves
Pout = Speedvals*Torquevals #Power out, Speed x Torque

efficiency = (Pout/(Vnom*Currentvals)) *100 #Efficiency P out / P in, P in is Volts x current

# Finding values at max efficiency
max_eff_idx = np.argmax(efficiency)
max_eff_torque = Torquevals[max_eff_idx]
max_eff_speed = Speedvals[max_eff_idx]
max_eff_current = Currentvals[max_eff_idx]
max_eff_power = Pout[max_eff_idx]
max_eff_value = efficiency[max_eff_idx]

# Plot
fig, ax1 = plt.subplots()

# First axis (Speed)
ax1.set_xlabel("Torque (Nm)")
ax1.set_ylabel("Speed (rad/s)", color="red")
ax1.plot(Torquevals, Speedvals, color="red", label="Speed (rad/s)")
ax1.tick_params(axis="y", labelcolor="red")

# Second axis (Power)
ax2 = ax1.twinx()
ax2.set_ylabel("Power outputted (W)", color="darkorange")
ax2.plot(Torquevals, Pout, color="darkorange", label="Power (W)")
ax2.tick_params(axis="y", labelcolor="darkorange")

# Third axis (Current)
ax3 = ax1.twinx()
ax3.spines["right"].set_position(("outward", 50))
ax3.set_ylabel("Current (A)", color="blue")
ax3.plot(Torquevals, Currentvals, color="blue", label="Current (A)")
ax3.tick_params(axis="y", labelcolor="blue")

# Fourth axis (Efficiency)
ax4 = ax1.twinx()
ax4.spines["right"].set_position(("outward", 100))
ax4.set_ylabel("Efficiency (%)", color="green")
ax4.plot(Torquevals, efficiency, color="green", label="Efficiency (%)")
ax4.tick_params(axis="y", labelcolor="green")

# Add a vertical blue dotted line at max efficiency point and add grid
ax1.axvline(x=max_eff_torque, color="blue", linestyle="dotted", label="Max Efficiency")
ax1.grid(True, linestyle="--", alpha=0.6)  # Dashed grid with transparency

# Print values at max efficiency
print(f"Max Efficiency: {max_eff_value:.2f}%")
print(f"Torque at Max Efficiency: {max_eff_torque:.4f} Nm")
print(f"Speed at Max Efficiency: {max_eff_speed:.2f} rad/s")
print(f"Current at Max Efficiency: {max_eff_current:.2f} A")
print(f"Power at Max Efficiency: {max_eff_power:.2f} W")

# Legends
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")
ax3.legend(loc="lower left")
ax4.legend(loc="lower right")

plt.title("Motor Performance Curves")
plt.show()