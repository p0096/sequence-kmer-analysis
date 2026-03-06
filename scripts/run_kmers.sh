#!/bin/bash

# Script para ejecutar kmer_counter.py de forma sencilla

# Revisar que se pasan los argumentos
if [ "$#" -ne 2 ]; then
    echo "Uso: ./run_kmers.sh <archivo_fasta> <k>"
    exit 1
fi

FASTA_FILE=$1
K=$2

# Crear carpeta results si no existe
mkdir -p ../results

# Ejecutar el script Python
python3 ./scripts/kmer_counter.py "$FASTA_FILE" "$K"

echo "Análisis de k-mers terminado para k=$K"
