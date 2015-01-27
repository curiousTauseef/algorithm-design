def mergesort(a):
  if len(a) <= 1:
    return a
  else:
    mid = len(a) // 2
    return merge(mergesort(a[:mid]), mergesort(a[mid:]))

def merge(left, right):
  merged = []
  while left and right:
    if left[0] < right[0]:
      merged.append(left.pop(0))
    else:
      merged.append(right.pop(0))
  merged.extend(left + right)
  return merged
