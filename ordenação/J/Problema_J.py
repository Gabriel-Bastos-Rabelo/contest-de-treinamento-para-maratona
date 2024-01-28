def josephus(A, P):
    if A == 1:
        return 1
    else:
        return (josephus(A - 1, P) + P - 1) % A + 1



while True:
  
    
  try:
     
     a, p = map(int, input().split())

     print(josephus(a, p))
    
      
  except EOFError:
    break