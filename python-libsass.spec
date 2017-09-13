%global srcname libsass
%global libname libsass-python
%global sum An example python module

Name:           python-%{srcname}
Version:        0.13.2
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/dahlia/%{libname}/releases
Source0:        https://github.com/dahlia/%{libname}/releases/download/%{version}/libsass-%{version}.tar.gz

ExclusiveArch:  %{ix86} x86_64
BuildRequires:  python2-devel python3-devel python2-six python3-six

%description
This package provides a simple Python extension module
sass which is binding Libsass (written in C/C++ by Hampton
Catlin and Aaron Leung). It’s very straightforward and
there isn’t any headache related Python distribution/deployment.
That means you can add just libsass into your setup.py’s
install_requires list or requirements.txt file.
Need no Ruby nor Node.js.

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
This package provides a simple Python extension module
sass which is binding Libsass (written in C/C++ by Hampton
Catlin and Aaron Leung). It’s very straightforward and
there isn’t any headache related Python distribution/deployment.
That means you can add just libsass into your setup.py’s
install_requires list or requirements.txt file.
Need no Ruby nor Node.js.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

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

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install
sed "1d" -i %{buildroot}/%{python2_sitearch}/sassc.py
sed "1d" -i %{buildroot}/%{python3_sitearch}/sassc.py

%check
%{__python2} setup.py test
%{__python3} setup.py test

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python2-%{srcname}
%license README.rst
%doc README.rst PKG-INFO
%{python2_sitearch}/_sass.so
%{python2_sitearch}/libsass-0.13.2-py2.7.egg-info/
%{python2_sitearch}/sass.py*
%{python2_sitearch}/sassc.py*
%{python2_sitearch}/sasstests.py*
%{python2_sitearch}/sassutils/

%files -n python3-%{srcname}
%license README.rst
%doc README.rst PKG-INFO
%{python3_sitearch}/__pycache__/
%{python3_sitearch}/_sass.cpython-36m-%{_arch}-linux-gnu.so
%{python3_sitearch}/libsass-0.13.2-py3.6.egg-info/
%{python3_sitearch}/sass.py
%{python3_sitearch}/sassc.py
%{python3_sitearch}/sasstests.py
%{python3_sitearch}/sassutils/

%{_bindir}/sassc
%{_bindir}/sassc.py

%changelog
* Tue Sep 12 2017 Marcel Plch <gmarcel.plch@gmail.com> - 0.13.2
- Initial version of the package

