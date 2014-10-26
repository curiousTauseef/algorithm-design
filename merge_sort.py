import numpy.random as rn
def msort (a):
  if len(a) <= 1:
    return a

  m = len(a)//2
  l = a[:m]
  r = a[m:]
  return merge (msort(l), msort(r))

def merge (l, r):
  merged = []
  while l and r:
    if l[0] < r[0]:
      merged.append(l.pop(0))
    else:
      merged.append(r.pop(0))
  merged.extend(l)
  merged.extend(r)
  return merged