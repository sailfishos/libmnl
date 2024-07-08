Name:          libmnl
Version:       1.0.5
Release:       1
Summary:       Minimalistic Netlink user-space library
License:       LGPLv2
Source0:       %{name}-%{version}.tar.bz2

URL:           https://github.com/sailfishos/libmnl/

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
libmnl is a minimalistic user-space library oriented to Netlink developers.
There are a lot of common tasks in parsing, validating, constructing of both
the Netlink header and TLVs that are repetitive and easy to get wrong.
This library aims to provide simple helpers that allows you to re-use code and
to avoid re-inventing the wheel.

%package       devel
Summary:       Development files for %{name}
Requires:      %{name} = %{version}-%{release}

%package       static
Summary:       Static development files for %{name}
Requires:      %{name}-devel = %{version}-%{release}

%description   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%description   static
The %{name}-static package contains static libraries for developing
applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%autogen
%configure
%make_build CFLAGS="%{optflags}"

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README
%{_libdir}/%{name}.so.0*

%files devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so
