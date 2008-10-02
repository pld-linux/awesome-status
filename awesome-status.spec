# TODO
# - use standard %doc in %files
# - use standard DESTDIR in %install
Summary:	awesome-status populates the awesome window manager's widgets
Summary(hu.UTF-8):	awesome-status az awesome ablakkezelő widget-jeit tölti meg információval
Name:		awesome-status
Version:	1.4
Release:	1
License:	GPL v2
Group:		X11/Window Managers
Source0:	http://udvzsolt.extra.hu/e107_files/downloads/own_progs/%{name}-%{version}.tar.bz2
# Source0-md5:	57e9e64ee50c429fedb66d187f826c79
URL:		http://udvzsolt.extra.hu/
BuildRequires:	alsa-lib-devel
BuildRequires:	libconfuse-devel
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%{expand:%%define	_sysconfdir	%{_sysconfdir}/X11}

%description
awesome-status populates the awesome window manager's widgets. It
features CPU usage, date/time, lm_sensors (CPU temperature, fan RPMs,
etc.), memory/swap information, mpd information, network
download/upload, sound card information (volume and outgoing level),
and uptime information. A skeleton, commented config file is included.
Awesome-status is compatible with awesome 2.x and 3.x too.

%description -l hu.UTF-8
Az awesome-status az awesome ablakkezelő widget-jeit tölti meg.
Lehetséges CPU használat, dátum/idő, lm_sensor (CPU hőmérséklet,
ventilátorok fordulatszáma, stb.), memória/swap, mpd információ,
hálózati le- és feltöltés, hangkártya és uptime információ. Egy váz
konfigurációs fájl a csomagban. Awesome-status kompatibilis az awesome
2.x és 3.x-szel is!

%prep
%setup -q
%{__sed} -i -e "s|doc/awesome-status/|doc/awesome-status-%{version}/|g" Makefile

%build
CFLAGS="%{rpmcflags}" \
./configure \
	--prefix=$RPM_BUILD_ROOT%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install
rm -rf $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%doc Changelog README config-skeleton
