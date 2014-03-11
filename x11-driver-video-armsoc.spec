# Tarfile created using git
# git clone git://git.linaro.org/arm/xorg/driver/xf86-video-armsoc.git
# git archive --format=tar --prefix=%{name}-%{version}/ %{gittag} | bzip2 > ~/%{name}-%{version}-%{gittag}.tar.bz2

%define gittag I4f99e
%define upname xf86-video-armsoc
%define Werror_cflags %nil

Summary:   Xorg X11 armsocdrm driver
Name:      x11-driver-video-armsoc
Version:   0.6.0
Release:   0.1
URL:       http://git.linaro.org/gitweb?p=arm/xorg/driver/xf86-video-armsoc.git
License:   MIT
Group:     System/X11

Source0:   %{upname}.tar.bz2

ExclusiveArch: %{arm}

BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(x11)

Requires:	udev

%description 
X.Org X11 armsocdrm driver for ARM MALI GPUs such as the Samsung 
Exynos 4/5 series ARM devices.

%prep
%setup -qn %{upname}
sed -i s'/-Werror//g' src/Makefile.am

%build
sh autogen.sh --with-drmmode=exynos
%configure2_5x --with-drmmode=exynos
make V=1

%install
%makeinstall_std

%files
%doc README COPYING
%{_libdir}/xorg/modules/drivers/armsoc_drv.so
%{_mandir}/man4/armsoc.4*
