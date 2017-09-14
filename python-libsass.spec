%global srcname libsass

Name:           python-%{srcname}
Version:        0.13.2
Release:        1%{?dist}
Summary:        Python bindings for libsass

License:        MIT
URL:            https://github.com/dahlia/libsass-python
Source0:        %{url}/releases/download/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python2-devel python2-six
BUildRequires:  python3-devel python3-six
BuildRequires:  libsass-devel

%description
This package provides a simple Python extension module
sass which is binding Libsass (written in C/C++ by Hampton
Catlin and Aaron Leung). It’s very straightforward and
there isn’t any headache related Python distribution/deployment.
That means you can add just libsass into your setup.py’s
install_requires list or requirements.txt file.
Need no Ruby nor Node.js.

%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}

Requires: libsass

%description -n python2-%{srcname}
This package provides a simple Python extension module
sass which is binding Libsass (written in C/C++ by Hampton
Catlin and Aaron Leung). It’s very straightforward and
there isn’t any headache related Python distribution/deployment.
That means you can add just libsass into your setup.py’s
install_requires list or requirements.txt file.
Need no Ruby nor Node.js.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires: libsass

%description -n python3-%{srcname}
This package provides a simple Python extension module
sass which is binding Libsass (written in C/C++ by Hampton
Catlin and Aaron Leung). It’s very straightforward and
there isn’t any headache related Python distribution/deployment.
That means you can add just libsass into your setup.py’s
install_requires list or requirements.txt file.
Need no Ruby nor Node.js.

%prep
%autosetup -n %{srcname}-%{version}
rm -Rf libsass/
sed -i 's/extra_link_args=link_flags,/extra_link_args=link_flags, libraries=["sass"],/' setup.py
sed "s|#!/usr/bin/env python||" -i sassc.py

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{srcname}
#%license 
%doc README.rst
%{python2_sitearch}/_sass.so
%{python2_sitearch}/libsass-0.13.2-py%{python2_version}.egg-info/*
%{python2_sitearch}/sass.py*
%{python2_sitearch}/sassc.py*
%{python2_sitearch}/sasstests.py*
%{python2_sitearch}/sassutils/*

%files -n python3-%{srcname}
#%license
%doc README.rst
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/_sass*.so
%{python3_sitearch}/libsass-0.13.2-py%{python3_version}.egg-info/*
%{python3_sitearch}/sass.py
%{python3_sitearch}/sassc.py
%{python3_sitearch}/sasstests.py
%{python3_sitearch}/sassutils/*
%{_bindir}/sassc
%{_bindir}/sassc.py

%changelog
* Tue Sep 12 2017 Marcel Plch <gmarcel.plch@gmail.com> - 0.13.2
- Initial version of the package

