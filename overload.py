from math import *

class Vector3D():
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z

    def __str__(self):
        return '({},{},{})'.format(self.x,self.y,self.z)
    
    def __add__(self,other):
		try:
			a=Vector3D(self.x+other.x,self.y+other.y,self.z+other.z)
		except Exception:
			a=Vector3D(self.x+other,self.y+other,self.z+other)
		return a
	
	def __sub__(self,other):
		
		try:
			a=Vector3D(self.x-other.x,self.y-other.y,self.z-other.z)
		except Exception:
			a=Vector3D(self.x-other,self.y-other,self.z-other)
		return a		
    
    def __mul__(self,other):
        a=Vector3D()
        try:
            a.x=self.y*other.z-self.z*other.y
            a.y=self.z*other.x-self.x*other.z
            a.z=self.x*other.y-self.y*other.x
        except Exception:
            a.x=self.x*other
            a.y=self.y*other
            a.z=self.z*other
        return a

    def __div__(self,other):

        return Vector3D(self.x/other,self.y/other,self.z/other)

    def __abs__(self):

        return sqrt(self.x**2+self.y**2+self.z**2)

    def norm(self):
        return self/abs(self)
        
        
    def __pow__(self,other):
		
        return (self.x*other.x+self.y*other.y+self.z*other.z)


if __name__=="__main__":
	vec=Vector3D(1,1,0)
	vec2=Vector3D(1,-1,0)
	vec3=vec*vec2
	vec4=vec*2.
	print str(vec3),'\n'
	print str(vec/2.),"\n"
	print str(vec.norm()),'\n'
	print str(vec4)
