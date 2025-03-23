import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functions import *

# Read data and clean

def clean_data(file_path):
    data = pd.read_csv(file_path, skiprows=10)
    data.drop(index=0, inplace=True)  # Remove unit row
    data.columns = data.columns.str.strip()  # Remove extra spaces
    return data.apply(pd.to_numeric, errors='coerce')

diesel_data = clean_data("Lab work/Engine Lab/Diesel_data.csv")
petrol_data = clean_data("Lab work/Engine Lab/Petrol_data.csv")

# Constants
gamma = 1.4
dens_a = 1.2
Clfm_d, Clfm_p = 55.9e-6, 50.199e-6
Vd_d, Vd_p = 1.9e-3, 1.2e-3
rv_d, rv_p = 22, 10.3
dens_f_d, dens_f_p = 840, 770
CVf_d, CVf_p = 42500, 44000

# Extract variables
params = ["Engine Speed", "Torque", "Air Flow Pressure", "Exhaust Temp.", "Air Temp.", "Fuel Flow Rate"]

def extract_values(df):
    return {param: df[param].values for param in params}

diesel_vals = extract_values(diesel_data)
petrol_vals = extract_values(petrol_data)

# Calculate derived values
def calculate_engine_values(vals, Clfm, dens_f, CVf, Vd, rv=None):
    air_mfr = find_air_mass_flow_rate(Clfm, dens_a, vals["Air Flow Pressure"])
    fuel_mfr = find_fuel_mass_flow_rate(vals["Fuel Flow Rate"], dens_f)
    brake_power = find_brake_power(vals["Torque"], vals["Engine Speed"])
    bmep = find_brake_mean_effective_pressure(vals["Torque"], Vd)
    brake_thermal_eff = find_brake_thermal_efficiency(brake_power, fuel_mfr, CVf)
    bsfc = find_brake_specific_fuel_consumption(fuel_mfr, brake_power)
    vol_eff = find_volumetric_efficiency(air_mfr, vals["Engine Speed"], dens_a, Vd)
    air_to_fuel_ratio = find_air_to_fuel_ratio(air_mfr, fuel_mfr)
    if rv:
        cut_off_ratio = find_cut_off_ratio(vals["Exhaust Temp."], vals["Air Temp."], gamma)
        theor_cycle_eff = find_theoretical_cycle_efficiency_diesel(cut_off_ratio, gamma, rv)
    else:
        theor_cycle_eff = np.full_like(vals["Engine Speed"], fill_value=find_theoretical_cycle_efficiency_petrol(rv_p, gamma))
        cut_off_ratio = None
    return locals()

diesel_calc = calculate_engine_values(diesel_vals, Clfm_d, dens_f_d, CVf_d, Vd_d, rv_d)
petrol_calc = calculate_engine_values(petrol_vals, Clfm_p, dens_f_p, CVf_p, Vd_p)

# Improved binning function
def bin_data(engine_speeds, values, bin_width=50):
    bins = np.arange(min(engine_speeds) // bin_width * bin_width, max(engine_speeds) + bin_width, bin_width)
    bin_centers = (bins[:-1] + bins[1:]) / 2
    binned_data = {}
    
    for center in bin_centers:
        mask = (engine_speeds >= center - bin_width / 2) & (engine_speeds < center + bin_width / 2)
        if np.any(mask):
            binned_data[center] = (np.mean(engine_speeds[mask]), np.std(engine_speeds[mask]),
                                    np.mean(values[mask]), np.std(values[mask]))
    return binned_data

# List of parameters to plot
plot_params = [
    ('Brake Power', 'brake_power', 'kW'),
    ('Brake Mean Effective Pressure (BMEP)', 'bmep', 'kPa'),
    ('Brake Thermal Efficiency', 'brake_thermal_eff', ''),
    ('Brake Specific Fuel Consumption (BSFC)', 'bsfc', 'g/kWh'),
    ('Volumetric Efficiency', 'vol_eff', ''),
    ('Air to Fuel Ratio', 'air_to_fuel_ratio', ''),
]

# Plot with error bars
for title, var, units in plot_params:
    plt.figure(figsize=(8, 6))
    
    diesel_binned = bin_data(diesel_vals['Engine Speed'], diesel_calc[var])
    petrol_binned = bin_data(petrol_vals['Engine Speed'], petrol_calc[var])
    
    # Extract bin values
    diesel_x, diesel_x_err, diesel_y, diesel_y_err = zip(*diesel_binned.values())
    petrol_x, petrol_x_err, petrol_y, petrol_y_err = zip(*petrol_binned.values())
    
    # Plot error bars
    plt.errorbar(diesel_x, diesel_y, yerr=diesel_y_err, xerr=diesel_x_err, fmt='bo', label='Diesel', capsize=3)
    plt.errorbar(petrol_x, petrol_y, yerr=petrol_y_err, xerr=petrol_x_err, fmt='rx', label='Petrol', capsize=3)
    
    plt.title(f'{title} vs Engine Speed')
    plt.xlabel('Engine Speed (RPM)')
    plt.ylabel(f'{title} ({units})' if units else title)
    plt.grid(True)
    plt.legend()
    plt.show()

# Diesel-only Cut Off Ratio
plt.figure(figsize=(8, 6))
diesel_cutoff_binned = bin_data(diesel_vals['Engine Speed'], diesel_calc['cut_off_ratio'])
if diesel_cutoff_binned:
    diesel_x, diesel_x_err, diesel_y, diesel_y_err = zip(*diesel_cutoff_binned.values())
    plt.errorbar(diesel_x, diesel_y, yerr=diesel_y_err, xerr=diesel_x_err, fmt='bo', label='Diesel', capsize=3)
    plt.title('Cut Off Ratio vs Engine Speed (Diesel Only)')
    plt.xlabel('Engine Speed (RPM)')
    plt.ylabel('Cut Off Ratio')
    plt.grid(True)
    plt.legend()
    plt.show()
