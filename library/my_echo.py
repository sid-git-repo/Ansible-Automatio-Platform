
#!/usr/bin/python
from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(message=dict(type='str', required=True))
    result = dict(changed=False, echoed=None)
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    msg = module.params['message']
    result['echoed'] = msg

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
