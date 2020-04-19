# pysumma-sciunit


This repository contains:

The Python script for the SUMMA Python wrapper software pySUMMA (Choi et al., 2018) to model the sensitivity of evapotranspiration to the stomatal resistance parameterization for the Aspen stand at the Reynolds Mountain East study site.

MyAnalsis notebook is used to repeat the analysis using sciunit command tool through JupyterHub on [HydroShare](https://www.hydroshare.org/resource/5c4941b8ae474c4faf8a2a0872832fd1/).

## SUMMA Model Installation 

The SUMMA model is installed from the SUMMA [Installation documentation](https://summa.readthedocs.io/en/latest/installation/SUMMA_installation/). 


## Steps required to replicate the sciunit package from CUAHSI HydroShare JupyterHub

1. Login to HydroShare.
2. Navigate to the HydroShare resource named [MyAnalysis](https://www.hydroshare.org/resource/7d1403636fd3444c87e3c5b40b000b91/).
3. Click the "Open with" button from the resource's landing page in HydroShare
4. Select CUAHSI JupyterHub. An instance will be opened on JupyterHub under the user account, where the user can reproduce and replicate the workflow analysis saved as a sciunit package.  
 
The user must issue sciunit commands by using the "!" expression in Jupyter. 

5. Open Sciunit

```
!sciunit open MyAnalysis
````
6. Show and list all sciunit packages within this resources
The sciunit show command will show the latest packaged experiment within the "MyAnalysis" sciunit. While the sciunit list command will list all the packaged experiments within "MyAnalysis" sciunit.
```
!sciunit show
!sciunit list
```
7. Repeat the Analysis
The sciunit repeat e1 command will rerun the experiment 1 (e1) analysis on the host machine. This command will create a new directory that includes software, data, and environment settings
`"
!sciunit repeat e1
```
8. Navigate to the newly created MyAnalysis directory
`"
cd 
cd sciunit
cd sciunit/MyAnalysis/cde-package/cde-root/home/ubuntu/pysumma
```
9. Commit changes to create a new package
```
!sciunit commit
```
10. Repeat the newly created sciunit package using a different dataset

```
!sciunit given ../../f4a84771e68c4abd90c135ce4f72cfbd/f4a84771e68c4abd90c135ce4f72cfbd/data/contents repeat e2
```

## License

[MIT License](https://github.com/uva-hydroinformatics/pysumma-sciunit/blob/master/LICENSE)
