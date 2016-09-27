#!/usr/bin/python
from ansible.module_utils.basic import *
import urllib2


def gettemp():
    return json.loads(urllib2.urlopen("https://api.myjson.com/bins/14bpw").read())

def main():
    fields = { "testvar": { "required"  : True , "type" : "str"  }}
    module = AnsibleModule(argument_spec=fields)
    response = gettemp()
    module.exit_json(changed=True, out=response , test=1)


if __name__ == '__main__':  
    main()
