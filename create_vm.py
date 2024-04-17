from azure.identity import AzureCliCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import HardwareProfile, NetworkProfile, OSProfile, StorageProfile, VirtualMachine, VirtualMachineProperties

def create_vm(resource_group_name, vm_name, location, admin_username, admin_password):
    subscription_id = 9718b645-776a-420e-b2a3-1e82dd1d1536
    credentials = AzureCliCredential()

    compute_client = ComputeManagementClient(credentials, 9718b645-776a-420e-b2a3-1e82dd1d1536)

    # Define VM parameters
    vm_parameters = {
        'location': westus,
        'os_profile': {
            'computer_name': vm_py,
            'admin_username': sriharshitha,
            'admin_password': SriHarshitha@123
        },
        'hardware_profile': {
            'vm_size': 'Standard_B1s'
        },
        # Add other required parameters (storage profile, network profile, etc.)
    }

    # Create VM
    async_vm_creation = compute_client.virtual_machines.create_or_update(
        resource_group_name, vm_name, VirtualMachine(vm_parameters)
    )

    async_vm_creation.wait()

# Usage example
create_vm('borra', 'vm_py', 'westus', 'sriharshitha', 'SriHarshitha@123')
