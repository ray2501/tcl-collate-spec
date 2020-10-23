#
# spec file for package tcl-collate
#

%define packagename collate

Name:           tcl-collate
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tcl-devel >= 8.6
Version:        1.0
Release:        0
Summary:        A Tcl interface to strcoll()
License:        zlib/libpng
Group:          Development/Languages/Tcl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
URL:            https://sourceforge.net/projects/tcl-collate/
Source0:        %packagename-%version.tar.gz

%description
A Tcl interface to strcoll() (or _mbscoll() on Windows). 
And a Tcl interface to setlocale().
    
%prep
%setup -q -n %{packagename}-%{version}

%build
make linux

%install
mkdir -p %buildroot%tcl_archdir/%{packagename}%{version}
cp pkgIndex.tcl %buildroot%tcl_archdir/%{packagename}%{version}
cp collsort.tcl %buildroot%tcl_archdir/%{packagename}%{version}
%if %{__isa_bits} == 64
mkdir -p %buildroot%tcl_archdir/%{packagename}%{version}/linux64
cp locale.so %buildroot%tcl_archdir/%{packagename}%{version}/linux64
cp collate.so %buildroot%tcl_archdir/%{packagename}%{version}/linux64
%else
mkdir -p %buildroot%tcl_archdir/%{packagename}%{version}/linux32
cp locale.so %buildroot%tcl_archdir/%{packagename}%{version}/linux32
cp collate.so %buildroot%tcl_archdir/%{packagename}%{version}/linux32
%endif

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%tcl_archdir
%doc README.txt

%changelog
