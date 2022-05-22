MAKEFLAGS  := -j 1

INS         = source/beamerthemetrigon.ins
PACKAGE_SRC = $(wildcard source/*.dtx)
PACKAGE_STY = $(notdir $(PACKAGE_SRC:%.dtx=%.sty))

DEMO_SRC    = demo/trigon_demo.tex
DEMO_PDF    = demo/trigon_demo.pdf
DEMO_ALT_SRC= demo/trigon_demo_alt.tex
DEMO_ALT_PDF= demo/trigon_demo_alt.pdf
DEMO_SRC_OTHER = demo/frames.tex \
		 demo/library.jpg \
		 demo/trigon_full.pdf \
		 demo/trigon_small.pdf

DOC_SRC     = docs/trigontheme.dtx
DOC_PDF     = docs/trigontheme.pdf

LAYOUTS_SRC     = screenshots/trigon_layouts.tex
LAYOUTS_PDF     = screenshots/trigon_layouts.pdf
LAYOUTS_IMG     := screenshots/layout_example-01.jpg \
		   screenshots/layout_example-02.jpg \
		   screenshots/layout_example-03.jpg

TESTS_DIR    = tests/
TESTS_SRC    = $(wildcard tests/test-*.tex)
TESTS_PDF    = $(notdir $(TESTS_SRC:%.tex=%.pdf))

CTAN_CONTENT = README.md Makefile $(INS) $(PACKAGE_SRC) $(DOC_SRC) $(DOC_PDF) $(DEMO_SRC) $(DEMO_SRC_OTHER) $(DEMO_PDF)

DESTDIR     ?= $(shell kpsewhich -var-value=TEXMFHOME)
INSTALL_DIR  = $(DESTDIR)/tex/latex/beamertheme-trigon
DOC_DIR      = $(DESTDIR)/doc/latex/beamertheme-trigon
LATEXMK_CONF = $(shell pwd)/latexmkrc
CACHE_DIR   := $(shell pwd)/.latex-cache

COMPILE_TEX := latexmk -xelatex -cd
CLEAN_TEX := latexmk -c -cd
CLEAN_PDF := latexmk -C -cd

export TEXINPUTS:=$(shell pwd):$(shell pwd)//:${TEXINPUTS}

.PHONY: all sty doc demo layouts screenshots tests clean install uninstall ctan clean-cache clean-sty Clean pkg-version

all: sty layouts doc demo

sty: $(PACKAGE_STY)

doc: $(DOC_PDF)

demo: $(DEMO_PDF) $(DEMO_ALT_PDF)

layouts: $(LAYOUTS_IMG)

screenshots: $(LAYOUTS_SRC) $(DEMO_PDF) $(DEMO_ALT_PDF)
	@cd $(dir $(DEMO_PDF)) && pdftoppm $(notdir $(DEMO_PDF)) trigon_demo -jpeg
	@cd $(dir $(DEMO_ALT_PDF)) && pdftoppm $(notdir $(DEMO_ALT_PDF)) trigon_demo_alt -jpeg
	@mv $(dir $(DEMO_PDF))trigon_demo*-{01,03,04,07,09,13}.jpg $(dir $(LAYOUTS_SRC))/.
	@rm $(dir $(DEMO_PDF))trigon_demo*.jpg

tests: $(TESTS_PDF)

clean: clean-cache clean-sty

Clean: clean clean-pdf clean-img

install: $(PACKAGE_STY) $(DOC_PDF)
	@mkdir -p $(INSTALL_DIR)
	@cp $(PACKAGE_STY) $(INSTALL_DIR)
	@mkdir -p $(DOC_DIR)
	@cp $(DOC_PDF) $(DOC_DIR)

uninstall:
	@rm -f "$(addprefix $(INSTALL_DIR)/, $(PACKAGE_STY))"
	@rmdir "$(INSTALL_DIR)"
	@rm -f "$(DOC_DIR)/$(notdir $(DOC_PDF))"
	@rmdir "$(DOC_DIR)"

clean-cache:
	@rm -rf "$(CACHE_DIR)"
	$(CLEAN_TEX) $(PACKAGE_SRC) $(DEMO_SRC) $(DEMO_ALT_SRC) $(DOC_SRC) $(LAYOUTS_SRC) $(TESTS_SRC)

clean-pdf:
	$(CLEAN_PDF) $(PACKAGE_SRC) $(DEMO_SRC) $(DEMO_ALT_SRC) $(DOC_SRC) $(LAYOUTS_SRC) $(TESTS_SRC)

clean-sty:
	@rm -f $(PACKAGE_STY)

clean-img:
	@rm -f $(dir $(LAYOUTS_SRC))/*.jpg


ctan: $(CTAN_CONTENT) pkg-version
	@tar --transform "s@\(.*\)@trigon/\1@" -cf trigon-$(shell date "+%Y-%m-%d").tar.gz $(CTAN_CONTENT)

pkg-version:
	@sed -i 's@v\([0-9]\{1,\}\.\)\{1,\}[0-9]\{1,\}@$(shell git describe --abbrev=0 --tags)@g' $(PACKAGE_SRC)
	@sed -i 's@\[20[0-9][0-9]/[0-9]*/[0-9]*@\[$(shell date "+%Y/%m/%d")@g' $(PACKAGE_SRC)

$(CACHE_DIR):
	@mkdir -p $(CACHE_DIR)

$(PACKAGE_STY): $(PACKAGE_SRC) $(INS) | clean-cache $(CACHE_DIR)
	@cd $(dir $(INS)) && latex -output-directory=$(CACHE_DIR) $(notdir $(INS))
	@cp $(addprefix $(CACHE_DIR)/,$(PACKAGE_STY)) .

$(DOC_PDF): $(DOC_SRC) $(PACKAGE_STY) $(LAYOUTS_IMG)
	$(CLEAN_TEX) $(DOC_SRC)
	$(COMPILE_TEX) $(DOC_SRC)

$(DEMO_PDF): $(LAYOUTS_IMG) $(DEMO_SRC) $(PACKAGE_STY)
	$(CLEAN_TEX) $(DEMO_SRC)
	$(COMPILE_TEX) $(DEMO_SRC)

$(DEMO_ALT_PDF): $(LAYOUTS_IMG) $(DEMO_ALT_SRC) $(PACKAGE_STY)
	$(CLEAN_TEX) $(DEMO_ALT_SRC)
	$(COMPILE_TEX) $(DEMO_ALT_SRC)

$(LAYOUTS_PDF): $(LAYOUTS_SRC) $(PACKAGE_STY)
	$(CLEAN_TEX) $(LAYOUTS_SRC)
	$(COMPILE_TEX) $(LAYOUTS_SRC)

$(LAYOUTS_IMG): $(LAYOUTS_PDF)
	@cd $(dir $(LAYOUTS_PDF)) && pdftoppm $(notdir $(LAYOUTS_PDF)) layout_example -jpeg

$(TESTS_PDF): $(TESTS_SRC) $(PACKAGE_STY)
	$(COMPILE_TEX) -quiet $(TESTS_SRC)
