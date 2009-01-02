%define api 0
%define	major 1
%define libname	%mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

Summary:	YAML 1.1 parser and emitter written in C
Name:		yaml
Version:	0.1.2
Release:	%mkrel 1
License:	MIT
Group:		System/Libraries
URL:		http://pyyaml.org/wiki/LibYAML
Source0:	http://pyyaml.org/download/libyaml/%name-%version.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
LibYAML is a YAML 1.1 parser and emitter written in C.

%package -n	%{libname}
Summary:	YAML 1.1 parser and emitter written in C
Group:          System/Libraries

%description -n	%{libname}
This package contains the shared libraries for %{name}

%package -n	%develname
Summary:	Development library and header files for the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%develname
This package contains the static %{libname} library and its header
files.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README
%{_libdir}/lib*.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/lib*.la
%{_libdir}/lib*.so
