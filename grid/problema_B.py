
def mdc(a, b):
  if b == 0:
    return a
  
  return mdc(b, a % b)

def mmc(a, b):
  return (a * b)/mdc(a, b)


while True:
  try:
    lista = list(map(int, input().split()))

    

    res = lista[0]
    for i in range(1, 4):
      res = mmc(lista[i], res)

    print(int(res))

  except EOFError:
    break