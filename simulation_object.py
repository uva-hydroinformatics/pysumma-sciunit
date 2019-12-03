from pysumma.Simulation import Simulation
import subprocess
import pylab
#import seaborn as sns
import xarray as xr
import matplotlib.pyplot as plt
from pysumma.Plotting import  Plotting
import netCDF4 as nc
import numpy as np
import glob
# create a pySUMMA simulation object using the SUMMA 'file manager' input file
S = Simulation('/home/ubuntu/summaTestCases_2.x/settings/wrrPaperTestCases/figure07/summa_fileManager_riparianAspenSimpleResi$
# set the simulation start and finish times
S.decision_obj.simulStart.value = "2005-07-01 00:00"
S.decision_obj.simulFinsh.value = "2007-08-20 00:00"
S.executable = "/home/ubuntu/summa/bin/summa.exe"
S.decision_obj.stomResist.value = 'BallBerry'
results_simpleResistance, out_file = S.execute(run_suffix="rootDistExp", run_option = 'local')

# Visualization

P= Plotting(out_file)
P.plot_1d("pptrate")
#savefig("scalarCanopyTranspiration.pdf")
#pylab.savefig('test')