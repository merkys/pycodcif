BUILD_LOG = build.log

all: ${BUILD_LOG}

${BUILD_LOG}:
	python2.7 setup.py build 2>&1 | tee $@

distclean cleanAll:
	rm -rf build/* ${BUILD_LOG}
	svn st --no-ignore cod-tools | xargs rm -f
