#
# Conditional build:
%bcond_without	gnome	# without GNOME support
%bcond_without	opengl	# without OpenGL support
%bcond_without	rox	# without ROX support
%bcond_without	sdl	# without SDL support
#
Summary:	General Applet Interface library
Summary(pl.UTF-8):	Ogólna biblioteka interfejsu apletu
Name:		gai
Version:	0.5.8
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/sourceforge/gai/%{name}-%{version}.tar.bz2
# Source0-md5:	29d90cb37fe5341009b27ffd09f871cb
Patch0:		%{name}-opt.patch
Patch1:		%{name}-libdir.patch
URL:		http://gai.sourceforge.net/
%{?with_sdl:BuildRequires:	SDL-devel >= 1.2}
BuildRequires:	autoconf >= 2.53
%{?with_opengl:BuildRequires:	gtkglext-devel >= 1.0}
%{?with_gnome:BuildRequires:	gnome-panel-devel >= 2.4.0}
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	pkgconfig
%{?with_rox:BuildRequires:	rox >= 2.1}
%{?with_rox:BuildRequires:	which}
BuildRequires:	zlib-devel
%{?with_gnome:Provides:	gai(gnome) = %{version}-%{release}}
%{?with_rox:Provides:	gai(rox) = %{version}-%{release}}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
This library is intended to simplify the development and use of
dockapps. With this library the programmer can focus on what the
applet shall do, not on the interface.

%description -l pl.UTF-8
Zamiarem tej biblioteki jest uproszczenie tworzenia i używania
apletów. Przy pomocy tej biblioteki programista może się skupić na tym
co aplet powinien robić a nie na jego interfejsie.

%package devel
Summary:	Development files for the GAI
Summary(pl.UTF-8):	Pliki rozwojowe dla GAI
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
%if %{with gnome}
Requires:	gnome-panel-devel >= 2.4.0
Requires:	gai(gnome) = %{version}-%{release}
Provides:	gai-devel(gnome) = %{version}-%{release}
%endif
%{?with_opengl:Requires:	gtkglext-devel >= 1.0}
%if %{with rox}
Requires:	gai(rox) = %{version}-%{release}
Provides:	gai-devel(rox) = %{version}-%{release}
%endif
Requires:	gtk+2-devel >= 2.0

%description devel
Header files required for development using GAI.

%description devel -l pl.UTF-8
Pliki nagłówkowe wymagane do tworzenia programów z użyciem GAI.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
%configure \
	%{!?with_opengl:--disable-gl} \
	%{!?with_gnome:--disable-gnome} \
	%{!?with_rox:--disable-rox} \
	%{!?with_sdl:--disable-sdl}

%{__make} \
	OPT="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -rf examples/[!C]* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README README.gai THANKS TODO WINDOWMANAGERS 
%attr(755,root,root) %{_libdir}/libgai.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_libdir}/libgai.so
%{_includedir}/gai
%{_pkgconfigdir}/gai.pc
%{_examplesdir}/%{name}-%{version}
