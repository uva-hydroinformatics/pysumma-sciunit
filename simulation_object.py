from pysumma.Simulation import Simulation
import subprocess
import pylab
import xarray as xr
import matplotlib.pyplot as plt
from pysumma.Plotting import  Plotting
import netCDF4 as nc
import numpy as np
import glob
import matplotlib.pyplot as plt
import pandas as pd
from jupyterthemes import jtplot

# create a pySUMMA simulation object using the SUMMA 'file manager' input file 
S = Simulation('/media/sf_pysumma/sciunit/SummaModel_ReynoldsAspenStand_StomatalResistance_sopron/settings/summa_fileManager_riparianAspenSimpleResistance.txt')
# set the simulation start and finish times
S.decision_obj.simulStart.value = "2006-07-01 00:00"
S.decision_obj.simulFinsh.value = "2007-09-30 00:00"
S.executable = "/media/sf_pysumma/sciunit/summa-master/bin/summa.exe"
S.decision_obj.stomResist.value = 'BallBerry'
S.output_prefix.value = "ET"
results_ET, out_file = S.execute(run_suffix="simpleResistance", run_option = 'local')
   
# Visualization 
# Create function to calculate Total ET from SUMMA output
def calc_total_et(et_output_df):
    total_et_data = (et_output_df['scalarLatHeatTotal'])*3600/2260000
    # create dates(X-axis) attribute from ouput netcdf
    dates = total_et_data.coords['time'].data
    # create data value(Y-axis) attribute from ouput netcdf
    data_values = total_et_data.data
    # create two dimensional tabular data structure 
    total_et_df = pd.DataFrame(data_values, index=dates)
    # round time to nearest hour (ex. 2006-10-01T00:59:59.99 -> 2006-10-01T01:00:00)
    total_et_df.index = total_et_df.index.round("H")
    # set the time period to display plot 
    total_et_df = total_et_df.loc["2007-05-31 23:00:00":"2007-08-20 23:00:00"]
    # resample data by the average value hourly
    total_et_df_hourly = total_et_df.resample("H").mean()
    # resample data by the average for hour of day
    total_et_by_hour = total_et_df_hourly.groupby(total_et_df_hourly.index.hour).mean()
    total_et_by_hour.index.name = 'hour'
    total_et_by_hour.columns = ['ET']
    # calculate 3 hour moving average
    total_et_by_hour.loc['24'] = total_et_by_hour.loc[0].values
    #for index in range(1,24,1):
    #    total_et_by_hour['ET'][index] = (total_et_by_hour['ET'][index-1]+total_et_by_hour['ET'][index]+total_et_by_hour['ET'][index+1])/3
    return total_et_by_hour
	
# Get hour of day output of the three stomatal resistance methods for the period 1 June to 20 August 2007
ET_hour = calc_total_et(results_ET)

# Plotting output of three different stomatal resistance parameterizations and observation data
# create plot with three different stomatal resistance parameterizations
ET_hour_Graph = ET_hour.plot(color=['blue'],linewidth=4.0,figsize=(13,10))
# invert y axis
ET_hour_Graph.invert_yaxis()
# add x, y label
plt.xlabel('Time of day (hr)', fontsize=25)
plt.ylabel('Total Evapotranspiration (mm/h)', fontsize=25)
# show up the legend
ET_hour_Graph.legend(fontsize=18, loc=2)
plt.xlim(0,24)
plt.ylim(0,-0.6)
x = [0,3,6,9,12,15,18,21,24]
plt.xticks(x, x, fontsize=25)
plt.yticks(fontsize=25)

plt.savefig('/media/sf_pysumma/sciunit/Evapotranspiration.png')