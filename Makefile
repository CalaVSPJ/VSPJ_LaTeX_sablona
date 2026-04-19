# Makefile for VSPJ LaTeX template

DOCKER ?= docker
DOCKER_IMAGE = texlive/texlive:latest
SRC_DIR = src
MAIN_FILE = semestralni_prace.tex
OUTPUT_DIR = output
TEMP_DIR = .tmp_build

.PHONY: all build clean help

all: build

build:
	mkdir -p $(OUTPUT_DIR)
	mkdir -p $(TEMP_DIR)
	$(DOCKER) run --rm \
		-v $$(pwd):/workspace \
		-w /workspace \
		$(DOCKER_IMAGE) \
		bash -c " \
			apt-get update && \
			apt-get install -y fontconfig fonts-crosextra-carlito inkscape && \
			fc-cache -f && \
			latexmk -xelatex -interaction=nonstopmode --shell-escape \
			-output-directory=$(TEMP_DIR) \
			$(SRC_DIR)/$(MAIN_FILE) && \
			cp $(TEMP_DIR)/$(MAIN_FILE:.tex=.pdf) $(OUTPUT_DIR)/semestralni_prace_$$(date +%Y-%m-%d_%H-%M).pdf \
		"
	rm -rf $(TEMP_DIR)
	@echo "Build successful. PDF is in $(OUTPUT_DIR)/"

clean:
	rm -rf $(OUTPUT_DIR) $(TEMP_DIR)

help:
	@echo "VSPJ LaTeX Template Makefile"
	@echo ""
	@echo "Targets:"
	@echo "  build   Compiles the LaTeX document and cleans up auxiliary files"
	@echo "  clean   Removes the output and temporary directories"
	@echo "  help    Displays this help message"
