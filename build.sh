#!/bin/bash

# Advanced build script for VSPJ LaTeX template
# Usage: [DOCKER=sudo] ./build.sh [output_directory]

DOCKER=${DOCKER:-docker}
OUTPUT_DIR=${1:-output}
TEMP_DIR=".tmp_build"
LOG_DIR="$OUTPUT_DIR/logs"
TIMESTAMP=$(date +%Y-%m-%d_%H-%M)
PDF_NAME="semestralni_prace_$TIMESTAMP.pdf"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}--- Starting VSPJ LaTeX Template Build ---${NC}"

# Create directories
mkdir -p "$OUTPUT_DIR"
mkdir -p "$LOG_DIR"
mkdir -p "$TEMP_DIR"

echo -n "1/3 Preparing environment (apt, fonts)... "
$DOCKER run --rm \
    -v "$(pwd)":/workspace \
    -w /workspace \
    texlive/texlive:latest \
    bash -c "
        (
            apt-get update && \
            apt-get install -y fontconfig fonts-crosextra-carlito inkscape && \
            fc-cache -f
        ) > /workspace/$LOG_DIR/setup.log 2>&1
    "

if [ $? -eq 0 ]; then
    echo -e "${GREEN}DONE${NC}"
else
    echo -e "${RED}FAILED${NC}"
    echo -e "Check log: $LOG_DIR/setup.log"
    exit 1
fi

echo -n "2/3 Compiling LaTeX document... "
$DOCKER run --rm \
    -v "$(pwd)":/workspace \
    -w /workspace \
    texlive/texlive:latest \
    bash -c "
        latexmk -xelatex -interaction=nonstopmode --shell-escape \
        -output-directory=$TEMP_DIR \
        src/semestralni_prace.tex > /workspace/$LOG_DIR/latex.log 2>&1
    "

if [ $? -eq 0 ]; then
    echo -e "${GREEN}DONE${NC}"
else
    echo -e "${RED}FAILED${NC}"
    echo -e "Check log: $LOG_DIR/latex.log"
    # Show last few lines of error
    tail -n 10 "$LOG_DIR/latex.log"
    exit 1
fi

echo -n "3/3 Cleaning up and finalizing... "
cp "$TEMP_DIR/semestralni_prace.pdf" "$OUTPUT_DIR/$PDF_NAME" 2>/dev/null
rm -rf "$TEMP_DIR"
echo -e "${GREEN}DONE${NC}"

echo -e "${BLUE}------------------------------------------${NC}"
echo -e "${GREEN}Build successful!${NC}"
echo -e "PDF:  $OUTPUT_DIR/$PDF_NAME"
echo -e "Logs: $LOG_DIR/"
echo -e "${BLUE}------------------------------------------${NC}"
