Summary:	A popular and easy to use graphical IRC (chat) client
Summary(pl.UTF-8):	Popularny i łatwy w użyciu graficzny klient IRC
Name:		hexchat
Version:	2.16.1
Release:	7
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	https://dl.hexchat.net/hexchat/%{name}-%{version}.tar.xz
# Source0-md5:	0af269d719c2c047310d44804bb31fdb
URL:		https://hexchat.github.io
BuildRequires:	dbus-glib-devel
BuildRequires:	glib2-devel >= 1:2.34.0
BuildRequires:	gtk+2-devel
BuildRequires:	hicolor-icon-theme
BuildRequires:	iso-codes
BuildRequires:	libcanberra-devel >= 0.22
BuildRequires:	libproxy-devel
BuildRequires:	lua54-devel
BuildRequires:	meson >= 0.47.0
BuildRequires:	ninja >= 1.5
BuildRequires:	openssl-devel >= 0.9.8
BuildRequires:	pciutils-devel
BuildRequires:	perl-devel
BuildRequires:	perl-ExtUtils-Embed
BuildRequires:	python3-cffi
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	rpmbuild(macros) >= 2.042
Requires:	enchant2
Requires:	glib2 >= 1:2.34.0
Requires:	libcanberra >= 0.22
Requires:	python3-cffi
Obsoletes:	xchat < 2.16.1
Recommends:	sound-theme-freedesktop
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HexChat is an easy to use graphical IRC chat client for the X Window
System. It allows you to join multiple IRC channels (chat rooms) at
the same time, talk publicly, private one-on-one conversations etc.
Even file transfers are possible.

%description -l pl.UTF-8
HexChat to łatwy w użyciu graficzny klient IRC dla systemu X Window.
Pozwala dołączać do wielu kanałów IRC w tym samym czasie, rozmawiać
publicznie, prywatnie z jedną osobą itp. Możliwe jest też przesyłanie
plików.

%package devel
Summary:	Development files for HexChat plugins
Summary(pl.UTF-8):	Pliki programistyczne dla wtyczek HexChata
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development files for HexChat.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki programistyczne HexChata.

%prep
%setup -q

%build
%meson \
	-Ddbus=enabled \
	-Dlibcanberra=enabled \
	-Dwith-lua=lua5.4

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__mv} $RPM_BUILD_ROOT%{_localedir}/ja{_JP,}
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/no

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc readme.md
%attr(755,root,root) %{_bindir}/hexchat
%dir %{_libdir}/hexchat
%dir %{_libdir}/hexchat/plugins
%attr(755,root,root) %{_libdir}/hexchat/plugins/checksum.so
%attr(755,root,root) %{_libdir}/hexchat/plugins/fishlim.so
%attr(755,root,root) %{_libdir}/hexchat/plugins/lua.so
%attr(755,root,root) %{_libdir}/hexchat/plugins/sysinfo.so
%attr(755,root,root) %{_libdir}/hexchat/plugins/perl.so
%attr(755,root,root) %{_libdir}/hexchat/plugins/python.so
%{_libdir}/hexchat/python
%{_desktopdir}/io.github.Hexchat.desktop
%{_iconsdir}/hicolor/*/apps/io.github.Hexchat.*
%{_datadir}/metainfo/io.github.Hexchat.appdata.xml
%{_datadir}/dbus-1/services/org.hexchat.service.service
%{_mandir}/man1/hexchat.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/hexchat-plugin.h
%{_pkgconfigdir}/hexchat-plugin.pc
