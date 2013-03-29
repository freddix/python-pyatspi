%define 	module	pyatspi

Summary:	AT-SPI Python bindings
Name:		python-%{module}
Version:	2.8.0
Release:	1
License:	LGPL v2
Group:		Development/Languages/Python
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pyatspi/2.8/%{module}-%{version}.tar.xz
# Source0-md5:	930f51c62cca60ebdf90f735d26385b2
URL:		http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
BuildRequires:	pkg-config
BuildRequires:	python-devel
BuildRequires:	python-pygobject-devel
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
Requires:	at-spi2-core
Requires:	python-dbus
Requires:	python-modules
Requires:	python-pygobject3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides AT-SPI Python bindings.

%prep
%setup -qn %{module}-%{version}

%build
%configure \
	--build=%{_build} \
	--host=%{_host}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{py_sitescriptdir}/pyatspi

