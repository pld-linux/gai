#
# Conditional build:
%bcond_without	gl	# without OpenGL support
%bcond_without	gnome	# without GNOME support
%bcond_without	sdl	# without SDL support
#
Summary:	General Applet Interface library
Summary(pl):	Ogólna biblioteka interfejsu apletu
Name:		gai
Version:	0.5.1
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/gai/%{name}-%{version}.tar.bz2
# Source0-md5:	5c3805238018423b3bba53c6fdffa921
Patch0:		%{name}-opt.patch
URL:		http://gai.sourceforge.net/
%{?with_sdl:BuildRequires:	SDL-devel >= 1.2}
BuildRequires:	autoconf >= 2.53
%{?with_gl:BuildRequires:	gtkglext-devel >= 1.0}
%{?with_gnome:BuildRequires:	gnome-panel-devel >= 2.4.0}
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
This library is intended to simplify the development and use of
dockapps. With this library the programmer can focus on what the
applet shall do, not on the interface.

%description -l pl
Zamiarem tej biblioteki jest uproszczenie tworzenia i u¿ywania
apletów. Przy pomocy tej biblioteki programista mo¿e siê skupiæ na tym
co aplet powinien robiæ a nie na jego interfejsie.

%package devel
Summary:	Development files for the GAI
Summary(pl):	Pliki rozwojowe dla GAI
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
%{?with_gl:Requires:	gtkglext-devel >= 1.0}
%{?with_gnome:Requires:	gnome-panel-devel >= 2.4.0}
Requires:	gtk+2-devel >= 2.0

%description devel
Header files required for development using GAI.

%description devel -l pl
Pliki nag³ówkowe wymagane do tworzenia programów z u¿yciem GAI.

%prep
%setup -q 
%patch0 -p1

%build
%{__autoconf}
%configure \
	%{!?with_gl:--disable-gl} \
	%{!?with_gnome:--disable-gnome}
	%{!?with_sdl:--disable-sdl}

%{__make} \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -rf examples/[!C]* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README README.gai THANKS TODO WINDOWMANAGERS docs/FAQ.html
%attr(755,root,root) %{_libdir}/libgai.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/referenceguide.html
%attr(755,root,root) %{_libdir}/libgai.so
%{_includedir}/gai
%{_pkgconfigdir}/gai.pc
%{_examplesdir}/%{name}-%{version}
