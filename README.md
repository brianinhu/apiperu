# Api de los 24 departamentos del Perú

Paquete básico de los 24 departamentos del Perú

## Pasos
1. Instale Python mediante la página oficial: [Python](https://www.python.org/).
2. Asegúrese de tener el comando pip en el path de su ordenador.
3. Abra su terminal favorito y escriba el siguiente codigo:
   `pip install apiperu`

## Ejemplo

**Código**

```python
from apiperu import departamentos
var = departamentos.Departamento()
var.search("Lima")
```

**Resultado**

```bash
Departamento: Lima
Ubigeo: 15
Población: 11128658
Superficie (km²): 32888.02
Capital: Lima
Número de provincias: 10
Provincias: Lima, Barranca, Cajatambo, Canta, Cañete, Huaral, Huarochirí, Huaura, Oyón, Yauyos
```
