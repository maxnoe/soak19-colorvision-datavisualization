all: build/soak19.pdf


build/soak19.pdf: build/img.tex
build/soak19.pdf: build/plots/u_cmaps.pdf
build/soak19.pdf: build/plots/norainbow.pdf
build/soak19.pdf: build/plots/colorblind_response.pdf
build/soak19.pdf: build/plots/u_sw.png
build/soak19.pdf: build/plots/cone_response.pdf
build/soak19.pdf: build/plots/cone_response_matrix.pdf
build/soak19.pdf: build/plots/lab_50.pdf
build/soak19.pdf: build/plots/gamut.pdf
build/soak19.pdf: build/plots/gamut_srgb.pdf
build/soak19.pdf: build/plots/photopic.pdf
build/soak19.pdf: build/plots/cmap_jet.pdf
build/soak19.pdf: build/plots/cmap_viridis.pdf
build/soak19.pdf: build/plots/gamut.pdf
build/soak19.pdf: build/plots/gamut_srgb.pdf
build/soak19.pdf: build/plots/spectrum0.pdf
build/soak19.pdf: build/plots/sequential.pdf
build/soak19.pdf: build/plots/diverging.pdf
build/soak19.pdf: build/plots/gamma_srgb.pdf
build/soak19.pdf: build/plots/iris.pdf
build/soak19.pdf: build/plots/europe_divnorm.pdf build/plots/europe_jet.pdf
build/soak19.pdf: build/plots/fireworks_deuter_50.jpg build/plots/fireworks_deuter_100.jpg
build/soak19.pdf: FORCE
	latexmk \
		--lualatex \
		--interaction=nonstopmode \
		--halt-on-error \
		--output-directory=build \
		soak19.tex


$(addprefix build/plots/, $(addsuffix .pdf, gamut gamut_srgb cone_response cone_response_matrix spectrum0 photopic)): scripts/soak19.py


build/plots/%.pdf: scripts/plot_%.py matplotlibrc_pgf header-matplotlib.tex | build/plots
	MATPLOTLIBRC=matplotlibrc_pgf TEXINPUTS=$$(pwd): python $<

build/plots/u_cmaps.pdf: images/dortmunder_u_rgb.jpg
build/plots/u_sw.png: build/plots/u_cmaps.pdf
build/img.tex: build/plots/u_cmaps.pdf


build/plots/fireworks_deuter_50.jpg build/plots/fireworks_deuter_100.jpg: scripts/simulate_deuter.py images/feuerwerk.jpg  | build/plots
	python scripts/simulate_deuter.py

build/plots/cmap_%.pdf:
	python -m viscm view $* --save $@ --quit

build:
	mkdir -p $@

data/ETOPO1_Ice_g_gdal.grd:
	curl -L  https://www.ngdc.noaa.gov/mgg/global/relief/ETOPO1/data/ice_surface/grid_registered/netcdf/ETOPO1_Ice_g_gdal.grd.gz | gunzip > $@


build/plots/europe_divnorm.pdf build/plots/europe_jet.pdf: scripts/plot_europe.py
build/plots/europe_divnorm.pdf build/plots/europe_jet.pdf: matplotlibrc_pgf data/ETOPO1_Ice_g_gdal.grd
	MATPLOTLIBRC=matplotlibrc_pgf TEXINPUTS=$$(pwd): python scripts/plot_europe.py


build/plots/spectrum0.pdf: scripts/plot_spectra.py
	python scripts/plot_spectra.py

build/plots:
	mkdir -p $@


FORCE:

clean:
	rm -rf build

.PHONY: all clean FORCE

