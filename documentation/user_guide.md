Below is an extensive Markdown file that you can use as a `user_guide.md` in your project. This file provides detailed instructions on how to use the network slicing automation framework.

---

# Network Slicing Automation Framework - User Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Setup and Installation](#setup-and-installation)
3. [Configuration](#configuration)
   - [Ansible Inventory](#ansible-inventory)
   - [Cisco Interface Templates](#cisco-interface-templates)
4. [Data Collection](#data-collection)
5. [Machine Learning Model Training](#machine-learning-model-training)
6. [Decision Engine](#decision-engine)
7. [Executing Commands](#executing-commands)
8. [KPI Monitoring](#kpi-monitoring)
9. [Logging](#logging)
10. [Testing](#testing)
11. [Monitoring with Prometheus](#monitoring-with-prometheus)
12. [Troubleshooting](#troubleshooting)

## Introduction
The Network Slicing Automation Framework is designed to automate the configuration and management of network slices on Cisco devices. It leverages machine learning to make data-driven decisions and adjust network parameters dynamically. This guide provides detailed instructions on setting up, configuring, and using the framework.

## Setup and Installation

### Prerequisites
- **Python 3.x**: Ensure you have Python 3 installed on your system.
- **Cisco IOS Devices**: The framework is designed to work with Cisco devices running IOS.
- **Ansible**: Used for automating configurations on network devices.

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/cisco-network-slicing-automation.git
   cd cisco-network-slicing-automation
   ```

2. **Install Python Dependencies**:
   Use the provided `requirements.txt` file to install all necessary Python packages.
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Ansible**:
   Ensure that Ansible is installed and configured properly on your system.
   ```bash
   sudo apt-get install ansible
   ```

## Configuration

### Ansible Inventory
The Ansible inventory file located at `config/ansible/inventory.yaml` defines the network devices that will be managed by the framework. Customize this file with the details of your Cisco devices.

```yaml
all:
  hosts:
    cisco_device:
      ansible_host: 192.168.1.1
      ansible_user: admin
      ansible_password: your_password
      ansible_network_os: ios
```

- **ansible_host**: The IP address of the Cisco device.
- **ansible_user**: The username for authentication.
- **ansible_password**: The password for authentication.
- **ansible_network_os**: Specifies the network operating system, which is `ios` for Cisco devices.

### Cisco Interface Templates
The framework uses Jinja2 templates to generate configurations for Cisco interfaces. These templates are located in the `config/cisco/` directory.

For example, the `interface_template.j2` file might look like this:

```jinja2
interface {{ interface_name }}
 description {{ description }}
 ip address {{ ip_address }} {{ subnet_mask }}
```

You can customize these templates based on your specific network requirements.

## Data Collection
Data collection is a crucial step in network automation as it gathers necessary information from your devices.

### Collecting Data
The `data_collection.py` script gathers data from the network devices specified in your Ansible inventory.

To run the data collection process:
```bash
python scripts/data_collection.py
```

- The script connects to the Cisco devices and retrieves interface data.
- The collected data is saved to a file in the `logs/` directory for further analysis.

## Machine Learning Model Training
Training a machine learning model is essential for the decision engine to make intelligent adjustments to network slices.

### Training the Model
The `ml_model_training.py` script trains a machine learning model using data you provide.

To train the model:
1. Ensure your training data is available in CSV format, e.g., `data/training_data.csv`.
2. Run the following command:
   ```bash
   python scripts/ml_model_training.py
   ```
   
- The script loads the data, trains the model, and saves the trained model as `trained_model.pkl` in the `models/` directory.
- Customize the model training process by modifying the script, particularly the machine learning algorithm and parameters.

## Decision Engine
The decision engine is responsible for evaluating the collected data and making adjustments to network slices based on the trained model's predictions.

### Running the Decision Engine
To run the decision engine:
```bash
python scripts/decision_engine.py
```

- The decision engine loads the latest network data and the trained machine learning model.
- It makes a prediction and adjusts the network configuration accordingly.

## Executing Commands
Sometimes, you might need to execute specific commands on your network devices directly.

### Running Commands
Use the `execute_commands.py` script to run commands on Cisco devices.

Example:
```bash
python scripts/execute_commands.py
```

This script can execute any Cisco IOS command and return the output.

## KPI Monitoring
Monitoring KPIs (Key Performance Indicators) is critical to ensure the network is performing optimally.

### Starting KPI Monitoring
The `kpi_monitoring.py` script allows you to start monitoring KPIs.

To start monitoring:
```bash
python scripts/kpi_monitoring.py
```

- KPIs are exposed via a Prometheus exporter, allowing you to integrate them with your monitoring setup.

## Logging
All scripts in the framework produce logs that are stored in the `logs/` directory. These logs are crucial for troubleshooting and understanding the framework's behavior.

- **execution.log**: Contains logs related to successful execution.
- **error.log**: Captures any errors encountered during the script execution.

Ensure to monitor these logs regularly to keep track of the system’s health and debug issues.

## Testing
The framework includes unit tests to verify the correctness of its components.

### Running Tests
Tests are located in the `tests/` directory and can be run using the `pytest` framework.

To run all tests:
```bash
pytest
```

Each test script corresponds to a specific component of the framework, ensuring that each part functions correctly.

## Monitoring with Prometheus
The framework supports Prometheus for monitoring various KPIs.

### Prometheus Setup
1. Ensure Prometheus is installed and running on your monitoring server.
2. Start the Prometheus exporter by running the `prometheus_exporter.py` script:
   ```bash
   python monitoring/prometheus_exporter.py
   ```

### Accessing Metrics
- The Prometheus metrics are available at `http://<your-server>:8000/metrics`.
- Integrate these metrics into your Prometheus server to start monitoring the KPIs.

## Troubleshooting
If you encounter issues while using the framework, refer to the logs in the `logs/` directory.

### Common Issues
- **Connection Errors**: Verify your Cisco device IPs, usernames, and passwords in the Ansible inventory.
- **Model Training Issues**: Ensure your training data is correctly formatted and that the necessary features are included.
- **Command Execution Failures**: Double-check the commands being executed and the device's capability to run those commands.

If issues persist, consider consulting the relevant Cisco documentation or seeking help from the community.

---

This `user_guide.md` provides a comprehensive walkthrough of how to use the framework. Each section is designed to guide you through the essential tasks needed to operate and maintain the network slicing automation framework effectively.
