
def print_msg(msg, error="No error",*kwargs):
	print ("Log :" +error+ ":" +msg )
	print(kwargs)


print_msg("This will be logged","File not found","1","2","32","234")
