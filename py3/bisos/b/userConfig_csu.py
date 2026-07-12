#!/bin/env python
# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: Generic persistent user-config file-parameter helpers and CS commands.

Config root: =~/.config/bisos/<csxu-name>/<parName>/value=
where =<csxu-name>= is the basename of =sys.argv[0]=.

Any PyCS param declared with =parPermanence="userConfig"= is automatically managed here.
Add =bisos.b.userConfig_csu= to a csxu's =csuList= and tag params with
=parPermanence="userConfig"= to get persistent user-config for free.
#+end_org """

import collections
import os
import pathlib
import sys
import typing

from bisos import b
from bisos.b import cs
from bisos.b import b_io
from bisos.b import fp
from bisos.common import csParam


# ---------------------------------------------------------------------------
# Config root
# ---------------------------------------------------------------------------

def _configRoot() -> str:
    csxuName = pathlib.Path(sys.argv[0]).name
    return os.path.expanduser(f'~/.config/bisos/{csxuName}')


# ---------------------------------------------------------------------------
# Discover params tagged parPermanence="userConfig" from all loaded modules
# ---------------------------------------------------------------------------

def _userConfigParams() -> typing.Dict[str, cs.param.CmndParam]:
    result: typing.Dict[str, cs.param.CmndParam] = {}
    for modName, mod in sys.modules.items():
        csParamsDict = getattr(mod, '_csParamsDict', None)
        if csParamsDict is None:
            continue
        for parName, param in csParamsDict.items():
            if getattr(param, 'parPermanence', None) == 'userConfig':
                result[parName] = param
    return result


def _allCsParams() -> typing.Dict[str, cs.param.CmndParam]:
    """Collect all CmndParam objects from commonParamsSpecify of __main__ and csuList modules."""
    csParams = cs.param.CmndParamDict()
    mainMod = sys.modules.get('__main__')
    if mainMod and hasattr(mainMod, 'commonParamsSpecify'):
        mainMod.commonParamsSpecify(csParams)
    csuList = getattr(mainMod, 'csuList', [])
    for modName in csuList:
        mod = sys.modules.get(modName)
        if mod and hasattr(mod, 'commonParamsSpecify') and mod is not sys.modules[__name__]:
            mod.commonParamsSpecify(csParams)
    return csParams.parDictGet()


def userConfigParamsGet() -> typing.Dict[str, cs.param.CmndParam]:
    """Return all params from __main__ (and csuList) tagged parPermanence='userConfig'."""
    return {
        name: param
        for name, param in _allCsParams().items()
        if getattr(param, 'parPermanence', None) == 'userConfig'
    }


# ---------------------------------------------------------------------------
# Read / write helpers
# ---------------------------------------------------------------------------

def parGet(
        parName: str,
        override: typing.Optional[str] = None,
) -> typing.Optional[str]:
    if override:
        return override
    val = fp.FileParamValueReadFrom(parRoot=_configRoot(), parName=parName)
    return val.strip() if val else None


def parSet(
        parName: str,
        value: str,
) -> None:
    fp.FileParamWriteTo(parRoot=_configRoot(), parName=parName, parValue=value.strip())


# ---------------------------------------------------------------------------
# commonParamsSpecify — contributes parName / parValue to the main CLI
# ---------------------------------------------------------------------------

def commonParamsSpecify(csParams: cs.param.CmndParamDict) -> None:
    csParams.parDictAdd(
        parName='parName',
        parDescription="Name of the persistent user-config parameter.",
        parDataType=None,
        parDefault=None,
        parChoices=[],
        argparseShortOpt=None,
        argparseLongOpt='--parName',
    )
    csParams.parDictAdd(
        parName='parValue',
        parDescription="Value to set for the persistent user-config parameter.",
        parDataType=None,
        parDefault=None,
        parChoices=[],
        argparseShortOpt=None,
        argparseLongOpt='--parValue',
    )


# ---------------------------------------------------------------------------
# examples_csu
# ---------------------------------------------------------------------------

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples_csu" :extent "verify" :ro "noCli" :comment "CSU Examples" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv "pyKwArgs"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<examples_csu>>  =verify= ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class examples_csu(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo()

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             pyKwArgs: typing.Any=None,
    ) -> b.op.Outcome:
        """CSU Examples"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        od = collections.OrderedDict
        cmnd = cs.examples.cmndEnter

        persistentParams = userConfigParamsGet()

        cs.examples.menuChapter('=userConfig_get= -- show current value of a persistent parameter')
        for parName, param in persistentParams.items():
            currentVal = parGet(parName)
            comment = f"# current: {currentVal}" if currentVal else "# (not set)"
            cmnd('userConfig_get',
                 pars=od([('parName', parName)]),
                 comment=comment)

        cs.examples.menuChapter('=userConfig_set= -- set a persistent parameter')
        for parName, param in persistentParams.items():
            cmnd('userConfig_set',
                 pars=od([('parName', parName), ('parValue', f'<{parName}-value>')]),
                 comment=f"# {param.parDescriptionGet()}")

        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)


# ---------------------------------------------------------------------------
# userConfig_get
# ---------------------------------------------------------------------------

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "userConfig_get" :comment "Show current value of a persistent user-config parameter" :extent "verify" :ro "cli" :parsMand "parName" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<userConfig_get>>  =verify= parsMand=parName ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class userConfig_get(cs.Cmnd):
    cmndParamsMandatory = [ 'parName', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             parName: typing.Optional[str]=None,  # Cs Mandatory Param
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'parName': parName, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        parName = csParam.mappedValue('parName', parName)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Show current value of a persistent user-config parameter.
Config root: =~/.config/bisos/<csxu-name>/=
        #+end_org """)

        val = parGet(parName)
        if val is None:
            b_io.ann.note(f"{parName}: (not set)  [config root: {_configRoot()}]")
        else:
            b_io.ann.note(f"{parName}: {val}")

        return cmndOutcome.set(
            opError=b.op.OpError.Success,
            opResults=val,
        )


# ---------------------------------------------------------------------------
# userConfig_set
# ---------------------------------------------------------------------------

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "userConfig_set" :comment "Set a persistent user-config parameter" :extent "verify" :ro "cli" :parsMand "parName parValue" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<userConfig_set>>  =verify= parsMand="parName parValue" ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class userConfig_set(cs.Cmnd):
    cmndParamsMandatory = [ 'parName', 'parValue', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             parName: typing.Optional[str]=None,   # Cs Mandatory Param
             parValue: typing.Optional[str]=None,  # Cs Mandatory Param
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'parName': parName, 'parValue': parValue, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        parName = csParam.mappedValue('parName', parName)
        parValue = csParam.mappedValue('parValue', parValue)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Set a persistent user-config parameter.
Writes value to =~/.config/bisos/<csxu-name>/<parName>/value=.
        #+end_org """)

        parSet(parName, parValue)
        b_io.ann.note(f"{parName} set to: {parValue}  [config root: {_configRoot()}]")

        return cmndOutcome.set(
            opError=b.op.OpError.Success,
            opResults=f"{parName}={parValue}",
        )