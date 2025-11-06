| Modo  | Significado            | Descripción                                                              |
| ------ | ---------------------- | ------------------------------------------------------------------------ |
| `'r'` | **Read** (lectura)     | Abre el archivo solo para leer. (Error si no existe).                    |
| `'w'` | **Write** (escritura)  | Crea o sobrescribe el archivo.                                           |
| `'a'` | **Append** (anexar)    | Abre el archivo para añadir texto al final (sin borrar lo anterior).     |
| `'x'` | **Exclusive creation** | Crea un archivo nuevo (error si ya existe).                              |
| `'b'` | **Binary**             | Se usa junto a otros modos para trabajar en binario (`'rb'`, `'wb'`...). |
| `'t'` | **Text**               | Modo texto (por defecto). Ejemplo: `'rt'` o `'wt'`.                      |
| `'+'` | **Update**             | Permite lectura y escritura (`'r+'`, `'w+'`, `'a+'`).                    |
