# deepimblearn


## Environments
* This package is tested on Linux OS.
* You are suggested to use a different virtual environment so as to avoid package dependency issue.
* For Pyenv & Virtualenv users, you can follow the below steps to create a new virtual environment or you can also skip this step.
#### Pyenv & Virtualenv (Optinal)
* For dependency isolation, it's better to create another virtual environment for usage.
* The following will be the demo for creating and managing virtual environment.
* Install `pyenv` & `virtualenv` first.
* `pyenv virtualenv [version] [virtualenv_name]`
    *  For example, if you'd like to use python 3.6.8, you can do: `pyenv virtualenv 3.6.8 TestEnv`
* `mkdir [dir_name]`
* `cd [dir_name]`
* `pyenv local [virtualenv_name]`
* Then, you will have a new (clean) python virtual environment for the package installation.

## Installation 
### Basic Requirement
* Python >= 3.6
* Others

```
git clone https://github.com/wccheng3011/deep-imbalanced-learn.git
cd deepimblearn
python -m pip install -r requirements.txt
python setup.py install

```

## Usage
```
cd example
python main.py --gpu 0 --seed 1126 --c config/config_cifar10.yaml --strategy ERM
```
* For more information about example and usage, please see the [Example README](https://github.com/wccheng3011/deep-imblanced-learn/tree/main/example)

## Test
* `python -m unittest -v`
