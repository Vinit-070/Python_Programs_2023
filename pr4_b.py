# Find out the list of subjects of a particular semester from the input
# provided as a list of dictionaries using lambda, map and filter together.
# i/p:[{'sem':6,'sub':'python'},{'sem':6,'sub':'cns'},{'sem':5,'sub':'java'},
# {'sem':5,'sub':'daa'}] o/p:sem 6 subjects:['python','cns']

l1=[]
n=int(input("enter total no. of dictionaries: "))
for i in range(0,n):
	d={}
	d['sem']=int(input("enter the semester: "))
	d['sub']=input("enter subject: ")
	l1.append(d)
a=int(input("enter the semester to find the subjects: "))
f=filter(lambda d : d['sem']==a,l1)
l2=(list(map(lambda d: d['sub'],f)))
print(l2)
