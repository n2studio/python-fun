import decimal

def calculate_pi(precision):
  """
  Calculates pi to the nth digit using the Chudnovsky algorithm.

  Args:
    precision: The number of decimal places to calculate.

  Returns:
    A decimal object representing pi to the specified precision.
    
  Known Issue: 
    This produces incorrect answers, e.g. -9.8476 or -98476392.876. 
    I tried getting chatgpt to correct mistakes about 5 times but it 
    was never able to create correct code. Different mistake each time. 
  """

  decimal.getcontext().prec = precision + 1  # Set decimal precision

  inverse_pi = decimal.Decimal(0) 
  k = 1
  while True:
    term = (
        decimal.Decimal(12 * (-1) ** k * (6 * k + 1))
        / decimal.Decimal(640320 ** (3 * k))
        * decimal.Decimal(
            (1359140860 * k + 545140134)
            / decimal.Decimal((3 * k) * (6 * k - 1) * (6 * k - 2))
        )
    )

    inverse_pi += term

    if abs(term) < 10 ** (-precision - 1):
      break
    k += 1

  pi = decimal.Decimal(1) / inverse_pi
  pi_str = str(pi)

  # Correct string slicing for rounding:
  pi_rounded = pi_str[:precision + 2] 

  return decimal.Decimal(pi_rounded)

if __name__ == "__main__":
  n = int(input("Enter the number of digits for pi: "))
  print(f"Pi to {n} digits: {calculate_pi(n)}")
