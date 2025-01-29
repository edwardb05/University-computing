from functions import *
import pandas as pd
import matplotlib.pyplot as plt


# read the data  and remove time column and first 10 rows
diesel_data = pd.read_csv("Lab work/Engine Lab/Diesel_data.csv",skiprows=10, usecols=lambda column: column != "Time")
petrol_data = pd.read_csv("Lab work/Engine Lab/Petrol_data.csv",skiprows=10,usecols=lambda column: column != "Time")  

# remove the units row to clean data
diesel_data.drop(index=0, inplace=True)
petrol_data.drop(index=0, inplace=True)

gamma = 1.4
dens_a = 1.2
# Use _d for diesel (CI) engine and _p for petrol(SI)
Clfm_d =55.9*10**-6 #Flowmeter calibration constant
Clfm_p = 50.199*10**-6

# set known values
Vd_d = 1.9*10**-3 #Cylinder displacement
Vd_p = 1.2*10**-3
rv_d = 22 #Compression ratio
rv_p = 10.3
dens_f_d = 840 #Fuel density
dens_f_p = 770
CVf_d=42500 #Fuel calorific value
CVf_p =44000

# obtain values from csv
# Diesel data
N_d = pd.to_numeric(diesel_data["Engine Speed "], errors='coerce')
T_d = pd.to_numeric(diesel_data["Torque "], errors='coerce')
del_p_d = pd.to_numeric(diesel_data["Air Flow Pressure "], errors='coerce')
T4_d = pd.to_numeric(diesel_data["Exhaust Temp. "], errors='coerce')
T1_d = pd.to_numeric(diesel_data["Air Temp. "], errors='coerce')
Vf_d = pd.to_numeric(diesel_data["Fuel Flow Rate  "], errors='coerce')

# Petrol data
N_p = pd.to_numeric(petrol_data["Engine Speed "], errors='coerce')
T_p = pd.to_numeric(petrol_data["Torque "], errors='coerce')
del_p_p = pd.to_numeric(petrol_data["Air Flow Pressure "], errors='coerce')
T4_p = pd.to_numeric(petrol_data["Exhaust Temp. "], errors='coerce')
T1_p = pd.to_numeric(petrol_data["Air Temp. "], errors='coerce')
Vf_p = pd.to_numeric(petrol_data["Fuel Flow Rate  "], errors='coerce')


# caluclate new diesel values using the functions defined in functions.py

air_mfr_d = find_air_mass_flow_rate(Clfm_d,dens_a,del_p_d )
fuel_mfr_d = find_fuel_mass_flow_rate(Vf_d, dens_f_d)
brake_power_d = find_brake_power(T_d, N_d)
bmep_d = find_brake_mean_effective_pressure(T_d, Vd_d)
brake_thermal_eff_d = find_brake_thermal_efficiency(brake_power_d, fuel_mfr_d, CVf_d)  
bsfc_d = find_brake_specific_fuel_consumption(fuel_mfr_d, brake_power_d)
vol_eff_d = find_volumetric_efficiency(air_mfr_d, N_d, dens_a, Vd_d)
air_to_fuel_ratio_d = find_air_to_fuel_ratio(air_mfr_d, fuel_mfr_d)
cut_off_rat_d = find_cut_off_ratio(T4_d, T1_d, gamma)  
theor_cycle_eff_d = find_theoretical_cycle_efficiency_diesel(cut_off_rat_d, gamma, rv_d)  

# Calculate new petrol values
air_mfr_p = find_air_mass_flow_rate(Clfm_p, dens_a, del_p_p)
fuel_mfr_p = find_fuel_mass_flow_rate(Vf_p, dens_f_p)
brake_power_p = find_brake_power(T_p, N_p)
bmep_p = find_brake_mean_effective_pressure(T_p, Vd_p)
brake_thermal_eff_p = find_brake_thermal_efficiency(brake_power_p, fuel_mfr_p, CVf_p)  
bsfc_p = find_brake_specific_fuel_consumption(fuel_mfr_p, brake_power_p)
vol_eff_p = find_volumetric_efficiency(air_mfr_p, N_p, dens_a, Vd_p)
air_to_fuel_ratio_p = find_air_to_fuel_ratio(air_mfr_p, fuel_mfr_p)
theor_cycle_eff_p = find_theoretical_cycle_efficiency_petrol(rv_p, gamma) 
# Only one constant theoretical efficiency
theor_cycle_eff_p = np.full_like(N_p, fill_value=theor_cycle_eff_p)



# List of parameters, units and titles
params = [
    ('Brake Power',"kW", 'brake_power_d', 'brake_power_p'),
    ('Brake Mean Effective Pressure (BMEP)',"kPa", 'bmep_d', 'bmep_p'),
    ('Brake Thermal Efficiency', "",'brake_thermal_eff_d', 'brake_thermal_eff_p'),
    ('Brake Specific Fuel Consumption (BSFC)',"g/Kwh", 'bsfc_d', 'bsfc_p'),
    ('Volumetric Efficiency', "",'vol_eff_d', 'vol_eff_p'),
    ('Air to Fuel Ratio',"", 'air_to_fuel_ratio_d', 'air_to_fuel_ratio_p'),
]

# Iterate through each parameter, plotting its values
for title, units, diesel_var, petrol_var in params:
    
    # Create a new figure for each plot
    plt.figure(figsize=(8, 6))  # You can adjust the size as needed

    # Evaluate the diesel and petrol variables
    diesel_data = eval(diesel_var)  # This evaluates the diesel variable
    petrol_data = eval(petrol_var)  # This evaluates the petrol variable
    
    # Plot for diesel (dots) and petrol (crosses)
    plt.plot(N_d, diesel_data, 'bo', label='Diesel', markersize=5)  # Blue dots for diesel
    plt.plot(N_p, petrol_data, 'rx', label='Petrol', markersize=5)  # Red crosses for petrol
    
    # Set the title and labels
    plt.title(f'{title} vs Engine Speed')
    plt.xlabel('Engine Speed (RPM)')
    plt.ylabel(f'{title}/{units}')
    
    # Optional: Add grid for better readability
    plt.grid(True)
    
    # Show the legend
    plt.legend()

    # Show the plot (this will open in a new window)
    plt.show()

# Plot for cut off ratio, only needed for diesel
plt.figure(figsize=(8, 6))  # You can adjust the size as needed

plt.plot(N_d, cut_off_rat_d, 'bo', label='Diesel', markersize=5)  # Blue dots for diesel

# Set the title and labels
plt.title(f'Cut off ratio vs Engine Speed (diesel only)')
plt.xlabel('Engine Speed (RPM)')
plt.ylabel(f'Cut off ratio/')
    
# Optional: Add grid for better readability
plt.grid(True)
    
# Show the legend
plt.legend()

# Show the plot (this will open in a new window)
plt.show()