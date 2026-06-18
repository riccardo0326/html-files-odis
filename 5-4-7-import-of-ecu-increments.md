[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.4. Importing Control Module Descriptions](5-4-importing-control-module-descriptions.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.4.7. Import of ECU Increments</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-4-6-display-oc-input-baseline.md">Prev</a> </td><th align="center" width="60%">5.4. Importing Control Module Descriptions</th><td align="right" width="20%"> <a accesskey="n" href="5-4-8-changing-comments-for-a-control-module-later.md">Next</a></td></tr></table>

---

#### <a id="sgbimport.inkrement"></a>5.4.7. Import of ECU Increments

If ECU increments are imported, ODIS Creator ensures that they are always imported completely according to their generation history. This ensures consistency of technical data.

During the import, the generation history is checked using "contentVersion". The check ensures that increments are only imported if their previous versions (increment or complete) are already present in the system.

Example:

A vehicle project with version "contentVersion='3040000060.2.85'” was already imported. If an attempt is now made to start importing increments in version "contentVersion='3040000080.2.91'", the import will be canceled because the intermediate version "contentVersion='3040000070.2.87'" is not present. The import of the vehicle project will be canceled and the status of the control module import will be set to “Canceled”. This has no effect on parallel imported vehicle projects.

The failure of the vehicle project import will be recorded in the control module import log. The log file will contain the following entry: "Vehicle project with name %s not imported, because version history is inconsistent with version '%s'.".

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-4-6-display-oc-input-baseline.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-4-importing-control-module-descriptions.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-4-8-changing-comments-for-a-control-module-later.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.4.6. Display OC input baseline </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.4.8. Changing Comments for a Control Module Later</td></tr></table>
