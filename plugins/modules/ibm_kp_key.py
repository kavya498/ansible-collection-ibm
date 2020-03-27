#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_kp_key
short_description: Configure IBM Cloud 'ibm_kp_key' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_kp_key' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.6
    - Terraform v0.12.20

options:
    key_protect_id:
        description:
            - (Required for new resource) 
        required: False
        type: str
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    resource_group_name:
        description:
            - The resource group name in which resource is provisioned
        required: False
        type: str
    key_id:
        description:
            - None
        required: False
        type: str
    force_delete:
        description:
            - set to true to force delete the key
        required: False
        type: bool
        default: False
    iv_value:
        description:
            - Only for imported root key
        required: False
        type: str
    resource_crn:
        description:
            - The crn of the resource
        required: False
        type: str
    standard_key:
        description:
            - None
        required: False
        type: bool
        default: False
    payload:
        description:
            - None
        required: False
        type: str
    encrypted_nonce:
        description:
            - Only for imported root key
        required: False
        type: str
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about the resource
        required: False
        type: str
    key_name:
        description:
            - (Required for new resource) 
        required: False
        type: str
    crn:
        description:
            - Crn of the key
        required: False
        type: str
    resource_name:
        description:
            - The name of the resource
        required: False
        type: str
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
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
    ('key_protect_id', 'str'),
    ('key_name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'key_protect_id',
    'resource_status',
    'resource_group_name',
    'key_id',
    'force_delete',
    'iv_value',
    'resource_crn',
    'standard_key',
    'payload',
    'encrypted_nonce',
    'resource_controller_url',
    'key_name',
    'crn',
    'resource_name',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    key_protect_id=dict(
        required=False,
        type='str'),
    resource_status=dict(
        required=False,
        type='str'),
    resource_group_name=dict(
        required=False,
        type='str'),
    key_id=dict(
        required=False,
        type='str'),
    force_delete=dict(
        default=False,
        type='bool'),
    iv_value=dict(
        required=False,
        type='str'),
    resource_crn=dict(
        required=False,
        type='str'),
    standard_key=dict(
        default=False,
        type='bool'),
    payload=dict(
        required=False,
        type='str'),
    encrypted_nonce=dict(
        required=False,
        type='str'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    key_name=dict(
        required=False,
        type='str'),
    crn=dict(
        required=False,
        type='str'),
    resource_name=dict(
        required=False,
        type='str'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
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

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_kp_key',
        tf_type='resource',
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
