import re
import argparse

parser = argparse.ArgumentParser(description='Used to convert a MAC address to a \'Cisco Compatible\' mac address (xxxx.xxxx.xxxx).\nFormat is C:\>modmac.py [mac address]')
parser.add_argument('mac', help='MAC address')
args = parser.parse_args()
arg_mac = args.mac

lower_mac = arg_mac.lower() #Lowercase the characters
lower_mac = ''.join(e for e in lower_mac if e.isalnum()) #If not already valid, drop all the special characters and modify it to be compatible
lower_mac = re.sub(r'(.{4})(?!$)', r'\1.', lower_mac)
pattern = re.compile('([0-9a-f]{4}[\.]){2}([0-9a-f]{4})')
if pattern.findall(lower_mac): #Validate that it's good
  print lower_mac
else:
	print 'MAC in wrong format' #If not good, throw an error
