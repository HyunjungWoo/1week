import math

class vector:

	def __init__(self,x = 0.0 , y =0.0 ,limit = 9999): #��ü ���� ����
		self.x = x
		self.y = y
		self.limit = limit

	def __add__(self,other):  # v3 = v1(self) + v2(other)
		return vector(self.x+other.x, self.y+other.y)

	def __sub__(self,other):
		return vector(self.x - other.x,self.y - other.y)

	def __mul__(self,other):
		return vector(self.x*other.x,self.y*other.y)
	
	def __truediv__(self,other):
		return vector(self.x/other.x,self.y/other.y)

	#���� ����
	def dotVector(self,other):
		return (self.x*other.x) + (self.y * other.y)

	#���� ����
	delf corssVecotr(self,other1,other2):
		pass

		def angleVector(self): # ���������κ��� ������ ������ ���ϴ� �Լ� 
		# -y ������ ��ǥ��� y�� ���ٷ�
		theta = math.atan2(0-self.y,self.x)
		deg = theta * 180.0 /math.pi

		if deg <0:
			deg += 360;
		return deg

	def angleBetweenVector(self,v2): #�� ������ ���̰�
		v = vector(self.x,self.y,self.limit)
		v.normalize()
		v2.normalize()

		theta = v.dotVecter(v2)
		theta = math.acos(theta)
		deg = theta * 180.0 / math.pi
		return deg

	#���� ����ȭ(��������,ũ�� 1��)
	def normalize(self): #������ ���� ���� ���ϱ� �Լ� 
		#��Ÿ����� ����(���� ���ϱ�)
		mag = math.sqrt(self.x * self.x + self.y *self.y)

		if mag>0:
			self.x /= mag
			self.y /= mag

	def setLimit(self,limit):
		self.limit = limit
		
		#copysign (x,y) y�� ��ȣ�� ���� x�� ����

		if abs(self.x) > self.limit:	
			self.x = math.copysign(limit,self.x)

		if abs(self.y) > self.limit:
			self.y = math.copysign(limit,self.y)
	
