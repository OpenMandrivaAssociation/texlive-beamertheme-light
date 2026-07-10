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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The LaTeX package beamertheme-light provides an aesthetic and minimal
beamer style by redefining colors and fonts.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-light
%dir %{_datadir}/texmf-dist/tex/latex/beamertheme-light
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-light/README
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-light/beamertheme-light-example.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-light/beamertheme-light-example.tex
%{_datadir}/texmf-dist/tex/latex/beamertheme-light/beamertheme-light.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-light/beamerthemelight.sty
