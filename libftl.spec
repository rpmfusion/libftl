Name:           libftl
Version:        0.9.14
Release:        5%{?dist}
Summary:        FTL audio/video streaming library

License:        MIT
URL:            https://github.com/mixer/ftl-sdk
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         libdir-fix.patch
Patch1:         headers-fix.patch

BuildRequires:  cmake3
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
FTL-SDK is a cross platform SDK written in C to enable sending audio/video to
mixer using FTL service.


%prep
%autosetup -p1 -n ftl-sdk-%{version}

%package devel
Summary:        Development files for libftl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libftl.


%build
mkdir -p build
pushd build
%cmake3 -DDISABLE_AUTO_INGEST=TRUE \
        -DDISABLE_FTL_APP=TRUE \
        -DFTL_INSTALL_INCLUDES=TRUE ..
%make_build
popd

%install
%make_install -C build

%files
%license LICENSE
%doc README.md
%{_libdir}/%{name}.so.0*


%files devel
%{_libdir}/%{name}.so
%{_includedir}/ftl/

%changelog
* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 03 2019 Momcilo Medic <fedorauser@fedoraproject.org> - 0.9.14-2
- Added patches for headers and library destination handling

* Tue Apr 02 2019 Momcilo Medic <fedorauser@fedoraproject.org> - 0.9.14-1
- First public release
