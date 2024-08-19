To set up network devices on Cisco DevNet Sandbox and test this framework, follow these steps:

### 1. **Access Cisco DevNet Sandbox**

1. **Sign Up/Log In:**
   - Go to [Cisco DevNet Sandbox](https://developer.cisco.com/sandbox/).
   - Create a Cisco DevNet account or log in if you already have one.

2. **Browse and Reserve a Sandbox:**
   - Navigate to the "Sandbox" section.
   - Browse available sandboxes by category or search for specific devices.
   - For network slicing, look for sandboxes with Cisco IOS or IOS-XE devices.

3. **Reserve a Sandbox:**
   - Select a sandbox that fits your needs (e.g., Cisco IOS-XE, Cisco CSR 1000V).
   - Reserve the sandbox by choosing the reservation options (start time, duration).

4. **Access Credentials:**
   - Once reserved, you will receive credentials (IP address, username, password) for accessing the devices.

### 2. **Configure Ansible for Cisco DevNet Sandbox**

1. **Update Inventory:**
   - Modify your `inventory.yaml` file in `config/ansible/` with the provided sandbox credentials.
   ```yaml
   all:
     hosts:
       cisco_device:
         ansible_host: <SANDBOX_IP>
         ansible_user: <USERNAME>
         ansible_password: <PASSWORD>
         ansible_network_os: ios
   ```

2. **Test Ansible Playbooks:**
   - Ensure you have Ansible installed. If not, install it using:
     ```sh
     pip install ansible
     ```
   - Test the `adjust_bandwidth.yaml` and `collect_data.yaml` playbooks by running:
     ```sh
     ansible-playbook -i config/ansible/inventory.yaml config/ansible/playbooks/collect_data.yaml
     ```

### 3. **Update and Test Python Scripts**

1. **Update Scripts with Sandbox Credentials:**
   - Update any hardcoded credentials or IP addresses in your Python scripts (e.g., `data_collection.py`, `execute_commands.py`).
   ```python
   if __name__ == "__main__":
       collect_data('<SANDBOX_IP>', '<USERNAME>', '<PASSWORD>')
   ```

2. **Run Python Scripts:**
   - Ensure all dependencies are installed:
     ```sh
     pip install -r requirements.txt
     ```
   - Test individual scripts. For example:
     ```sh
     python scripts/data_collection.py
     python scripts/execute_commands.py
     ```

### 4. **Verify Model and Monitoring**

1. **Test ML Model:**
   - Ensure the model training and decision-making scripts work with the sandbox data. For example:
     ```sh
     python scripts/ml_model_training.py
     ```

2. **Monitor KPIs:**
   - Start the Prometheus exporter:
     ```sh
     python monitoring/prometheus_exporter.py
     ```
   - Verify KPI values using Prometheus or a similar monitoring tool.

### 5. **Review Logs and Debug**

1. **Check Logs:**
   - Review `logs/execution.log` and `logs/error.log` for any issues during script execution.

2. **Debug Issues:**
   - If you encounter errors, verify the sandbox configuration, check network connectivity, and ensure that all dependencies are correctly installed and configured.

By following these steps, you can effectively set up network devices on Cisco DevNet Sandbox and test this Python-based automation framework.
