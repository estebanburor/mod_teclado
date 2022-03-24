## Mod Teclado Español Latino para MacBook con Ubuntu 20.04
### Instalación

1. Selecciona la distribución de **Español (latinoamericano)** en la configuración **Región e Idioma** de Ubuntu 20.04
2. Descarga el mod 
```
git clone https://github.com/aburgoaor/mod_teclado
```
3. Da permisos de ejecución al archivo **teclado_latino.py** 
```
cd mod_teclado/
chmod +x teclado_latino.py
```
4. Luego ejecuta el archivo como **admin**
```
sudo ./teclado_latino.py
```

### Persistencia

Los cambios se perderán una vez que reinicies o apagues tu equipo, por lo que al iniciar debes ejecutar el archivo.

#### Notas

Este script creado en Python 3, se hizo para un MacBook Pro mid 2013, al cual se le instaló Ubuntu 20.04. 
A día de hoy **NO se ha probado** en otra versión de Ubuntu por lo que no podemos asegurar que funcione en otra versión u otra distribución.
