# Setup Guide

## Requirements
- Python 3.x
- Ansible
- Cisco IOS devices

## Installation
1. Clone the repository.
2. Install Python dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Set up your Cisco devices in the `config/ansible/inventory.yaml` file.

## Running the Scripts
- To collect data:
    ```
    python scripts/data_collection.py
    ```
- To train the model:
    ```
    python scripts/ml_model_training.py
    ```
