Summary:	An extra playlist plugin for gmpc
Name:		gmpc-extraplaylist
Version:	0.20.0
Release:	3
License:	GPLv2+
Group:		Sound
Url:		https://www.sarine.nl/
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	libmpd-devel >= 0.15.98
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.4
BuildRequires:	gmpc-devel >= 0.19.2
BuildRequires:	intltool
Requires:	gmpc

%description
An extra playlist plugin for gmpc.

%prep
%setup -q
#patch0 -p0

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_libdir}/gmpc/plugins/libextraplaylist.so
