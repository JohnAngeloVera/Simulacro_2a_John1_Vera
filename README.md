# Ejercicio simulacro de examen (Entornos de Desarrollo) 

## Indice

1. [Enunciado](#1-enunciado)
2. [Resolución](#2-resolución)
3. [Pruebas](#3-pruebas)

<br>

## 1. Enunciado
Realiza un programa en un main.py que tiene dos variables con dos nu meros cualesquiera.
El programa realiza la suma, la resta, la multiplicacio n y la divisio n con esos nu meros y lo muestra por pantalla. Suponiendo que una variable es el 4 y otra el 3, la ejecución debe verse del siguiente modo:

```cmd
7
1
12
1,3333333
```
**Entiéndase que el 7 es la suma, 1 la resta, 12 la multiplicacio n y 1.3333 la división**

## 2. Resolución
1. Asignar variables a cada una de las operaciones que se van a mostrar en pantalla:

```python
add_nums = num1 + num2
sub_nums = num1 - num2
mul_nums = num1 * num2
div_nums = num1 / num2 if num2 != 0 else 0
```
**Importante tener en cuenta el caso límite de no división entre 0**

`if num2 != 0 else 0`

2. Imprimir por pantalla el resultado separando con un `\n` por cada uno de los resultados:

```python
print(f"{add_nums}\n{sub_nums}\n{mul_nums}\n{div_nums}")
```

3. Meter todo en una sola función con cabecera `operation_numbers` que acepte dos int y no devuelva nada:

```python
def operation_numbers(num1: int, num2: int) -> None:

    add_nums = num1 + num2
    sub_nums = num1 - num2
    mul_nums = num1 * num2
    div_nums = num1 / num2 if num2 != 0 else 0
    print(f"{add_nums}\n{sub_nums}\n{mul_nums}\n{div_nums}")
```

## 3. Pruebas

En este apartado vamos a hacer las siguientes pruebas:

| Función           | num1     | num2     | 
| ----------------- | -------- | -------- | 
| operation_numbers | 4        | 3        | 
| operation_numbers | 80       | 20       | 
| operation_numbers | 2        | 0        | 

Estas pruebas son relevantes porque:

- *En el primer caso*: 
    - Comprobamos si el ejemplo propuesto funciona.
        - ` operation_numbers(4,3)`
- *En el segundo caso*: 
    - Comprobamos si funciona con otro ejemplo inventado.
        - ` operation_numbers(80,20)`
- *En el tercer caso*: 
    - Comprobamos si funciona con un caso límite
        - ` operation_numbers(2,0)`

**Añadimos la línea `if __name__ == "__main__":` para verificar que en el caso de que se llame a nuestra función desde otro main no se ejecuten nuestras pruebas**

- [x] Primer caso :

```python
operation_numbers(4,3)
```

```cmd
7
1
12
1,3333333
```

- [x] Segundo caso :

```python
operation_numbers(80,20)
```

```cmd
100
60
1600
4.0
```

- [x] Tercer caso :

```python
operation_numbers(2,0)
```

```cmd
2
2
0
0
```