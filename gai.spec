Summary:	General Applet Interface Library
Summary(pl):	Ogólna Biblioteka Interfejsu Apletu
Name:		gai
Version:	0.5.0
%define _pre    pre6
Release:	0.%{_pre}.1
License:	GPL v2
Group:		X11/Development/Libraries
Source0:	http://cesnet.dl.sourceforge.net/sourceforge/gai/%{name}-%{version}%{_pre}.tar.bz2
URL:		http://gai.sourceforge.net
BuildRequires:	gtk+2-devel
Requires:	gtk+2
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description devel
Header files required for GAI

%description devel -l pl
Pliki nag³ówkowe wymagane przez GAI

%prep
%setup -q -n %{name}-%{version}%{_pre}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}
%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS TODO examples
%{_libdir}/libgai*

%files devel
%defattr(644,root,root,755)
%{_includedir}/gai/gai.h
%{_libdir}/pkgconfig/gai.pc
