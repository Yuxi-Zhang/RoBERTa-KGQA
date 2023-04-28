# RoBERTa-KGQA
We present an efficient and robust system for view synthesis and pose estimation by integrating PoseCNN and iNeRF. Our method leverages the pose and object segmentation predictions from PoseCNN to improve the initial camera pose estimation and accelerate the optimization process in iNeRF.

<img src="figures/system.png" width="600">
<img src="figures/roberta.png" width="600">

## Installation

1. To start, install `pytorch` and `cuda` according to your own GPU version, and then create the environment using conda:

    ```sh
    git clone https://github.com/Yuxi-Zhang/RoBERTa-KGQA.git
    cd RoBERTa-KGQA
    conda env create -f environment.yml
    conda activate RoBERTa-KGQA
    ```
The code is tesed with PyTorch==1.13.1 and cuda=11.7
