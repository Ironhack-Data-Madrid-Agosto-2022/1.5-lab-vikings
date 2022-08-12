# Lab | Vikings
![viking](https://github.com/Ironhack-Data-Madrid-Marzo-2022/1.5-lab-vikings/blob/main/img/Captura%20de%20pantalla%202022-03-25%20a%20las%2012.34.57.png)

## Introduction

Los vikingos y los sajones están en guerra. Ambos son soldados, pero tienen sus propios métodos para luchar. Los vikingos son portados a Python. YAY!!

In this laboratory you will work with the concept of inheritance in Python.

### Getting Started

Encontrarás los siguientes archivos en la carpeta de este laboratorio:

- `vikingsClasses.py`
- `1-testSoldier.py`
- `2-testVikings.py`
- `3-testSaxons.py`
- `4-testWar.py`

Eres libre de usar cualquiera de los editores de código que tienes para abrir estos archivos.

### Challenge Question

Modificar el archivo `vikingsClasses.py` Para que todas las pruebas sean correctas.

## Submission

- Modificar `vikingsClasses.py` Y guarda los cambios.

## Tests

La mejor manera de saber cómo va nuestro código es trabajar con pruebas. Probarás el archivo `vikingsClases.py` paso a paso. 

Vas **only** be **editing** the vikingsClasses.py. Los archivos que **running** Para probar tu código son los siguientes: 1-testsSoldier.py, 2-testsVikings.py, 3-testsSaxons.py & 4-testsWar.py, Dependiendo de lo lejos que hayas escrito tu código.

Por lo tanto, digamos que ya has creado la clase para soldados.

1. Has escrito tu código

2. Asegúrate de guardar los cambios en tu editor

3. En tu terminal, ejecuta el archivo de prueba para esa clase

```bash
$ python3 1-testSoldier.py --v
```

### Correct Test

Cuando todas las pruebas sean correctas, recibirás el siguiente mensaje en el terminal.

```
$ python3 1-testSoldier.py --v

testAttackHasNoParams (__main__.TestSoldier) ... ok
testAttackRetunsStrength (__main__.TestSoldier) ... ok
testAttackShouldBeFunction (__main__.TestSoldier) ... ok
testCanReceiveDamage (__main__.TestSoldier) ... ok
testConstructorSignature (__main__.TestSoldier) ... ok
testHealth (__main__.TestSoldier) ... ok
testReceiveDamageReturnNone (__main__.TestSoldier) ... ok
testReceivesDamage (__main__.TestSoldier) ... ok
testReceivesDamageHasParams (__main__.TestSoldier) ... ok
testStrength (__main__.TestSoldier) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK
```

### Failed Test

When any test is incorrect you will receive the following message in the terminal. It means that you must keep making changes in the `vikingsClasses.py` file.

```
$ python3 1-testSoldier.py --v

testAttackHasNoParams (__main__.TestSoldier) ... ok
testAttackRetunsStrength (__main__.TestSoldier) ... ok
testAttackShouldBeFunction (__main__.TestSoldier) ... ok
testCanReceiveDamage (__main__.TestSoldier) ... FAIL
testConstructorSignature (__main__.TestSoldier) ... ok
testHealth (__main__.TestSoldier) ... ok
testReceiveDamageReturnNone (__main__.TestSoldier) ... ok
testReceivesDamage (__main__.TestSoldier) ... ok
testReceivesDamageHasParams (__main__.TestSoldier) ... ok
testStrength (__main__.TestSoldier) ... ok

======================================================================
FAIL: testCanReceiveDamage (__main__.TestSoldier)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "1-testsSoldier.py", line 44, in testCanReceiveDamage
    self.assertEqual(self.soldier.health, self.health + 50)
AssertionError: 250 != 350

----------------------------------------------------------------------
Ran 10 tests in 0.001s
```

## Exercise

![](https://i.imgur.com/5TPElt8.jpg)

---

**Write the code**

Ahora tenemos que escribir el código correcto en el `vikingsClasses.py` Archivo para hacer que la prueba pase. El código de inicio que encontrarás en el archivo es el siguiente:

```
# Soldier
class Soldier:

# Viking
class Viking:

# Saxon
class Saxon:

# War
class War:
```

En este caso, la prueba dice que _Soldier constructor function debería recibir 2 argumentos (salud y fuerza)_, por lo que tenemos que escribir el código correcto que pase esta prueba. Hagamos que la función constructora `Soldier` reciba dos argumentos:

```importante!!
# Soldier
class Soldier:
    def __init__(self, health, strength):
        # add code here

# Viking
class Viking:

# Saxon
class Saxon:

# War
class War:

```

### Soldier

Modificar el `Soldier` Función constructora y añadir 2 métodos a su prototipo: `attack()`, Y `receiveDamage()`.

#### constructor function

- Debería recibir **2 arguments** (Salud y fuerza)
- Debería recibir el **`health` property** Como su **1st argument**
- Debería recibir el **`strength` property** Como su **2nd argument**

#### `attack()` Procedimiento

- Debería ser una función
- Debería recibir **0 arguments**
- Debería volver **the `strength` Propiedad de la `Soldier`**

#### `receiveDamage()` method

- Debería ser una función
- Debería recibir **1 argument** (El daño)
- Debe eliminar el daño recibido de la `health` propiedad
- **shouldn't return** Algo

---

### Viking

A `Viking` Es un `Soldier` Con una propiedad adicional, Su `name`. También tienen un `receiveDamage()` Método y nuevo método, `battleCry()`.

Modificar el `Viking` Función constructora, haz que herede de `Soldier`, Reimplementar el`receiveDamage()` Método para `Viking`, Y añade un nuevo `battleCry()` Procedimiento.

#### Herencia

- `Viking` Debe heredar de `Soldier`

#### constructor function

- Debería recibir **3 arguments** (name, health & strength)
- Debería recibir el **`name` property** Como su **1st argument**
- Debería recibir el **`health` property** Como su **2nd argument**
- Debería recibir el **`strength` property** Como su **3rd argument**

#### `attack()` method

(Este método debe ser **inherited** Desde `Soldier`, No es necesario volver a implementarlo.)

- Debería ser una función
- Debería recibir **0 arguments**
- Debería volver **the `strength` property of the `Viking`**

#### `receiveDamage()` method

(Este método debe ser **reimplemented** Para `Viking` Porque el `Viking` La versión debe tener diferentes valores de retorno.)

- Debería ser una función
- Debería recibir **1 argument** (El daño)
- Debe eliminar el daño recibido de la `health` Propiedad
- **if the `Viking` is still alive**, Debería devolver **"NAME has received DAMAGE points of damage"**
- **if the `Viking` dies**, Debería devolver **"NAME has died in act of combat"**

#### `battleCry()` method

[Learn more about battle cries](http://www.artofmanliness.com/2015/06/08/battle-cries/).

- Debería ser una función
- Debería recibir **0 arguments**
- Debería volver **"Odin Owns You All!"**

---

### Saxon

A `Saxon` Es un tipo más débil de `Soldier`. A diferencia de un `Viking`, a `Saxon` No tiene nombre. Su `receiveDamage()` También será diferente al original `Soldier` Adaptación.

Modificar el `Saxon`, Función constructora, haz que herede de `Soldier` Y volver a implementar el `receiveDamage()` Método para `Saxon`.

#### inheritance

- `Saxon` Debe heredar de `Soldier`

#### constructor function

- Debería recibir **2 arguments** (health & strength)
- should receive the **`health` property** as its **1st argument**
- should receive the **`strength` property** as its **2nd argument**

#### `attack()` method

(Este método debe ser **inherited** Desde `Soldier`, No es necesario volver a implementarlo.)

- Debería ser una función
- Debería recibir **0 arguments**
- Debería volver **the `strength` property of the `Saxon`**

#### `receiveDamage()` method

(Este método debe ser **reimplemented** for `Saxon` Porque el `Saxon` La versión debe tener diferentes valores de devolución.)

- Debería ser una función
- Debería recibir **1 argument** (the damage)
- Debe eliminar el daño recibido de la `health` Propiedad
- **if the Saxon is still alive**, Debería devolver _**"A Saxon has received DAMAGE points of damage"**_
- **if the Saxon dies**, Debería devolver _**"A Saxon has died in combat"**_

---

### War

Ahora llegamos a lo bueno: ¡GUERRA! Nuestro `War` La función constructora nos permitirá tener un `Viking` army and a `Saxon` army that battle Entre sí.

Modify the `War` Constructor y añadir 5 métodos a su prototipo:

- `addViking()`
- `addSaxon()`
- `vikingAttack()`
- `saxonAttack()`
- `showStatus()`

#### constructor function

Cuando creamos por primera vez un `War`, Los ejércitos deben estar vacíos. Añadiremos soldados a los ejércitos más tarde.

- Debería recibir **0 arguments**
- Debe asignar una matriz vacía al **`vikingArmy` property**
- Debe asignar una matriz vacía al **`saxonArmy` property**

#### `addViking()` method

Añade 1 `Viking` to the `vikingArmy`. Si quieres un 10 `Viking` army, Tienes que llamar a esto 10 veces.

- Debería ser una función
- Debería recibir **1 argument** (a `Viking` object)
- Debería añadir el `Viking` Al ejército
- **shouldn't return** Algo

#### `addSaxon()` method

The `Saxon` version of `addViking()`.

- should be a function
- should receive **1 argument** (a `Saxon` object)
- Debería añadir el `Saxon` to the army
- **shouldn't return** anything

#### `vikingAttack()` method

A `Saxon` (Elegido al azar) Tiene su `receiveDamage()` Método llamado con el daño igual al`strength` De un `Viking` (También elegido al azar). Esto solo debería realizar un solo ataque y el `Saxon` No puede devolver el ataque.

- should be a function
- should receive **0 arguments**
-  hacer un `Saxon` `receiveDamage()` Igual a la `strength` De un `Viking`
-  eliminar los saxones muertos del ejército
-  volver **result of calling `receiveDamage()` of a `Saxon`** Con el `strength` of a `Viking`

#### `saxonAttack()` method

The `Saxon` version of `vikingAttack()`. A `Viking` receives the damage equal to the `strength` of a `Saxon`.

- should be a function
- should receive **0 arguments**
- should make a `Viking` `receiveDamage()` equal to the `strength` of a `Saxon`
- should remove dead vikings from the army
- should return **result of calling `receiveDamage()` of a `Viking`** with the `strength` of a `Saxon`

#### `showStatus()` method

Returns the current status of the `War` based on the size of the armies.

- should be a function
- should receive **0 arguments**
- **if the `Saxon` array is empty**, should return _**"Vikings have won the war of the century!"**_ #######
- **if the `Viking` array is empty**, should return _**"Saxons have fought for their lives and survive another day..."**_
- **if there are at least 1 `Viking` and 1 `Saxon`**, should return _**"Vikings and Saxons are still in the thick of battle."**_ ######


## BONUS

Create a game using the classes you defined. For this, you will need to:
- Create a new `file.py`
- Import the classes you defined earlier
- Define functions to create the workflow of the game: i.e. functions to create teams (maybe you can create random teams with your classmates' names), run the game, etc.

## Deliverables

- REQUIRED: `vikingsClases.py` modified with your solution to the challenge question.

## Resources

- https://docs.python.org/3/library/unittest.html
- https://www.python-course.eu/python3_inheritance.php

## Additional Challenge for the Nerds

You can try to make your own tests for your code by creating another test file.
