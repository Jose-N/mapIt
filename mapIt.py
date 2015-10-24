#! python 3
# mapIt.py
# Launches a map in the bowser using an address from the command line or clipboard.

import webbrowser, sys
if len(sys.argv) > 1:
	# Get address from the command line.
	address = ''.join(sys.argv[1:])

# TODO: Get address from the clipboard
