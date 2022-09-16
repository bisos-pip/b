# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =PyLib+CsLib= for manipulation of File Parameters (FP). ~bisos.b.fp~
#+end_org """

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of Blee ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Libre-Halaal Foundation. Subject to AGPL.
** It is not part of Emacs. It is part of Blee.
** Best read and edited  with Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: NOTYET
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:python:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['fp'], }
csInfo['version'] = '202209125155'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'fp-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* /[[elisp:(org-cycle)][| Description |]]/ :: [[file:/bisos/panels/bisos-model/fileParameters/fullUsagePanel-en.org][File Parameters --- BISOS.B.FP Panel]]
See panel for details.
** Status: In use with blee3
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
#+end_org """
####+END:

####+BEGIN: b:python:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:cs:python:icmItem :itemType "=PyImports= " :itemTitle "*Py Library IMPORTS*"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

# __all__ = [
#     'FP_readTreeAtBaseDir',
# ]

import typing

from bisos import b
from bisos.b import cs
from bisos.b import io

from bisos.transit import pattern

import os
import collections
#import pathLib


import __main__


####+BEGIN: bx:cs:py3:section :title "*Class Based Interface*"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] **Class Based Interface**  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:


####+BEGIN: b:py3:class/decl :className "BaseDir" :superClass "b.fto.FILE_TreeObject" :comment "Expected to be subclassed" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /BaseDir/  superClass=b.fto.FILE_TreeObject =Expected to be subclassed=   [[elisp:(org-cycle)][| ]]
#+end_org """
class BaseDir(b.fto.FILE_TreeObject):
####+END:
    """ FP_Base is also a FILE_TreeObject.
    """

####+BEGIN: b:py3:cs:method/typing :methodName "__init__" :deco "default"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-     [[elisp:(outline-show-subtree+toggle)][||]] /__init__/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def __init__(
####+END:
            self,
            fileSysPath,
    ):
        """Representation of a FILE_TreeObject when _objectType_ is FileParamBase (a node)."""
        super().__init__(fileSysPath,)

####+BEGIN: b:py3:cs:method/typing :methodName "baseCreate" :deco ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-     [[elisp:(outline-show-subtree+toggle)][||]] /baseCreate/ deco=    [[elisp:(org-cycle)][| ]]
    #+end_org """
    def baseCreate(
####+END:
            self,
    ):
        """  """
        return self.nodeCreate()

####+BEGIN: b:py3:cs:method/typing :methodName "baseValidityPredicate" :deco "default"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-     [[elisp:(outline-show-subtree+toggle)][||]] /baseValidityPredicate/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def baseValidityPredicate(
####+END:
                self,
    ):
        """  """
        pass

####+BEGIN: b:py3:cs:method/typing :methodName "fps_asIcmParamsAdd" :deco "staticmethod"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-     [[elisp:(outline-show-subtree+toggle)][||]] /fps_asIcmParamsAdd/ deco=staticmethod  deco=staticmethod   [[elisp:(org-cycle)][| ]]
    #+end_org """
    @staticmethod
    def fps_asIcmParamsAdd(
####+END:
            icmParams,
    ):
        """staticmethod: takes in icmParms and augments it with fileParams. returns icmParams."""
        icmParams.parDictAdd(
            parName='exampleFp',
            parDescription="Name of Bpo of the live AALS Platform",
            parDataType=None,
            parDefault=None,
            parChoices=list(),
            parScope=icm.CmndParamScope.TargetParam,  # type: ignore
            argparseShortOpt=None,
            argparseLongOpt='--exampleFp',
        )

        return icmParams

####+BEGIN: b:py3:cs:method/typing :methodName "fps_namesWithRelPath" :deco "classmethod"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-     [[elisp:(outline-show-subtree+toggle)][||]] /fps_namesWithRelPath/ deco=classmethod  deco=classmethod   [[elisp:(org-cycle)][| ]]
    #+end_org """
    @classmethod
    def fps_namesWithRelPath(
####+END:
            cls,
    ):
        """classmethod: returns a dict with fp names as key and relBasePath as value.
        The names refer to icmParams.parDictAdd(parName) of fps_asIcmParamsAdd
        """
        relBasePath = "."
        return (
            {
                'exampleFP': relBasePath,
            }
        )

####+BEGIN: b:py3:cs:method/typing :methodName "fps_namesWithAbsPath" :deco "default"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-     [[elisp:(outline-show-subtree+toggle)][||]] /fps_namesWithAbsPath/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def fps_namesWithAbsPath(
####+END:
            self,
    ):
        """Uses fps_namesWithRelPath to construct absPath for relPath values. Returns a dict."""
        namesWithRelPath = self.__class__.fps_namesWithRelPath()
        namesWithAbsPath = dict()
        for eachName, eachRelPath in namesWithRelPath.items():
            namesWithAbsPath[eachName] = os.path.join(self.fileTreeBaseGet(), eachRelPath)
        return namesWithAbsPath

####+BEGIN: b:py3:cs:method/typing :methodName "fps_readTree" :deco "default"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-     [[elisp:(outline-show-subtree+toggle)][||]] /fps_readTree/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def fps_readTree(
####+END:
            self,
    ):
        """Returns a dict of FileParam s. Reads in all FPs at self.fps_absBasePath()."""
        cmndOutcome = b.op.Outcome()
        FP_readTreeAtBaseDir = b.fp.FP_readTreeAtBaseDir()
        FP_readTreeAtBaseDir.cmndOutcome = cmndOutcome

        FP_readTreeAtBaseDir.cmnd(
            interactive=False,
            FPsDir=self.fileTreeBaseGet(),
        )
        if cmndOutcome.error: return cmndOutcome

        self.fps_dictParams = cmndOutcome.results
        return cmndOutcome

####+BEGIN: b:py3:cs:method/typing :methodName "fps_setParam" :deco "default"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-     [[elisp:(outline-show-subtree+toggle)][||]] /fps_setParam/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def fps_setParam(
####+END:
            self,
            paramName,
            paramValue,
    ):
        """Returns a dict of FileParam s. Reads in all FPs at self.fps_absBasePath()."""
        namesWithAbsPath = self.fps_namesWithAbsPath()
        fpBase = namesWithAbsPath[paramName]
        b.fp.FileParamWriteTo(fpBase, paramName, paramValue)

####+BEGIN: b:py3:cs:method/typing :methodName "fps_getParam" :deco "default"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-     [[elisp:(outline-show-subtree+toggle)][||]] /fps_getParam/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def fps_getParam(
####+END:
            self,
            paramName,
    ):
        """Returns a dict of FileParam s. Reads in all FPs at self.fps_absBasePath()."""
        namesWithAbsPath = self.fps_namesWithAbsPath()
        #print(namesWithAbsPath)
        fpBase = os.path.abspath(namesWithAbsPath[paramName])
        #print(fpBase)
        paramValue = b.fp.FileParamReadFrom(fpBase, paramName,)
        return paramValue




####+BEGIN: bx:dblock:python:section :title "Common Parameters Specification"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common Parameters Specification*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:dblock:python:func :funcName "commonParamsSpecify" :funcType "ParSpec" :retType "" :deco "" :argsList "icmParams"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-ParSpec  [[elisp:(outline-show-subtree+toggle)][||]] /commonParamsSpecify/ retType= argsList=(icmParams)  [[elisp:(org-cycle)][| ]]
#+end_org """
def commonParamsSpecify(
    icmParams,
):
####+END:
    icmParams.parDictAdd(
        parName='fpBase',
        parDescription="File Parameters Directory Base Path.",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        #parScope=icm.ICM_ParamScope.TargetParam,  # type: ignore
        argparseShortOpt=None,
        argparseLongOpt='--fpBase',
    )



####+BEGIN: bx:cs:py3:section :title "CS-Lib Examples"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *CS-Lib Examples*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:


####+BEGIN: bx:dblock:python:func :funcName "examples_fpBase" :comment "Show/Verify/Update For relevant PBDs" :funcType "examples" :retType "none" :deco "" :argsList "fpBase cls menuLevel='chapter'"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-examples [[elisp:(outline-show-subtree+toggle)][||]] /examples_fpBase/ =Show/Verify/Update For relevant PBDs= retType=none argsList=(fpBase cls menuLevel='chapter')  [[elisp:(org-cycle)][| ]]
#+end_org """
def examples_fpBase(
    fpBase,
    cls,
    menuLevel='chapter',
):
####+END:
    """
** Common examples.
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    # def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)

    if menuLevel == 'chapter':
        cs.examples.menuChapter('*FileParams Access And Management*')
    else:
        cs.examples.menuChapter('*FileParams Access And Management*')

    cmndName = "fpParamsList" ; cmndArgs = "" ;
    cps=cpsInit() ; cps['fpBase'] = fpBase ; cps['cls'] = cls
    menuItem(verbosity='little')

    cmndArgs = "basic setExamples getExamples" ; menuItem(verbosity='little')

    cmndName = "fpParamsSetDefaults" ; cmndArgs = "" ;
    cps=cpsInit() ; cps['fpBase'] = fpBase ; cps['cls'] = cls
    menuItem(verbosity='little')

    cmndName = "fpParamsRead" ; cmndArgs = "" ;
    cps=cpsInit() ; cps['fpBase'] = fpBase ; cps['cls'] = cls
    menuItem(verbosity='little')

    cmndArgs = "basic setExamples getExamples" ; menuItem(verbosity='little')


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "CmndSvcs" :anchor ""  :extraInfo "File Parameters Get/Set -- Commands"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _CmndSvcs_: |]]  File Parameters Get/Set -- Commands  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "fpParamsList" :extent "verify" :parsMand "fpBase cls" :parsOpt "" :argsMin 0 :argsMax 3 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<fpParamsList>>parsMand=fpBase cls parsOpt= argsMin=0 argsMax=3 pyInv=
#+end_org """
class fpParamsList(cs.Cmnd):
    cmndParamsMandatory = [ 'fpBase', 'cls', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             fpBase: typing.Optional[str]=None,  # Cs Mandatory Param
             cls: typing.Optional[str]=None,  # Cs Mandatory Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        callParamsDict = {'fpBase': fpBase, 'cls': cls, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        # global fpBaseInst; fpBaseInst = typing.cast(getattr(__main__, cls), None)
        # exec(
        #     "fpBaseInst = __main__.{cls}('{fpBase}',)".format(cls=cls, fpBase=fpBase,),
        #     globals(),
        # )
        # fps_namesWithAbsPath = fpBaseInst.fps_namesWithAbsPath()

        #from bisos.examples import fp_csu

        fpBaseInst = b.pattern.sameInstance(getattr(__main__, cls), fpBase)
        #fpBaseInst = b.pattern.sameInstance(getattr(fp_csu, cls), fpBase)
        fps_namesWithAbsPath = fpBaseInst.fps_namesWithAbsPath()

        cmndArgsSpecDict = self.cmndArgsSpec()

        #if interactive:
        if True:
            formatTypes = self.cmndArgsGet("0&2", cmndArgsSpecDict, argsList)
        else:
            formatTypes = argsList

        if formatTypes:
            if formatTypes[0] == "all":
                    cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&2")
                    argChoices = cmndArgsSpec.argChoicesGet()
                    argChoices.pop(0)
                    formatTypes = argChoices

        for each in formatTypes:    # type: ignore
            if each == 'basic':
                FP_listIcmParams(fps_namesWithAbsPath,)
            elif each == 'getExamples':
                print("Get Examples Come Here")
            elif each == 'setExamples':
                print("Set Examples Come Here")
            else:
                io.eh.problem_usageError(f"Unknown {each}")

        return cmndOutcome

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&2",
            argName="formatTypes",
            argDefault="all",
            argChoices=['all', 'basic', 'setExamples', 'getExamples'],
            argDescription="Action to be specified by rest"
        )

        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "fpParamsSet" :parsMand "fpBase cls" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<fpParamsSet>>parsMand=fpBase cls parsOpt= argsMin=0 argsMax=0 pyInv=
#+end_org """
class fpParamsSet(cs.Cmnd):
    cmndParamsMandatory = [ 'fpBase', 'cls', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             fpBase: typing.Optional[str]=None,  # Cs Mandatory Param
             cls: typing.Optional[str]=None,  # Cs Mandatory Param
    ) -> b.op.Outcome:

####+END:

        #from bisos.examples import fp_csu

        fpBaseInst = pattern.sameInstance(getattr(__main__, cls), fpBase)
        #fpBaseInst = pattern.sameInstance(getattr(fp_csu, cls), fpBase)
        fps_namesWithAbsPath = fpBaseInst.fps_namesWithAbsPath()  # type: ignore

        FP_writeWithIcmParams(fps_namesWithAbsPath,)

        return cmndOutcome


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "fpParamSetWithNameValue" :parsMand "fpBase cls" :parsOpt "" :argsMin 2 :argsMax 2 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<fpParamSetWithNameValue>>parsMand=fpBase cls parsOpt= argsMin=2 argsMax=2 pyInv=
#+end_org """
class fpParamSetWithNameValue(cs.Cmnd):
    cmndParamsMandatory = [ 'fpBase', 'cls', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 2, 'Max': 2,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             fpBase: typing.Optional[str]=None,  # Cs Mandatory Param
             cls: typing.Optional[str]=None,  # Cs Mandatory Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

####+END:
        paramName = self.cmndArgsGet("0", cmndArgsSpecDict, effectiveArgsList)
        paramValue = self.cmndArgsGet("1", cmndArgsSpecDict, effectiveArgsList)

        print(f"{paramName} {paramValue}")

        fpBaseInst = pattern.sameInstance(getattr(__main__, cls), fpBase)

        fpBaseInst.fps_setParam(paramName, paramValue)

        return cmndOutcome


####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec():
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="paramName",
            argDefault="OopsName",
            argChoices=[],
            argDescription="Action to be specified by rest"
        )
        cmndArgsSpecDict.argsDictAdd(
            argPosition="1",
            argName="paramValue",
            argDefault="OopsValue",
            argChoices=[],
            argDescription="Action to be specified by rest"
        )

        return cmndArgsSpecDict

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "fpParamGetWithName" :parsMand "fpBase cls" :parsOpt "" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<fpParamGetWithName>>parsMand=fpBase cls parsOpt= argsMin=1 argsMax=1 pyInv=
#+end_org """
class fpParamGetWithName(cs.Cmnd):
    cmndParamsMandatory = [ 'fpBase', 'cls', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             fpBase: typing.Optional[str]=None,  # Cs Mandatory Param
             cls: typing.Optional[str]=None,  # Cs Mandatory Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

####+END:
        paramName = self.cmndArgsGet("0", cmndArgsSpecDict, effectiveArgsList)

        fpBaseInst = pattern.sameInstance(getattr(__main__, cls), fpBase)

        paramValue = fpBaseInst.fps_getParam(paramName,)

        print(f"{paramValue.parValueGet()}")

        return cmndOutcome


####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec():
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="paramName",
            argDefault="OopsName",
            argChoices=[],
            argDescription="Action to be specified by rest"
        )

        return cmndArgsSpecDict



####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "fpParamsSetDefaults" :parsMand "fpBase cls" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<fpParamsSetDefaults>>parsMand=fpBase cls parsOpt= argsMin=0 argsMax=0 pyInv=
#+end_org """
class fpParamsSetDefaults(cs.Cmnd):
    cmndParamsMandatory = [ 'fpBase', 'cls', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             fpBase: typing.Optional[str]=None,  # Cs Mandatory Param
             cls: typing.Optional[str]=None,  # Cs Mandatory Param
    ) -> b.op.Outcome:

####+END:
        fpBaseInst = pattern.sameInstance(getattr(__main__, cls), fpBase)
        fps_namesWithAbsPath = fpBaseInst.fps_namesWithAbsPath()  # type: ignore

        FP_writeDefaultsWithIcmParams(fps_namesWithAbsPath,)

        return cmndOutcome

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "fpParamsRead" :parsMand "fpBase cls" :parsOpt "" :argsMin 0 :argsMax 999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<fpParamsRead>>parsMand=fpBase cls parsOpt= argsMin=0 argsMax=999 pyInv=
#+end_org """
class fpParamsRead(cs.Cmnd):
    cmndParamsMandatory = [ 'fpBase', 'cls', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 999,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             fpBase: typing.Optional[str]=None,  # Cs Mandatory Param
             cls: typing.Optional[str]=None,  # Cs Mandatory Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

####+END:
        fpBaseInst = pattern.sameInstance(getattr(__main__, cls), fpBase)
        fpBaseDir = fpBaseInst.fileTreeBaseGet()  # type: ignore

        if interactive:
            formatTypes = self.cmndArgsGet("0&999", cmndArgsSpecDict, effectiveArgsList)
        else:
            formatTypes = effectiveArgsList

        for each in formatTypes:   # type: ignore
            if each == 'all':
                icm.LOG_here(f"""format={each} -- fpBaseDir={fpBaseDir}""")
                FP_readTreeAtBaseDir_CmndOutput(
                    interactive=interactive,
                    fpBaseDir=fpBaseDir,
                    cmndOutcome=cmndOutcome,
                )
            # elif each == 'obj':
            #     cmndOutcome= fpBaseDir.fps_readTree()
            #     if cmndOutcome.error: return cmndOutcome

            #     thisParamDict = fpBaseDir.fps_dictParams
            #     if interactive:
            #         icm.ANN_write(fpBaseDir.fps_absBasePath())
            #         icm.FILE_paramDictPrint(thisParamDict)

            else:
                icm.LOG_here(f"""format={each} -- fpBaseDir={fpBaseDir}""")

                # Read the wholething in:
                # FP_readTreeAtBaseDir_CmndOutput(
                #     interactive=False,
                #     fpBaseDir=fpBaseDir,
                #     cmndOutcome=cmndOutcome,
                # )
                #
                # print(cmndOutcome.results)
                #fpsDict = cmndOutcome.results
                #fp = fpsDict[each]
                #print(fp.parValueGet())

                # Or read one by one.
                fp = icm.FileParamReadFrom(
                    parRoot=fpBaseDir,
                    parName=each,
                )
                print(fp.parValueGet())   # type: ignore

        return cmndOutcome

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "fpBase cls"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(
    fpBase,
    cls,
):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        argChoices = ['all', ]


        fpBaseInst = pattern.sameInstance(getattr(__main__, cls), fpBase)

        for each in fpBaseInst.fps_namesWithRelPath():  # type: ignore
            argChoices.append(each)

        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&999",
            argName="formatTypes",
            argDefault="all",
            argChoices=argChoices,
            argDescription="One, many or all"
        )

        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:func/typing :funcName "FP_readTreeAtBaseDir_CmndOutput" :funcType "extTyped" :retType "extTyped" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /FP_readTreeAtBaseDir_CmndOutput/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def FP_readTreeAtBaseDir_CmndOutput(
####+END:
    interactive,
    fpBaseDir,
    cmndOutcome,
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Invokes FP_readTreeAtBaseDir.cmnd as interactive-output only.
    #+end_org """

    # Interactive-Output + Chained-Outcome Command Invokation
    #
    FP_readTreeAtBaseDir = icm.FP_readTreeAtBaseDir()
    FP_readTreeAtBaseDir.cmndLineInputOverRide = True
    FP_readTreeAtBaseDir.cmndOutcome = cmndOutcome

    return FP_readTreeAtBaseDir.cmnd(
        interactive=interactive,
        FPsDir=fpBaseDir,
    )


####+BEGIN: bx:cs:python:func :funcName "FP_writeDefaultsWithIcmParams" :funcType "succFail" :retType "bool" :deco "" :argsList "icmParamsAndDests"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-succFail [[elisp:(outline-show-subtree+toggle)][||]] /FP_writeDefaultsWithIcmParams/ retType=bool argsList=(icmParamsAndDests)  [[elisp:(org-cycle)][| ]]
#+end_org """
def FP_writeDefaultsWithIcmParams(
    icmParamsAndDests,
):
####+END:
    G = cs.globalContext.get()
    icmParams = G.icmParamDictGet()

    # Write relevant cmndParams as fileParams
    for eachParam, eachDest  in icmParamsAndDests.items():
        thisIcmParam = icmParams.parNameFind(eachParam)   # type: ignore
        thisIcmParam.parValueSet(thisIcmParam.parDefaultGet())
        thisIcmParam.writeAsFileParam(parRoot=eachDest,)

####+BEGIN: bx:cs:python:func :funcName "FP_writeWithIcmParams" :funcType "succFail" :retType "bool" :deco "" :argsList "icmParamsAndDests"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-succFail [[elisp:(outline-show-subtree+toggle)][||]] /FP_writeWithIcmParams/ retType=bool argsList=(icmParamsAndDests)  [[elisp:(org-cycle)][| ]]
#+end_org """
def FP_writeWithIcmParams(
    icmParamsAndDests,
):
####+END:
    G = cs.globalContext.get()
    icmRunArgs = G.icmRunArgsGet() #; icm.unusedSuppressForEval(icmRunArgs)
    icmParams = G.icmParamDictGet()

    cmndParamsDict = dict()

    # Read from cmndLine into callParamsDict
    for eachKey in icmParamsAndDests:
        cmndParamsDict[eachKey] = None
        try:
            exec("cmndParamsDict[eachKey] = icmRunArgs." + eachKey)
        except AttributeError:
            continue

    # Write relevant cmndParams as fileParams
    for eachParam, eachDest  in icmParamsAndDests.items():
        if cmndParamsDict[eachParam]:
            thisIcmParam = icmParams.parNameFind(eachParam)   # type: ignore
            thisIcmParam.parValueSet(cmndParamsDict[eachParam])
            thisIcmParam.writeAsFileParam(parRoot=eachDest,)


####+BEGIN: bx:cs:python:func :funcName "FP_listIcmParams" :funcType "succFail" :retType "bool" :deco "" :argsList "icmParamsAndDests"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-succFail [[elisp:(outline-show-subtree+toggle)][||]] /FP_listIcmParams/ retType=bool argsList=(icmParamsAndDests)  [[elisp:(org-cycle)][| ]]
#+end_org """
def FP_listIcmParams(
    icmParamsAndDests,
):
####+END:
    G = cs.globalContext.get()
    icmRunArgs = G.icmRunArgsGet() #; cs.unusedSuppressForEval(icmRunArgs)
    icmParams = G.icmParamDictGet()

    # List relevant cmndParams as fileParams
    for eachParam, eachDest  in icmParamsAndDests.items():
        thisIcmParam = icmParams.parNameFind(eachParam)   # type: ignore
        print(thisIcmParam)
        print(eachDest)




####+BEGIN: b:prog:file/endOfFile :extraParams nil
""" #+begin_org
* *[[elisp:(org-cycle)][| END-OF-FILE |]]* :: emacs and org variables and control parameters
#+end_org """
### local variables:
### no-byte-compile: t
### end:
####+END:
