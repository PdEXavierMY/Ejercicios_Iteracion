def mcd(n, m):
  if n < m:
    return mcd(m, n)
  elif m == 0:
    return n
  else:
    return mcd(m, n%m)
print(str(mcd(5, 8)))