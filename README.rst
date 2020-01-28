=================
VNG-Selectielijst
=================

:Version: 0.5.4
:Source: https://github.com/open-zaak/vng-selectielijst
:Keywords: Open Zaak, selectielijst, api, zaakgericht werken
:PythonVersion: 3.8
:Url: https://selectielijst.openzaak.nl

|build-status| |coverage| |black| |docker|

Ontsluiting van de `Gemeentelijke Selectielijst`_ 2017 uitgegeven door VNG.

Deze implementatie van de selectielijst komt voort uit een fork van de
`VNG Referentielijsten <https://github.com/VNG-Realisatie/vng-referentielijsten>`_ API.

Inleiding
=========

VNG-Realisatie heeft in 2017 de Gemeentelijke Selectielijst 2017 uitgegeven waarin
een set procestypen en resultaten ontsloten wordt, met bijhorende archiveringstermijnen.

Deze selectielijst wordt via een API ontsloten t.b.v. API's voor zaakgericht werken. De
API is `publiek toegankelijk <https://selectielijst.open-zaak.nl>`_, met dank aan
`Gemeente Utrecht <https://utrecht.nl>`_ voor de hosting.

Documentation
=============

See ``INSTALL.rst`` for installation instructions, available settings and
commands.

References
==========

* `Issues <https://github.com/open-zaak/vng-selectielijst/issues>`_
* `Code <https://github.com/open-zaak/vng-selectielijst>`_

.. _Gemeentelijke Selectielijst: https://vng.nl/nieuws/selectielijst-gemeenten-en-intergemeentelijke-organen-2017

.. |build-status| image:: https://travis-ci.org/open-zaak/vng-selectielijst.svg?branch=master
    :alt: Build status
    :target: https://travis-ci.org/open-zaak/vng-selectielijst

.. |coverage| image:: https://codecov.io/github/open-zaak/vng-selectielijst/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage
    :target: https://codecov.io/gh/open-zaak/vng-selectielijst

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. |docker| image:: https://images.microbadger.com/badges/image/openzaak/vng-selectielijst.svg
    :target: https://microbadger.com/images/openzaak/vng-selectielijst

Licentie
========

Copyright © VNG Realisatie 2018
Copyright © Dimpact 2020

Licensed under the EUPL_

.. _EUPL: LICENCE.md
