#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-optextras
Version  : 2019.12.4
Release  : 23
URL      : https://cran.r-project.org/src/contrib/optextras_2019-12.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/optextras_2019-12.4.tar.gz
Summary  : Tools to Support Optimization Possibly with Bounds and Masks
Group    : Development/Tools
License  : GPL-2.0
Requires: R-numDeriv
BuildRequires : R-numDeriv
BuildRequires : buildreq-R

%description
derivative function to optimization programs. These are primarily function 
   minimization methods with at most bounds and masks on the parameters.
   Provides a way to check the basic computation of objective functions that 
   the user provides, along with proposed gradient and Hessian functions, 
   as well as to wrap such functions to avoid failures when inadmissible parameters 
   are provided. Check bounds and masks. Check scaling or optimality conditions. 
   Perform an axial search to seek lower points on the objective function surface. 
   Includes forward, central and backward gradient approximation codes.

%prep
%setup -q -c -n optextras
cd %{_builddir}/optextras

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589525858

%install
export SOURCE_DATE_EPOCH=1589525858
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library optextras
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library optextras
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library optextras
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc optextras || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/optextras/DESCRIPTION
/usr/lib64/R/library/optextras/INDEX
/usr/lib64/R/library/optextras/Meta/Rd.rds
/usr/lib64/R/library/optextras/Meta/features.rds
/usr/lib64/R/library/optextras/Meta/hsearch.rds
/usr/lib64/R/library/optextras/Meta/links.rds
/usr/lib64/R/library/optextras/Meta/nsInfo.rds
/usr/lib64/R/library/optextras/Meta/package.rds
/usr/lib64/R/library/optextras/NAMESPACE
/usr/lib64/R/library/optextras/NEWS
/usr/lib64/R/library/optextras/R/optextras
/usr/lib64/R/library/optextras/R/optextras.rdb
/usr/lib64/R/library/optextras/R/optextras.rdx
/usr/lib64/R/library/optextras/help/AnIndex
/usr/lib64/R/library/optextras/help/aliases.rds
/usr/lib64/R/library/optextras/help/optextras.rdb
/usr/lib64/R/library/optextras/help/optextras.rdx
/usr/lib64/R/library/optextras/help/paths.rds
/usr/lib64/R/library/optextras/html/00Index.html
/usr/lib64/R/library/optextras/html/R.css
/usr/lib64/R/library/optextras/tests/tfnchk.R
/usr/lib64/R/library/optextras/tests/tgrchk.R
/usr/lib64/R/library/optextras/tests/tkktc.R
