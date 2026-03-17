def operation_numbers(num1: int, num2: int) -> None:

    add_nums = num1 + num2
    sub_nums = num1 - num2
    mul_nums = num1 * num2
    div_nums = num1 / num2 if num2 != 0 else 0
    print(f"{add_nums}\n{sub_nums}\n{mul_nums}\n{div_nums}")

if __name__ == "__main__":
    # Prueba ejemplo propuesto
    operation_numbers(4,3)
    # Prueba ejemplo inventado
    operation_numbers(4,3)
    # Prueba caso límite
    operation_numbers(2,0)

