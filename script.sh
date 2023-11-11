#!/bin/bash

# Directorio que contiene los archivos
directorio="./data/images/"

# Cambia al directorio especificado
cd "$directorio" || exit

# Itera sobre todos los archivos en el directorio que coinciden con el patrón "*.jpg"
for archivo in *.jpg; do
    # Extrae la parte del nombre de archivo después del primer guión bajo
    nuevo_nombre=$(echo "$archivo" | cut -d '_' -f 2-)

    # Renombra el archivo
    mv "$archivo" "$nuevo_nombre"
done

echo "¡Renombrado completado!"