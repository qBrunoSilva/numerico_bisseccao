import argparse
from math import * 
 
OKGREEN = '\033[92m' 
ENDC = '\033[0m'
BOLD = '\033[1m' 
FAIL = '\033[91m'

class CLI:
  def __init__(self): 
    self.args = self.parse_args()

  def parse_args(self):
    parser = argparse.ArgumentParser(
      add_help=True,
      description="Calcula a raiz de uma função pelo método da bissecção",
      usage="dt --help",
    )

    parser.add_argument(
      "--f", 
      type=str,
      help="Função a ser calculada",      
      nargs="?",
    )

    
    parser.add_argument( 
      "--x0",
      type=str,
      help="x0",
    )
    
    parser.add_argument( 
      "--x1",
      type=str,
      help="x1",
    )
    
    parser.add_argument( 
      "--tol",
      type=str,
      help="Tolerância",
    )


    return parser.parse_args()

  def bisect(self, f, a, b, tol=1.0e-9):
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if fa*fb > 0.0: raise Exception(f"{FAIL}Nenhuma raiz encontrada{ENDC}")

    n = int(ceil(log(abs(b-a)/tol)/log(2.0))) 
    
    iteracao = 0
    for _ in range(n): 
        c = 0.5*(a + b) 
        fc = f(c)
        if fc == 0.0: return c
        if fa*fc < 0.0:
            b = c; fb = fc
        else:
            a = c; fa = fc
            
        iteracao += 1
        print(f"Iteração {iteracao}\nx{iteracao} = {c}") 
        print("-" * 30) 

    return 0.5*(a + b), iteracao

          
  def format_function(self, f): 
    f = f.replace("^", "**")
    f = f.replace("sen", "sin")
    f = f.replace("ln", "log") 
    f = f.replace("\n", "")
    f = f.replace("\t", "")
    f = f.replace(" ", "")
    return f

  def run(self) -> None:
    # Executa o programa 

    func = self.args.f or input('Digite a função: ')
    func = self.format_function(func)

    f =  eval(f"lambda x: {func}")
    x0 = self.args.x0 or input("x0: ")
    x1 = self.args.x1 or input("x1: ")
    tol = self.args.tol or input("Tolerância: ") 

    print("\n")
    raiz, iteracoes = self.bisect(f, float(x0), float(x1), float(tol))

    
    print(f"Função: {func}")
    print(f"x0: {x0}")
    print(f"x1: {x1}")
    print(f"Tolerância: {tol}") 
    print(f"\nA raiz é {BOLD}{OKGREEN}{raiz}{ENDC} com {BOLD}{OKGREEN}{iteracoes}{ENDC} iterações") 
    print("-" * 30 + "\n") 