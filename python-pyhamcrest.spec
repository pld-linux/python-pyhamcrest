# NOTE: for versions >= 2.0 see python3-pyhamcrest.spec
#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Hamcrest framework for matcher objects
Summary(pl.UTF-8):	Szkielet Hamcrest do obiektów dopasowujących
Name:		python-pyhamcrest
# keep 1.x here (2.x drops python 2 support)
Version:	1.10.1
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pyhamcrest/
Source0:	https://files.pythonhosted.org/packages/source/p/pyhamcrest/PyHamcrest-%{version}.tar.gz
# Source0-md5:	6be265e4704aacd20cf8e4dd4eeb7dd3
URL:		https://pypi.org/project/PyHamcrest/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-six
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	sphinx-pdg-3
%endif
# replace with other requires if defined in setup.py
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyHamcrest is a framework for writing matcher objects, allowing you to
declaratively define "match" rules. There are a number of situations
where matchers are invaluable, such as UI validation, or data
filtering, but it is in the area of writing flexible tests that
matchers are most commonly used.

%description -l pl.UTF-8
PyHamcrest to szkielet do pisania obiektów dopasowujących,
pozwalających deklaratywnie definiować reguły dopasowań. Jest wiele
sytuacji, gdzie dopasowywanie jest bezcenne, np. sprawdzanie
poprawności w interfejsie użytkownika, filtrowanie danych, ale
najczęściej jest przydatne w obszarze pisania elastycznych testów.

%package -n python3-pyhamcrest
Summary:	Hamcrest framework for matcher objects
Summary(pl.UTF-8):	Szkielet Hamcrest do obiektów dopasowujących
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-pyhamcrest
PyHamcrest is a framework for writing matcher objects, allowing you to
declaratively define "match" rules. There are a number of situations
where matchers are invaluable, such as UI validation, or data
filtering, but it is in the area of writing flexible tests that
matchers are most commonly used.

%description -n python3-pyhamcrest -l pl.UTF-8
PyHamcrest to szkielet do pisania obiektów dopasowujących,
pozwalających deklaratywnie definiować reguły dopasowań. Jest wiele
sytuacji, gdzie dopasowywanie jest bezcenne, np. sprawdzanie
poprawności w interfejsie użytkownika, filtrowanie danych, ale
najczęściej jest przydatne w obszarze pisania elastycznych testów.

%package apidocs
Summary:	API documentation for Python pyhamcrest module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona pyhamcrest
Group:		Documentation

%description apidocs
API documentation for Python pyhamcrest module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona pyhamcrest.

%prep
%setup -q -n PyHamcrest-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C doc html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python-pyhamcrest-%{version}
cp -p examples/*.py $RPM_BUILD_ROOT%{_examplesdir}/python-pyhamcrest-%{version}

%py_postclean
%endif

%if %{with python3}
%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-pyhamcrest-%{version}
cp -a examples/*.py $RPM_BUILD_ROOT%{_examplesdir}/python3-pyhamcrest-%{version}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.rst
%{py_sitescriptdir}/hamcrest
%{py_sitescriptdir}/PyHamcrest-%{version}-py*.egg-info
%{_examplesdir}/python-pyhamcrest-%{version}
%endif

%if %{with python3}
%files -n python3-pyhamcrest
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.rst
%{py3_sitescriptdir}/hamcrest
%{py3_sitescriptdir}/PyHamcrest-%{version}-py*.egg-info
%{_examplesdir}/python3-pyhamcrest-%{version}
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/{_static,*.html,*.js}
%endif
