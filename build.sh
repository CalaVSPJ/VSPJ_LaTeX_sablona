#!/bin/bash

# Simple build script for VSPJ LaTeX template
# Usage: [DOCKER=sudo] ./build.sh [output_directory]

DOCKER=${DOCKER:-docker}
OUTPUT_DIR=${1:-output}
TEMP_DIR=".tmp_build"
TIMESTAMP=$(date +%Y-%m-%d_%H-%M)

echo "Building LaTeX project into directory: $OUTPUT_DIR using $DOCKER"

mkdir -p "$OUTPUT_DIR"
mkdir -p "$TEMP_DIR"

$DOCKER run --rm \
    -v "$(pwd)":/workspace \
    -w /workspace \
    texlive/texlive:latest \
    bash -c " \
        apt-get update && \
        apt-get install -y fontconfig fonts-crosextra-carlito inkscape && \
        fc-cache -f && \
        latexmk -xelatex -interaction=nonstopmode --shell-escape \
        -output-directory=$TEMP_DIR \
        src/semestralni_prace.tex && \
        cp $TEMP_DIR/semestralni_prace.pdf $OUTPUT_DIR/semestralni_prace_$TIMESTAMP.pdf \
    "

rm -rf "$TEMP_DIR"
echo "Build complete. Output PDF: $OUTPUT_DIR/semestralni_prace_$TIMESTAMP.pdf"
