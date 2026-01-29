Name:       horizon-themes
Version:    1.0
Release:    1%{?dist}
Summary:    Horizon themes
License:    GPLv3+

URL:        https://github.com/horizonlinux/horizon-themes
Source0:    https://github.com/horizonlinux/horizon-themes/archive/refs/tags/1.0.tar.gz

%description
Horizon themes

%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonDark/contents/layouts
mkdir -p $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonLight/contents/layouts

install -p -m 644 io.github.horizonlinux.HorizonLight/contents/layouts/org.kde.plasma.desktop-layout.js $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonLight/contents/layouts/org.kde.plasma.desktop-layout.js
install -p -m 644 io.github.horizonlinux.HorizonLight/contents/defaults $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonLight/contents/defaults
install -p -m 644 io.github.horizonlinux.HorizonLight/metadata.json $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonLight/metadata.json

install -p -m 644 io.github.horizonlinux.HorizonDark/contents/layouts/org.kde.plasma.desktop-layout.js $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonDark/contents/layouts/org.kde.plasma.desktop-layout.js
install -p -m 644 io.github.horizonlinux.HorizonDark/contents/defaults $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonDark/contents/defaults
install -p -m 644 io.github.horizonlinux.HorizonDark/metadata.json $RPM_BUILD_ROOT%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonDark/metadata.json

%files
%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonDark/*
%{_datadir}/plasma/look-and-feel/io.github.horizonlinux.HorizonLight/*

%changelog
* Thu Jan 29 2026 Marcel Mrówka <micro.mail88@gmail.com>
- package created
