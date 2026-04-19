#!/bin/bash

# Simple build script for VSPJ LaTeX template
# Usage: [DOCKER=sudo] ./build.sh [output_directory]

DOCKER=${DOCKER:-docker}
OUTPUT_DIR=${1:-output}

echo "Building LaTeX project into directory: $OUTPUT_DIR using $DOCKER"

mkdir -p "$OUTPUT_DIR"

$DOCKER run --rm \
    -v "$(pwd)":/workspace \
    -w /workspace \
    texlive/texlive:latest \
    bash -c " \
        apt-get update && \
        apt-get install -y fontconfig fonts-crosextra-carlito inkscape && \
        fc-cache -f && \
        latexmk -xelatex -interaction=nonstopmode --shell-escape \
        -output-directory=$OUTPUT_DIR \
        src/semestralni_prace.tex
    "
