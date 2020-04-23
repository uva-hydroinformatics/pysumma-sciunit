
# pysumma-sciunit


This repository contains:

The Python script for the SUMMA Python wrapper software pySUMMA (Choi et al., 2018) to model the sensitivity of evapotranspiration to the stomatal resistance parameterization for the Aspen stand at the Reynolds Mountain East study site.

MyAnalsis notebook is used to repeat the analysis using sciunit command tool through JupyterHub on [HydroShare](https://www.hydroshare.org/resource/7d1403636fd3444c87e3c5b40b000b91/).

## SUMMA Model Installation 

The SUMMA model is installed from the SUMMA [Installation documentation](https://summa.readthedocs.io/en/latest/installation/SUMMA_installation/). 


## Steps required to replicate the sciunit package from CUAHSI HydroShare JupyterHub

1. Login to HydroShare.
2. Navigate to the HydroShare resource named [MyAnalysis](https://www.hydroshare.org/resource/7d1403636fd3444c87e3c5b40b000b91/).
3. Click the "Open with" button from the resource's landing page in HydroShare
4. Select CUAHSI JupyterHub. An instance will be opened on JupyterHub under the user account, where the user can reproduce and replicate the workflow analysis saved as a sciunit package.  
 
The user must issue sciunit commands by using the "!" expression in Jupyter. 

5. Open sciunit

```
!sciunit open MyAnalysis
````
6. List all sciunit packages within this resources
The sciunit list command will list all the packaged experiments within "MyAnalysis" sciunit.
```
!sciunit list
```
7. Repeat the Analysis
The sciunit repeat e1 command will rerun the experiment 1 (e1) analysis on the host machine. This command will create a new directory that includes software, data, and environment settings
```
!sciunit repeat e1
```
8. Navigate to the reproduced output in sciunit package 
```
!ls "/home/jovyan/work/sciunit/MyAnalysis/cde-package/cde-root/media/sf_pysumma/sciunit/"
```
9. Change SUMMA configuration from Ball-berry to Jarvis method to analyze the impact of ET 
10. Commit Sciunit to replicate sciunit packages using different dataset
```
!sciunit commit
```
10. Repeat the newly created sciunit package using a different dataset
```
!sciunit repeat e2
```

## License

[MIT License](https://github.com/uva-hydroinformatics/pysumma-sciunit/blob/master/LICENSE)