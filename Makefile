# Makefile for VSPJ LaTeX template

DOCKER ?= docker
OUTPUT_DIR = output

.PHONY: all build fast clean help

all: build

build:
	@DOCKER=$(DOCKER) ./build.sh $(OUTPUT_DIR)

# Rychlý náhled bez Dockeru (vyžaduje tectonic a font Carlito) → output/prace.pdf
fast:
	@mkdir -p $(OUTPUT_DIR)/logs
	tectonic -Z search-path="$(CURDIR)" --keep-logs --outdir $(OUTPUT_DIR) src/prace.tex
	@cp $(OUTPUT_DIR)/prace.log $(OUTPUT_DIR)/logs/build.log

clean:
	rm -rf $(OUTPUT_DIR) .tmp_build

help:
	@echo "VSPJ LaTeX Template Makefile"
	@echo ""
	@echo "Targets:"
	@echo "  build   Compiles the LaTeX document (calls build.sh)"
	@echo "  fast    Quick preview with local tectonic, no Docker (output/prace.pdf)"
	@echo "  clean   Removes the output directory"
	@echo "  help    Displays this help message"
