[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.4. Importing Control Module Descriptions](5-4-importing-control-module-descriptions.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.4.2. Control Module Import Phases</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-4-1-initiating-the-import-of-control-module-descriptions.md">Prev</a> </td><th align="center" width="60%">5.4. Importing Control Module Descriptions</th><td align="right" width="20%"> <a accesskey="n" href="5-4-3-observing-the-import-of-control-module-descriptions.md">Next</a></td></tr></table>

---

#### <a id="sgbimport.start.phasen"></a>5.4.2. Control Module Import Phases

A control module import is divided into three phases that are performed one after the other.

##### <a id="sgbimport.start.phasen.pruefsumme"></a>5.4.2.1. Phase 1: Checksum Check

During this phase, any checksums that are present are verified. If the verification of an extract file fails, the import of the surrounding vehicle project will be aborted. The control module import will be aborted completely with an error if all vehicle projects from the import folder are canceled in this way as a result of the check. As long as at least one vehicle project passes this check without errors, the import will continue in the next phase.

Each failed verification is written in the log file for this phase (ecuimport\_phase\_check\_error\_log).

##### <a id="sgbimport.start.phasen.importderdateien"></a>5.4.2.2. Phase 2: File Import

During the “File Import” phase, VRT/VPT vehicle projects or control module extracts are imported. The following checks are performed:

- Schema violation of VRT/VPT files

  The import is aborted completely with an error if only the VRT/VPT files are to be imported. If vehicle project folders are also to be imported, the import will continue in the next phase.

  The errors that occur will be logged in "ecuimport\_phase\_vpt\_vrt\_error\_log”.
- VRT/VPT files not present

  If the folder only contains vehicle projects that already exist in the database, i.e. that are known, an import without VRP/VPT files is also possible. If all vehicle projects from the import folder are unknown, then the import will abort completely with an error.

  The errors that occur will be logged in "ecuimport\_phase\_vpt\_vrt\_error\_log”.
- Import of control module extracts

  In this phase, the history for incremental control module imports, the schema of the control module extracts, and the relationship between the control modules are checked.

  Anomalies or errors that occur will be logged in "ecuimport\_phase\_vpt\_vrt\_error\_log”.

##### <a id="sgbimport.start.phasen.relationsverarbeitung"></a>5.4.2.3. Phase 3: Processing Relationships between Editorial Objects

The places where vehicle projects are used are updated during this phase.

The errors that occur will be logged in "ecuimport\_phase\_relation\_obj\_error\_log"

##### <a id="sgbimport.start.phasen.status"></a>5.4.2.4. Control Module Import Status

If an error occurs in a phase and the import is not aborted completely with an error, this will be signaled by the final import status of “Completed with errors”. This status is indicated with a yellow exclamation point in the navigator.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-4-1-initiating-the-import-of-control-module-descriptions.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-4-importing-control-module-descriptions.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-4-3-observing-the-import-of-control-module-descriptions.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.4.1. Initiating the Import of Control Module Descriptions </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.4.3. Observing the Import of Control Module Descriptions</td></tr></table>
