# Makefile for VSPJ LaTeX template

DOCKER ?= docker
OUTPUT_DIR = output

.PHONY: all build clean help

all: build

build:
	@DOCKER=$(DOCKER) ./build.sh $(OUTPUT_DIR)

clean:
	rm -rf $(OUTPUT_DIR) .tmp_build

help:
	@echo "VSPJ LaTeX Template Makefile"
	@echo ""
	@echo "Targets:"
	@echo "  build   Compiles the LaTeX document (calls build.sh)"
	@echo "  clean   Removes the output directory"
	@echo "  help    Displays this help message"
