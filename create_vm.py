from azure.identity import AzureCliCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import HardwareProfile, NetworkProfile, OSProfile, StorageProfile, VirtualMachine

def create_vm(resource_group_name, vm_name, location, admin_username, admin_password):
    # Hardcoded subscription ID for demonstration purposes, consider retrieving it securely
    subscription_id = '9718b645-776a-420e-b2a3-1e82dd1d1536'
    credentials = AzureCliCredential()

    compute_client = ComputeManagementClient(credentials, subscription_id)

    # Define VM parameters for Windows VM
    vm_parameters = {
        'location': location,
        'os_profile': {
            'computer_name': vm_name,  # Using vm_name instead of 'YOUR_COMPUTER_NAME'
            'admin_username': admin_username,
            'admin_password': admin_password
        },
        'hardware_profile': {
            'vm_size': 'Standard_B1s'
        },
        'storage_profile': {
            'os_disk': {
                'create_option': 'FromImage',
                'os_type': 'Windows',
                'disk_size_gb': 128
            },
            'image_reference': {
                'publisher': 'MicrosoftWindowsServer',
                'offer': 'WindowsServer',
                'sku': '2019-Datacenter',
                'version': 'latest'
            }
        },
        # Add other required parameters (network profile, etc.)
    }

    # Create VM with error handling
    try:
        async_vm_creation = compute_client.virtual_machines.create_or_update(
            resource_group_name, vm_name, VirtualMachine(vm_parameters)
        )
        async_vm_creation.wait()
        print("Virtual machine creation successful.")
    except Exception as e:
        print(f"Error creating virtual machine: {str(e)}")

# Usage example
create_vm('harshi', 'vm_py', 'westus', 'sriharshitha', 'SriHarshitha@123')

