%global srcname libsass

Name:           python-%{srcname}
Version:        0.13.2
Release:        1%{?dist}
Summary:        Python bindings for libsass

License:        MIT
URL:            https://github.com/dahlia/libsass-python
Source0:        %{url}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
#Patches for using the system libraries instead of bundled ones
Patch0:		python-libsass-systemlib.patch
Patch1:		python-libsass-systemlib-man.patch

BuildRequires:  python2-devel python2-six python2-pytest python-werkzeug
BuildRequires:  python3-devel python3-six python3-pytest python3-werkzeug
BuildRequires:  libsass-devel
#needed for docs
BuildRequires:	python3-sphinx

%description
This package provides a simple Python extension module
sass which is binding Libsass (written in C/C++ by Hampton
Catlin and Aaron Leung).

%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}

Requires: python2-six

%description -n python2-%{srcname}
This package provides a simple Python extension module
sass which is binding Libsass (written in C/C++ by Hampton
Catlin and Aaron Leung).

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires: python3-six

%description -n python3-%{srcname}
This package provides a simple Python extension module
sass which is binding Libsass (written in C/C++ by Hampton
Catlin and Aaron Leung).

%prep
%autosetup -n %{srcname}-python-%{version} -p1
sed "s|#!/usr/bin/env python||" -i sassc.py
# Because system libsass is used (not bundled), version from this file is not needed at all
# so just an empty file is created.
touch .libsass-upstream-version

%build
%py2_build
%py3_build
pushd docs
PLATFORM=$(python3 -c "import sysconfig; print(sysconfig.get_platform())")
export PYTHONPATH=../build/lib.${PLATFORM}-%{python3_version}
make html SPHINXBUILD=sphinx-build-3
popd

%install
%py2_install
%py3_install

%check
export PYTHONPATH=%{buildroot}%{python2_sitearch}
py.test-%{python2_version} sasstests.py
export PYTHONPATH=%{buildroot}%{python3_sitearch}
py.test-%{python3_version} sasstests.py

%files -n python2-%{srcname}
%license LICENSE
%doc README.rst docs/_build/html/
%{python2_sitearch}/_sass.so
%{python2_sitearch}/libsass-0.13.2-py%{python2_version}.egg-info/*
%{python2_sitearch}/sass.py*
%{python2_sitearch}/sassc.py*
%{python2_sitearch}/sasstests.py*
%{python2_sitearch}/sassutils/*

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst docs/_build/html/
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/_sass*.so
%{python3_sitearch}/libsass-0.13.2-py%{python3_version}.egg-info/*
%{python3_sitearch}/sass.py
%{python3_sitearch}/sassc.py
%{python3_sitearch}/sasstests.py
%{python3_sitearch}/sassutils/*
%exclude %{_bindir}/sassc
%exclude %{_bindir}/sassc.py

%changelog
* Tue Sep 12 2017 Marcel Plch <gmarcel.plch@gmail.com> - 0.13.2
- Initial version of the package

