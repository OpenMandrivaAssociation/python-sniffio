%define module sniffio

Summary:	Sniff out which async library your code is running under 
Name:		python-%{module}
Version:	1.2.0
Release:	1
License:	MIT or Apache
Group:		Development/Python
Url:		https://github.com/python-trio/sniffio/%{module}
Source:		https://files.pythonhosted.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
# test
BuildRequires:	python3dist(curio)

BuildArch:	noarch

%description
You're writing a library. You've decided to be ambitious, and support multiple
async I/O packages, like Trio, and asyncio, and ... You've written a bunch of
clever code to handle all the differences. But... how do you know which piece
of clever code to run?

This is a tiny package whose only purpose is to let you detect which async
library your code is running under.

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}-py%{pyver}.egg-info/

#----------------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install

