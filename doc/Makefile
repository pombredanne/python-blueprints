# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = build

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source

.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest gettext

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  pickle     to make pickle files"
	@echo "  json       to make JSON files"
	@echo "  htmlhelp   to make HTML files and a HTML help project"
	@echo "  qthelp     to make HTML files and a qthelp project"
	@echo "  devhelp    to make HTML files and a Devhelp project"
	@echo "  epub       to make an epub"
	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  text       to make text files"
	@echo "  man        to make manual pages"
	@echo "  gettext    to make PO message catalogs"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  doctest    to run all doctests embedded in the documentation (if enabled)"
	@echo "  msgmerge   to merge new pot files with $LANG po files"

clean:
	-rm -rf $(BUILDDIR)/*

html:
	make msgfmt
	$(SPHINXBUILD) -b html -D language=$(LANG) $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

dirhtml:
	make msgfmt
	$(SPHINXBUILD) -b dirhtml -D language=$(LANG) $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

singlehtml:
	make msgfmt
	$(SPHINXBUILD) -b singlehtml -D language=$(LANG) $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
	@echo
	@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml."

pickle:
	make msgfmt
	$(SPHINXBUILD) -b pickle -D language=$(LANG) $(ALLSPHINXOPTS) $(BUILDDIR)/pickle
	@echo
	@echo "Build finished; now you can process the pickle files."

json:
	make msgfmt
	$(SPHINXBUILD) -b json -D language=$(LANG) $(ALLSPHINXOPTS) $(BUILDDIR)/json
	@echo
	@echo "Build finished; now you can process the JSON files."

htmlhelp:
	make msgfmt
	$(SPHINXBUILD) -b htmlhelp -D language=$(LANG) $(ALLSPHINXOPTS) $(BUILDDIR)/htmlhelp
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in $(BUILDDIR)/htmlhelp."

qthelp:
	make msgfmt
	$(SPHINXBUILD) -b qthelp -D language=$(LANG) $(ALLSPHINXOPTS) $(BUILDDIR)/qthelp
	@echo
	@echo "Build finished; now you can run "qcollectiongenerator" with the" \
	      ".qhcp project file in $(BUILDDIR)/qthelp, like this:"
	@echo "# qcollectiongenerator $(BUILDDIR)/qthelp/django.qhcp"
	@echo "To view the help file:"
	@echo "# assistant -collectionFile $(BUILDDIR)/qthelp/django.qhc"

devhelp:
	make msgfmt
	$(SPHINXBUILD) -b devhelp -D language=$(LANG) $(ALLSPHINXOPTS) $(BUILDDIR)/devhelp
	@echo
	@echo "Build finished."
	@echo "To view the help file:"
	@echo "# mkdir -p $$HOME/.local/share/devhelp/django"
	@echo "# ln -s $(BUILDDIR)/devhelp $$HOME/.local/share/devhelp/django"
	@echo "# devhelp"

epub:
	make msgfmt
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub
	@echo
	@echo "Build finished. The epub file is in $(BUILDDIR)/epub."

latex:
	make msgfmt
	$(SPHINXBUILD) -b latex -D language=$(LANG) $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
	@echo "Run \`make' in that directory to run these through (pdf)latex" \
	      "(use \`make latexpdf' here to do that automatically)."

latexpdf:
	make msgfmt
	$(SPHINXBUILD) -b latex -D language=$(LANG) $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	make -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

text:
	make msgfmt
	$(SPHINXBUILD) -b text -D language=$(LANG) $(ALLSPHINXOPTS) $(BUILDDIR)/text
	@echo
	@echo "Build finished. The text files are in $(BUILDDIR)/text."

man:
	make msgfmt
	$(SPHINXBUILD) -b man -D language=$(LANG) $(ALLSPHINXOPTS) $(BUILDDIR)/man
	@echo
	@echo "Build finished. The manual pages are in $(BUILDDIR)/man."

gettext:
	$(SPHINXBUILD) -b gettext $(I18NSPHINXOPTS) $(BUILDDIR)/locale
	@echo
	@echo "Build finished. The message catalogs are in $(BUILDDIR)/locale."

changes:
	make msgfmt
	$(SPHINXBUILD) -b linkcheck -D language=$(LANG) $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

linkcheck:
	make msgfmt
	$(SPHINXBUILD) -b linkcheck -D language=$(LANG) $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

doctest:
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."

msgfmt:
	find locale/$$LANG/LC_MESSAGES/ -name "*.po" | sed 's,^[^/]*/[^/]*/[^/]*/,,' | awk '{ PO="\".po\""; system("BASENAME=`basename "$$0" "PO "` && DIRNAME=`dirname "$$0"` && msgfmt locale/$$LANG/LC_MESSAGES/$$DIRNAME/$$BASENAME.po -o locale/$$LANG/LC_MESSAGES/$$DIRNAME/$$BASENAME.mo")}'

msgmerge:
	find build/locale/ -name "*.pot" | sed 's,^[^/]*/[^/]*/,,' | awk '{ POT="\".pot\""; system("BASENAME=`basename "$$0" "POT "` && DIRNAME=`dirname "$$0"` && msgmerge -F locale/$$LANG/LC_MESSAGES/$$DIRNAME/$$BASENAME.po build/locale/$$DIRNAME/$$BASENAME.pot -o locale/$$LANG/LC_MESSAGES/$$DIRNAME/$$BASENAME.po")}'
