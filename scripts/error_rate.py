import re

def error_rate_calculation(log_path):
    with open(log_path, 'r') as file:
        log_content = file.read()

    # Simple regex to detect errors in logs
    errors = re.findall(r'ERROR|Error|error', log_content)
    error_count = len(errors)

    print(f"Number of Errors Detected: {error_count}")
    return error_count

if __name__ == "__main__":
    error_count = error_rate_calculation('../logs/error.log')
```