# Makefile for VSPJ LaTeX template

DOCKER_IMAGE = texlive/texlive:latest
SRC_DIR = src
MAIN_FILE = semestralni_prace.tex
OUTPUT_DIR = output

.PHONY: all build clean help

all: build

build:
	mkdir -p $(OUTPUT_DIR)
	docker run --rm \
		-v $$(pwd):/workspace \
		-w /workspace \
		$(DOCKER_IMAGE) \
		bash -c " \
			apt-get update && \
			apt-get install -y fontconfig fonts-crosextra-carlito inkscape && \
			fc-cache -f && \
			latexmk -xelatex -interaction=nonstopmode --shell-escape \
			-output-directory=$(OUTPUT_DIR) \
			$(SRC_DIR)/$(MAIN_FILE) \
		"

clean:
	rm -rf $(OUTPUT_DIR)

help:
	@echo "VSPJ LaTeX Template Makefile"
	@echo ""
	@echo "Targets:"
	@echo "  build   Compiles the LaTeX document using Docker"
	@echo "  clean   Removes the output directory"
	@echo "  help    Displays this help message"
