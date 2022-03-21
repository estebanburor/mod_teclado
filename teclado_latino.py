#!/bin/python3

import os

os.system("clear")
titulo = "[+] Mod Teclado Español Latino para MacBook con Ubuntu 20.04"
print(titulo+"\n"+"-"*len(titulo)+"\n")

resp = input("[+] ¿Desea instalar el mod de teclado? (s/n) ")

if resp.lower() == "s" or resp.lower() == "y":
    print("[+] Instalando mod de teclado...")
    # Aqui la configuracion de teclado
    os.system("xmodmap -e 'keycode  12 = 3 periodcentered 3 periodcentered numbersign'")
    os.system("xmodmap -e 'keycode  21 = exclamdown questiondown NoSymbol NoSymbol NoSymbol'")
    os.system("xmodmap -e 'keycode  34 = dead_grave dead_circumflex dead_grave dead_circumflex bracketleft'")
    os.system("xmodmap -e 'keycode  35 = plus asterisk plus asterisk bracketleft'")
    os.system("xmodmap -e 'keycode  48 = dead_acute dead_diaeresis dead_acute dead_diaeresis braceleft'")
    os.system("xmodmap -e 'keycode  49 = less greater less greater NoSymbol'")
    os.system("xmodmap -e 'keycode  51 = ccedilla Ccedilla ccedilla Ccedilla braceright'")
    os.system("xmodmap -e 'keycode  94 = degree ordfeminine degree ordfeminine backslash'")

    print("[+] Mod instalado con exito, enjoy!")

else:
    print("[+] El mod no se ha instalado :(")
