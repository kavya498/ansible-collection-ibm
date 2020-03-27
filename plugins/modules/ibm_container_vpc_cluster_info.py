#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_vpc_cluster_info
short_description: Retrieve IBM Cloud 'ibm_container_vpc_cluster' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_container_vpc_cluster' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.6
    - Terraform v0.12.20

options:
    resource_group_name:
        description:
            - The resource group name in which resource is provisioned
        required: False
        type: str
    workers:
        description:
            - None
        required: False
        type: list
        elements: str
    worker_pools:
        description:
            - None
        required: False
        type: list
        elements: dict
    alb_type:
        description:
            - None
        required: False
        type: str
        default: all
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    private_service_endpoint:
        description:
            - None
        required: False
        type: bool
    public_service_endpoint_url:
        description:
            - None
        required: False
        type: str
    resource_crn:
        description:
            - The crn of the resource
        required: False
        type: str
    ingress_hostname:
        description:
            - None
        required: False
        type: str
    public_service_endpoint:
        description:
            - None
        required: False
        type: bool
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    resource_name:
        description:
            - The name of the resource
        required: False
        type: str
    albs:
        description:
            - None
        required: False
        type: list
        elements: dict
    ingress_secret:
        description:
            - None
        required: False
        type: str
    crn:
        description:
            - CRN of resource instance
        required: False
        type: str
    master_url:
        description:
            - None
        required: False
        type: str
    health:
        description:
            - None
        required: False
        type: str
    kube_version:
        description:
            - None
        required: False
        type: str
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster
        required: False
        type: str
    cluster_name_id:
        description:
            - Name of the cluster
        required: True
        type: str
    worker_count:
        description:
            - Number of workers
        required: False
        type: int
    private_service_endpoint_url:
        description:
            - None
        required: False
        type: str
    status:
        description:
            - The status of the cluster master
        required: False
        type: str
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    ibmcloud_api_key:
        description:
            - The API Key used for authentification. This can also be
              provided via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False
    ibmcloud_zone:
        description:
            - Denotes which IBM Cloud zone to connect to in multizone
              environment. This can also be provided via the environmental
              variable 'IC_ZONE'.
        required: False

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('cluster_name_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'resource_group_name',
    'workers',
    'worker_pools',
    'alb_type',
    'resource_group_id',
    'private_service_endpoint',
    'public_service_endpoint_url',
    'resource_crn',
    'ingress_hostname',
    'public_service_endpoint',
    'tags',
    'resource_name',
    'albs',
    'ingress_secret',
    'crn',
    'master_url',
    'health',
    'kube_version',
    'resource_controller_url',
    'cluster_name_id',
    'worker_count',
    'private_service_endpoint_url',
    'status',
    'resource_status',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    resource_group_name=dict(
        required=False,
        type='str'),
    workers=dict(
        required=False,
        elements='',
        type='list'),
    worker_pools=dict(
        required=False,
        elements='',
        type='list'),
    alb_type=dict(
        default='all',
        type='str'),
    resource_group_id=dict(
        required=False,
        type='str'),
    private_service_endpoint=dict(
        required=False,
        type='bool'),
    public_service_endpoint_url=dict(
        required=False,
        type='str'),
    resource_crn=dict(
        required=False,
        type='str'),
    ingress_hostname=dict(
        required=False,
        type='str'),
    public_service_endpoint=dict(
        required=False,
        type='bool'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    resource_name=dict(
        required=False,
        type='str'),
    albs=dict(
        required=False,
        elements='',
        type='list'),
    ingress_secret=dict(
        required=False,
        type='str'),
    crn=dict(
        required=False,
        type='str'),
    master_url=dict(
        required=False,
        type='str'),
    health=dict(
        required=False,
        type='str'),
    kube_version=dict(
        required=False,
        type='str'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    cluster_name_id=dict(
        required=True,
        type='str'),
    worker_count=dict(
        required=False,
        type='int'),
    private_service_endpoint_url=dict(
        required=False,
        type='str'),
    status=dict(
        required=False,
        type='str'),
    resource_status=dict(
        required=False,
        type='str'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True),
    ibmcloud_region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_zone=dict(
        type='str',
        fallback=(env_fallback, ['IC_ZONE']))
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_container_vpc_cluster',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.2.6',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=ibmcloud.Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
