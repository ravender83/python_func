# -------------------------------------------
#	Date:			2022.10.30
#	Author:			Piotr Ślęzak
#	
#	Description:
#		Function is checking, if given string is in Siemens format:
#		Ix.y for inputs, Qx.y for outputs where x = [0-99999] and y = [0-7]
#		
#		str = 'I' if checking only inputs,
#		str = 'Q' if checking only outputs,
#		str = 'IQ' if checking inputs or outputs
#
#	ToDo:
#		-
# -------------------------------------------
import re


def tag_parse(tag, str):
    regex = re.compile('^['+str.upper()+'][0-9]{1,5}[.][0-7]')
    return True if regex.match(tag.upper()) else False
