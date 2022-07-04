from sympy import *
from sympy.plotting import *

def newton(f, df, x0, epsilon, maxIter):    #f = Função f; df = Derivada de f; x0 = Aproximação inicial; epsilon = Precisão/Erro; maxIter = Máximo de iterações
  contador = 0
  if abs(f(x0)) == 0:   #Verifica se x0 é raíz
    print("\nO X\u2080 inserido já é uma raíz da função %s" % (funcao))
    return (0, x0, contador)          #Retorna x0 e encerra

  print("\nk \t x \t\t |f(x)| \t |X\u2099 - X\u2099\u208b\u2081|")          #Cabeçalho
  print("%d \t %.5f \t %.5f \t" % (0, x0, abs(f(x0))))    #Aproximação inicial

  for k in range(1, maxIter+1):   #Iterações
    if df(x0) == 0:         #Verificação do erro da derivada nula
      print("\n\033[1;31mErro!\nO método encontrou uma derivada nula!")
      return (1, x0, contador)

    x1 = x0 - f(x0) / df(x0)    #Fórmula de Newton-Raphson
    print("%d \t %.5f \t %.5f \t %.5f" % (k, x1, abs(f(x1)), abs(x1-x0)))    #Resultado das iterações
    contador += 1

    if abs(f(x1)) < epsilon and abs(x1-x0) < epsilon:   #Verificação dos dois critérios de parada
       print("\nOs critérios de parada |f(x)| < \u03B5 e |X\u2099 - X\u2099\u208b\u2081| < \u03B5 foram atingidos!")
       return (0, x1, contador)         #Retorna a raíz encontrada e encerra

    elif abs(f(x1)) < epsilon:   #Verificação do primeiro critério de parada
      print("\nO critério de parada |f(x)| < \u03B5 foi atingido!")
      return (0, x1, contador)          #Retorna a raíz encontrada e encerra

    elif abs(x1-x0) < epsilon:  #Verificação do segundo critério de parada
      print("\nO critério de parada |X\u2099 - X\u2099\u208b\u2081| < \u03B5 foi atingido!")
      return (0, x1, contador)          #Retorna a raíz encontrada e encerra

    x0 = x1

  print("\n\033[1;31mNúmero máximo de iterações atingido!")  #Atingiu o máximo de iterações
  return (1, x1, contador)   #Retorna a última raíz encontrada

def f(x):   #Função f
  return eval(funcao)

def df(x):    #Derivada de f(x)
  return eval(derivada)

#Parâmetros
x = symbols("x")
e = symbols("e")
v = symbols("v")

funcao = input("f(x): ")
funcao = funcao.replace("^", "**")
funcao = funcao.replace(",", ".")
funcao = funcao.replace("e", "E")
funcao = funcao.replace("v", "sqrt")

derivada = str(diff(funcao))

x0 = input("X\u2080: ")
x0 = float(x0.replace(",", "."))

epsilon = input("\u03B5: ")
epsilon = float(epsilon.replace(",", "."))

maxIter = int(input("Máximo de Iterações: ")) 

(erro, raiz, contador) = newton(f, df, x0, epsilon, maxIter)

if erro:
  print("\033[1;31mA última aproximação da raíz encontrada foi %.5f, após %d iterações.\n" % (raiz, contador))

elif raiz is not None:
  if contador == 0:
    print("\033[1mA raíz encontrada foi: %.5f\n" % (raiz))
  elif contador > 0:
    print("A aproximação da raíz encontrada foi \033[1;30;47m%.5f\033[0m, após %d iterações.\n" % (raiz, contador))

plot(eval(funcao), (x, -5,5), title= "Gráfico da Função", legend=true)
