===============================================================
bisos.b: PyCS-Foundation Package – Python Commands and Services
===============================================================

.. contents::
   :depth: 3
..

Overview
========

**bisos.b** (**PyCS-Foundation**) is a python package which functions as
a foundation for development of Command-Services based on the general
model of **Expectation Complete Operations** (**ECO**)s.

PyCS-Foundation is further enhanced with other packages and tools
forming **PyCS-Framework**. PyCS-Framework are a set of
Standalone-BISOS-Packages.

PyCS-Framework can be used in python environments without BISOS.

Python BISOS-Applications and BISOS-Capabilities are all based on the
PyCS-BISOS-Framework.

This layering is captured below:

======================= ===================
PyCS-BISOS-Applications bisos.marmee
PyCS-BISOS-Framework    bisos.bpo bisos.aas
PyCS-Framework          bisos.currents
PyCS-Foundation         bisos.b
======================= ===================

.. _table-of-contents:

Table of Contents TOC
=====================

-  `Overview <#overview>`__
-  `About BISOS – ByStar Internet Services Operating System – and ByStar
   DE <#about-bisos----bystar-internet-services-operating-system----and-bystar-de>`__
-  `Concept of Command-Services and Expection Complete Operations
   (ECP) <#concept-of-command-services-and-expection-complete-operations-ecp>`__

   -  `Current and Prior Art <#current-and-prior-art>`__
   -  `Our model and terminology for
      Remote-Operation <#our-model-and-terminology-for-remote-operation>`__
   -  `PyCS (Python Command Services):BISOS's Integration
      Framework <#pycs-python-command-servicesbisoss-integration-framework>`__
   -  `Commands-Services as Python
      ECP <#commands-services-as-python-ecp>`__

-  `Installation <#installation>`__

   -  `With pip <#with-pip>`__
   -  `With pipx <#with-pipx>`__

-  `Usage <#usage>`__

   -  `Locally (system command-line) <#locally-system-command-line>`__
   -  `Remotely (as a service) <#remotely-as-a-service>`__

-  `bisos.facter Code Walkthrough <#bisosfacter-code-walkthrough>`__

   -  `bisos.facter Source Code is in
      COMEEGA <#bisosfacter-source-code-is-in-comeega>`__
   -  `Take from
      120033/common/engAdopt <#take-from-120033commonengadopt>`__
   -  `./bin/facter.cs (./bin/facter-roPerf.cs
      ./bin/facter-roInv.cs) <#binfactercs--binfacter-roperfcs--binfacter-roinvcs>`__
   -  `./bisos/facter/facter.py <#bisosfacterfacterpy>`__
   -  `./bisos/facter/facter\ csu.py <#bisosfacterfacter_csupy>`__

-  `Support <#support>`__
-  `Documentation <#documentation>`__

About BISOS – ByStar Internet Services Operating System – and ByStar DE
=======================================================================

Layered on top of Debian, **BISOS**: (**ByStar Internet Services
Operating System**) is a unified and universal platform for developing
both internet services and software-service continuums that use internet
services. See `Bootstrapping ByStar, BISOS and
Blee <https://github.com/bxGenesis/start>`__ for information about
getting started with BISOS.

*bisos.b* is a small piece of a much bigger picture. **BISOS** is a
foundation for **The Libre-Halaal ByStar Digital Ecosystem** which is
described as a cure for losses of autonomy and privacy that we are
experiencing in a book titled: `Nature of
Polyexistentials <https://github.com/bxplpc/120033>`__

Concept of Command-Services and Expection Complete Operations (ECP)
===================================================================

Current and Prior Art
---------------------

Conventionally, a good number of packages and frameworks have been
produced to facilitate development of CLI based python applications.
These include: Click, Typer (based on Pydantic), cyto,
`argparse <https://docs.python.org/3/library/argparse.html>`__, Docopt,
fire, plumbum, cleo, etc.

Conventionally, a good number of packages and frameworks have been
produced to facilitate development of
Web-APIs/Web-Services/REST-APIs/OpenAPI/Swagger based python clients and
servers. These include: FastAPI (based on Pydantic), gRPC, pyswagger,
Bravado, Flask-API, djangorestframework, RPyC, etc.

These common conventional approaches have several shorcomings which
include:

-  The model and terminology of
   Web-APIs/Web-Services/REST-APIs/OpenAPI/SOAP/gRPC is ill directed.
   The proper model and terminology is that of **Remote Operations**.

-  All of the web services models mix web with remote operations at
   protocol layer. This is particularly true of OpenAPI and is wrong.

-  All of the web services models confuse the Remote Operations
   invoke/perform architecture with the Client/Server architecture. This
   modeling and terminology error has caused immense confusion.

-  The CLI development and API development frameworks have a great deal
   in common and can be merged.

-  None of the exisiting frameworks combine CLI development and API
   development.

Our model and terminology for Remote-Operation
----------------------------------------------

Our model and terminology for Remote-Operations is based on:

   **X.880 ( ISO/IEC 13712-1): Remote Operations: Model, Notation and
   Service Definition**

ITU X.880 and X.881 which are harmonized with ISO/IEC 13712-1, provide a
model, terminology and service definitions for Remote Operations. These
date back to mid 1990s

Such a valuable formal model and terminology is absent in the Web
Services world and the OpenAIP/Swagger world.

Our model and terminology is based on the Remote Operations Services
Element (ROSE).

PyCS (Python Command Services):BISOS's Integration Framework
------------------------------------------------------------

 [sec:PyCS:BISOS'sIntegrationFramework]

BISOS is largely focused on configuration and integration of related
software packages towards creation of consistent services. This is
typically done with "scripts" that augment the software packages in a
consistent way. By scripts, we mean programs that are executed at
command line. At times we also need to build Remote Operations (RO) to
accommodate remote invocation of central services.

There are three fundamental important choices to be made:

#. What programming language should we use for integration?

#. What command-line framework should we use?

#. What Remote Operations (Web Services, REST, Micro Services) framework
   should we use?

BISOS primarily uses Python and some Bash for scripting.

There are various Python frameworks for command-line and web services.
These include click, FastAPI, Flask, Django, RPyC and various others.
None of these provide a comprehensive enough framework for BISOS. BPyF
(BISOS Python Framework) is a comprehensive integration framework of
BISOS that combines existing capabilities from various Python
frameworks.

`/lcnt/lgpc/bystar/permanent/common/figures/pycsAnatomy.pdf <file:///lcnt/lgpc/bystar/permanent/common/figures/pycsAnatomy.pdf>`__

As depicted in Figure `[fig:pycsAnatomy <#fig:pycsAnatomy>`__], BPyF
consists of five major parts.

-  Common facilities — logging, io, error handling, etc.

-  File Parameters (FP) and Schema of File Parameters — BISOS's data
   representation and configuration model

-  PyCS: Python Command Services

-  BISOS Abstractions

-  CS-Units and CS-MultiUnits

In Figure `[fig:pycsAnatomy <#fig:pycsAnatomy>`__], boxes under the
dashed line represent various libraries. General purpose libraries (on
the right side is light green) provide common facilities such as IO,
logging, error handling and configuration management which are used
throughout BISOS. Various libraries that represent BISOS abstractions in
Python such as BPOs, PALS and PAAI. These are shown on the left side in
darker green.

For data representation, BISOS uses its own model called File
Parameters. The equivalent functionality of File Parameters is often
provided by Yaml and Json in typical open-source software packages.

PyCS Expectation Complete Operations (ECO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 [sec:PyCSExpectationCompleteOperations(ECO)]

PyCS is rooted in the model of Expectation Complete Operations (ECO),
which allows for local invocation of an ECO to map to command-line
invocation and remote invocation of an ECO to map to the microservices
model and Remote Operations. This universality of ECOs allows for
command-line facilities to become microservices.

Facilities for command line invocation are depicted above the dashed
line, on the left side of "internet". Facilities in support of service
(Remote Operation) performers are depicted above the dashed line, on the
right side of "internet".

Expectation complete operations are specified and implemented in
CS-Units. A CS-Multi-Unit represents a collection of CS-Units. Notice
that CS-Unit and CS-Multi-Unit boxes are replicated on both sides of
"internet". This indicates that both commands and remote operations map
to expectation complete operations.

Each ECO is capable of describing everything expected from the operation
in full detail which includes all typing information. The information in
Expectation Complete Operation includes:

-  Name of the operation

-  All input parameters

   -  List of optional and mandatory parameters

   -  List of positional arguments

   -  Stdin expectations

-  All outcome parameters

   -  All result parameters

   -  All error parameters

The information of expectation complete operation then maps to
command-line verbs, parameters and arguments, and similarly for remote
operations. The list of available verbs is specified by the
CS-Multi-Unit. Since CS-Multi-Units are capable of describing all of the
expectations of all of their operations, very powerful automated user
interfaces for invocation of operations can be built. The "CS Player"
box in Figure `[fig:pycsAnatomy <#fig:pycsAnatomy>`__] illustrates that.

BISOS PyCS Remote Operations (Web Services)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 [sec:BISOSPyCSRemoteOperations(WebServices)]

Many BISOS facilities need to be implemented and are implemented as
remote operations. We use the concept and abstraction of remote
operations instead of web services or microservices, to define network
exposed operations.

In BISOS, instead of choosing specific web services or rpc paradigms
such as OpenAPI/Swagger, FastAPI, SOAP, gRPC, RPyC, etc, we bind our
model of Expectation Complete Operations (ECO) to these at a later
stage.

At this time, PyCS remote operations are implemented using RPyC. RPyC or
Remote Python Call, is a transparent library for symmetrical remote
procedure calls, clustering, and distributed-computing. Use of RPyC is
depicted with the line going through the vertical box labeled
"internet". Names used by invokers and performers are shown in the boxes
labeled "RO-Sap" (Remote Operation Service Access Point).

PyCS framework provides a solid foundation for transformation of
software into services and integration of software and services in
BISOS.

Commands-Services as Python ECP
-------------------------------

bisos.facter can be used locally on command-line or remotely as a
service. bisos.facter is a PyCS multi-unit command-service. PyCS is a
framework that converges developement of CLI and Services. PyCS is an
alternative to FastAPI, Typer and Click.

bisos.facter uses the PyCS Framework to:

#. Provide access to facter information through python namedtuple
#. Provide local access to facter information on CLI
#. Provide remote access to facter information through remote invocation
   of python Expection Complete Operations using
   `rpyc <https://github.com/tomerfiliba-org/rpyc>`__.
#. Provide remote access to facter information on CLI

What is unique in the PyCS Framework is that these four models are all a
single abstraction.

Installation
============

The sources for the bisos.facter pip package is maintained at:
https://github.com/bisos-pip/facter.

The bisos.facter pip package is available at PYPI as
https://pypi.org/project/bisos.facter

You can install bisos.facter with pip or pipx.

With pip
--------

If you need access to bisos.facter as a python module, you can install
it with pip:

.. code:: bash

   pip install bisos.facter

With pipx
---------

If you only need access to bisos.facter on command-line, you can install
it with pipx:

.. code:: bash

   pipx install bisos.facter

The following commands are made available:

-  facter.cs
-  facter-roInv.cs
-  facter-roPerf.cs

These are all one file with 3 names. *facter-roInv.cs* and
*facter-roPerf.cs* are sym-links to *facter.cs*

Usage
=====

Locally (system command-line)
-----------------------------

``facter.cs`` does the equivalent of facter.

.. code:: bash

   bin/facter.cs

Remotely (as a service)
-----------------------

You can also run

Performer
~~~~~~~~~

Invoke performer as:

.. code:: bash

   bin/facter-roPerf.cs

Invoker
~~~~~~~

.. code:: bash

   bin/facter-roInv.cs

bisos.facter Code Walkthrough
=============================

bisos.facter Source Code is in COMEEGA
--------------------------------------

bisos.facter can be used locally on command-line or remotely as a
service.

.. _take-from-120033commonengadopt:

TODO Take from 120033/common/engAdopt
-------------------------------------

./bin/facter.cs (./bin/facter-roPerf.cs ./bin/facter-roInv.cs)
--------------------------------------------------------------

A multi-unit

./bisos/facter/facter.py
------------------------

./bisos/facter/facter\ :sub:`csu`.py
------------------------------------

Support
=======

| For support, criticism, comments and questions; please contact the
  author/maintainer
| `Mohsen Banan <http://mohsen.1.banan.byname.net>`__ at:
  http://mohsen.1.banan.byname.net/contact

Documentation
=============

Part of ByStar Digital Ecosystem http://www.by-star.net.

This module's primary documentation is in
http://www.by-star.net/PLPC/180047
