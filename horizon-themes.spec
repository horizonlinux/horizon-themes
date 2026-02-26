%global debug_package %{nil}

Name:       horizon-themes
Version:    1.2
Release:    1%{?dist}
Summary:    Horizon themes
License:    GPLv3+

URL:        https://github.com/horizonlinux/horizon-themes
Source0:    https://github.com/horizonlinux/horizon-themes/archive/refs/tags/1.2.tar.gz

%description
Horizon themes

%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonDark/contents/layouts
mkdir -p $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonLight/contents/layouts
mkdir -p $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonDark/contents/previews
mkdir -p $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonLight/contents/previews

install -p -m 644 io.github.horizonlinux.HorizonLight/contents/layouts/org.kde.plasma.desktop-layout.js $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonLight/contents/layouts/org.kde.plasma.desktop-layout.js
install -p -m 644 io.github.horizonlinux.HorizonLight/contents/previews/preview.png $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonLight/contents/previews/preview.png
install -p -m 644 io.github.horizonlinux.HorizonLight/contents/previews/fullscreenpreview.jpg $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonLight/contents/previews/fullscreenpreview.jpg
install -p -m 644 io.github.horizonlinux.HorizonLight/contents/defaults $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonLight/contents/defaults
install -p -m 644 io.github.horizonlinux.HorizonLight/metadata.json $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonLight/metadata.json

install -p -m 644 io.github.horizonlinux.HorizonDark/contents/layouts/org.kde.plasma.desktop-layout.js $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonDark/contents/layouts/org.kde.plasma.desktop-layout.js
install -p -m 644 io.github.horizonlinux.HorizonDark/contents/previews/preview.png $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonDark//contents/previews/preview.png
install -p -m 644 io.github.horizonlinux.HorizonDark/contents/previews/fullscreenpreview.jpg $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonDark//contents/previews/fullscreenpreview.jpg
install -p -m 644 io.github.horizonlinux.HorizonDark/contents/defaults $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonDark/contents/defaults
install -p -m 644 io.github.horizonlinux.HorizonDark/metadata.json $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonDark/metadata.json

mkdir -p $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas
install -p -m 644 10_org.gnome.desktop.interface.horizon.override $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas

%files
%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonDark/*
%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonLight/*
%{_datadir}/glib-2.0/schemas/*.override

%changelog
* Thu Feb 26 2026 Marcel Mrówka <micro.mail88@gmail.com>
- Update theme for Plasma 6.6

* Fri Jan 30 2026 Marcel Mrówka <micro.mail88@gmail.com>
- Create GTK theme override

* Thu Jan 29 2026 Marcel Mrówka <micro.mail88@gmail.com>
- package created
