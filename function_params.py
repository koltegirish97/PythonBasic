
#difference between *kwargs and **kwargs
def print_msg(msg, error="No error", *args, **kwargs):
	print ("Log :" +error+ ":" +msg )
	print("Args :", args)
	print("kwargs :", kwargs)


print_msg("This will be logged","File not found", "abcd", key= "1,2,32,234",key_2 = "23,45,45,67,677,78")
