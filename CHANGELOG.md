# Changelog

Every change in the project is listed here !  
Versions use the following format: ``major.minor.patch-<release state>``  
* ``major`` is updated on major changes, the runtime API isn't compatible between 2 major versions.  
* ``minor`` is updated on every minor changes, runtime API is compatible with older versions (except when mentioned).
* ``patch`` is updated every fix, the runtime is guaranteed to be compatible with older versions.
* ``<release state>`` is the state of the version, could be "pre" or "stable". "pre" versions are not guaranteed to be stable and are only for test purposes. 

# Timeline

01/03/2019 - `` v0.2.0-pre``  
26/02/2019 - `` v0.1.0-pre``

# Releases

---

## [Pre-release 2 (v0.2.0-pre)](https://github.com/BasileCombet/Thttil/releases/tag/v0.2.0-pre)

This version is incompatible with the v0.1.0-pre (language and runtime API). 

* Added a proper error handler.
* Reworked command collections.
* Modified syntax to avoid errors when running empty programs.
* Added some documentations.
* Created the official discord server.
* Hidden the antlr4 dependency from the runtime API.
* Added multiple output streams.
* Added basic tutorial scripts into https://github.com/BasileCombet/Thttil/tree/master/Examples/Tutorials

*Known issues:*

* The Sublime Text 3 syntax highlight hasn't been updated yet.

## [Pre-release 1 (v0.1.0-pre)](https://github.com/BasileCombet/Thttil/releases/tag/v0.1)

* Created Thttil.