# kwin-but-fuck-gestures
kwin6 for openSUSE Tumbleweed x86_64 with sane gestures + the ability to disable them
* based on: https://aur.archlinux.org/packages/kwin-without-gestures

-> setting KWIN_WAYLAND_NO_GESTURE environment variable disables the hardcoded touchpad gestures entirely

changes from Arch package:
1. only 4-finger swipes change between desktops
2. for 6.6.0, had to add two lines to the SPEC file around `gamecontroller.so` or the package build would fail. It is not presently clear to me why this is, because other than adding the 'Patch1' declaration to the SPEC file, there is no difference between the distribution provided SPEC and the one I was attempting to use, and that was also the only change I made to the previous SPEC file, which built without issue. I will probably not troubleshoot this, because it works, so I no longer care.
