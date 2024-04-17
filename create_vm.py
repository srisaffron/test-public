from azure.identity import AzureCliCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import HardwareProfile, NetworkProfile, OSProfile, StorageProfile, VirtualMachine, VirtualMachineProperties

def create_vm(resource_group_name, vm_name, location, admin_username, admin_password):
    subscription_id = 'YOUR_SUBSCRIPTION_ID'
    credentials = AzureCliCredential()

    compute_client = ComputeManagementClient(credentials, subscription_id)

    # Define VM parameters for Windows VM
    vm_parameters = {
        'location': location,
        'os_profile': {
            'computer_name': vm_name,
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

    # Create VM
    async_vm_creation = compute_client.virtual_machines.create_or_update(
        resource_group_name, vm_name, VirtualMachine(vm_parameters)
    )

    async_vm_creation.wait()

# Usage example
create_vm('myResourceGroup', 'myWindowsVM', 'eastus', 'azureuser', 'Passw0rd1234')
