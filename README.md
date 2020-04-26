
# pysumma-sciunit

This repository contains software described in the manuscript "A Taxonomy for Reproducible and Replicable Research in Environmental Modelling" by Essawy, Goodall, Voce, Morsy, Sadler, Choi, Tarboton, and Malik the is currently under peer review. 

The MyAnalsis notebook is used to repeat a scientific analysis using the [Sciunit  tool] (https://sciunit.run/) through JupyterHub on [HydroShare] (https://www.hydroshare.org/). The MyAnalysis noteboke is available on HydroShare [here] (https://www.hydroshare.org/resource/7d1403636fd3444c87e3c5b40b000b91/).

The scientific analysis uses the [pySUMMA library] (https://github.com/UW-Hydro/pysumma) to model the sensitivity of total evapotranspiration to the stomatal resistance parameterization for the Aspen stand at the Reynolds Mountain East study site. More information about this experiment can be found in [Clark et al. (2015b)] (https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1002/2015WR017200).

pySUMMA wraps the hydrologic model [SUMMA] (https://ral.ucar.edu/projects/summa), which is configured to allow for exploring different model configurations to easy test hyrdologic modeling hypotheses.

The purpose of this code is to illustrate how Sciunit can be used to containerize a pySUMMA modeling experiment so that it can be reporoduced and replicated by others. Scientific software is often difficult to package due to complex software dependencies and computational environments. By using Sciunit on the CUAHSI JupyterHub, this configuration is simplified for end users as described in the steps below.

## Steps required to replicate the sciunit package from CUAHSI JupyterHub

The steps to replicate the modeling experiment described in the Essawy et al. manuscript on the CUAHSI JupyterHub are as follows. 

Please note - In order to run Notebooks on CUAHSI JupyterHub, the user's account must be added to the [CUAHSI JupyterHub Group] (https://www.hydroshare.org/group/156). This step is to prevent malicious use of the CUAHSI JupyterHub computational environment. 

1. Login to HydroShare or create a new account.
2. Navigate to the HydroShare resource named MyAnalysis either through the search feature or using this direct link [here] (https://www.hydroshare.org/resource/7d1403636fd3444c87e3c5b40b000b91/).
3. Click the "Open with..." button from the resource's landing page in HydroShare
4. Select CUAHSI JupyterHub. An instance will be opened on JupyterHub under the user account, where the user can reproduce and replicate the workflow analysis saved as a sciunit package using the following steps. 
 
Note: The user must issue sciunit shell commands by using the "!" expression in Jupyter. 

5. Open the MyAnalysis sciunit container.

```
!sciunit open MyAnalysis
````

6. List all computational experiments within the MyAnalysis sciunit container.
    
```
!sciunit list
```

7. Repeat the Analysis.
    
    The command below will run the experiment 1 (e1) analysis on the host machine. This e1 analysis is the hydrologic modeling workflow described in the Essawy at al. manuscript. 
    
```
!sciunit repeat e1
```

8. Navigate to the reproduced output in the sciunit package. 

   Once the experiment completes from the prior step, it will create a new directory on JupyterHub that includes software, data, and environment settings for the analysis run. You can navigate to this director using the following command. 

```
!ls "/home/jovyan/work/sciunit/MyAnalysis/cde-package/cde-root/media/sf_pysumma/sciunit/"
```

9. Change SUMMA configurations from Ball-berry to Jarvis method to analyze the impact of total ET. 

   The prior step illustrated reproducing a past model run. To take a step further and replicate the study by changing the workflow and running the new analysis, it is possible to edit the Notebook within the MyAnlysis container to reconfigure the pySUMMA model run.

```
with open(simulation_object, "r") as f:
    read_data = f.read()
    line = read_data.replace('BallBerry', "Jarvis")
    f.close()
with open(simulation_object, "w") as f:
    f.write(line)
    f.close()
```

10. Commit sciunit to replicate the sciunit container.

    Once the change has been made to the Notebook file, it can be committed to the sciunit container as a new experiment. 
   
```
!sciunit commit
```

11. Repeat the newly created the sciunit experiment.

  The prior command creates a new experiment in the Sciunit container (e2) that can be run using the repeat command, just as we did before for e1 in step 7.

```
!sciunit repeat e2
```

These basic steps allow one to rerun a computational experiment created by others and change that experiment to something new. The new experiment is also stored in the sciunit container, allowing it to be easily shared and rerun by others. 

Questions or problems executing these steps should be directed to Jon Goodall (goodall@virginia.edu). 

## License

[MIT License](https://github.com/uva-hydroinformatics/pysumma-sciunit/blob/master/LICENSE)
