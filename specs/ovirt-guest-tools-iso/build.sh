#!/bin/sh

NAME="ovirt-guest-tools-iso"

SCRIPTDIR="$(dir="$(readlink -f "$(dirname "$0")")" && cd "${dir}" && pwd)"
SOURCESDIR="$(dir="$(readlink -f "$(dirname "$0")")" && cd "${dir}/../../sources/${NAME}" && pwd)"
rm -rf "${SCRIPTDIR}/noarch" "${SCRIPTDIR}"/*.rpm "${SCRIPTDIR}"/*.zip

spectool --all --get-files --directory "${SCRIPTDIR}" "${SCRIPTDIR}/${NAME}.spec"

rpmbuild \
	-bs \
	--define="_sourcedir ${SOURCESDIR}" \
	--define="_srcrpmdir ${SCRIPTDIR}" \
	--define="_rpmdir ${SCRIPTDIR}" \
	"${SCRIPTDIR}/${NAME}.spec"
