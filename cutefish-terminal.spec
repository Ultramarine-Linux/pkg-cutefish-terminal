%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

%define component_name terminal
#%%define git_refspec ee490280c8499db8152307b2ae025d022dc462a5
#%%define git_refspec_short %%(echo %%{git_refspec} | cut -c -7)

Name: cutefish-%{component_name}
Version: 0.7
#Version: 0.0.0git.%%(date +%Y%m%d).%%{git_refspec_short}
Release: 1%{?dist}
License: GPLv3
Summary: A terminal emulator for Cutefish

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: qt5-qtbase-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel qt5-linguist
BuildRequires: fishui-devel
Requires: fishui

# the qmltermwidget has been patched by Cutefish team
Provides: bundled(qmltermwidget) = 0.2.0git.65e75bc+patched.e8b841f

Source0: https://github.com/cutefishos/%{component_name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Source0: https://github.com/cutefishos/%%{component_name}/tarball/%%{git_refspec}#/%%{component_name}-%%{git_refspec}.tar.gz
Patch0: 0001-change-terminal-dark-mode-text.patch

%description
A terminal emulator for Cutefish

%prep
%setup -qn %{component_name}-%{version}
#%%setup -qn cutefishos-%%{component_name}-%%{git_refspec_short}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_libdir}/qt5/qml/Cutefish/TermWidget
