class MagicList :
	def __init__(self):
		self.data = [0]
	
	def findMin(self):
		M = self.data
		''' you need to find and return the smallest
			element in MagicList M.
			Write your code after this comment.
		'''
		l=M[:]
		l1=sorted(l)
		if M==[0]:
			return 0
		else:
			return l1[1]		

	
	def insert(self, E):
		M = self.data
		''' you need to insert E in MagicList M, so that
			properties of the MagicList are satisfied. 
			Return M after inserting E into M.
			Write your code after this comment.
		'''
		s=[]
		for i in range(len(M)):
			s.append(M[i])
		z=len(s)
		k1=s[:]
		k1.append(E)
		if s==[0]:
			self.data = k1
		else:
			while z>0:
				if (k1[z//2])>(k1[z]):
					temp = k1[z]
					k1[z]=k1[z//2]
					k1[z//2]=temp
					z=z//2
				else:
					break
			self.data=k1	
	
	def deleteMin(self):
		M = self.data
		''' you need to delete the minimum element in
			MagicList M, so that properties of the MagicList
			are satisfied. Return M after deleting the 
			minimum element.
			Write your code after this comment.
		'''
		a=self.findMin()
		s=[]
		for i in range(len(M)):
			if M[i]==a:
				pass
			else:
				s.append(M[i])
		self.data = s
	
	def return_list(self):
		M=self.data
		s=M[:]
		return s

def K_sum(L, K):
	''' you need to find the sum of smallest K elements
		of L using a MagicList. Return the sum.
		Write your code after this comment.
	'''
	M1=MagicList()
	for z in range(len(L)):
		M1.insert(L[z])
	l1=M1.return_list()
	sum=l1[1]
	l1.remove(l1[0])
	for i in range(K):
		M=MagicList()
		for z in range(len(l1)):
			M.insert(l1[z])
		sum+=M.findMin()
		l1.remove(M.findMin())
	return sum

	
if __name__ == "__main__" :
	'''Here are a few test cases'''
	
	'''insert and findMin'''
	M = MagicList()
	M.insert(4)
	M.insert(3)
	M.insert(5)
	x = M.findMin()
	if x == 3 :
		print("testcase 1 : Passed")
	else :
		print("testcase 1 : Failed")
		
	'''deleteMin and findMin'''
	M.deleteMin()
	x = M.findMin()
	if x == 4 :
		print("testcase 2 : Passed")
	else :
		print("testcase 2 : Failed")
		
	'''k-sum'''
	L = [2,5,8,3,6,1,0,9,4]
	K = 4
	x = K_sum(L,K)
	if x == 6 :
		print("testcase 3 : Passed")
	else :
		print("testcase 3 : Failed")