file_name = "my_task.txt"

#f =  open(file_name,'w')
#f.write("1.Attend the meetup")
#f.write("2.Go home and get sleep")
#f.write("3.Make sure you had lauch before going to sleep")
#f.close()

#print("File Written Successfully")

with open("my_task.txt",'a') as f:
	f.write("4.Complete the python")

print("Done") 
