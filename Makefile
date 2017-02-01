BUILD_LOG = build.log
SDIST_LOG = sdist.log

CIF_PARSER_SRC = cod-tools/src/components/codcif/cif_grammar.tab.c

all: ${BUILD_LOG}

sdist: ${SDIST_LOG}

${BUILD_LOG}: ${CIF_PARSER_SRC}
	python2.7 setup.py build 2>&1 | tee $@

${SDIST_LOG}: ${CIF_PARSER_SRC}
	python2.7 setup.py sdist 2>&1 | tee $@

${CIF_PARSER_SRC}:
	$(MAKE) -C $(@D) $(@F)

distclean cleanAll:
	rm -rf build/* dist pycodcif.egg-info ${BUILD_LOG} ${SDIST_LOG}
	svn st --no-ignore cod-tools | xargs rm -f
