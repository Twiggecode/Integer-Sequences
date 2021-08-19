// Calculate the nth fibonacci number


def fibonacci_recur(n: Int): BigInt = n match {
  //Using naive recursion
  case 0 | 1 => n
  case _ => fibonacci_recur(n - 1) + fibonacci_recur(n - 2)
}

def fibonacci_tail_recur(num: Int): BigInt = {
  //Using tail recursion where the recusion gets called last
  @scala.annotation.tailrec
  def tail_recur(n: Int, a: BigInt, b: BigInt): BigInt = n match {
    case 0 => a
    case 1 => b
    case _ => tail_recur(n - 1, b, a + b)
  }

  tail_recur(num, 0, 1)
}

def fibonacci_pisano( n : Int) : BigInt = { 
  //Pisano period => sequence of fib numbers taken modulo n repeats
  def tail_pisano( n: Int, a:BigInt, b:BigInt): BigInt = n match {
    case 0 => a 
    case _ => tail_pisano(n-1, b, (a+b)%1000000 )
  }

  tail_pisano(n%1500000, 0, 1)
}