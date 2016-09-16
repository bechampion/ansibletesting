#!/usr/bin/python
from ansible.module_utils.basic import *

def main():
    fields = { "testvar": { "required"  : True , "type" : "str"  }}
    module = AnsibleModule(argument_spec=fields)
    response = {"demo":[1,2,3,4]}
    module.exit_json(changed=False, meta=response , test=1)


if __name__ == '__main__':  
    main()
