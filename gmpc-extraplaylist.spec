Summary:	An extra playlist plugin for gmpc
Name:		gmpc-extraplaylist
Version:	0.15.5.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl/
Source0:	http://download.sarine.nl/download/gmpc-0.15.5/%{name}-%{version}.tar.bz2
BuildRequires:	libmpd-devel
BuildRequires:	libxml2-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	gmpc-devel
Requires:	gmpc
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
An extra playlist plugin for gmpc.

%prep
%setup -q

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/gmpc/plugins/libextraplaylist.la
%{_datadir}/gmpc/plugins/libextraplaylist.so
