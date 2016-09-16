#!/usr/bin/python
import sys
import simplejson as json

def main():
	if sys.argv[1] == "--list":
		print json.dumps({"virtual": {"hosts":["127.0.0.1"],"vars":{"ansible_ssh_port":"5222"}}})
	
	if sys.argv[1] == "--host":
		print json.dumps(dict())
	return 0
if __name__ == "__main__":
	main()


	


