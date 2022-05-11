import random
import numpy as np
import math 

##Primality testing

def isPrime(a):
    if a==2:
        return True
    i=0
    while i<5:
        p=np.random.randint(2,20)
        if pow(p,a-1,a)!=1:
            return False
        else:
            return True
        i+=1 
       
def generateLargePrime(k):  ## Large prime number generator code from
## Code from https://langui.sh/2009/03/07/generating-very-large-primes/
    
     #k is the desired bit length
    r=(100*(math.log(k,2)+1)) #number of attempts max
    r_ = r
    while r>0:
        #randrange is mersenne twister and is completely deterministic
        #unusable for serious crypto purposes
        n = random.randrange(pow(2,(k-1)),pow(2,(k)))
        r-=1
        if isPrime(n) == True:
            return n
    return "Failure after "+r_ + " tries."


p=generateLargePrime(1500)
#p=37
print(p)

q=generateLargePrime(1500)
#q=13
print(q)
n=(p*q)
phi=((p-1)*(q-1))
print(phi)

def gcd(e, phi):
    while phi != 0:
        e, phi = phi, e%phi
    return e
    


def euclid_ext_algo(a,b): #x = y1 - ⌊b/a⌋ * x1  ##y = x1
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,x,t = euclid_ext_algo(b,a%b) #recursive call of  gcd(b,a%b)
        
        
        x =x-((a//b)*t)
        return(gcd,t,x)
    
def mulinv(e,phi):
    gcd,x,_=euclid_ext_algo(e,phi)
    if(gcd!=1):
        return None
    else:
        if(x<0):
            (x,x,x%phi)
        elif(x>0):
            print(x)
        return x%phi 
    

def priv_pub(p,q):
    n=(p*q)
    phi=((p-1)*(q-1))
    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d=mulinv(e,phi)
    return (d,n),(e,n)
    
    
def encrypt(pub_key, message):
    d, n = pub_key
    secret = [pow(ord(char), d,n) for char in message]
    return secret


def decrypt(pri_key, secret):
    e, n = pri_key
    message = [chr(pow(char,e,n)) for char in secret]

    return ''. join(message)
    
    
public,private=priv_pub(p,q)
print(public,private)


msg='Is this good?' ##Enter your message!!
value=encrypt(public,msg)
print(value)


f=(input('Do you wanna decrypt your message? If yes type "yes" otherwise "no": '))
if f=='yes':
    print(decrypt(private,value))
elif f=='no':
    print('Your loss!!')
else:
    print('Wrong option bud!')
