import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
file_path = "motors.xlsx"  # Update with your actual file path
df = pd.read_excel(file_path,header= 2)
# Insert values for you motor

for index , row in df.iterrows():
    model = row["MODEL"]
    Vnom = row["V"]
    
    # Convert units
    NLspeedrpm = row["r/min"]  
    NLcurrent = row["A"]
    Storque = row["mN・m"] / 1000  # Convert from mN·m to Nm
    Scurrent = row["B"]
    
    ###Plotting code - don't change###

    # Evaluating the torque, speed, current all asumed linear equations
    NLspeed = (NLspeedrpm/60)*2*np.pi #Converts from RPM to rad/s
    Torquevals = np.linspace(0,Storque,1000) #Takes 1000 values of torque between 0 and max torque
    Speedvals = NLspeed + Torquevals*(0-NLspeed/Storque) #Gives a linear increas of speed vals between NLspeed and stall
    Currentvals =NLcurrent+ Torquevals*((Scurrent-NLcurrent)/Storque) #Gives current vals between NL current and stall

    # Evaluating power and efficiency curves
    Pout = Speedvals*Torquevals #Power out, Speed x Torque

    efficiency = (Pout/(Vnom*Currentvals)) *100 #Efficiency P out / P in, P in is Volts x current

    ##Accessing values
    # target_torque = 0.1  # Insert your target value in Nm
    # current_at_target_torque = np.interp(target_torque, Torquevals, Currentvals) #Finds your secondary value at the target value
    # print(current_at_target_torque)

    # Finding values at max efficiency
    max_eff_idx = np.argmax(efficiency)
    max_eff_torque = Torquevals[max_eff_idx]
    max_eff_speed = Speedvals[max_eff_idx]
    max_eff_current = Currentvals[max_eff_idx]
    max_eff_power = Pout[max_eff_idx]
    max_eff_value = efficiency[max_eff_idx]
    if max_eff_power >= 10:
       # Print values at max efficiency
        print(f"Max Efficiency: {max_eff_value:.2f}%")
        print(f"Torque at Max Efficiency: {max_eff_torque:.4f} Nm")
        print(f"Speed at Max Efficiency: {max_eff_speed:.2f} rad/s")
        print(f"Current at Max Efficiency: {max_eff_current:.2f} A")
        print(f"Power at Max Efficiency: {max_eff_power:.2f} W")
        fig, ax1 = plt.subplots()
        fig.subplots_adjust(left=0.1, right=0.75)

        ax1.set_xlabel("Torque (Nm)")
        ax1.set_ylabel("Speed (rad/s)", color="red")
        ax1.plot(Torquevals, Speedvals, color="red", label="Speed (rad/s)")
        ax1.tick_params(axis="y", labelcolor="red")

        ax2 = ax1.twinx()
        ax2.set_ylabel("Power output (W)", color="darkorange")
        ax2.plot(Torquevals, Pout, color="darkorange", label="Power (W)")
        ax2.tick_params(axis="y", labelcolor="darkorange")

        ax3 = ax1.twinx()
        ax3.spines["right"].set_position(("outward", 50))
        ax3.set_ylabel("Current (A)", color="blue")
        ax3.plot(Torquevals, Currentvals, color="blue", label="Current (A)")
        ax3.tick_params(axis="y", labelcolor="blue")

        ax4 = ax1.twinx()
        ax4.spines["right"].set_position(("outward", 100))
        ax4.set_ylabel("Efficiency (%)", color="green")
        ax4.plot(Torquevals, efficiency, color="green", label="Efficiency (%)")
        ax4.tick_params(axis="y", labelcolor="green")

        ax1.axvline(x=max_eff_torque, color="blue", linestyle="dotted", label="Max Efficiency")
        ax1.grid(True, linestyle="--", alpha=0.6)
        plt.title(f"Motor Performance - {model}")
        plt.show()
