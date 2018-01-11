%global srcname libsass

Name:           python-%{srcname}
Version:        0.13.4
Release:        1%{?dist}
Summary:        Python bindings for libsass

License:        MIT
URL:            https://github.com/dahlia/libsass-python
Source0:        %{url}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
#Patch for correct naming of manpages
Patch0:     python-libsass-man.patch

BuildRequires:  python2-devel python2-six python2-pytest python-werkzeug
BuildRequires:  python3-devel python3-six python3-pytest python3-werkzeug
BuildRequires:  libsass-devel
#needed for docs
BuildRequires:  python3-sphinx

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
export SYSTEM_SASS="true"
%py2_build
%py3_build
pushd docs
PLATFORM=$(python3 -c "import sysconfig; print(sysconfig.get_platform())")
export PYTHONPATH=../build/lib.${PLATFORM}-%{python3_version}
make man
popd

%install
%py2_install
%py3_install
mkdir -p %{buildroot}%{_mandir}/man1/
cp %{_builddir}/%{srcname}-python-%{version}/docs/_build/man/pysassc.1 %{buildroot}%{_mandir}/man1/

%check
export PYTHONPATH=%{buildroot}%{python2_sitearch}
py.test-%{python2_version} sasstests.py
export PYTHONPATH=%{buildroot}%{python3_sitearch}
py.test-%{python3_version} sasstests.py

%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{_mandir}/man1/pysassc.1.gz
%{python2_sitearch}/_sass.so
%{python2_sitearch}/%{srcname}-%{version}-py%{python2_version}.egg-info/
%{python2_sitearch}/sass.py*
%{python2_sitearch}/sassc.py*
%{python2_sitearch}/sasstests.py*
%{python2_sitearch}/sassutils/

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{_mandir}/man1/pysassc.1.gz
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/_sass*.so
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitearch}/sass.py
%{python3_sitearch}/sassc.py
%{python3_sitearch}/sasstests.py
%{python3_sitearch}/sassutils/
%{_bindir}/pysassc
%exclude %{_bindir}/sassc
%exclude %{_bindir}/sassc.py

%changelog
* Thu Jan 11 2018 Marcel Plch <gmarcel.plch@gmail.com> - 0.13.4
- Initial version of the package

