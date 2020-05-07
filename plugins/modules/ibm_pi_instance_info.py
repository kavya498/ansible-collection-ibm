#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_pi_instance_info
short_description: Retrieve IBM Cloud 'ibm_pi_instance' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_pi_instance' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.5.2
    - Terraform v0.12.20

options:
    minmem:
        description:
            - None
        required: False
        type: int
    maxproc:
        description:
            - None
        required: False
        type: int
    pi_instance_name:
        description:
            - Server Name to be used for pvminstances
        required: True
        type: str
    pi_cloud_instance_id:
        description:
            - None
        required: True
        type: str
    processors:
        description:
            - None
        required: False
        type: int
    addresses:
        description:
            - None
        required: False
        type: list
        elements: dict
    minproc:
        description:
            - None
        required: False
        type: int
    maxmem:
        description:
            - None
        required: False
        type: int
    volumes:
        description:
            - None
        required: False
        type: list
        elements: str
    state:
        description:
            - None
        required: False
        type: str
    health_status:
        description:
            - None
        required: False
        type: str
    proctype:
        description:
            - None
        required: False
        type: str
    status:
        description:
            - None
        required: False
        type: str
    zone:
        description:
            - Denotes which IBM Cloud zone to connect to in multizone
              environment. This can also be provided via the environment
              variable 'IC_ZONE'.
        required: False
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('pi_instance_name', 'str'),
    ('pi_cloud_instance_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'minmem',
    'maxproc',
    'pi_instance_name',
    'pi_cloud_instance_id',
    'processors',
    'addresses',
    'minproc',
    'maxmem',
    'volumes',
    'state',
    'health_status',
    'proctype',
    'status',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    minmem=dict(
        required=False,
        type='int'),
    maxproc=dict(
        required=False,
        type='int'),
    pi_instance_name=dict(
        required=True,
        type='str'),
    pi_cloud_instance_id=dict(
        required=True,
        type='str'),
    processors=dict(
        required=False,
        type='int'),
    addresses=dict(
        required=False,
        elements='',
        type='list'),
    minproc=dict(
        required=False,
        type='int'),
    maxmem=dict(
        required=False,
        type='int'),
    volumes=dict(
        required=False,
        elements='',
        type='list'),
    state=dict(
        required=False,
        type='str'),
    health_status=dict(
        required=False,
        type='str'),
    proctype=dict(
        required=False,
        type='str'),
    status=dict(
        required=False,
        type='str'),
    zone=dict(
        type='str',
        fallback=(env_fallback, ['IC_ZONE'])),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_pi_instance',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.5.2',
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
