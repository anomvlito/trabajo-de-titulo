#!/bin/bash

# Script to initialize Git repositories for Trasplan components locally

BASE_DIR="/home/fabian/src/codefuente"
REPOS=("backend" "web" "App" "mobile")
GH_ORG="trasplan2026"
GH_NAMES=(
    "trasplan-backend"
    "trasplan-web"
    "trasplan-app"
    "trasplan-mobile-legacy"
)

echo "=== Inicializando repositorios locales ==="

for i in "${!REPOS[@]}"; do
    FOLDER="${REPOS[$i]}"
    GH_NAME="${GH_NAMES[$i]}"
    DIR="$BASE_DIR/$FOLDER"
    
    echo ""
    echo "----------------------------------------"
    echo "Procesando carpeta: $FOLDER"
    echo "----------------------------------------"
    
    if [ -d "$DIR" ]; then
        cd "$DIR"
        
        # Check if already a git repo
        if [ -d ".git" ]; then
            echo "Aviso: $FOLDER ya tiene una carpeta .git. Omitiendo inicialización."
        else
            echo "Inicializando repositorio Git en $FOLDER..."
            git init
            git checkout -b main
            
            echo "Añadiendo archivos..."
            git add .
            
            echo "Creando primer commit..."
            git commit -m "Initial commit for $GH_NAME"
            echo "Repositorio local inicializado con éxito."
        fi
        
        echo ""
        echo "Para asociar y subir este repositorio a GitHub, ejecuta:"
        echo "  cd $DIR"
        echo "  git remote add origin git@github.com:$GH_ORG/$GH_NAME.git"
        echo "  git push -u origin main"
    else
        echo "Error: La carpeta $DIR no existe."
    fi
done

echo ""
echo "========================================"
echo "Siguientes pasos:"
echo "1. Ve a GitHub y crea los 4 repositorios vacíos en la organización:"
echo "   - https://github.com/organizations/trasplan2026/repositories/new"
echo "   Nombres de los repositorios:"
echo "   - trasplan-backend"
echo "   - trasplan-web"
echo "   - trasplan-app"
echo "   - trasplan-mobile-legacy"
echo ""
echo "2. Ejecuta los comandos indicados arriba para subir cada repositorio."
echo "========================================"
