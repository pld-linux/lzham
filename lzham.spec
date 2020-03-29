Summary:	LZHAM - Lossless Data Compression Codec
Summary(pl.UTF-8):	LZHAM - kodek bezstratnej kompresji danych
Name:		lzham
Version:	1.0.stable1
%define	tagver	%(echo %{version} | tr . _)
Release:	0.1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/richgel999/lzham_codec/releases
Source0:	https://github.com/richgel999/lzham_codec/archive/v%{tagver}/lzham_codec-%{tagver}.tar.gz
# Source0-md5:	68ec3db42d2263d7e79d0581293f946d
Patch0:		%{name}-includedir.patch
Patch1:		%{name}-x32.patch
URL:		https://github.com/richgel999/lzham_codec
BuildRequires:	cmake >= 2.8
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LZHAM is a lossless data compression codec written in C/C++
(specifically C++03), with a compression ratio similar to LZMA but
with 1.5x-8x faster decompression speed.

%description -l pl.UTF-8
LZHAM to kodek bezstratnej kompresji danych, napisany w C/C++ (w
szczególności C++03). Współczynnik kompresji jest podobny do LZMA, ale
szybkość dekompresji jest 1.5-8 razy większa.

%package devel
Summary:	Header files for LZHAM libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek LZHAM
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for LZHAM libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek LZHAM.

%prep
%setup -q -n lzham_codec-%{tagver}
%patch0 -p1
%patch1 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_libdir}/liblzhamcomp.so
%attr(755,root,root) %{_libdir}/liblzhamdecomp.so
%attr(755,root,root) %{_libdir}/liblzhamdll.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/lzham
