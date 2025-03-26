#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 7ef8d3f
#
Name     : R-reticulate
Version  : 1.42.0
Release  : 89
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/reticulate_1.42.0.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/reticulate_1.42.0.tar.gz
Summary  : Interface to 'Python'
Group    : Development/Tools
License  : Apache-2.0
Requires: R-reticulate-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppTOML
Requires: R-here
Requires: R-jsonlite
Requires: R-png
Requires: R-rappdirs
Requires: R-rlang
Requires: R-withr
BuildRequires : R-Rcpp
BuildRequires : R-RcppTOML
BuildRequires : R-here
BuildRequires : R-jsonlite
BuildRequires : R-png
BuildRequires : R-rappdirs
BuildRequires : R-rlang
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
into 'Python', R data types are automatically converted to their equivalent 'Python'
    types. When values are returned from 'Python' to R they are converted back to R
    types. Compatible with all versions of 'Python' >= 2.7.

%package lib
Summary: lib components for the R-reticulate package.
Group: Libraries

%description lib
lib components for the R-reticulate package.


%prep
%setup -q -n reticulate
pushd ..
cp -a reticulate buildavx2
popd
pushd ..
cp -a reticulate buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1743002366

%install
export SOURCE_DATE_EPOCH=1743002366
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/reticulate/DESCRIPTION
/usr/lib64/R/library/reticulate/INDEX
/usr/lib64/R/library/reticulate/Meta/Rd.rds
/usr/lib64/R/library/reticulate/Meta/features.rds
/usr/lib64/R/library/reticulate/Meta/hsearch.rds
/usr/lib64/R/library/reticulate/Meta/links.rds
/usr/lib64/R/library/reticulate/Meta/nsInfo.rds
/usr/lib64/R/library/reticulate/Meta/package.rds
/usr/lib64/R/library/reticulate/Meta/vignette.rds
/usr/lib64/R/library/reticulate/NAMESPACE
/usr/lib64/R/library/reticulate/NEWS.md
/usr/lib64/R/library/reticulate/R/reticulate
/usr/lib64/R/library/reticulate/R/reticulate.rdb
/usr/lib64/R/library/reticulate/R/reticulate.rdx
/usr/lib64/R/library/reticulate/config/config.py
/usr/lib64/R/library/reticulate/doc/arrays.Rmd
/usr/lib64/R/library/reticulate/doc/arrays.html
/usr/lib64/R/library/reticulate/doc/calling_python.Rmd
/usr/lib64/R/library/reticulate/doc/calling_python.html
/usr/lib64/R/library/reticulate/doc/index.html
/usr/lib64/R/library/reticulate/doc/package.Rmd
/usr/lib64/R/library/reticulate/doc/package.html
/usr/lib64/R/library/reticulate/doc/python_dependencies.Rmd
/usr/lib64/R/library/reticulate/doc/python_dependencies.html
/usr/lib64/R/library/reticulate/doc/python_packages.Rmd
/usr/lib64/R/library/reticulate/doc/python_packages.html
/usr/lib64/R/library/reticulate/doc/python_primer.Rmd
/usr/lib64/R/library/reticulate/doc/python_primer.html
/usr/lib64/R/library/reticulate/doc/r_markdown.Rmd
/usr/lib64/R/library/reticulate/doc/r_markdown.html
/usr/lib64/R/library/reticulate/doc/versions.Rmd
/usr/lib64/R/library/reticulate/doc/versions.html
/usr/lib64/R/library/reticulate/help/AnIndex
/usr/lib64/R/library/reticulate/help/aliases.rds
/usr/lib64/R/library/reticulate/help/figures/python_r_object.png
/usr/lib64/R/library/reticulate/help/figures/python_repl.png
/usr/lib64/R/library/reticulate/help/figures/reticulate_completion.png
/usr/lib64/R/library/reticulate/help/figures/reticulated_python.png
/usr/lib64/R/library/reticulate/help/figures/rmarkdown_engine_zoomed.png
/usr/lib64/R/library/reticulate/help/paths.rds
/usr/lib64/R/library/reticulate/help/reticulate.rdb
/usr/lib64/R/library/reticulate/help/reticulate.rdx
/usr/lib64/R/library/reticulate/html/00Index.html
/usr/lib64/R/library/reticulate/html/R.css
/usr/lib64/R/library/reticulate/python/rpytools/__init__.py
/usr/lib64/R/library/reticulate/python/rpytools/ark_variables.py
/usr/lib64/R/library/reticulate/python/rpytools/call.py
/usr/lib64/R/library/reticulate/python/rpytools/generator.py
/usr/lib64/R/library/reticulate/python/rpytools/help.py
/usr/lib64/R/library/reticulate/python/rpytools/ipython.py
/usr/lib64/R/library/reticulate/python/rpytools/loader.py
/usr/lib64/R/library/reticulate/python/rpytools/output.py
/usr/lib64/R/library/reticulate/python/rpytools/run.py
/usr/lib64/R/library/reticulate/python/rpytools/subprocess.py
/usr/lib64/R/library/reticulate/python/rpytools/test.py
/usr/lib64/R/library/reticulate/python/rpytools/thread.py
/usr/lib64/R/library/reticulate/tests/testthat.R
/usr/lib64/R/library/reticulate/tests/testthat/_snaps/py_require.md
/usr/lib64/R/library/reticulate/tests/testthat/_snaps/python-knitr-engine/knitr-print.md
/usr/lib64/R/library/reticulate/tests/testthat/_snaps/python-knitr-engine/knitr-print2.md
/usr/lib64/R/library/reticulate/tests/testthat/_snaps/python-knitr-engine/knitr-warn.md
/usr/lib64/R/library/reticulate/tests/testthat/_snaps/python-knitr-engine/test-chunking.md
/usr/lib64/R/library/reticulate/tests/testthat/helper-py-require.R
/usr/lib64/R/library/reticulate/tests/testthat/resources/_snaps/python-knitr-engine/test-chunking.md
/usr/lib64/R/library/reticulate/tests/testthat/resources/altair-example.Rmd
/usr/lib64/R/library/reticulate/tests/testthat/resources/eng-reticulate-example.Rmd
/usr/lib64/R/library/reticulate/tests/testthat/resources/figure/py-plot-1.png
/usr/lib64/R/library/reticulate/tests/testthat/resources/figure/r-plot-1.png
/usr/lib64/R/library/reticulate/tests/testthat/resources/import-test.R
/usr/lib64/R/library/reticulate/tests/testthat/resources/knitr-print.Rmd
/usr/lib64/R/library/reticulate/tests/testthat/resources/knitr-print.md
/usr/lib64/R/library/reticulate/tests/testthat/resources/knitr-print2.md
/usr/lib64/R/library/reticulate/tests/testthat/resources/knitr-warn.Rmd
/usr/lib64/R/library/reticulate/tests/testthat/resources/knitr-warn.md
/usr/lib64/R/library/reticulate/tests/testthat/resources/matplotlib-example.Rmd
/usr/lib64/R/library/reticulate/tests/testthat/resources/pandas-example.Rmd
/usr/lib64/R/library/reticulate/tests/testthat/resources/plotly-example.Rmd
/usr/lib64/R/library/reticulate/tests/testthat/resources/seaborn-example.Rmd
/usr/lib64/R/library/reticulate/tests/testthat/resources/test-chunking.Rmd
/usr/lib64/R/library/reticulate/tests/testthat/resources/test-chunking.md
/usr/lib64/R/library/reticulate/tests/testthat/resources/test-custom-root-dir.Rmd
/usr/lib64/R/library/reticulate/tests/testthat/resources/test-custom-root-dir.md
/usr/lib64/R/library/reticulate/tests/testthat/resources/venv-activate.R
/usr/lib64/R/library/reticulate/tests/testthat/script.py
/usr/lib64/R/library/reticulate/tests/testthat/setup.R
/usr/lib64/R/library/reticulate/tests/testthat/test-aaa.R
/usr/lib64/R/library/reticulate/tests/testthat/test-callable-dynamic-dots.R
/usr/lib64/R/library/reticulate/tests/testthat/test-delay-load.R
/usr/lib64/R/library/reticulate/tests/testthat/test-examples.R
/usr/lib64/R/library/reticulate/tests/testthat/test-finalize.R
/usr/lib64/R/library/reticulate/tests/testthat/test-help-handlers.R
/usr/lib64/R/library/reticulate/tests/testthat/test-interrupts.R
/usr/lib64/R/library/reticulate/tests/testthat/test-multiprocessing.R
/usr/lib64/R/library/reticulate/tests/testthat/test-py_func.R
/usr/lib64/R/library/reticulate/tests/testthat/test-py_require.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-arrays.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-base-r-generics.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-class.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-classes.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-closures.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-comparisons.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-complex.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-datetime.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-dict.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-envs.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-exceptions.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-factors.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-formals.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-function.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-import-hook.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-info.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-initialize.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-iterators.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-knitr-engine.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-lists.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-modules.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-numpy.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-objects.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-output.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-pandas.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-pickle.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-pipenv.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-poetry.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-raw.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-run.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-scipy-sparse-matrix.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-scope.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-source.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-strings.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-threads.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-vectors.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-virtual-environments.R
/usr/lib64/R/library/reticulate/tests/testthat/test-r-extptr-capsule.R
/usr/lib64/R/library/reticulate/tests/testthat/test-repl-magics.R
/usr/lib64/R/library/reticulate/tests/testthat/test-subprocess.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/reticulate/libs/reticulate.so
/V4/usr/lib64/R/library/reticulate/libs/reticulate.so
/usr/lib64/R/library/reticulate/libs/reticulate.so
