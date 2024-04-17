from azure.identity import AzureCliCredential
from azure.mgmt.compute import ComputeManagementClient

def delete_vm(resource_group_name, vm_name):
    subscription_id = 'YOUR_SUBSCRIPTION_ID'
    credentials = AzureCliCredential()

    compute_client = ComputeManagementClient(credentials, subscription_id)

    # Delete VM
    async_vm_deletion = compute_client.virtual_machines.begin_delete(resource_group_name, vm_name)
    async_vm_deletion.wait()

# Usage example
delete_vm('myResourceGroup', 'myWindowsVM')
