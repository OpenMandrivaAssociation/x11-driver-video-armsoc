# Tarfile created using git
# git clone https://anongit.freedesktop.org/git/xorg/driver/xf86-video-armsoc.git
# git archive --format=tar --prefix xf86-video-armsoc-1.4.1/ HEAD | xz -vf > ../xf86-video-armsoc-1.4.1.tar.xz

%define gittag 1.4.1
%define upname xf86-video-armsoc
%define Werror_cflags %nil

Summary:   Xorg X11 armsocdrm driver
Name:      x11-driver-video-armsoc
Version:   1.4.1
Release:   1
URL:       https://anongit.freedesktop.org/git/xorg/driver/xf86-video-armsoc.git
License:   MIT
Group:     System/X11

Source0:   %{upname}-%{version}.tar.xz

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(udev)

Requires:	udev

%description 
X.Org X11 armsocdrm driver for ARM MALI GPUs such as the Samsung 
Exynos 4/5 series ARM devices.

%prep
%setup -qn %{upname}-%{version}
sed -i s'/-Werror//g' src/Makefile.am

%build
sh autogen.sh
%configure
%make V=1

%install
%makeinstall_std

%files
%doc README COPYING
%{_libdir}/xorg/modules/drivers/armsoc_drv.so
%{_mandir}/man4/armsoc.4*
