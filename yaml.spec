%define api 0
%define major 2
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

Summary:	YAML 1.1 parser and emitter written in C
Name:		yaml
Version:	0.1.4
Release:	6
License:	MIT
Group:		System/Libraries
URL:		http://pyyaml.org/wiki/LibYAML
Source0:	http://pyyaml.org/download/libyaml/%{name}-%{version}.tar.gz
BuildRequires:	doxygen

%description
LibYAML is a YAML 1.1 parser and emitter written in C.

%package -n	%{libname}
Summary:	YAML 1.1 parser and emitter written in C
Group:		System/Libraries

%description -n	%{libname}
This package contains the shared libraries for %{name}

%package -n	%develname
Summary:	Development library and header files for the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package contains the devel %{libname} library and its header
files.

%prep
%setup -q

%build
libtoolize --copy --force
autoreconf -fiv
%configure2_5x \
		--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%doc README
%{_includedir}/*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/yaml-0.1.pc

%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-3mdv2011.0
+ Revision: 671940
- mass rebuild
