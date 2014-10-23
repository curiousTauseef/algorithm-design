def sort_and_count(A, n):
  if n == 1:
    return (A, 0)
  else:
    middle = n//2
    (left, count_left) = sort_and_count(A[:middle], middle)
    (right, count_right) = sort_and_count(A[middle:], n-middle)
    (merged, count_split) = merge_and_count_split(left, right)
    return (merged, count_left+count_right+count_split)

def merge_and_count_split(left, right):
  count = 0
  merged = []
  while left or right:
    if left and right:
      if left[0] <= right[0]:
        merged.append(left[0])
        left = left [1:]
      else:
        merged.append(right[0])
        right = right[1:]
        count += len(left)
    elif left:
      merged.append(left[0])
      left = left[1:]
    elif right:
      merged.append(right[0])
      right = right[1:]
  return (merged, count)
