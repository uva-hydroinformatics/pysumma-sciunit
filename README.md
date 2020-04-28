
# pysumma-sciunit

This repository contains software described in the manuscript "A Taxonomy for Reproducible and Replicable Research in Environmental Modelling" by Essawy, Goodall, Voce, Morsy, Sadler, Choi, Tarboton, and Malik the is currently under peer review. 

The MyAnalysis notebook is used to repeat a scientific analysis using the [Sciunit  tool](https://sciunit.run/) through JupyterHub on [HydroShare](https://www.hydroshare.org/). The MyAnalysis notebook is available on HydroShare [here](https://www.hydroshare.org/resource/7d1403636fd3444c87e3c5b40b000b91/).

The scientific analysis uses the [pySUMMA library](https://github.com/UW-Hydro/pysumma) to model the sensitivity of total evapotranspiration to the stomatal resistance parameterization for the Aspen stand at the Reynolds Mountain East study site. More information about this experiment can be found in [Clark et al. (2015b)](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1002/2015WR017200).

pySUMMA wraps the hydrologic model [SUMMA](https://ral.ucar.edu/projects/summa), which is configured to allow for exploring different model configurations to easy test hyrodologic modeling hypotheses.

The purpose of this code is to illustrate how Sciunit can be used to containerize a pySUMMA modeling experiment so that it can be reporoduced and replicated by others. Scientific software is often difficult to package due to complex software dependencies and computational environments. By using Sciunit on the CUAHSI JupyterHub, this configuration is simplified for end users as described in the steps below.

## Steps required to replicate the sciunit package from CUAHSI JupyterHub

The steps to replicate the modeling experiment described in the Essawy et al. manuscript on the CUAHSI JupyterHub are as follows. 

Please note - In order to run Notebooks on CUAHSI JupyterHub, the user's account must be added to the [CUAHSI JupyterHub Group](https://www.hydroshare.org/group/156). This step is to prevent malicious use of the CUAHSI JupyterHub computational environment. Once logged into your HydroShare account, you can request to be added to the group at the group HydroShare page.

1. Login to HydroShare or create a new account.
2. Navigate to the HydroShare resource named MyAnalysis either through the search feature or using this direct link [here](https://www.hydroshare.org/resource/7d1403636fd3444c87e3c5b40b000b91/).
3. Click the "Open with..." button from the resource's landing page in HydroShare
4. Select CUAHSI JupyterHub. An instance will be opened on JupyterHub under the user account, where the user can reproduce and replicate the workflow analysis saved as a sciunit package by executing the MyAnalsis_CUAHSI_JH.ipynb notebook.

Those with access to the [CyberGIS for Water JupyterHub] (https://www.hydroshare.org/resource/4cfd280e8eb747169b293aec2862d4f5/) can use the additional MyAnalsis_CyberGIS.ipynb notebook provided to run a slightly modified version of the analysis (file paths are updated) within this second compute environment. 

Questions or problems executing these steps should be directed to Jon Goodall (goodall@virginia.edu). 

## License

[MIT License](https://github.com/uva-hydroinformatics/pysumma-sciunit/blob/master/LICENSE)
