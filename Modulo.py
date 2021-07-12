def modular_exponent(base, exponent, modulus):          
    ans = 1;
    base = base % modulus 
    while (exponent > 0):
        if(exponent & 1):
            ans = (ans*base) % m
        exponent >>= 1
        base = (base**2) % m
    return ans
    
def modular_inverse_prime(x, m):                     ### when m is prime
    return modular_exponent(x, m-2, m)

def modular_multiplication(a, b, m):           
    ans = 0
    a = a % m
    while(b):
        if(b & 1):
            ans = (ans + a) % m
        b >>= 1
        a = (2*a) % m
    return ans

def modular_inverse_nonprime(x, m):
	r0 = x
	r1 = m
	s0 = 1
	s1 = 0
	while(r0 > 1):
		q = r0 // r1
		temp = r1
		r1 = r0 % r1
		r0 = temp
		temp = s1
		s1 = s0 - q*s1
		s0 = temp
	if(s0<0):
		s0 = s0+m
	return s0
		
	

m = 19807040628566084398385987581 
x = 11226815350263531814963336315 
y = 9190548667900274300830391220
z = 4138652629655613570819000497 

xz = modular_multiplication(x, z, m)                 
yinv = modular_inverse_prime(y, m)               ### yinv = y^-1
yinv2 = modular_exponent(yinv, 2, m)             ### yinv2 = y^-2
rhs = modular_multiplication(xz, yinv2, m)       ### rhs = xzy^-2
power = 5147
power_inv = modular_inverse_nonprime(power, m-1) 
g = modular_exponent(rhs, power_inv, m)          ### g = (xzy^-2)^{5147^-1}
print("g = " + str(g))
ginv = modular_inverse_prime(g, m)               ### ginv = g^-1
ginvp = modular_exponent(ginv, 324, m)           ### ginvp = g^-324
password = modular_multiplication(ginvp, x, m)   ### password = x*g^-324
print("password = " + str(password))
