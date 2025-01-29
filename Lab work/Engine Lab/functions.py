import numpy as np

def find_air_mass_flow_rate(Clfm,dens_a,del_p):
    air_mfr = Clfm * dens_a*del_p
    return air_mfr

def find_fuel_mass_flow_rate(Vf, dens_f):
    fuel_mfr=(Vf*10**-6/60)*dens_f #change to m^3 /sec
    return fuel_mfr

def find_brake_power(T,N):
    brake_power = (T*(2*np.pi*N)/60)/1000 # return in kW
    return brake_power

def find_brake_mean_effective_pressure(T,Vd):
    bmep = (((4*np.pi)/Vd)*T)/ 1000 #return in kPa
    return bmep 

def find_brake_thermal_efficiency(brake_power, fuel_mfr, CVf):
    b_therm_eff = brake_power/(fuel_mfr*CVf)
    return b_therm_eff

def find_brake_specific_fuel_consumption(fuel_mfr, brake_power):
    bsfc = (fuel_mfr/ brake_power)*1000*3600 #Convert to grams/Kwh
    return bsfc

def find_volumetric_efficiency(air_mfr,N,dens_a,Vd):

    vol_eff = (air_mfr/(N/120))/(dens_a*Vd) #N over 120 as 2 revs per cycle and put it into sec
    return vol_eff

def find_air_to_fuel_ratio(air_mfr,fuel_mfr):
    air2fuel_rat = air_mfr/fuel_mfr
    return air2fuel_rat

def find_cut_off_ratio(T4,T1,gamma):
    cut_off_rat= ((T4+273.2)/(T1+273.2))**(1/gamma)
    return cut_off_rat

def find_theoretical_cycle_efficiency_diesel(cut_off_rat,gamma,rv):
    theor_cycle_eff_d = 1-(1/(gamma*rv**(gamma-1)))*((cut_off_rat**(gamma)-1)/(cut_off_rat-1))
    return theor_cycle_eff_d

def find_theoretical_cycle_efficiency_petrol(rv, gamma):
    theor_cycle_eff_d = 1-1/(rv**(gamma-1))
    return theor_cycle_eff_d
