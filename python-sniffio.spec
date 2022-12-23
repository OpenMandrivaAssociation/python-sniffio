Summary:	Sniff out which async library your code is running under 
Name:		python-sniffio
Version:	1.3.0
Release:	1
License:	MIT or Apache
Group:		Development/Python
Url:		https://github.com/python-trio/sniffio/sniffio
Source:		https://files.pythonhosted.org/packages/source/s/sniffio/sniffio-%{version}.tar.gz

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)
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
%{python_sitelib}/sniffio/
%{python_sitelib}/sniffio-*.*-info/

#----------------------------------------------------------------------------

%prep
%autosetup -n sniffio-%{version}

%build
%py_build

%install
%py_install

