#Name- Nandika Jain
#Roll no-2019064
#Group no-1


def MatrixA(m,n):
	MatrixA=[] #Matrix A construction
	Matrix=[]
	print("Enter the entries row wise")
	for j in range(0,m):
		print("Entries of the "+str(j+1)+" row : ")
		for i in range(0,n):
			Matrix.append(int(input()))
		MatrixA.append(Matrix)
		Matrix=[]
	#print(MatrixA)
	print("The matrix A is :")
	for i in range(0,m):
		print(MatrixA[i])
	MatrixQ(MatrixA,m,n)

def Modulus(list):
	a=0
	for i in range(0,len(list)):
		a+=(list[i])**2
	return a**0.5

def DotProduct(l1,l2):
	l=len(l1)
	a=0
	for i in range(0,l):
		a+=l1[i]*l2[i]
	return a

def Projection(MatrixT,index):
	temp=0
	sum=0
	projection=[]
	temp2=[]
	temp3=[]



	#for j in range(0,index):
	for k in range(index-1,-1,-1):


		temp=DotProduct(MatrixT[index],MatrixT[k])/(DotProduct(MatrixT[k],MatrixT[k]))
		for l in range(0,len(MatrixT[0])):
			temp2.append((MatrixT[k][l])*temp)
		temp3.append(temp2)
		temp2=[]
			
	length=len(temp3)
	for p in range(0,len(MatrixT[0])):
		for q in range(0,length):
			sum+=temp3[q][p]
		projection.append(sum)
		sum=0
	#print(projection)
	return projection

def OrthogonalBasis(MatrixT,list,index):
	projection=Projection(MatrixT,index)
	for i in range(0,len(projection)):
		MatrixT[index][i]=MatrixT[index][i]-projection[i]
	return MatrixT[index]

def MatrixQ(MatrixA,m,n):
	MatrixQ=[] #Matrix Q construction 
	Matrix=[]
	MatrixT=[]
	temp=[]
	for j in range(0,n): #Transpose of Matrix A
		for i in range(0,m):
			Matrix.append(MatrixA[i][j])
		MatrixT.append(Matrix)
		Matrix=[]
	var=len(MatrixT)
	for i in range(0,var):
		MatrixT[i]=OrthogonalBasis(MatrixT,MatrixT[i],i)
	for i in range(0,var):
		mod=Modulus(MatrixT[i])
		for j in range(0,len(MatrixT[0])):
			MatrixT[i][j]=(MatrixT[i][j])/mod

	for j in range(0,m): #Transpose of the transpose matrix to get Matrix Q
		for i in range(0,n):
			temp.append(MatrixT[i][j])
		MatrixQ.append(temp)
		temp=[]
	print("The Matrix Q is :")
	for i in range(0,len(MatrixQ)):
		print(MatrixQ[i])
		
	MatrixQTranspose=MatrixTranspose(MatrixQ,m,n)
	MatrixReq=MatrixR(MatrixQTranspose,MatrixA)


def MatrixTranspose(MatrixQ,m,n):
	MatrixTranspose=[]  #Transpose of Matrix Q
	Matrix=[]
	for j in range(0,n):
		for i in range(0,m):
			Matrix.append(MatrixQ[i][j])
		MatrixTranspose.append(Matrix)
		Matrix=[]
	"""print("Transpose of Matrix Q is :")
	for i in range(0,n):
		print(MatrixTranspose[i])"""
	return MatrixTranspose

def MatrixR(MatrixTranspose,MatrixA):
	MatrixR=[] #Contruction of Matrix R of order nxn
	Matrix=[]
	n=len(MatrixTranspose) #no of rows of required matrix
	m=len(MatrixA[0]) #no of columns of matrix A
	for i in range(0,n):
		for j in range(0,m):
			l=0
			for k in range(0,len(MatrixA)):
				l+=MatrixTranspose[i][k]*MatrixA[k][j]
			Matrix.append(l)
		MatrixR.append(Matrix)
		Matrix=[]
	print("The Matrix R is :")
	for i in range(0,n):
		print(MatrixR[i])
	
m=int(input("Enter the no of rows :"))
n=int(input("Enter the no of columns :"))
MatrixA(m,n)
