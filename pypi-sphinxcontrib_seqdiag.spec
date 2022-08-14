#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-sphinxcontrib_seqdiag
Version  : 3.0.0
Release  : 50
URL      : https://files.pythonhosted.org/packages/9d/e6/5430aa6d8750337e14555d94bf9fac5ae7e1f0ac9198cd0c2c59a2e226b7/sphinxcontrib-seqdiag-3.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/9d/e6/5430aa6d8750337e14555d94bf9fac5ae7e1f0ac9198cd0c2c59a2e226b7/sphinxcontrib-seqdiag-3.0.0.tar.gz
Summary  : Sphinx "seqdiag" extension
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-sphinxcontrib_seqdiag-license = %{version}-%{release}
Requires: pypi-sphinxcontrib_seqdiag-python = %{version}-%{release}
Requires: pypi-sphinxcontrib_seqdiag-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(blockdiag)
BuildRequires : pypi(seqdiag)
BuildRequires : pypi(sphinx)

%description
=====================
sphinxcontrib-seqdiag
=====================
.. image:: https://travis-ci.org/blockdiag/sphinxcontrib-seqdiag.svg?branch=master
:target: https://travis-ci.org/blockdiag/sphinxcontrib-seqdiag

%package license
Summary: license components for the pypi-sphinxcontrib_seqdiag package.
Group: Default

%description license
license components for the pypi-sphinxcontrib_seqdiag package.


%package python
Summary: python components for the pypi-sphinxcontrib_seqdiag package.
Group: Default
Requires: pypi-sphinxcontrib_seqdiag-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinxcontrib_seqdiag package.


%package python3
Summary: python3 components for the pypi-sphinxcontrib_seqdiag package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_seqdiag)
Requires: pypi(blockdiag)
Requires: pypi(seqdiag)
Requires: pypi(sphinx)

%description python3
python3 components for the pypi-sphinxcontrib_seqdiag package.


%prep
%setup -q -n sphinxcontrib-seqdiag-3.0.0
cd %{_builddir}/sphinxcontrib-seqdiag-3.0.0
pushd ..
cp -a sphinxcontrib-seqdiag-3.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656370685
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_seqdiag
cp %{_builddir}/sphinxcontrib-seqdiag-3.0.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_seqdiag/1df558a5711c101907d8f15c608a58793588fa6e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinxcontrib_seqdiag/1df558a5711c101907d8f15c608a58793588fa6e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
