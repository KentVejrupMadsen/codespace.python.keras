#!/usr/bin/env bash
python3 -m venv .venv
source ./.venv/bin/activate

# Installation of packages
pip install wandb

pip install scikit-learn
pip install tensorflow
pip install keras
pip install opencv-python


