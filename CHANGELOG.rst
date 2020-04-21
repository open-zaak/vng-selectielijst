==============
Change history
==============

1.0.3 (2020-04-21)
==================

Mostly bugfixes

* Included K8s deployment tooling
* Fixed health check endpoint
* Dropped django-webtest dependency
* Removed reference to JS bundle, which crashes on the staticfiles manifest in
  production. There is no JS in this API project.

1.0.1 (2020-02-17)
==================

* Added missing ``resultaattypeomschrijvinggeneriek`` resource

1.0.0 (2020-01-28)
==================

* Initial release: include procestypen & resultaten.
