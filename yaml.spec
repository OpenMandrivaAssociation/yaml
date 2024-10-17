%define api 0
%define major 2
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

# (tpg) optimize it a bit
%global optflags %{optflags} -O3

Summary:	YAML 1.1 parser and emitter written in C
Name:		yaml
Version:	0.2.5
Release:	2
License:	MIT
Group:		System/Libraries
URL:		https://pyyaml.org/wiki/LibYAML
Source0:	https://github.com/yaml/libyaml/archive/%{version}.tar.gz
BuildRequires:	doxygen

%description
LibYAML is a YAML 1.1 parser and emitter written in C.

%package -n %{libname}
Summary:	YAML 1.1 parser and emitter written in C
Group:		System/Libraries

%description -n %{libname}
This package contains the shared libraries for %{name}.

%package -n %{develname}
Summary:	Development library and header files for the %{name} library
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
This package contains the devel %{libname} library and its header
files.

%prep
%autosetup -p1 -n lib%{name}-%{version}

%build
libtoolize --copy --force
autoreconf -fiv
%configure \
	--disable-static

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_includedir}/*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/yaml-0.1.pc
