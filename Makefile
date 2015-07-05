USE_PKGBUILD=1
include /usr/local/share/luggage/luggage.make

TITLE=MSC-Do-Not-Disturb
PACKAGE_NAME=${TITLE}
PACKAGE_VERSION=2.0
REVERSE_DOMAIN=uk.ac.bris
APP_PATH=.
APP="Managed\ Software\ Center\ Do\ Not\ Disturb.app"
PREFLIGHT=msc-do-not-disturb.py
PAYLOAD=\
  pack-server \
  pack-script-postinstall

pack-server:
	@sudo /bin/mkdir -p ${WORK_D}/Library/Management/${TITLE}
	@sudo ${CP} -R "${APP_PATH}/${APP}" ${WORK_D}/Library/Management/${TITLE}/
	@sudo ${CP} "${APP_PATH}/${PREFLIGHT}" ${WORK_D}/Library/Management/${TITLE}/
	
