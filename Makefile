BUILD_LOG = build.log
SDIST_LOG = sdist.log

CIF_PARSER_SRC = cod-tools/src/components/codcif/cif_grammar.tab.c \
				 cod-tools/src/components/codcif/cif2_grammar.tab.c \
				 cod-tools/src/components/pycodcif/pycodcif_wrap.c

all: ${BUILD_LOG}

.PHONY: test tests check upload distclean cleanAll

sdist: ${SDIST_LOG}

${BUILD_LOG}: ${CIF_PARSER_SRC}
	python setup.py build 2>&1 | tee $@

${SDIST_LOG}: ${CIF_PARSER_SRC}
	python setup.py sdist 2>&1 | tee $@

${CIF_PARSER_SRC}:
	quilt top || quilt push -a --quiltrc .quiltrc
	$(MAKE) -C $(@D) $(@F)
	
test tests check:
	python setup.py test

upload: ${SDIST_LOG}
	python setup.py sdist upload -r pypi

distclean cleanAll:
	rm -rf build/* dist pycodcif.egg-info ${BUILD_LOG} ${SDIST_LOG}
	-quilt pop -a --quiltrc .quiltrc
	svn st --no-ignore cod-tools | xargs rm -f
