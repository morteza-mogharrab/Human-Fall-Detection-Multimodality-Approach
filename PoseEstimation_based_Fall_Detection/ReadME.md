## Requirements
matplotlib==3.8.0
mediapipe==0.10.0
numpy==1.26.2
opencv_contrib_python==4.8.1.78
opencv_python==4.8.1.78
regex==2023.10.3
scikit_learn==1.3.1
seaborn==0.13.0
torch==2.1.0
tensorboard


## Dataset Preparation
 - Create a folder called dataset in the root folder of the project. The folder structure should be as follows:
    ```bash
    Fall Detection
    ├── data
    │   ├── adl-01-cam0-urfdd-1-no_keypoints.npy
    │   ├── ...
    ├── remaining files
    ```

## Training
- To start training, run the following command:
    ```bash
    python main.py --dataset ./data
    ```
- Other arguments can be found in the [main.py](./main.py) file.
- The trained models are stored in the `./output` folder.
- The hyperparameters of the model can be changed in the [./config/model.json](./config/model.json) file.