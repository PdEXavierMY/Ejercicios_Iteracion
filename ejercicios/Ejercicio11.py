def mcd(n, m):
  if n < m:
    return mcd(m, n)
  elif m == 0:
    return n
  else:
    return mcd(m, n%m)
print(str(mcd(28, 360)))

def mcdresta(n, m): 
    if n < m:
      return mcdresta(m, n)
    if m == 0: 
        return n 
    if n == m: 
        return n 
    if n > m: 
        return mcdresta(n-m, m) 
    return mcdresta(n, m-n)
print(str(mcdresta(28, 360)))