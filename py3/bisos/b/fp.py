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

import __main__

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


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Classes, Functions and Operations" :anchor ""  :extraInfo "FP Base Facilities"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Classes, Functions and Operations_: |]]  FP Base Facilities  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:


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
        FP_readTreeAtBaseDir = icm.FP_readTreeAtBaseDir()
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
        icm.FileParamWriteTo(fpBase, paramName, paramValue)

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
        fpBase = namesWithAbsPath[paramName]
        paramValue = icm.FileParamReadFrom(fpBase, paramName,)
        return paramValue


####+BEGIN: b:py3:class/decl :className "FileParam" :superClass "" :comment "" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /FileParam/  superClass=object   [[elisp:(org-cycle)][| ]]
#+end_org """
class FileParam(object):
####+END:
    """ #+begin_org
** [[elisp:(org-cycle)][| DocStr| ]]  Representation of One FILE Parameter.

    A FileParam consists of 3 parts
       1) ParameterName
       2) ParameterValue
       3) ParameterAttributes

    On the file system:
      1- name of directory is ParameterName
      2- content of ParameterName/value is ParameterValue
      3- rest of the files in ParameterName/ are ParameterAttributes.

    The concept of a FileParam dates back to [[http://www.qmailwiki.org/Qmail-control-files][Qmail Control Files]] (at least).
    A FileParam is broader than that concept in two respects.
     1) A FileParam is represented as a directory on the file system. This FileParam
        permits the parameter to have attributes beyond just a value. Other attributes
        are themselves in the form of a traditional filename/value.
     2) The scope of usage of a FileParam is any parameter not just a control parameter.


    We are deliberately not using a python dictionary to represent a FileParam
    instead it is a full fledged python-object.
    #+end_org """

    def __init__(self,
                 parName=None,
                 parValue=None,
                 storeBase=None,
                 storeRoot=None,
                 storeRel=None,
                 attrRead=None,
                 ):
        '''Constructor'''
        self.__parName = parName
        self.__parValue = parValue
        self.__storeBase = storeBase   # storeBase = storeRoot + storeRel
        self.__storeRoot = storeRoot
        self.__storeRel = storeRel
        self.__attrRead = attrRead


    def __str__(self):
        return  format(
            str(self.parNameGet()) + ": " + str(self.parValueGet())
            )

    def parNameGet(self):
        """  """
        return self.__parName

    def parValueGet(self):
        """        """
        return self.__parValue

    def parValueGetLines(self):
        """        """
        if self.__parValue == None:
            return None
        return self.__parValue.splitlines()

    def parValueSet(self, value):
        """        """
        self.__parValue = value

    def attrReadGet(self):
        """        """
        return self.__attrRead

    def attrReadSet(self, attrRead):
        """        """
        self.__attrRead = attrRead

    @b.io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def readFrom(self, storeBase=None, parName=None):
        """Read into a FILE_param content of parBase/parName.

        Returns a FILE_param which was contailed in parBase/parName.
        """
        if self.__storeBase == None and storeBase == None:
            return io.eh.problem_usageError("storeBase")

        if self.__parName == None and parName == None:
            return io.eh.problem_usageError("parName")

        if storeBase:
            self.__storeBase = storeBase

        if parName:
            self.__parName = parName

        self.__parName = parName

        parNameFullPath = os.path.join(self.__storeBase, parName)

        return self.readFromPath(parNameFullPath)

    # Undecorated because called before initialization
    #@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def readFromPath(self, parNameFullPath):
        """Read into a FILE_param content of parBase/parName.

        Returns a FILE_param which was contailed in parBase/parName.
        """

        if not os.path.isdir(parNameFullPath):
            #return io.eh.problem_usageError("parName: " + parNameFullPath)
            return None

        fileParam = self

        fileParam.__parName = os.path.basename(parNameFullPath)

        #
        # Now we will fill fileParam based on the directory content
        #
        #if os.path.exists(parNameFullPath):
            #return io.eh.problem_usageError(f"Missing Path: {parNameFullPath}")

        for item in os.listdir(parNameFullPath):
            if item == "CVS":
                continue
            fileFullPath = os.path.join(parNameFullPath, item)
            if os.path.isfile(fileFullPath):
                if item == 'value':
                    lineString = open(fileFullPath, 'r').read().strip()    # Making sure we get rid of \n on read()
                    self.parValueSet(lineString)
                    continue

                # Rest of the files are expected to be attributes

                #lineString = open(fileFullPath, 'r').read()
                # NOTYET, check for exceptions
                #eval('self.attr' + str(item).title() + 'Set(lineString)')
            #else:
                #io.eh.problem_usageError("Unexpected Non-File: " + fileFullPath)

        return fileParam


    @b.io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def writeTo(self, storeBase=None, parName=None, parValue=None):
        """Write this FileParam to storeBase.

        """
        if self.__storeBase == None and storeBase == None:
            return io.eh.problem_usageError("storeBase")

        if self.__parName == None and parName == None:
            return io.eh.problem_usageError("parName")

        if self.__parValue == None and parValue == None:
            return io.eh.problem_usageError("parValue")

        if storeBase:
            self.__storeBase = storeBase

        if parName:
            self.__parName = parName
        else:
            parName = self.__parName

        if parValue:
            self.__parValue = parValue
        else:
            parValue = self.__parValue

        parNameFullPath = os.path.join(self.__storeBase, parName)
        try: os.makedirs( parNameFullPath, 0o777 )
        except OSError: pass

        fileTreeObject = b.fto.FILE_TreeObject(parNameFullPath)

        fileTreeObject.leafCreate()

        parValueFullPath = os.path.join(parNameFullPath, 'value')
        with open(parValueFullPath, "w") as valueFile:
             valueFile.write(str(parValue) +'\n')
             # NOTYET, this should be a pr
             io.pr("FileParam.writeTo path={path} value={value}".
                      format(path=parValueFullPath, value=parValue))

        return parNameFullPath


    @b.io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def writeToPath(self, parNameFullPath=None, parValue=None):
        """Write this FileParam to storeBase.
        """

        return self.writeTo(storeBase=os.path.dirname(parNameFullPath),
                            parName=os.path.basename(parNameFullPath),
                            parValue=parValue)


    @b.io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def writeToFromFile(self, storeBase=None, parName=None, parValueFile=None):
        """Write this FileParam to storeBase.

        """
        if self.__storeBase == None and storeBase == None:
            return io.eh.problem_usageError("storeBase")

        if self.__parName == None and parName == None:
            return io.eh.problem_usageError("parName")

        if parValueFile == None:
             return io.eh.problem_usageError("parValueFile")

        if storeBase:
            self.__storeBase = storeBase

        if parName:
            self.__parName = parName
        else:
            parName = self.__parName

        # if parValue:
        #     self.__parValue = parValue
        # else:
        #     parValue = self.__parValue

        parNameFullPath = os.path.join(self.__storeBase, parName)
        try: os.makedirs( parNameFullPath, 0o777 )
        except OSError: pass

        fileTreeObject = b.fto.FILE_TreeObject(parNameFullPath)

        fileTreeObject.leafCreate()

        parValueFullPath = os.path.join(parNameFullPath, 'value')
        with open(parValueFullPath, "w") as valueFile:
            with open(parValueFile, "r") as inFile:
                for line in inFile:
                    valueFile.write(line)

        return parNameFullPath


    def reCreationString(self):
        """Provide the string needed to recreate this object.

        """
        return


####+BEGIN: b:py3:class/decl :className "FileParamDict" :superClass "" :comment "" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /FileParamDict/  superClass=object   [[elisp:(org-cycle)][| ]]
#+end_org """
class FileParamDict(object):
####+END:
    """ #+begin_org
** [[elisp:(org-cycle)][| DocStr| ]] Maintain a list of FileParams.
    NOTYET, nesting of dictionaries.
    #+end_org """

    def __init__(self):
        self.__fileParamDict = dict()

    def parDictAdd(self, fileParam=None):
        """        """
        self.__fileParamDict.update({fileParam.parNameGet():fileParam})

    def parDictGet(self):
        """        """
        return self.__fileParamDict

    def parNameFind(self, parName=None):
        """        """
        return self.__fileParamDict[parName]

    def readFrom(self, path=None):
        """Read each file's content into a FLAT dictionary item with the filename as key.

        Returns a Dictionary of paramName:FileParam.
        """

        absolutePath = os.path.abspath(path)

        if not os.path.isdir(absolutePath):
            return None

        for item in os.listdir(absolutePath):
            fileFullPath = os.path.join(absolutePath, item)
            if os.path.isdir(fileFullPath):

                blank = FileParam()

                itemParam = blank.readFrom(storeBase=absolutePath, parName=item)

                self.parDictAdd(itemParam)

        return self.__fileParamDict

####+BEGIN: bx:cs:py3:section :title "*Individual Write Params Functional Interface*"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] **Individual Write Params Functional Interface**  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:func/typing :funcName "FileParamWriteTo" :funcType "extTyped" :retType "extTyped" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /FileParamWriteTo/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def FileParamWriteTo(
####+END:d
        parRoot=None,
        parName=None,
        parValue=None,
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    thisFileParam = FileParam(parName=parName, parValue=parValue,)

    if thisFileParam == None:
        return io.eh.critical_usageError('')

    return thisFileParam.writeTo(storeBase=parRoot)

####+BEGIN: b:py3:cs:func/typing :funcName "FileParamWriteToPath" :funcType "extTyped" :retType "extTyped" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /FileParamWriteToPath/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def FileParamWriteToPath(
####+END:
        parNameFullPath=None,
        parValue=None,
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    thisFileParam = FileParam()

    if thisFileParam == None:
        return io.eh.critical_usageError('')

    return thisFileParam.writeToPath(parNameFullPath=parNameFullPath,
                                     parValue=parValue)


####+BEGIN: b:py3:cs:func/typing :funcName "FileParamWriteToFromFile" :funcType "extTyped" :retType "extTyped" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /FileParamWriteToFromFile/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def FileParamWriteToFromFile(
####+END:
        parRoot=None,
        parName=None,
        parValueFile=None,
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    thisFileParam = FileParam(parName=parName)

    if thisFileParam == None:
        return io.eh.critical_usageError('')

    return thisFileParam.writeToFromFile(storeBase=parRoot, parValueFile=parValueFile)


####+BEGIN: b:py3:cs:func/typing :funcName "FileParamVerWriteTo" :funcType "extTyped" :retType "extTyped" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /FileParamVerWriteTo/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def FileParamVerWriteTo(
####+END:
        parRoot=None,
        parName=None,
        parVerTag=None,
        parValue=None,
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Given ticmoBase, Create parName, then assign parValue to parVerTag
    #+end_org """

    parFullPath = os.path.join(parRoot, parName)
    try: os.makedirs( parFullPath, 0o777 )
    except OSError: pass

    thisFileParam = FileParam(parName=parVerTag,
                                    parValue=parValue,
                                    )

    if thisFileParam == None:
        return io.eh.critical_usageError('')

    return thisFileParam.writeTo(storeBase=parFullPath)


####+BEGIN: bx:cs:py3:section :title "*Individual Read Params Functional Interface*"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] **Individual Read Params Functional Interface**  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:


####+BEGIN: b:py3:cs:func/typing :funcName "FileParamReadFrom" :funcType "extTyped" :retType "extTyped" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /FileParamReadFrom/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def FileParamReadFrom(
####+END:
        parRoot=None,
        parName=None,
        parVerTag=None,
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    blank = FileParam()

    if blank == None:
        return io.eh.critical_usageError('blank')

    filePar = blank.readFrom(storeBase=parRoot, parName=parName)

    if filePar == None:
        #print('Missing: ' + parRoot + parName)
        raise IOError
        #return io.eh.critical_usageError('blank')
        return None

    return filePar

####+BEGIN: b:py3:cs:func/typing :funcName "FileParamValueReadFrom" :funcType "extTyped" :retType "extTyped" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /FileParamValueReadFrom/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def FileParamValueReadFrom(
####+END:
        parRoot=None,
        parName=None,
        parVerTag=None,
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    blank = FileParam()

    if blank == None:
        return io.eh.critical_usageError('blank')

    filePar = blank.readFrom(storeBase=parRoot, parName=parName)

    if filePar == None:
        print(('Missing: ' + parRoot + parName))
        #raise IOError
        #return io.eh.critical_usageError('blank')
        return None

    return(filePar.parValueGet())

####+BEGIN: b:py3:cs:func/typing :funcName "FileParamReadFromPath" :funcType "extTyped" :retType "extTyped" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /FileParamReadFromPath/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def FileParamReadFromPath(
####+END:
        parRoot=None,
        parVerTag=None,
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    blank = FileParam()

    if blank == None:
        return io.eh.critical_usageError('blank')

    filePar = blank.readFromPath(parRoot)

    if filePar == None:
        #print('Missing: ' + parRoot + parName)
        raise IOError
        #return io.eh.critical_usageError('blank')

    return filePar


####+BEGIN: b:py3:cs:func/typing :funcName "FileParamValueReadFromPath" :funcType "extTyped" :retType "extTyped" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /FileParamValueReadFromPath/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def FileParamValueReadFromPath(
####+END:
        parRoot=None,
        parVerTag=None,
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    blank = FileParam()

    if blank == None:
        return io.eh.critical_usageError('blank')

    filePar = blank.readFromPath(parRoot)

    if filePar == None:
        print(('Missing: ' + parRoot))
        return io.eh.critical_usageError('blank')

    return(filePar.parValueGet())


####+BEGIN: b:py3:cs:func/typing :funcName "FileParamVerReadFrom" :funcType "extTyped" :retType "extTyped" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /FileParamVerReadFrom/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def FileParamVerReadFrom(
####+END:
        parRoot=None,
        parName=None,
        parVerTag=None,
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    blank = FileParam()

    if blank == None:
        try:  io.eh.critical_usageError('blank')
        except RuntimeError:  return

    parFullPath = os.path.join(parRoot, parName)
    try: os.makedirs( parFullPath, 0o777 )
    except OSError: pass


    filePar = blank.readFrom(storeBase=parFullPath, parName=parVerTag)

    if filePar == None:
        #print('Missing: ' + parRoot + parName)
        return io.eh.critical_usageError('blank')

    #print(filePar.parValueGet())
    return filePar

####+BEGIN: bx:cs:py3:section :title "FILE_paramDict Functional Interface"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *FILE_paramDict Functional Interface*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:func/typing :funcName "FILE_paramDictRead" :comment "OLD Style CMND" :funcType "extTyped" :retType "extTyped" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /FILE_paramDictRead/ deco=default  =OLD Style CMND= deco=default   [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def FILE_paramDictRead(
####+END:
        interactive=None, # NOTYET, icm.Interactivity.Both,
        inPathList=None
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Old Style CMND
    #+end_org """

    try: icm.callableEntryEnhancer(type='cmnd')
    except StopIteration:  return(icm.ReturnCode.ExtractionSuccess)

    G = cs.globalContext.get()
    G.curFuncNameSet(b.ast.FUNC_currentGet().__name__)

    if icm.Interactivity().interactiveInvokation(interactive):
        icmRunArgs = G.icmRunArgsGet()
        #if cmndArgsLengthValidate(cmndArgs=icmRunArgs.cmndArgs, expected=0, comparison=int__gt):
            #return(ReturnCode.UsageError)

        inPathList = []
        for thisPath in icm.icmRunArgs.cmndArgs:
            inPathList.append(thisPath)
    else:
        if inPathList == None:
            return io.eh.critical_usageError('inPathList is None and is Non-Interactive')

    for thisPath in inPathList:
        blankDict = FileParamDict()
        thisParamDict = blankDict.readFrom(path=thisPath)
        icm.TM_here('path=' + thisPath)

        if thisParamDict == None:
            continue

        for parName, filePar  in thisParamDict.items():
            print(('parName=' + parName))
            if filePar == None:
                continue
            thisValue=filePar.parValueGetLines()
            if thisValue == None:
                icm.TM_here("Skipping: " + filePar.parNameGet())
                continue
            print((
                filePar.parNameGet() +
                '=' +
                thisValue[0]))
    return


####+BEGINNOT: b:py3:cs:cmnd/classHead :modPrefix "" :cmndName "FP_readTreeAtBaseDir" :comment "" :parsMand "FPsDir" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<FP_readTreeAtBaseDir>> parsMand=FPsDir parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class FP_readTreeAtBaseDir(b.cs.Cmnd):
    cmndParamsMandatory = [ 'FPsDir', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        FPsDir=None,         # or Cmnd-Input
    ) -> b.op.Outcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'FPsDir': FPsDir, }
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        FPsDir = callParamsDict['FPsDir']

####+END:
        #G = cs.globalContext.get()

        # return FP_readTreeAtBaseDir_f(
        #     interactive=interactive,
        #     outcome = cmndOutcome,
        #     FPsDir=FPsDir,
        # )

        blankParDictObj  = FileParamDict()
        thisParamDict = blankParDictObj.readFrom(path=FPsDir)
        icm.TM_here(f"path={FPsDir}")

        if thisParamDict == None:
            return icm.eh_problem_usageError(
                cmndOutcome,
                "thisParamDict == None",
            )

        if interactive:
            icm.ANN_write(FPsDir)
            FILE_paramDictPrint(thisParamDict)

        return cmndOutcome.set(
            opError=cs.OpError.Success,
            opResults=thisParamDict,
        )

    def cmndDocStr(self): return """
** Reads and recurses through all FPs.  [[elisp:(org-cycle)][| ]]
*** When interactive, also prints out parValues as read.
"""


def cmndCallParamsValidate(
        callParamDict,
        interactive,
        outcome=None,

):
    """Expected to be used in all CMNDs.

MB-2022 --- This is setting the variable not validating it.
    Perhaps the function should have been cmndCallParamsSet.

Usage Pattern:

    if not icm.cmndCallParamValidate(FPsDir, interactive, outcome=cmndOutcome):
       return cmndOutcome
"""
    #G = cs.globalContext.get()
    #if type(callParamOrList) is not list: callParamOrList = [ callParamOrList ]

    if not outcome:
        outcome = b.op.Outcome()

    for key  in callParamDict:
        # print(f"111 {key}")
        # interactive could be true in two situations:
        # 1) When a cs is executed on cmnd-line.
        # 2) When a cs is invoked with interactive as true.
        # When (2) callParamDict[key] is expcted to be true by having been specified at invokation.
        #
        if not callParamDict[key]:
            # MB-2022 The logic here seems wrong. When non-interactive, only mandattories
            # should be verified.
            # if not interactive:
            #     return eh_problem_usageError(
            #         outcome,
            #         "Missing Non-Interactive Arg {}".format(key),
            #     )
            if interactive:
                exec("callParamDict[key] = IcmGlobalContext().usageParams." + key)
            # print(f"222 {callParamDict[key]}")


    return True

####+BEGIN: b:py3:cs:func/typing :funcName "FILE_paramDictPrint" :funcType "extTyped" :retType "extTyped" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /FILE_paramDictPrint/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def FILE_paramDictPrint(
####+END:
        fileParamDict,
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Returns a Dictionary of paramName:FileParam.
    #+end_org """
    for parName, filePar  in fileParamDict.items():
        #print('parName=' + parName)
        if filePar == None:
            continue
        thisValue=filePar.parValueGetLines()
        if thisValue == None:
            icm.TM_here("Skipping: " + filePar.parNameGet())
            continue
        if thisValue:
            print((
                filePar.parNameGet() +
                '=' +
                thisValue[0]))
        else: # Empty list
            print((
                filePar.parNameGet() +
                '='))



####+BEGIN: b:py3:cs:func/typing :funcName "FILE_paramDictReadDeep" :comment "OLD Style Cmnd" :funcType "extTyped" :retType "extTyped" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /FILE_paramDictReadDeep/ deco=default  =OLD Style Cmnd= deco=default   [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def FILE_paramDictReadDeep(
####+END:
        interactive=None, # NOTYET, icm.Interactivity.Both,
        inPathList=None
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] OLD Style Cmnd --- NOTYET, to be revisited
    #+end_org """

    try: icm.callableEntryEnhancer(type='cmnd')
    except StopIteration:  return(icm.ReturnCode.ExtractionSuccess)

    G = cs.globalContext.get()
    G.curFuncNameSet(b.ast.FUNC_currentGet().__name__)

    if icm.Interactivity().interactiveInvokation(interactive):
        icmRunArgs = G.icmRunArgsGet()
        #if cmndArgsLengthValidate(cmndArgs=icmRunArgs.cmndArgs, expected=0, comparison=int__gt):
            #return(ReturnCode.UsageError)

        inPathList = []
        for thisPath in icm.icmRunArgs.cmndArgs:
            inPathList.append(thisPath)
    else:
        if inPathList == None:
            return io.eh.critical_usageError('inPathList is None and is Non-Interactive')

    fileParamsDict = {}

    for thisPath in inPathList:
        #absolutePath = os.path.abspath(thisPath)

        if not os.path.isdir(thisPath):
            return io.eh.critical_usageError('Missing Directory: {thisPath}'.format(thisPath=thisPath))

        for root, dirs, files in os.walk(thisPath):
            #print("root={root}".format(root=root))
            #print ("dirs={dirs}".format(dirs=dirs))
            #print ("files={files}".format(files=files))

            thisFileParamValueFile = os.path.join(root, "value")
            if os.path.isfile(thisFileParamValueFile):
                try:
                    fileParam = FileParamReadFromPath(parRoot=root)
                except IOError:
                    io.eh.problem_info("Missing " + root)
                    continue

                fileParamsDict.update({root:fileParam.parValueGet()})
                if interactive:
                    print((root + "=" + fileParam.parValueGet()))

    return fileParamsDict


####+BEGIN: b:py3:cs:func/typing :funcName "readTreeAtBaseDir_wOp" :funcType "wOp" :retType "OpOutcome" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-wOp    [[elisp:(outline-show-subtree+toggle)][||]] /readTreeAtBaseDir_wOp/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def readTreeAtBaseDir_wOp(
####+END:
        fpsDir: typing.AnyStr,
        outcome: typing.Optional[b.op.Outcome] = None,
) -> b.op.Outcome:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] A Wrapped Operation with results
    #+end_org """

    if not outcome:
        outcome = b.op.Outcome()

    blankParDictObj  = FileParamDict()
    thisParamDict = blankParDictObj.readFrom(path=fpsDir)
    icm.TM_here(f"path={fpsDir}")

    if thisParamDict == None:
        return icm.eh_problem_usageError(
            outcome,
            "thisParamDict == None",
        )

    # icm.ANN_write(fpsDir)
    # FILE_paramDictPrint(thisParamDict)

    return outcome.set(
        opError=cs.OpError.Success,
        opResults=thisParamDict,
    )

####+BEGIN: b:py3:cs:func/typing :funcName "parsGetAsDictValue_wOp" :funcType "wOp" :retType "OpOutcome" :deco "default" :argsList "typed"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-wOp    [[elisp:(outline-show-subtree+toggle)][||]] /parsGetAsDictValue_wOp/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def parsGetAsDictValue_wOp(
####+END:
        parNamesList: typing.Optional[list],
        fpsDir: typing.AnyStr,
        outcome: typing.Optional[b.op.Outcome] = None,
) -> b.op.Outcome:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] A Wrapped Operation with results being a dictionary of values.
    if not ~parNamesList~, get all the values.
*** TODO --- NOTYET This needs to be moved to
    #+end_org """

    outcome = readTreeAtBaseDir_wOp(fpsDir, outcome=outcome)

    results = outcome.results

    opResults = dict()
    #opErrors = ""

    if parNamesList:
        for each in parNamesList:
            # NOTYET, If no results[each], we need to record it in opErrors
            if each in results.keys():
                opResults[each] = results[each].parValueGet()
            else:
                opResults[each] = "UnFound"


            #print(f"{each} {eachFpValue}")

    else:
        for eachFpName in results:
            opResults[eachFpName] = results[eachFpName].parValueGet()
            #print(f"{eachFpName} {eachFpValue}")

    return outcome.set(
        opError=cs.OpError.Success,
        opResults=opResults,
    )


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

        from bisos.examples import fp_csu

        #fpBaseInst = b.pattern.sameInstance(getattr(__main__, cls), fpBase)
        fpBaseInst = b.pattern.sameInstance(getattr(fp_csu, cls), fpBase)
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

        from bisos.examples import fp_csu

        #fpBaseInst = pattern.sameInstance(getattr(__main__, cls), fpBase)
        fpBaseInst = pattern.sameInstance(getattr(fp_csu, cls), fpBase)
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
