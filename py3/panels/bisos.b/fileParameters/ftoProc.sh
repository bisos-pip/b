#!/bin/bash

####+BEGIN: bx:bsip:bash:seed-spec :types "seedFtoCommon.sh"
SEED="
*  /[dblock]/ /Seed/ :: [[file:/bisos/core/bsip/bin/seedFtoCommon.sh]] |
"
FILE="
*  /This File/ :: /bisos/git/auth/bxRepos/bisos-pip/b/py3/panels/bisos.b/fileParameters/ftoProc.sh
"
if [ "${loadFiles}" == "" ] ; then
    /bisos/core/bsip/bin/seedFtoCommon.sh -l $0 "$@"
    exit $?
fi
####+END:

seedExamplesType="pypi"

leavesExcludes=""

leavesOrdered=""

nodesExcludes=""

nodesOrdered=""

####+BEGIN: bx:dblock:pypi:bash:leavesList :types ""
leavesList="
"
####+END:

####+BEGIN: bx:dblock:pypi:bash:nodesList :types ""
nodesList="
b.fpCls-BaseDir
b.fp-FilePram
_nodeBase_
"
####+END:

####+BEGIN: bx:dblock:bash:end-of-file :types ""
_CommentBegin_
*  [[elisp:(org-cycle)][| ]]  Common        ::  /[dblock] -- End-Of-File Controls/ [[elisp:(org-cycle)][| ]]
_CommentEnd_
#+STARTUP: showall
#local variables:
#major-mode: sh-mode
#fill-column: 90
# end:
####+END:
