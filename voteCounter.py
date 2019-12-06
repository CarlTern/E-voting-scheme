import math
# Grump = +1
# Flint = -1

# Note that in Zn, the number “−x” is written as “n − x”.
def decryption (lambdaValue, n, mu, c):
    return (L(c**lambdaValue % n**2, n) * mu % n) 
    
# Least common multiple
def lcm(p, q):

    return int((p * q) / math.gcd(p,q))

def L(u, n):
    
    return int((u - 1) / n)

def getInverse(x, n):
    for i in range(1, n):
        if(i == x):
            continue
        elif((i * x) % n == 1):
            return i
    return None

if __name__ == "__main__":
    (p, q) = (5, 7)
    n = p * q
    Z = n**2 # This is the ring used for g
    g = 867
    file = open('votes.txt', 'rt')
    votes = file.read().splitlines()
    numberOfVotes = len(votes)
    file.close()
    productOfCiphers = 1
    lambdaValue = lcm(p-1, q-1)
    mu = getInverse(L(g**lambdaValue % Z, n), n)
    for vote in votes:
        productOfCiphers *= int(vote)
    productOfCiphers = productOfCiphers % Z
    print("Product of Ciphers:", productOfCiphers)

    decryptedValue = decryption(lambdaValue, n, mu, productOfCiphers)
    if(decryptedValue > n ):
        answer = decryptedValue
    else:
        answer = decryptedValue - n 
    print (answer)