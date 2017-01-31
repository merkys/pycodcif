BUILD_LOG = build.log
SDIST_LOG = sdist.log

all: ${BUILD_LOG}

sdist: ${SDIST_LOG}

${BUILD_LOG}:
	python2.7 setup.py build 2>&1 | tee $@

${SDIST_LOG}:
	python2.7 setup.py sdist 2>&1 | tee $@

distclean cleanAll:
	rm -rf build/* dist pycodcif.egg-info ${BUILD_LOG} ${SDIST_LOG}
	svn st --no-ignore cod-tools | xargs rm -f
