#
# spec file for package kwin6
#
# Copyright (c) 2026 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


# Internal QML imports
%global __requires_exclude qt6qmlimport\\(org\\.kde\\.KWin\\.Effect\\.WindowView.*

%define kf6_version 6.18.0
%define qt6_version 6.9.0

%define rname   kwin
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kwin6
Version:        6.6.0
Release:        1.1
Summary:        KDE Window Manager
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
# ok you filthy drunken whore, put your patches (in order) here
Patch1:         0001-feature-allow-disable-hardcoded-touchpad-gestures.patch
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
# GCC 13 doesn't know std::ranges::to
%if 0%{?suse_version} == 1500
BuildRequires:  gcc14-PIE
BuildRequires:  gcc14-c++
%endif
%if 0%{?suse_version} == 1600
BuildRequires:  gcc15-PIE
BuildRequires:  gcc15-c++
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel >= %{qt6_version}
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(Breeze) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KDecoration3) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Declarative) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Holidays) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Runner) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KGlobalAccelD) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KNightTime) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KScreenLocker) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KWayland) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.14.0
BuildRequires:  cmake(QAccessibilityClient6)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sensors) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(epoxy) >= 1.3
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libdisplay-info) >= 0.2.0
BuildRequires:  pkgconfig(libdrm) >= 2.4.116
BuildRequires:  pkgconfig(libeis-1.0)
BuildRequires:  pkgconfig(libinput) >= 1.26
%if 0%{?suse_version} > 1500
# Leap 15 version is too old
BuildRequires:  pkgconfig(libpipewire-0.3) >= 1.2.0
%endif
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libxcvt)
BuildRequires:  pkgconfig(wayland-cursor) >= 1.22
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.38
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb) >= 1.10
BuildRequires:  pkgconfig(xcb-composite) >= 1.10
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-dri3) >= 1.10
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-present) >= 1.10
BuildRequires:  pkgconfig(xcb-randr) >= 1.10
BuildRequires:  pkgconfig(xcb-render) >= 1.10
BuildRequires:  pkgconfig(xcb-res) >= 1.10
BuildRequires:  pkgconfig(xcb-shape) >= 1.10
BuildRequires:  pkgconfig(xcb-shm) >= 1.10
BuildRequires:  pkgconfig(xcb-sync) >= 1.10
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xfixes) >= 1.10
BuildRequires:  pkgconfig(xcb-xinerama) >= 1.10
BuildRequires:  pkgconfig(xcb-xinput) >= 1.10
BuildRequires:  pkgconfig(xcb-xkb) >= 1.10
BuildRequires:  pkgconfig(xkbcommon) >= 0.7.0
BuildRequires:  pkgconfig(xkbcommon-x11)
Requires:       breeze6-decoration >= %{_plasma6_bugfix}
# Needed to show dialogs
Requires:       kdialog
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kglobalacceld6 >= %{_plasma6_bugfix}
Requires:       libkwin6 = %{version}
Requires:       xwayland
# SECTION QML dependencies
Requires:       kf6-kdeclarative-imports >= %{kf6_version}
Requires:       kf6-kitemmodels-imports >= %{kf6_version}
Requires:       plasma6-framework-components >= %{_plasma6_bugfix}
Requires:       qt6-declarative-imports >= %{qt6_version}
Requires:       qt6-multimedia-imports >= %{qt6_version}
# /SECTION
# For post and verifyscript
Requires(post): permissions
Requires(verify): permissions
# For displaying full monitor vendor names
Recommends:     hwdata
# xorg-x11-server-wayland is required by plasma6-session-wayland, but not kwin6 itself
Recommends:     xorg-x11-server-wayland
# /usr/share/kwin/tabbox/thumbnail_grid/metadata.json conflicts with plasma5-addons
# (Use a version check as plasma6-addons provides plasma5-addons)
Conflicts:      plasma5-addons < 6.0
Conflicts:      plasma5-addons-lang < 6.0
Provides:       kwin5 = %{version}
Obsoletes:      kwin5 < %{version}
Obsoletes:      kwin5-lang < %{version}
Provides:       windowmanager
Provides:       qt6qmlimport(org.kde.kwin)
Provides:       qt6qmlimport(org.kde.kwin.3) = 0

%description
KWin is Plasma window manager.

%package -n libkwin6
Summary:        KWin library

%description -n libkwin6
KWin is Plasma window manager.
This package provides the kwin library.

%package devel
Summary:        KDE Window Manager - development files
Requires:       kdecoration6-devel >= %{_plasma6_bugfix}
Requires:       libkwin6 = %{version}
Requires:       pkgconfig(epoxy)
Requires:       pkgconfig(libdrm) >= 2.4.116
Provides:       kwin5-devel = %{version}
Obsoletes:      kwin5-devel < %{version}

%description devel
KWin is Plasma window manager.
This package provides development files.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 \
%if 0%{?suse_version} == 1500
  -DCMAKE_C_COMPILER:STRING=gcc-14 \
  -DCMAKE_CXX_COMPILER:STRING=g++-14
%endif
%if 0%{?suse_version} == 1600
  -DCMAKE_C_COMPILER:STRING=gcc-15 \
  -DCMAKE_CXX_COMPILER:STRING=g++-15
%endif
%{nil}

%kf6_build

%install
%kf6_install

%find_lang kwin6 --with-html --all-name

%fdupes %{buildroot}%{_kf6_libdir}
%fdupes %{buildroot}%{_kf6_sharedir}

%preun
%{systemd_user_preun plasma-kwin_wayland.service}

%post
%ldconfig
%ldconfig -n libkwin6
%set_permissions %{_kf6_bindir}/kwin_wayland
%{systemd_user_post plasma-kwin_wayland.service}

%postun
%ldconfig
%ldconfig -n libkwin6
%{systemd_user_postun plasma-kwin_wayland.service}

%ldconfig_scriptlets -n libkwin6

%verifyscript
%verify_permissions -e %{_kf6_bindir}/kwin_wayland

%files
%verify(not caps) %{_kf6_bindir}/kwin_wayland
%license LICENSES/*
%doc README.md
%doc %lang(en) %{_kf6_htmldir}/en/*
%{_kf6_applicationsdir}/kcm_animations.desktop
%{_kf6_applicationsdir}/kcm_kwin_effects.desktop
%{_kf6_applicationsdir}/kcm_kwin_scripts.desktop
%{_kf6_applicationsdir}/kcm_kwin_virtualdesktops.desktop
%{_kf6_applicationsdir}/kcm_kwindecoration.desktop
%{_kf6_applicationsdir}/kcm_kwinoptions.desktop
%{_kf6_applicationsdir}/kcm_kwinrules.desktop
%{_kf6_applicationsdir}/kcm_kwintabbox.desktop
%{_kf6_applicationsdir}/kcm_kwinxwayland.desktop
%{_kf6_applicationsdir}/kcm_virtualkeyboard.desktop
%{_kf6_applicationsdir}/org.kde.kwin.killer.desktop
%{_kf6_bindir}/kwin_wayland_wrapper
%{_kf6_bindir}/kwindowprop
%{_kf6_configkcfgdir}/*
%{_kf6_debugdir}/org_kde_kwin.categories
%{_kf6_iconsdir}/hicolor/*/apps/kwin.png
%{_kf6_iconsdir}/hicolor/scalable/apps/kwin.svgz
%{_kf6_knsrcfilesdir}/*.knsrc
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-delete-desktop-switching-shortcuts
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-remove-breeze-tabbox-default
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-reset-active-mouse-screen
%{_kf6_libdir}/kconf_update_bin/kwin-6.1-remove-gridview-expose-shortcuts
%{_kf6_libdir}/kconf_update_bin/kwin-6.5-showpaint-changes
%{_kf6_libdir}/kconf_update_bin/kwin5_update_default_rules
%{_kf6_libdir}/libkcmkwincommon.so.*
%{_kf6_notificationsdir}/kwin.notifyrc
%dir %{_kf6_plugindir}/kwin
%dir %{_kf6_plugindir}/kwin/effects
%dir %{_kf6_plugindir}/kwin/effects/configs
%{_kf6_plugindir}/kwin/effects/configs/kcm_kwin4_genericscripted.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_blur_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_diminactive_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_glide_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_hidecursor_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_magiclamp_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_mouseclick_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_mousemark_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_overview_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_slide_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_thumbnailaside_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_tileseditor_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_trackmouse_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_windowview_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_wobblywindows_config.so
%dir %{_kf6_plugindir}/kwin/plugins
%{_kf6_plugindir}/kwin/plugins/BounceKeysPlugin.so
%{_kf6_plugindir}/kwin/plugins/KeyNotificationPlugin.so
%{_kf6_plugindir}/kwin/plugins/StickyKeysPlugin.so
%{_kf6_plugindir}/kwin/plugins/SlowKeysPlugin.so
%{_kf6_plugindir}/kwin/plugins/buttonsrebind.so
%{_libdir}/qt6/plugins/kwin/plugins/gamecontroller.so
%{_prefix}/lib/debug%{_libdir}/qt6/plugins/kwin/plugins/gamecontroller.so.debug
%if %{pkg_vcmp pkgconfig(libeis-1.0) >= 1.4}
%{_kf6_plugindir}/kwin/plugins/eis.so
%endif
%{_kf6_plugindir}/kwin/plugins/krunnerintegration.so
%{_kf6_plugindir}/kwin/plugins/nightlight.so
%{_kf6_plugindir}/kwin/plugins/MouseKeysPlugin.so
%if 0%{?suse_version} > 1500
%{_kf6_plugindir}/kwin/plugins/screencast.so
%endif
%{_kf6_plugindir}/kwin/plugins/screenshot.so
%{_kf6_plugindir}/kwin/plugins/TouchpadShortcutsPlugin.so
%dir %{_kf6_plugindir}/kf6/packagestructure
%{_kf6_plugindir}/kf6/packagestructure/kwin_aurorae.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_decoration.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_effect.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_scripts.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_windowswitcher.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm*.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kwin*.so
%dir %{_kf6_qmldir}/org/kde/kwin/
%{_kf6_qmldir}/org/kde/kwin/private/
%{_kf6_sharedir}/kconf_update/kwin.upd
%{_kf6_sharedir}/krunner/dbusplugins/kwin-runner-windows.desktop
%{_kf6_sharedir}/kwin-wayland/
%{_libexecdir}/kwin_killer_helper
%{_libexecdir}/kwin-applywindowdecoration
%{_libexecdir}/kwin-tabbox-preview
%{_userunitdir}/plasma-kwin_wayland.service

%files -n libkwin6
%{_kf6_libdir}/libkwin.so.*

%files devel
%{_includedir}/kwin/
%{_kf6_cmakedir}/KWin/
%{_kf6_cmakedir}/KWinDBusInterface/
%{_kf6_dbusinterfacesdir}/org.kde.kwin.*
%{_kf6_dbusinterfacesdir}/org.kde.KWin.*
%{_kf6_libdir}/libkwin.so

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en

%changelog
* Thu Feb 12 2026 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.6.0:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.6.0
- Too many changes to list here
* Wed Jan 28 2026 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.5.91:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.5.91
- Too many changes to list here
* Sat Jan 17 2026 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.5.90:
  * New feature release
  * For more details see https://kde.org/announcements/plasma/6/6.5.90
- Too many changes to list here
* Tue Jan 13 2026 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.5.5:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.5.5
- Changes since 6.5.4:
  * Update version for new release 6.5.5
  * useractions: use output order for "switch to screen i" shortcuts
  * useractions: use output order for "move window to screen i" shortcuts (kde#514465)
  * backends/wayland: fix the cursor hotspot with scaling
  * wayland/linuxdmabuf: drop buffers instead of deleting directly
  * Handle key repeat state from input method keys (kde#513637)
  * compositor: don't attempt to use cursor sizes other than the recommended one (kde#513810)
  * wayland/outputmanagement: reject clearly nonsensical positions
  * scene/workspacescene: ignore items with an opacity of zero (kde#513203)
  * core/sessions: don't take ownership of an fd that Qt will close (kde#513151)
  * Missing exported header file a11ykeyboardmonitor.h added
  * wayland: Fix sending wl_data_source::dnd_action(0) after drop (kde#512235)
  * rules: pass an activation token to the window rules KCM
  * xwayland: Fix keysniffing repeating keys (kde#510404)
- Drop patches, now upstream:
  * 0001-core-sessions-don-t-take-ownership-of-an-fd-that-Qt-.patch
* Sat Dec 13 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Add patch to fix kwin freezes (kde#513151):
  * 0001-core-sessions-don-t-take-ownership-of-an-fd-that-Qt-.patch
* Tue Dec  9 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.5.4:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.5.4
- Changes since 6.5.3:
  * Update version for new release 6.5.4
  * inputmethod: send empty surrounding text when the input method is force activated (kde#512245)
  * scene: Fix computed painted area of transformed items with HiDPI (kde#510029)
  * plugins/trackmouse: Fix stuttering (kde#512767)
  * Fix wrong assumption about the tablet pad strip position
  * outputconfigurationstore: be more conservative with VGA displays (kde#512146)
  * A11yKeyboardMonitor: Fix KeyEvent being emitted too often when grabbing keys (kde#512189)
  * Start adding test for A11yKeyboardManager
  * backends/libinput: clamp tablet and touch coordinates to target output (kde#512672)
  * events: ignore XCB_FOCUS_OUT events by default (kde#509115)
  * x11window: support xrandr emulation (kde#501505)
  * wayland: Don't withdraw data offers when keyboard focus changes (kde#511509)
  * backends/virtual: Allow creating virtual outputs
  * plugins/qpa: Fix build with Qt 6.11 and Qt 6.10.2
  * ci: Temporarily disable Qt 6.11 pipeline
  * plugins/windowview: Fix clear button
  * xwayland: Prevent more invalidated iterators
  * Use correct DBus interface for inhibiting sleep (kde#512276)
  * backends/drm: add missing thread include
  * activation: always allow activating child windows of the active one
  * backends/drm: don't do modesets if all pipelines are removed (kde#512097)
  * backends/drm: add missing layer repaints for night light changes (kde#511812)
  * scene/scene: schedule pending repaints for child items too (kde#511653)
  * scene/workspacescene: don't put non-opaque items on an underlay (kde#511491)
* Tue Nov 18 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.5.3:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.5.3
- Too many changes to list here
* Tue Nov  4 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.5.2:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.5.2
- Changes since 6.5.1:
  * Fix kwin_wayland crash on FreeBSD
  * Update version for new release 6.5.2
  * dpmsinputeventfilter: Disable proximity sensor and add null check
  * plugins/showfps,-compositing: apply vertical offset to geometry (kde#511232)
  * plugins/blur: Make contrast opt-in (kde#510818)
  * Revert "Only keep the saturation component from the old contrast effect"
  * compositor: fix KWIN_FORCE_SW_CURSOR
  * plugins/screenshot: filter out decoration and shadows to match the options (kde#510982,kde#511171)
  * plugins/screencast: on close, reset screencast sources instead of just pausing (kde#511150)
  * backends/drm: handle changing output layers of virtual outputs correctly
  * backends/drm: fix warnings when the virtual output is used
  * backends/drm: fix implicit modifier fallback (kde#511216)
  * xwayland: Initialize Selection::m_timestamp
  * xwayland: Drop Selection::setWindow()
  * xwayland: Avoid potentially creating an X11 source for own proxy data
  * xwayland: Drop Selection::m_disownPending
  * scene/cursoritem: always reset the surface item if the surface is nullptr (kde#511075)
  * backends/drm: prevent using the same cursor plane on multiple screens (kde#511281)
  * Update version for new release 6.5.2
  * xwayland: Update clipboard when active window changes (kde#511063)
  * plugins/mousekeys: Do not release the pointer button on key repeat events (kde#510248)
* Tue Oct 28 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.5.1:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.5.1
- Too many changes to list here
* Thu Oct 16 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.5.0:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.5.0
- Too many changes to list here
* Thu Oct  2 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.4.91:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.4.91
- Changes since 6.4.90:
  * Update version for new release 6.4.91
  * effects/overview: fix behavior when deskotp grid doesn't layout (kde#510056)
  * backends/wayland: Fix render time query with sw renderer
  * kcms/tabbox: Hide bottom separator if KNS is disabled
  * autotests: Check that a drag will be cancelled when the current touch sequence is cancelled
  * [plugins/buttonsrebindfilter] Fix infinite loop when walking config group hierarchy
  * ButtonsRebindsFilter: Fix my bad ring math, allow completing a circle
  * ButtonsRebindsFilter: Remove assumption about how config keys are stored
  * Make sure XdgToplevelWindow always has an icon
  * core: Add dropped assert in GraphicsBuffer destructor
  * wayland: Use std::make_shared to allocate sync release points
  * core: Fix GraphicsBufferRef copy constructor
  * xwayland: remove warning about not finding matching X11 output
  * autotests: Rewrite xwayland selection test
  * autotests: Add primary selection wrappers
  * autotests: Include mime types in TARGETS in testXwaylandDnd
  * tabbox: unify on "Peek at Desktop" name (kde#507401)
  * Revert "wayland: Check current drag and drop action"
  * autotests/integration: make the sticky keys test more complete
  * inputmethod: Fix printing hexadecimal unicode code points
  * wayland_server: re-enable wl_drm by default
  * Adjust to activities changes
  * autotests/integration: add test for fractional scaling glitches (kde#509165)
  * Fix a few potential missing opportunity that input method active state is not synced. (kde#506095)
  * Add a small helper around queryWindowInfo
  * Drop unused xcb-util-cursor dependency
* Tue Sep 23 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.4.90:
  * New feature release
  * For more details see https://kde.org/announcements/plasma/6/6.4.90
- Too many changes to list here
* Tue Sep  9 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.4.5:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.4.5
- Changes since 6.4.4:
  * Update version for new release 6.4.5
  * wayland/colormanagement: add inert protocol error
  * outputconfigurationstore: never choose a removed mode
  * outputconfigurationstore: add some debug logging for mode selection
  * outputconfigurationstore: add logging category specific to output configs
  * wayland/surface: don't clear fifo barrier on new commits (kde#508822)
  * backends/libinput: prefer output UUID over output names for identifying outputs
  * wayland: Check for nullptr output in ColorManagementOutputV1
  * backends/drm: work around amdgpu applying GAMMA_LUT in test-only commits
  * wayland: fix only changing the rendering intent not doing anything
  * wayland/outputdevice: add missing scheduleDone calls (kde#507087)
  * wayland: Make ColorManagementOutputV1 handle output removal better (kde#504959)
  * backends/drm: Reduce gamma LUT resolution requirement for color offload
  * backends/drm: Also restrict gamma LUT size for atomic modesetting
  * backends/drm: Use correct color pipeline for linear night light fallback
  * backends/drm: ignore disabled outputs when checking for dpms off (kde#493879)
  * plugins/maximize: ensure all animations end on the same frame (kde#505478)
  * core/Outputlayer: fix the check for supported formats
  * backends/libinput: Don't ask the session to take /sys/ devices
  * kcms/tabbox: Use Plasma theme for preview (kde#507819)
- Drop patch, now upstream:
  * 0001-backends-drm-work-around-amdgpu-applying-GAMMA_LUT-i.patch
* Thu Aug 21 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Add patch to avoid flicker due to amdgpu driver bug (kde#508350):
  * 0001-backends-drm-work-around-amdgpu-applying-GAMMA_LUT-i.patch
* Wed Aug  6 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.4.4:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.4.4
- Changes since 6.4.3:
  * Update version for new release 6.4.4
  * kcms/tabbox: set up i18n for preview
  * scene/itemrenderer_opengl: use the correct rendering intent for the color pipeline
  * a11ykeyboardmanager: Send second modifier press to screenreader (kde#507545)
  * plugins/screencast: Only offer explicit sync if the DRM device supports it
  * autotests/screencast: make the window fullscreen, and wait for it to be presented
  * backends/drm: avoid dropping the color pipeline cache for empty pipelines
  * plugins/magnifier: allocate an fbo when rendering, and don't crash if it fails
  * plugins/magnifier: actually set the initial zoom properly (kde#507248)
  * backends/drm: never use default colorimetry of the edid
  * tabbox: Work around QtQuick crashing kwin (kde#506502)
* Tue Jul 15 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.4.3:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.4.3
- Changes since 6.4.2:
  * Update version for new release 6.4.3
  * Guard against internal window being null when dispatching tablet events (kde#506886)
  * Fix "activate and raise" action with panels (kde#461414)
  * wayland: close popups upon window activation (kde#497075)
  * wayland: Fix resizing with fractional increments
  * plugins/magnifier: Constrain zoom factors (kde#506549)
  * cmake: install wayland/textinput.h
  * A11yKeyboardMonitor: Distinguish modifier and other key (kde#506715)
  * tablet: Fix sending delta for relative dials
  * backends/drm: Fix memory leak in DrmGpu::createNonMasterFd
  * backends/drm: never use DEGAMMA_LUT (kde#505869)
  * wayland: Remove buffer checks in xdg_surface and layer_surface factory requests (kde#506412)
  * backends/drm: don't use UUID to identify outputs (kde#493879,kde#506135,kde#505953)
  * xdgshellwindow: Reset gravity on interactive resize finish
  * workspace: Fix window activation on activity change (kde#501393)
  * utils/edid: also read edid colorimetry (kde#505971)
  * OutputConfigurationStore: Don't auto-generate low-but-not-1 scale factors
  * backends/virtual: use explicit modifiers for egl
  * A11yKeyboardMonitor: Fix sending keycodes to AT (kde#506445)
  * xwayland: don't forward left/middle/right mouse buttons to Xwayland
* Tue Jul  1 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.4.2:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.4.2
- Changes since 6.4.1:
  * tabbox: Guard for empty key sequences (kde#506369)
  * Update version for new release 6.4.2
  * scene: Skip visibility check for the Item itself in framePainted
  * a11ykeyboardmanager: Grab keys when grabbed modifier is pressed (kde#506078)
  * output management: add some safe guards for invalid brightness overrides (kde#506090)
  * Don't add deleted windows to the stacking order
  * backends/drm: allow night light to get closer to the edges of the gamut (kde#505495)
  * plugins/fadingpopups: Blacklist spectacle popup menus from fading effect (kde#505803)
* Tue Jun 24 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.4.1:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.4.1
- Changes since 6.4.0:
  * Update version for new release 6.4.1
  * plugins/slide: Fix animation after moving a desktop
  * Update version for new release 6.4.1
  * compositor: clamp artificial hdr headroom to the currently max possible one
  * core,opengl: allow the tone mapper to reduce reference luminance more
  * backends/drm: use the next artificial hdr headroom instead of the current one
  * backends/drm: apply the limit for max artificial hdr headroom to max luminance
  * outputconfigurationstore: disallow DDC/CI for the Samsung Odyssey G5 (kde#494522)
  * Fix Window::mousePressCommandConsumesEvent() for "activate" action (kde#506007)
  * Sync virtual desktop grid to new virtual desktop order (kde#506022)
  * kcms/screenedges: Fix listing third party extensions (kde#505934)
  * Fix tablet cursor getting stuck in hidden state in relative mode (kde#505989)
  * core/renderloop: fix subsurfaces vrr scheduling
  * effect: Add missing triggerRepaint() in retarget()
  * wayland_server: re-enable wl_drm by default
  * Split tablet tool tip event data in two frames (kde#479856)
  * wayland/tablet_v2: fix the tablet cursor hotspot with Xwayland scaling
  * kcms/animations: disable configure button for disabled checkable effects (kde#505789)
  * plugins/slideback: Scale smoothness proportionally to adjusted strength from 6.3 (kde#503964)
  * Fix direct scanout target rect on rotated outputs
  * Drop no longer used KF6ConfigWidgets dependency
  * plugins/systembell: Throttle visual bell
* Thu Jun 12 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.4.0:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.4.0
- Changes since 6.3.91:
  * Update version for new release 6.4.0
  * backends/drm: also handle GPU resets on secondary GPUs
  * backends/drm: disable direct scanout on secondary GPUs
  * plugins/translucency: Fix unsetting animations for minimized windows (kde#504687)
  * Implement proper virtual desktop reordering (kde#504848)
  * scene/surfaceitem_wayland: handle some missing initial properties
  * scripting/scriptedeffect: Fix effect loading due to shadowed file path (kde#505242)
  * scene: Signal presentation feedbacks on blank commits too
  * wayland: Send wl_data_source.cancelled if wl_data_device.start_drag is rejected
  * Make horizontal panels take precedence in reserved space
  * autotests/integration/outputchanges: wait for frame callbacks before committing
  * scene/item: restrict frame callbacks based on the output rather than geometry (kde#479694,kde#498628,kde#505060)
  * compositor: take min vrr refresh rate into account for cursor updates
  * backends/drm: reduce severity of pageflip failure logging (kde#505028)
  * Use desktop id to restore keyboard layout
  * wayland: Fix focused surface check in wl_data_device.start_drag (kde#497031)
* Thu May 29 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.3.91:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.3.91
- Too many changes to list here
* Mon May 19 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.3.90:
  * New feature release
  * For more details see https://kde.org/announcements/plasma/6/6.3.90
- Too many changes to list here
* Tue May  6 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.3.5:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.3.5
- Too many changes to list here
- Drop patches, now upstream:
  * 0001-xwayland-Only-pass-actual-mime-type-offers-to-Waylan.patch
  * 0001-backends-drm-also-clean-up-pending-commits-with-lega.patch
* Fri Apr 11 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Add upstream fixes:
  * 0001-xwayland-Only-pass-actual-mime-type-offers-to-Waylan.patch
  * 0001-backends-drm-also-clean-up-pending-commits-with-lega.patch
* Wed Apr  2 2025 Christophe Marin <christophe@krop.fr>
- Update to 6.3.4
  * New bugfix release
  * For more details please see:
  * https://kde.org/announcements/plasma/6/6.3.4
- Too many changes since 6.3.3, only listing bugfixes:
  * wayland: Clip surface damage (kde#501113)
  * Combine tile modes when tiling via arrow keys (kde#501731)
  * plugins/systembell: Throttle audio bell (kde#500916)
  * compositor: only delay hardware cursor updates when necessary (kde#487563)
  * kcms/rules: Remove pragma on OptionsComboBox (kde#501357)
- Drop patches:
  * 0001-Version-6.3.3.patch
  * 0002-kcms-rules-Remove-pragma-on-OptionsComboBox.patch
* Tue Mar 11 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.3.3:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.3.3
- Changes since 6.3.2:
  * backends/drm: properly reset buffer age when switching swapchains
  * update version for new release
  * plugins/keynotification: Fix notification for unlatching Meta
  * xkb: Fix reporting state for multiple modifiers (kde#501159)
  * autotests: add test for Workspace::lowerWindow
  * layers: fix stacking issues in Workspace::lowerWindow (kde#478382,kde#478383)
  * plugins/touchpadshortcuts: Add touchpad toggle shortcut with meta keys
  * scene/workspacescene: don't check opaque region with QRegtion::contains
  * window: reimplement restriction in moveResize (kde#401271,kde#481610,kde#493797)
  * backends/drm: include header for std::this_thread::sleep_until
  * utils/edid: Report monitor name without serial number (kde#500471)
  * x11: Update XStacking order when adding override-redirect windows (kde#483163)
  * plugins/blur: clear all textures after allocating them (kde#499935)
  * kcms/rules: Fix keyboard usability for comboboxes with multiple selection (kde#488703)
  * backends/drm: also don't use DEGAMMA_LUT on Intel (kde#500837)
  * workspace: watch kdeglobals and update Xwayland scale accordingly (kde#499923)
  * backends/drm: fix testing for more connectors than CRTCs (kde#500819)
  * backends/drm: allow overriding the safety margin
  * backends/drm: Print connector name in QDebug output
  * backends/drm: Log connector<->CRTC matching steps
  * window: Compare currentTile to requestedTile (kde#500666)
  * backends/drm: add an environment variable to override the dpms timeout
  * plugins/buttonrebinds: Create input device on demand
  * Revert "workspace: better deal with having more outputs than the GPU can drive"
  * kcms/rules: Fix showing selected VD on X11 (kde#484165)
  * autotests: Fix testInputCapture with libei 1.4.0
- Drop patches, now upstream:
  * 0001-backends-drm-Log-connector-CRTC-matching-steps.patch
  * 0002-backends-drm-fix-testing-for-more-connectors-than-CR.patch
- Add patch to fix the project version:
  * 0001-Version-6.3.3.patch
- Add patch to fix KCM comboboxes:
  * 0002-kcms-rules-Remove-pragma-on-OptionsComboBox.patch
* Thu Mar  6 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Add patches to fix crashes with multiple monitors (kde#500819, kde#500797)
  * 0001-backends-drm-Log-connector-CRTC-matching-steps.patch
  * 0002-backends-drm-fix-testing-for-more-connectors-than-CR.patch
* Wed Feb 26 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.3.2.1:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.3.2.1
- Changes since 6.3.2:
  * Revert "workspace: better deal with having more outputs than the GPU can drive"
  * kcms/rules: Fix showing selected VD on X11 (kde#484165)
  * autotests: Fix testInputCapture with libei 1.4.0
* Tue Feb 25 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.3.2:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.3.2
- Changes since 6.3.1:
  * workspace: don't set brightness to the display value on every startup (kde#494408)
  * workspace: better deal with having more outputs than the GPU can drive
  * backends/drm: reject output configurations that can't be powered at all (kde#500031)
  * update version for new release
  * Workaround hard freeze during interactive move
  * input: remove check for touch sequence (kde#500557)
  * Fix build compat with Qt 6.7
  * workspace: use frameGeometry for findWindowToActivate (kde#500529)
  * core/renderloop: use PreciseTimer for render loop.
  * killer: take abort result into consideration
  * backends/drm: log when link training is necessary
  * core/renderloop: take vrr into account for output layer repaints (kde#499848)
  * backends/libinput: confine TabletToolEvent to output (kde#480658)
  * Prevent virtual input devices from blocking tablet mode (kde#500025)
  * backends/drm: use a shadow buffer with "prefer color accuracy" if night light is enabled (kde#500404)
  * autotests/test_colorspaces: add some real-world validity check test cases
  * core/colorspace: relax validity check (kde#500295)
  * backends/drm: reimplement software brightness for ICC profiles (kde#500210)
  * Factor out {previousRestricted,restricted}MoveArea calls out of loops (kde#500310)
  * Implement KDecoration3::DecoratedWindow::applicationMenu{ServiceName,ObjectPath}
  * wayland: make the fallback for broken HDR metadata less strict (kde#500144)
  * core/colorspace: improve formatting of logging functions
  * wayland: switch to the upstream color management protocol
  * Round native geometry in InternalWindow
  * Fix overlooked frameRectToClientRect() in InternalWindow
  * update version for new release
* Tue Feb 18 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.3.1:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.3.1
- Too many changes to list here
- Drop patch, now upstream:
  * 0001-core-outputlayer-guard-against-null-m_output.patch
* Mon Feb 10 2025 Fusion Future <qydwhotmail@gmail.com>
- Add patch to fix crash on login on X11
  * 0001-core-outputlayer-guard-against-null-m_output.patch
* Thu Feb  6 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.3.0:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.3.0
- Too many changes to list here
* Thu Jan 23 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.2.91:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.2.91
- Too many changes to list here
* Sat Jan 11 2025 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.2.90:
  * New feature release
  * For more details see https://kde.org/announcements/plasma/6/6.2.90
- Too many changes to list here
* Tue Dec 31 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.2.5:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.2.5
- Changes since 6.2.4:
  * update version for new release
  * plugins/krunnner-integration: don't trust inputs from the dbus call
  * CMake: do not expand variables beforehand
  * plugins/krunner-integration: Fix crash
  * plugins/screencast: take scaling into account for window sources (kde#497571)
  * opengl: Fix cached size check in GLTexture::render()
  * plugins/shakecursor: don't trigger for warp events
  * backends/drm: fix the incorrect use of std::optional
  * Do not call ScreenLocker::KSldApp::unlocked when it unlocked in the meantime
  * backends/x11: Fix a crash in KWin::X11WindowedEglPrimaryLayer::present()
  * autotests/integration: add a color management test
  * wayland/xx color management: fix max > lum luminance checks
  * wayland: Fix XdgToplevelWindow::moveResizeInternal() committing geometry with fractional client size
  * wayland: Fix sending wl_pointer.leave event to Xwayland during dnd
  * opengl/eglnativefence: fix file descriptor leak
  * effects/overview: Animate if the thumbnail is dropped in an heap (kde#496646)
  * update version for new release
* Wed Nov 27 2024 Christophe Marin <christophe@krop.fr>
- Fix the pipewire BuildRequires condition for Leap 15.6
* Tue Nov 26 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.2.4:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.2.4
- Changes since 6.2.3:
  * update version for new release
  * Cancel interactive move resize only on Wayland
  * backends/drm: reject cursor updates already in beginFrame
  * compositor_wayland: don't commit cursor changes if the layer wasn't actually enabled (kde#495843)
  * backends/drm: don't set the dpms mode to AboutToTurnOff if the screen is already off
  * layers: add null check
  * outputconfigurationstore: fix choosing the default mode
  * plugins/screencast, screenshot: switch color transforms to relative colorimetric (kde#496185)
  * effects/overview: Properly map the windowHeap geometry
  * effects/overview: Don't make thumbnails fly off the screen (kde#495444)
  * core: Set object ownership for Output
  * backends/drm: re-allow HDR on NVidia with driver version 565.57.01+
  * backends/drm: re-allow HDR on Intel by default
  * Revert "scene: Ignore xwayland window shape" (kde#493934)
  * tiling: fix some asserts from scripts
  * utils: Use QList::removeLast() in DamageJournal::add()
  * Ensure active window isn't focused when screen is locked (kde#495325)
  * Cancel interactive move resize when outputs change
  * backends/drm: fix DrmGpu::needsModeset check with leased outputs (kde#495400)
  * effect/offscreenquickview: ensure the view that accepts touch down also gets touch up
  * workspace: fix the dpms input event filter sometimes being wrongly deleted
  * Close layer shell window if its preferred output has been removed
  * activation: don't activate windows that don't accept keyboard input (kde#495537)
  * tabbox: Do not add windows that have modal children
  * core/colorspace: fix the max luminance of linear (kde#494930)
  * update version for new release
* Tue Nov  5 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.2.3:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.2.3
- Changes since 6.2.2:
  * update version for new release
  * input: don't crash if the internal handle is nullptr (wheelEvent)
  * backends/x11: fix colormap leak
  * Update ExpoCell contentItem position upon its parent change (kde#495501)
  * scene: Fix item restacking repaints
  * xwayland: Fix a couple of file descriptor leaks (kde#442846)
  * plugins/keynotification: Fix event ID for notification (kde#495264)
  * backends/drm: don't set backlight brightness to 1 in HDR mode (kde#495242)
  * core/colorspace: ensure that we don't create elevated blacks with black point compensation (kde#494854)
  * autotests: test that ColorPipeline and OpenGL shader results at least somewhat match
  * core/colorpipeline: do ICtCp conversion the correct way around
  * core/colorpipeline: use PQ with min. luminance zero for tone mapping
  * core/colorpipeline: fix multiplier+matrix optimization
  * core/colorpipeline: don't transpose the ICtCp matrix
  * core/colorpipeline: fix tone mapping luminances being switched around
  * backends/drm: check if m_commits is empty after waiting for commitPending
  * use xcb_connection_has_error to check for failue
  * Fix "window to next desktop" shortcut during interactive move/resize session
  * backends/drm: add an environment variable to force glFinish on multi gpu copies
  * backends/drm: disable software brightness if there was ever a hardware brightness device assigned
* Tue Oct 22 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.2.2:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.2.2
- Changes since 6.2.1.1:
  * update version for new release
  * backends/drm: leave all outputs disabled by default, including VR headsets (kde#493148)
  * cmake: fix build with KWIN_BUILD_X11_BACKEND
  * cmake: don't try to build kwin_x11 when KWIN_BUILD_X11_BACKEND is turned off
  * ci: Switch to Qt 6.8
  * Initialize KCrash for kwin_x11 too
  * backends/drm: don't allow tearing until the cursor plane is disabled (kde#493166)
  * core: make sure we don't call a null buffer
  * Revert "temporarily revert version number for respin"
  * effect: Make opengl context current in OffscreenEffect::unredirect() and CrossFadeEffect::unredirect()
  * backends/drm: check for the output being active before setting legacy gamma
  * Avoid creating Unmanaged for reparented window
* Thu Oct 17 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.2.1.1:
  * New bugfix release
- Changes since 6.2.1:
  * backends/drm: don't skip colorops when matching the pipeline (kde#494611)
  * backends/drm: transform damage to match the framebuffer (kde#494837)
  * Set WAYLAND_DISPLAY before starting wayland server
  * scene/itemrenderer_opengl: use the color pipeline to check if color transformations are needed (kde#493295)
  * temporarily revert version number for respin
  * backends/drm: don't scale infiniteRegion()
  * backends/drm: fix crash with multi gpu
  * ci: Require tests to pass only on Linux
  * Report correct input timestamps for popup keyboard events
  * backends/drm: disable hdr if we removed the capabilities for it (kde#494706)
  * wayland/color management: ignore obviously wrong HDR metadata (kde#494502)
  * update version for new release
* Tue Oct 15 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.2.1:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.2.1
- Too many changes to list here
* Sat Oct  5 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.2.0:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.2.0
- Too many changes to list here
* Tue Sep 17 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.1.90:
  * New feature release
  * For more details see https://kde.org/announcements/plasma/6/6.1.90
- Too many changes to list here
* Tue Sep 10 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.1.5:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.1.5
- Changes since 6.1.4:
  * update version for new release
  * Don't process pad button events from a device that has been removed
  * workspace: don't rearrange immediately when a window with struts gets removed
  * input.cpp: initialize m_touchpadsEnabled in addInputDevice (kde#486763)
  * scene: Add an assert to debug crash in BlurEffect::prePaintWindow()
  * plugins/synchronizeskipswitcher: Fix Window::skipTaskbarChanged handler (kde#465600)
  * Fix null dereference in Workspace::workspaceEvent()
  * window: make setQuickTileMode more sane
  * effect: Refuse starting quick effect if keyboard cannot be grabbed
  * decorations: Show tooltip at current cursor position (kde#491143)
  * opengl/gltexture: Fix format for 565 textures
  * Fix a crash in computeLayer() (kde#491618)
  * Make Workspace::removeUnmanaged() keep the window in the stack
  * colorblindesscorrection: fix incorrect variable name in shader program
  * opengl: Fix a typo in GLTexture::upload()
  * backends/drm: allow triple buffering on NVidia if KWIN_DRM_DISABLE_TRIPLE_BUFFERING=0 is set
  * wayland: Fix a potential null dereference when sending current output device mode
  * platformsupport/scene/opengl: do test imports for external_only formats properly
  * opengl/egldisplay: add the invalid modifier to the correct list
  * scene: Fix SurfaceItemWayland::freeze()
  * placeholderinputeventfilter: don't block media keys (kde#491531)
  * plugins/trackmouse: listen to mouse events when active (kde#487820)
  * screenedge: allow activating clients in drag and drop (kde#450579)
  * update version for new release
* Tue Aug  6 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.1.4:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.1.4
- Changes since 6.1.3:
  * update version for new release
  * activation: fix X11 windows being stuck in should_get_focus more properly
  * plugins/buttonrebinds: correctly handle level 1 keys (kde#484367)
  * backends/drm: don't block direct scanout if color profile source isn't set to ICC
  * Fix checking whether GraphicsBufferView is null
  * backends/drm: don't apply the brightness factor without HDR
  * activation: don't add the active window to should_get_focus list (kde#484155)
  * core/renderloop: don't move the target presentation timestamp back when rescheduling (kde#488843)
  * core/renderloop: fix triple buffering hysteresis
  * scene/itemrenderer_opengl: reset OpenGL state for YUV conversion back to RGB
  * autotests: test placement to always put the titlebar on the screen
  * placement: keep the titlebar in the screen with centered placement (kde#489500)
  * placement: don't overwrite scheduled position change in cascadeIfCovering
  * Make Workspace::desktopResized() reassign outputs of uninitialized windows
  * wayland: Avoid klipper loop with existing but empty clipboards (kde#469644)
  * backends/drm: Fix a crash in DrmGpu::releaseBuffers()
  * wayland: Ignore plasma shell reposition requests during interactive move resize (kde#481829)
  * backends/drm: limit max_bpc to 8 by default with docks
  * compositor_wayland: count rendering time for all steps of compositing
  * xdgshellwindow: never request clients to resize to a negative size (kde#489983)
  * backends/libinput: Ignore redundant events for pointer buttons and keyboard keys when pressed/released on multiple devices (kde#486034)
  * backends/x11: Fix crash that happens when toggling compositing
  * plugins/stickykeys: Unlatch modifiers when locking
  * Fix sticky keys for AltGr
  * Test locking sticky keys for all modifiers
  * Release key in sticky key test
  * utils: Fix gaining realtime scheduling with musl (kde#487996)
  * core/renderloop: add some hysteresis to triple buffering
* Tue Jul 16 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.1.3:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.1.3
- Changes since 6.1.2:
  * update version for new release
  * plugins/nightlight: Relax custom times constraints (kde#489366)
  * wayland: Simplify XdgPopupWindow::sendRoleConfigure()
  * wayland: Dismiss XdgPopupWindow when the parent window is closed (kde#472013)
  * tiling: Don't put maximized windows in tile (kde#489463)
  * Input method window should not break showing desktop (kde#489057)
  * plugins/fadingpopups: don't block direct scanout (kde#487780)
  * backends/drm: test and apply all mode changes at once
  * autotests/drm: add test for vrr capability changing without a hotunplug
  * backends/drm: update output properties after they're created too (kde#486149)
  * use separation dep_version to build against, updated by release scripts
  * plugins/screencast: Don't download texture data if target size and texture size mismatch
  * plugins/screencast: Allocate offscreen texture in WindowScreenCastSource::render(QImage) as big as the memfd buffer (kde#489764)
  * autotests: Skip testScreencasting in CI
  * Foward modifiers after disabling sticky keys
  * plugins/screenshot: Port blitScreenshot() to glReadnPixels()
  * wayland: add error handling for QFile::open failure in org_kde_plasma_window_get_icon
  * placement: ignore the active output with place under mouse (kde#488110)
  * opengl: Add OpenGlContext::glGetnTexImage()
  * plugins/screencast: Prefer glReadnPixels() and glGetnTexImage()
  * WindowHeapDelegate: label topMargin to small, remove height padding (kde#489595)
  * plugins/glide: drop references to closed windows if they're not animated
  * update version for new release
  * plugins/screencast: Handle frame rate throttling timer firing a bit earlier
  * backends/drm: disable triple buffering on NVidia (kde#487833)
* Tue Jul  2 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.1.2:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.1.2
- Changes since 6.1.1.2:
  * Don't assert on null output
  * quicktiling: Reset layout when last quicktile ceases to exist (kde#465937)
  * wayland: Bump default max buffer size to 1 MiB
  * plugins/qpa: set deprecated functions option correctly
  * plugins/kdecoration: Fix MenuButton not accepting button press events (kde#488993)
  * plugins/colorcorrection: simplify the effect, merge the shader files and support color management
  * opengl: Reset OpenGlContext::currentContext() if it's destroyed (kde#488830)
  * window: adhere to window rules in checkWorkspacePosition (kde#489117)
  * plugins/hidecursor: show the cursor on tablet events (kde#489009)
* Thu Jun 27 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.1.1.2:
  * New bugfix release
- Changes since 6.1.1:
  * 3rdparty: Reformat xcursor.{h,c}
  * utils: Load Xcursor themes using QFile (kde#489241)
  * 3rdparty: Drop xcursor write hook
  * plugins/hidecursor: Set minimum to allow disabling hiding cursor on inactivity
  * WindowHeapDelegate: Label text background (kde#483016)
  * plugins/backgroundcontrast,blur: correct support checks
  * opengl/glframebuffer: handle missing support for blits on Wayland (kde#484193)
  * opengl: glBufferStorage is not supported on GL ES by default
  * core/renderloop: assume high render times if the last frame has been a while ago
* Tue Jun 25 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.1.1:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.1.1
- Too many changes to list here
* Thu Jun 13 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.1.0:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.1.0
- Too many changes to list here
* Sat May 25 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.0.90.1:
  * New feature release
  * For more details see https://kde.org/announcements/plasma/6/6.0.90
- Too many changes to list here
* Wed May 22 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.0.5:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.0.5
- Too many changes to list here
* Mon Apr 22 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.0.4.1:
  * New bugfix release
- Changes since 6.0.4:
  * Fall back to breeze_cursors if neither configured nor default can be loaded
  * scene/workspacescene: don't check direct scanout candidates for a pixmap
    (kde#485639, kde#485730, kde#485712)
* Wed Apr 17 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.0.4:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.0.4
- Too many changes to list here
* Wed Mar 27 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.0.3.1:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.0.3.1
- Changes since 6.0.3:
  * plugins/screencast: Handle failing to import dmabuf
  * plugins/screencast: Simplify damage calculation in region screen cast source
  * plugins/screencast: Drop "stream" in ScreenCastStream::streamReady
  * plugins/screencast: Rename ScreenCastStream::stop() to close()
  * plugins/screencast: Pause/resume source when stream is paused/resumed
  * Fix oversights on shortcut handling within Overview/Grid effect (kde#482931)
  * tiles: Evacuate windows in CustomTile::remove()
  * tiles: Use deleteLater() in CustomTile::remove()
* Tue Mar 26 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.0.3:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.0.3
- Too many changes to list here
* Wed Mar 13 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.0.2:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.0.2
- Changes since 6.0.1:
  * plugins/screencast: fix the cursor being offset after changing the scale
  * xkb: fix testing if on keypad
  * wayland: Only send artificial mouse up events for xwayland drags
  * wayland: Only partially revert send pointer leave on drag
  * Properly intersect the shape with clipRect
  * core/colorspace: fix ColorDescription comparisons (kde#482809)
  * utils/xcbutils: Don't call toXNative with unsigned integer (kde#482687)
  * backends/drm: handle dumb buffer target correctly (kde#482859)
  * Port IdleDetector to QBasicTimer
  * Add timeout assert in IdleDetector
  * xdgshellwindow: Always update window position and size along all axes when fully miximizing window (kde#482086)
  * Fix sending window to all desktops (kde#482670)
  * backends/drm: also set legacy gamma after VT switches
  * backends/drm: don't set gamma with legacy unless really necessary
  * backends/drm: ignore ctm support on legacy (kde#482143)
  * Rename Workspace::updateClientArea as Workspace::rearrange
  * wayland: Fix windows shrinking when output layout changes
  * x11window: Skip strict geometry checks in isFullScreenable()
  * xwayland: Use correct key for key release events
  * xwayland: Send to xwayland even when no window is focussed (kde#478705)
  * update version for new release
* Wed Mar  6 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.0.1:
  * New bugfix release
  * For more details see https://kde.org/announcements/plasma/6/6.0.1
- Too many changes to list here
- Drop patches, now upstream:
  * intel-compositor-freeze.patch
* Mon Mar  4 2024 Christophe Marin <christophe@krop.fr>
- Add Provides/Obsoletes to replace Plasma 5
* Thu Feb 29 2024 Bruno Pitrus <brunopitrus@hotmail.com>
- Add backported intel-compositor-freeze.patch
  * fixes kde#481721
* Wed Feb 21 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 6.0.0:
  * New bugfix release
  * Release announcement not available yet
- Too many changes to list here
* Wed Jan 31 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 5.93.0 (6.0 RC 2):
  * New bugfix release
  * See https://kde.org/announcements/megarelease/6/rc2/ for details
- Too many changes to list here
* Mon Jan 15 2024 Fabian Vogt <fabian@ritter-vogt.de>
- Update to 5.92.0 (6.0 RC 1)
  * For more details please see:
    https://kde.org/announcements/megarelease/6/rc1/
* Thu Dec 28 2023 Neal Gompa <ngompa@opensuse.org>
- Split X11 window manager into a subpackage
* Sat Jul  1 2023 Christophe Marin <christophe@krop.fr>
- Init kwin6
