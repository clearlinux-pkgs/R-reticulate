#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-reticulate
Version  : 1.13
Release  : 29
URL      : https://cran.r-project.org/src/contrib/reticulate_1.13.tar.gz
Source0  : https://cran.r-project.org/src/contrib/reticulate_1.13.tar.gz
Summary  : Interface to 'Python'
Group    : Development/Tools
License  : Apache-2.0
Requires: R-reticulate-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-callr
Requires: R-jsonlite
BuildRequires : R-Rcpp
BuildRequires : R-callr
BuildRequires : R-jsonlite
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
%setup -q -c -n reticulate

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1564028812

%install
export SOURCE_DATE_EPOCH=1564028812
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reticulate
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reticulate
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reticulate
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc reticulate || :


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
/usr/lib64/R/library/reticulate/doc/arrays.R
/usr/lib64/R/library/reticulate/doc/arrays.Rmd
/usr/lib64/R/library/reticulate/doc/arrays.html
/usr/lib64/R/library/reticulate/doc/calling_python.R
/usr/lib64/R/library/reticulate/doc/calling_python.Rmd
/usr/lib64/R/library/reticulate/doc/calling_python.html
/usr/lib64/R/library/reticulate/doc/index.html
/usr/lib64/R/library/reticulate/doc/package.R
/usr/lib64/R/library/reticulate/doc/package.Rmd
/usr/lib64/R/library/reticulate/doc/package.html
/usr/lib64/R/library/reticulate/doc/python_packages.R
/usr/lib64/R/library/reticulate/doc/python_packages.Rmd
/usr/lib64/R/library/reticulate/doc/python_packages.html
/usr/lib64/R/library/reticulate/doc/r_markdown.R
/usr/lib64/R/library/reticulate/doc/r_markdown.Rmd
/usr/lib64/R/library/reticulate/doc/r_markdown.html
/usr/lib64/R/library/reticulate/doc/versions.R
/usr/lib64/R/library/reticulate/doc/versions.Rmd
/usr/lib64/R/library/reticulate/doc/versions.html
/usr/lib64/R/library/reticulate/help/AnIndex
/usr/lib64/R/library/reticulate/help/aliases.rds
/usr/lib64/R/library/reticulate/help/paths.rds
/usr/lib64/R/library/reticulate/help/reticulate.rdb
/usr/lib64/R/library/reticulate/help/reticulate.rdx
/usr/lib64/R/library/reticulate/html/00Index.html
/usr/lib64/R/library/reticulate/html/R.css
/usr/lib64/R/library/reticulate/python/rpytools/__init__.py
/usr/lib64/R/library/reticulate/python/rpytools/call.py
/usr/lib64/R/library/reticulate/python/rpytools/generator.py
/usr/lib64/R/library/reticulate/python/rpytools/help.py
/usr/lib64/R/library/reticulate/python/rpytools/output.py
/usr/lib64/R/library/reticulate/python/rpytools/test.py
/usr/lib64/R/library/reticulate/python/rpytools/thread.py
/usr/lib64/R/library/reticulate/tests/testthat.R
/usr/lib64/R/library/reticulate/tests/testthat/helper-utils.R
/usr/lib64/R/library/reticulate/tests/testthat/resources/eng-reticulate-example.Rmd
/usr/lib64/R/library/reticulate/tests/testthat/resources/eng-reticulate-example.html
/usr/lib64/R/library/reticulate/tests/testthat/resources/venv-activate.R
/usr/lib64/R/library/reticulate/tests/testthat/script.py
/usr/lib64/R/library/reticulate/tests/testthat/test-delay-load.R
/usr/lib64/R/library/reticulate/tests/testthat/test-examples.R
/usr/lib64/R/library/reticulate/tests/testthat/test-help-handlers.R
/usr/lib64/R/library/reticulate/tests/testthat/test-py_func.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-arrays.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-classes.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-closures.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-comparisons.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-complex.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-datetime.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-dict.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-envs.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-factors.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-function.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-iterators.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-knitr-engine.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-lists.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-numpy.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-objects.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-output.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-pandas.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-pickle.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-raw.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-scipy-sparse-matrix.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-source.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-strings.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-vectors.R
/usr/lib64/R/library/reticulate/tests/testthat/test-python-virtual-environments.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/reticulate/libs/reticulate.so
/usr/lib64/R/library/reticulate/libs/reticulate.so.avx2
/usr/lib64/R/library/reticulate/libs/reticulate.so.avx512
