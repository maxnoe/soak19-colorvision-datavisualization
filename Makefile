all: build/soak19.pdf


build/soak19.pdf: build/img.tex
build/soak19.pdf: build/plots/u_cmaps.pdf
build/soak19.pdf: build/plots/u_sw.png
build/soak19.pdf: build/plots/cone_response.pdf
build/soak19.pdf: FORCE
	latexmk \
		--lualatex \
		--interaction=nonstopmode \
		--halt-on-error \
		--output-directory=build \
		soak19.tex

build/plots/%.pdf: scripts/plot_%.py matplotlibrc_pgf | build/plots
	MATPLOTLIBRC=matplotlibrc_pgf TEXINPUTS=$$(pwd): python $<

build/plots/u_cmaps.pdf: images/dortmunder_u_rgb.jpg
build/plots/u_sw.png: build/plots/u_cmaps.pdf
build/img.tex: build/plots/u_cmaps.pdf


build:
	mkdir -p $@


build/plots:
	mkdir -p $@


FORCE:

clean:
	rm -rf build

.PHONY: all clean FORCE

