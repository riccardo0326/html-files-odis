[ODIS Creator Help](odis-creator-help.md) > [8. ODIS Creator Preparation Process](8-odis-creator-preparation-process.md) > [8.11. Cooperation export](8-11-cooperation-export.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">8.11.7. Export Check Sum</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="8-11-6-managing-a-global-exclusion-list.md">Prev</a> </td><th align="center" width="60%">8.11. Cooperation export</th><td align="right" width="20%"> <a accesskey="n" href="9-odis-creator-configuration.md">Next</a></td></tr></table>

---

#### <a id="coopexport.checksum_editor"></a>8.11.7. Export Check Sum

After a successful export, the calculated SHA512 check sum for the export file will be displayed in the editor. The check sum can be copied to the clipboard for further use using a button.

<a id="figure.coopexport.checksum"></a>

![Illustration: check sum for an export file](images/coopexport_pruefsumme.png)

**Figure 636. Checksum**

  

<a id="export.pruefsumme"></a>In addition to the display in the editor, the check sum will be written in a text file that is located near the actual export file.

The check sum is used to check the integrity of the export file. For an integrity test, the recipient can calculate the check sum using standard Windows applications and compare it with the value provided by the exporter. If the value is the same, then integrity is ensured. The data was not modified during transmission.

Windows PowerShell application is used to calculate the SHA512 check sum of an export file. The following command can be entered there to generate the check sum: Get-FileHash Pfad-zur-Export-Datei -Algorithm SHA512 | Format-List

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="8-11-6-managing-a-global-exclusion-list.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="8-11-cooperation-export.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="9-odis-creator-configuration.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">8.11.6. Managing a Global Exclusion List </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 9. ODIS Creator Configuration</td></tr></table>
