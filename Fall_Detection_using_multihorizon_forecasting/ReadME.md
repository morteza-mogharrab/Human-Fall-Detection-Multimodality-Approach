## Ling to datasets
SmartFall and Notch dataset: https://userweb.cs.txstate.edu/~hn12/data/SmartFallDataSet/
DLR dataset: https://www.dlr.de/kn/en/desktopdefault.aspx/tabid-12705/22182_read-50785/
MobiAct dataset: https://bmi.hmu.gr/the-mobifall-and-mobiact-datasets-2/

## Requirements
python==3.7.3
tensorflow==2.5.3
sklearn==0.24.2

## Running
-Data Preprocess
Please download all datasets through the URL or `zip` files provided in `dataset/`.

-SmartFall Dataset
1. Put dataset into directory named `dataset/SmartFall_Dataset/`.
2. For SmartFall dataset, preprocessing codes are included in `ipynb` files. 

-Notch Dataset
1. Put dataset into directory named `dataset/Notch_Dataset/`
2. For Notch dataset, preprocessing codes are included in `ipynb` files.

-DLR Dataset
1. Put dataset into directory named `dataset/ARS DLR Data Set/`.
2. Use `dataset/DLR_preprocess.ipynb` for preprocessing. Run all cells in the ipynb file. 
3. Save all preprocessed files in `dataset/dlr_preprocessed`. 

-MobiAct Dataset
1. Put dataset into directory named `dataset/MobiAct_Dataset_v2.0`.
2. Use `dataset/MobiAct_preprocess.ipynb` for preprocessing. Run all cells in the ipynb file.
3. Save all preprocessed files in `dataset/mobiact_preprocessed`.

-For DL Methods
> run `python dl_main.py <dataset_name> <model> <use_gpu>`

- `dataset_name`: choose between <mobiact, dlr, notch, smartfall>
- `model`: choose between <singleLSTM, stackedLSTM, CNN>
- `use_gpu`: if like to use GPU set to `yes` or set to `no`

-----
- You can find all previous ipynb files in `prev_jupyter_files/` .

-For TFT Method
> run `python tft_main.py <dataset_name> <save_dir_name> <use_gpu> <restart_opt>`

- `dataset_name`: choose between <mobiact, dlr, notch, smartfall>
- `save_dir_name`: set save name
- `use_gpu`: if like to use GPU set to `yes` or set to `no`
- `restart_opt`: if like to restart set to `yes` or set to `no`
