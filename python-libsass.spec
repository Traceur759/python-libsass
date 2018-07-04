%global srcname libsass

Name:           python-%{srcname}
Version:        0.14.5
Release:        1%{?dist}
Summary:        Python bindings for libsass

License:        MIT
URL:            https://github.com/dahlia/libsass-python
Source0:        %{url}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
# Patch for correct naming of manpages
Patch0:     python-libsass-man.patch

BuildRequires:  python3-devel
BuildRequires:  python3-six
BuildRequires:  python3-pytest
BuildRequires:  python3-werkzeug
BuildRequires:  libsass-devel
# Needed for docs
BuildRequires:  python3-sphinx

%description
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
sed -i -e '/^#!\//, 1d' sassc.py

%build
# Export SYSTEM_SASS environment variable to use the
# system library, not the bundled one
export SYSTEM_SASS="true"
%py3_build
pushd docs
# There are differences between Python's naming of arches and the
# %%{_arch} macro. We need to ask Python for the platform name
PLATFORM=$(python3 -c "import sysconfig; print(sysconfig.get_platform())")
export PYTHONPATH=../build/lib.${PLATFORM}-%{python3_version}
make man    SPHINXBUILD=sphinx-build-3
popd

%install
# Same as above
export SYSTEM_SASS="true"
%py3_install
install -m 644 -D docs/_build/man/pysassc.1 %{buildroot}%{_mandir}/man1/pysassc.1

%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
py.test-3 sasstests.py

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/_sass*.so
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitearch}/sass.py
%{python3_sitearch}/sassc.py
%{python3_sitearch}/sasstests.py
%{python3_sitearch}/sassutils/
%{_mandir}/man1/pysassc.1.gz
%{_bindir}/pysassc
# Collides with libsass.
%exclude %{_bindir}/sassc
# Same thing as %%{python3_sitearch}/sassc.py
# Also, we don't want *.py files in bindir.
%exclude %{_bindir}/sassc.py

%changelog
* Thu Jan 11 2018 Marcel Plch <gmarcel.plch@gmail.com> - 0.14.5
- Initial version of the package

