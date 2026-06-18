[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.20. Export and Import](7-20-export-and-import.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.20.2. Import Function</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-20-1-export-function.md">Prev</a> </td><th align="center" width="60%">7.20. Export and Import</th><td align="right" width="20%"> <a accesskey="n" href="8-odis-creator-preparation-process.md">Next</a></td></tr></table>

---

#### <a id="import.only"></a>7.20.2. Import Function

The „Import“ menu item ![](images/import1.png) is visible or active depending on the current focus and the selection in the ODIS Creator application. The menu item is only then displayed in the global menu (file), if the „function library“ navigation tree is in focus.

If you mark a structure node, then you can start the import of a function test, a general test or a test procedure. After selecting the import file in the local folder, the import will be started and the object is inserted under the selected structure node. An import log is stored in the import file folder. This log will list which function codes were imported and any errors that occurred.

The [Figure 597, “Message for the import of existing objects”](7-20-2-import-function.md#figure.import.meldung "Figure 597. Message for the import of existing objects") shows a message if an object already exists in the environment while importing.

<a id="figure.import.meldung"></a>

![Message for the import of existing objects](images/import_meldung.png)

**Figure 597. Message for the import of existing objects**

The object files to be exported will be checked for integrity before the import. The checksum from the Index.xml file will be used for this. If the check for an object file fails, the import will be aborted and the user will be informed with a message (see [Figure 598, “Message when Importing Faulty Check of Object Files”](7-20-2-import-function.md#figure.import.checksum "Figure 598. Message when Importing Faulty Check of Object Files")). In this case, an import log will be stored in the import file folder. This log contains all object files for which the check failed.

<a id="figure.import.checksum"></a>

![Message when Importing Faulty Check of Object Files](http://127.0.0.1:55991/help/topic/MasterData_Client_Control/html/images/import_pruefsumme_fehler.png)

**Figure 598. Message when Importing Faulty Check of Object Files**

If the package to be imported does not match the structure node, the import will be canceled. If this is the case, then there is no import log in the folder. Rather, there is only a message given to the user (see [Figure 599, “Message when importing to incorrect structure node”](7-20-2-import-function.md#figure.import.fehler "Figure 599. Message when importing to incorrect structure node")).

<a id="figure.import.fehler"></a>

![Message when importing to incorrect structure node](images/Import_falscher_Knoten.png)

**Figure 599. Message when importing to incorrect structure node**

If all objects were checked correctly for integrity, you can select the desired option. In this case, there will not be an import log for the integrity check in the import file folder.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-20-1-export-function.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-20-export-and-import.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="8-odis-creator-preparation-process.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.20.1. Export function </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 8. ODIS Creator Preparation Process</td></tr></table>
