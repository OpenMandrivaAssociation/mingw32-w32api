%define __strip %{_mingw32_strip}
%define __objdump %{_mingw32_objdump}
%define _use_internal_dependency_generator 0
%define __find_requires %{_mingw32_findrequires}
%define __find_provides %{_mingw32_findprovides}

Name:           mingw32-w32api
Version:	3.13
Release:        %mkrel 1
Summary:        Win32 header files and stubs

License:        Public Domain
Group:          Development/Other
URL:            http://www.mingw.org/
Source0:        http://dl.sourceforge.net/sourceforge/mingw/w32api-%{version}-mingw32-src.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 39-3
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-runtime

Requires:       mingw32-runtime

# Once this is installed, mingw32-bootstrap (binary bootstrapper) is no
# longer needed.
Obsoletes:      mingw32-w32api-bootstrap


%description
MinGW Windows cross-compiler Win32 header files.


%prep
%setup -q -n w32api-%{version}-mingw32

%build
%{_mingw32_configure}
make


%install
rm -rf $RPM_BUILD_ROOT

%{_mingw32_makeinstall}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%{_mingw32_includedir}/*
%{_mingw32_libdir}/*.a
