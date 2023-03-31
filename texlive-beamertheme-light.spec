Name:		texlive-beamertheme-light
Version:	49867
Release:	2
Summary:	A minimal beamer style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamertheme-light
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-light.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-light.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The LaTeX package beamertheme-light provides an aesthetic and
minimal beamer style by redefining colors and fonts.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/beamertheme-light
%doc %{_texmfdistdir}/doc/latex/beamertheme-light

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
