#!/bin/env python
# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: Generic per-directory persistent file-parameter helpers and CS commands.

Config root: =<cwd>/.<csxu-name>/fps/<parName>/value=
where =<csxu-name>= is the basename of =sys.argv[0]= and =<cwd>= is the
current working directory at invocation time.

Companion to =bisos.b.userConfig_csu= (which stores under =~/.config/bisos/=).
Where =userConfig_csu= provides machine-wide defaults, =cwdConfig_csu= provides
per-directory overrides. The two are independent — a caller decides precedence
policy by asking one or the other (or both) in the desired order.

Any PyCS param declared with =parPermanence="userConfig"= is discoverable here
the same way as in =userConfig_csu=. Add =bisos.b.cwdConfig_csu= to a csxu's
=csuList= to expose =cwdConfig_get= / =cwdConfig_set= commands.
#+end_org """

import collections
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
    return str(pathlib.Path.cwd().resolve() / f'.{csxuName}' / 'fps')


# ---------------------------------------------------------------------------
# Discover params tagged parPermanence="userConfig" from __main__ and csuList
# ---------------------------------------------------------------------------

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


def cwdConfigParamsGet() -> typing.Dict[str, cs.param.CmndParam]:
    """Return all params whose parPermanence list contains 'cwdConfig'.

    parPermanence is a list of persistence tags (Python literal), e.g.
    ["userConfig"], ["cwdConfig"], or ["userConfig", "cwdConfig"] for
    params managed by both stores. Missing / None / empty is treated as
    an empty list (param is not persistent).
    """
    result = {}
    for name, param in _allCsParams().items():
        perm = getattr(param, 'parPermanence', None) or []
        if "cwdConfig" in perm:
            result[name] = param
    return result


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
# commonParamsSpecify — no params of its own; reuses parName / parValue from
# userConfig_csu when that CSU is also in csuList. If cwdConfig_csu is used
# without userConfig_csu, the main csxu is responsible for declaring
# parName / parValue.
# ---------------------------------------------------------------------------

def commonParamsSpecify(csParams: cs.param.CmndParamDict) -> None:
    pass


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

        persistentParams = cwdConfigParamsGet()

        cs.examples.menuChapter('=cwdConfig_get= -- show per-directory value of a persistent parameter')
        for parName, param in persistentParams.items():
            currentVal = parGet(parName)
            comment = f"# current: {currentVal}" if currentVal else "# (not set)"
            cmnd('cwdConfig_get',
                 pars=od([('parName', parName)]),
                 comment=comment)

        cs.examples.menuChapter('=cwdConfig_set= -- set a per-directory persistent parameter')
        for parName, param in persistentParams.items():
            cmnd('cwdConfig_set',
                 pars=od([('parName', parName), ('parValue', f'<{parName}-value>')]),
                 comment=f"# {param.parDescriptionGet()}  (writes ./.<csxu-name>/fps/{parName}/value)")

        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)


# ---------------------------------------------------------------------------
# cwdConfig_get
# ---------------------------------------------------------------------------

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "cwdConfig_get" :comment "Show per-directory value of a persistent parameter" :extent "verify" :ro "cli" :parsMand "parName" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<cwdConfig_get>>  =verify= parsMand=parName ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class cwdConfig_get(cs.Cmnd):
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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Show per-directory value of a persistent parameter.
Config root: =<cwd>/.<csxu-name>/fps/=
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
# cwdConfig_set
# ---------------------------------------------------------------------------

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "cwdConfig_set" :comment "Set a per-directory persistent parameter" :extent "verify" :ro "cli" :parsMand "parName parValue" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<cwdConfig_set>>  =verify= parsMand="parName parValue" ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class cwdConfig_set(cs.Cmnd):
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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Set a per-directory persistent parameter.
Writes value to =<cwd>/.<csxu-name>/fps/<parName>/value=.
        #+end_org """)

        parSet(parName, parValue)
        b_io.ann.note(f"{parName} set to: {parValue}  [config root: {_configRoot()}]")

        return cmndOutcome.set(
            opError=b.op.OpError.Success,
            opResults=f"{parName}={parValue}",
        )
