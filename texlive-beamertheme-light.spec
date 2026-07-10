%global tl_name beamertheme-light
%global tl_revision 73158

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	A minimal beamer style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamertheme-light
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-light.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-light.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The LaTeX package beamertheme-light provides an aesthetic and minimal
beamer style by redefining colors and fonts.

