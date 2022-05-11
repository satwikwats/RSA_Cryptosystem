#Karatsuba multiplication
import random
def mult(a,b):
    result=0
    while b>0:
        if b & 1: #& performs bitwise operator
            result+=a
        a=a<<1# this function doubles the value of a
        b=b>>1
#multi is my defined function that will perform karatsuba multiplication
def multi(x,y):
    
    
    n1=len(str(x))  ## detremining length of x and y 
    
    n2=len(str(y))
    
    if n1==1 or n2==1: #Assert: If n1 or n2 are equal to zero then perform simple multiplication
        return x*y
    
    else:
        n=max(n1,n2)//2 #We split them in half
    
        a=x//10**n # 10**n becomes my new base 
        
        b=x%10**n # mod of this plus above value will return my entire function.
        ## Example: 12345= 12*10**3+345
        
        c=y//10**n ## repeat the same steps
        d=y%10**n
        
        ac=multi(a,c) #Now we again recursively compute ac and bd then ad_bc
        
        bd=multi(b,d)
        
        ad_bc=multi(a+b,c+d)-ac-bd #reducing 4 multiplication to 3 multiplication
        
        return ac*10**(2*n)+ad_bc*10**n+bd ## return fucntion in its normal form
    
    
x=5679876543456709876567876545654567890567890
y=4567899876548765434876567876556456789076547
print(multi(x,y))

def powe(x, n):
##Computing the power of a number  with base x and power n
    
    if n == 0: ## if n=0 we return 1, as 2^0=1
        return 1
 
    
    p = powe(x, n // 2) # WE use the dividing technique
 
    if n & 1:    #if the number is odd we do one extra step
        return x * p * p
 
    #if the number is odd we continue with our even mulitplication steps
    return p * p
x=50000
n=200567



def expo(x, y, n):
    
    if (x == 0):
        return 0
    if (y == 0):
        return 1
    

    i = 0
    if (y % 2 == 0):
        i = expo(x, y // 2, n)
        i = (i*i) % n
    
    else:
        i = x % n
        i = (i * expo(x, y - 1,n) % n) % n
    return ((i + n) % n)

expo(2,5,2) #testing the function


def divide(x,y):
    if x == 0: ##if x=0 return 0
        return (0,0)
    
    elif y==0: ##if y=0 return 'Error'
      
      
        print('Error')    
    
    
    elif x==0 and y==0: ##if both x and y are 0 return 0
        print('Error')
    
    #For 0<=n<x divide (n,y) to return (q,r) such that n=qy+r 
    else:
        (q,r) = divide(x // 2, y)
        q1 = 2*q
        r1 = 2*r
        ## If x is odd then divide(x//2, y) and return r=2*q+1
        if (x%2 == 1):
            r2 = r1+1
            if (r2<y): ##if r2 is less than y then return (2*q,2*q+1) 
                return (q1,r2)
            else: #if r2>y then return (q1+1,r2 − y = 2r + 1 − y)
                return (q1+1,r2-y)
        ##if the x is odd 
        #then algorithm returns x = (q1 + 1)y + (r1 − y)
        else:
            if (r1<y):
                return (q1,r1)
            else:
                return(q1+1,r1-y)
def rem(d) : #This function finds the mod value of (x,y)
    return d[1]
rem(divide(5,2))

#PRIMALITY TESTING
def isPrime(a):
    if a==2:
        return True
    i=0
    while i<5:
        p=np.random.randint(2,20)
        if expo(p,a-1,a)!=1:
            return False
        else:
            return True
        i+=1 
  
p,q=467149188829,347477903887
# p,q=537649271309,541603558003
# p,q=2427965704063,2518504668809
# p,q=2427965704063,3350445728171
# p,q=2427965704063,2631097573639 ##Random set of prime p and q to use for RSA
# p,q=373873957969,340792830107
# p,q=312321158183,478344924017

print(p,q)
n=multi(p,q)
#ruler's function
phi=multi((p-1),(q-1))
print(phi)


def gcd(e, phi):
    
    while phi != 0:
        e, phi = phi, rem(divide(e,phi))
    return e

def euclid_ext_algo(a,b): #x = y1 - ⌊b/a⌋ * x1  ##y = x1
    de,re=divide(a,b)
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,x,t = euclid_ext_algo(b,re) #recursive call of  gcd(b,a%b)
        f=multi((de),t)
        x =x-f
        return(gcd,t,x)
  
  
def mulinv(e,phi):
    gcd,x,_=euclid_ext_algo(e,phi)
    if(gcd!=1):
        return None
    else:
        if(x<0):
            (x,x,rem(divide(x,phi)))
        elif(x>0):
            print(x)
        return rem(divide(x,phi)) 
    

def priv_pub(p,q):
    n=multi(p,q)
    phi=multi((p-1),(q-1))
    e = random.randrange(1, 1000000)

    value = gcd(e, phi)
    while value != 1:
        e = random.randrange(1, 1000000)
        value = gcd(e, phi)
    d=mulinv(e,phi)
    return (d,n),(e,n)
  
  
def encrypt(pub_key, message):
    d, n = pub_key
    secret = [expo(ord(char), d,n) for char in message] 
    return secret


def decrypt(pri_key, secret):
    e, n = pri_key
    message = [chr(expo(char,e,n)) for char in secret]

    return ''. join(message)  
  
  
  
public,private=priv_pub(p,q)
print(public,private)

msg='Is this okay?' ##Enter your message!!
value=encrypt(public,msg)
print(value)

 
f=(input('Do you wanna decrypt your message? If yes type "yes" otherwise "no": '))
if f=='yes':
    print(decrypt(private,value))
elif f=='no':
    print('Your loss!!')
else:
    print('Wrong option bud!')
  






