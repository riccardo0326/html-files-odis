[ODIS Creator Help](odis-creator-help.md) > [6. ODIS Creator Order Management Process](6-odis-creator-order-management-process.md) > [6.4. Translation](6-4-translation.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">6.4.11. Excel Export of Translation Packages</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="6-4-10-translation-disputes.md">Prev</a> </td><th align="center" width="60%">6.4. Translation</th><td align="right" width="20%"> <a accesskey="n" href="7-odis-creator-editing-process.md">Next</a></td></tr></table>

---

#### <a id="uebersetzung.excelexport"></a>6.4.11. Excel Export of Translation Packages

The excel export serves to export translation packages from different locations for different languages during a certain time period. The Excel file contains an overview table, which lists all effected translation packages. Furthermore, there is an individual table page for each of the listed translation packages, in which the specific package information is contained.

##### <a id="Excel.export"></a>6.4.11.1. Excel Export

The Excel export can be started by a [translation coordinator](3-3-1-description-of-roles.md "3.3.1. Description of Roles"). The function can be started through the context menu or through the file -> **Excel export**. The lower displayed dialog appears to enter the parameters for the export.

<a id="figure.auftragsverwaltung.uebersetzung.excel"></a>

![Image: Excel Export Dialog](images/ExcelExport.jpg)

**Figure 167. Excel Export Dialog**

You can select the following parameters for the export. Some of these parameters are optional and some are mandatory.

- **Target date**

  The user can give specifications in the dialog for the planned target date of the translation packages being exported. This specification is optional. If a date is set, it is possible to give a closed interval ("from" and "to") or give open intervals. The entered day is therefore always included.
- **Creation date**

  The user can give specifications in the dialog for the created on date of the translation packages being exported. This specification is optional. If a date is set, it is possible to give a closed interval ("from" and "to") or give open intervals. The entered day is therefore always included.
- **Import date**

  The user can give specifications in the dialog for the import date of the translation packages being exported. This specification is optional. If a date is set, it is possible to give a closed interval ("from" and "to") or give open intervals. The entered day is therefore always included. This specification is only effective if the user has also selected the package status as "imported".
- **"used by" number of entries**

  The user can specify in the dialog the maximum entries can be displayed in the "used by" column. The preset default value is 3. Correspondingly here, many paths to the root nodes (for example the brand of the equipment network or the knowledge base) of the released editorial objects, that use the respective editorial object, are given.
- **Location**

  The user can select a number of locations, to which the translations packages should be exported. All locations can be selected by the role of "translation coordinator". Therefore at least one location must be selected.
- **Target languages**

  The user can select a number of target languages, to which the translations packages should be exported. Therefore at least one target language should be selected.
- **Package status**

  The user can select a number of translation package statuses, to which the translations packages should be exported. Therefore at least one status should be selected.
- **Market name**

  The user can select one or more market names from a list, that has defined market names for the existing translation packages. To provide a better overview, the market designations can be filtered using a text field.

It may be found through the export parameter specification that no single matching translation package can be determined. If this is the case, an excel file will be exported which only contains the entered parameters in the data overview sheet. It is stated in the notification that no packages fitting the parameters could be identified.

<a id="figure.auftragsverwaltung.uebersetzung.excel.timeout"></a>

![Image: timeout message](images/timeout_meldung.jpg)

**Figure 168. Timeout Notification**

An Excel export may cause a timeout if there is a very large amount of data. It is important that this timeout does not end the Excel export, but rather no message is given to the user after the export ends.

You will however be informed of the timeout as seen in [Figure 168, “Timeout Notification”](6-4-11-excel-export-of-translation-packages.md#figure.auftragsverwaltung.uebersetzung.excel.timeout "Figure 168. Timeout Notification").

##### <a id="excel.exportergebnis"></a>6.4.11.2. Export Results

The export result is stored as a notification in the system and is only visible to you. Notifications can be seen in the task navigator and in the translation navigator.

You can receive the excel export through the corresponding notification and save it locally on your computer. If a notification is marked with reference to an Excel export, then the function is visible in the context menu and under File > **Save result**. After specifying the target directory and confirming the dialog, the export result is stored in the specified target directory. If you do not have any authoring rights in the selected directory, then saving will be canceled with an error message.

<a id="figure.auftragsverwaltung.uebersetzung.exceldatei1"></a>

![Image: Excel file overview table](images/ExcelExport_Uebersicht.jpg)

**Figure 169. Excel File Overview Table**

The first sheet of an Excel file can be seen in [Figure 169, “Excel File Overview Table”](6-4-11-excel-export-of-translation-packages.md#figure.auftragsverwaltung.uebersetzung.exceldatei1 "Figure 169. Excel File Overview Table"). All of the parameters specified by the user will be exported here. All fields from the unspecified, optional parameters will remain empty. The basic information about the identified translation packages is listed under the parameters. The following information will be exported by line for every translation package:

- **Package name:** Name of the translation package.
- **Target date:** the “planned end date” of the translation package, meaning when it will be expected back from GoCAT/DELS.
- **Package number:** The serial number of a package. It is counted separately per target language and location and is displayed at the end of the package name.
- **Location:** The responsible editorial location for the translation package.
- **Source language:** The source language of the translation package (ISO code display).
- **Target language:** The target language of the translation package (ISO code display).
- **Object quantity:** The amount of objects exported with the translation package.
- **File quantity:** The amount of files exported with the translation package.
- **Package creation date:** The date the translation package was created (specification is in "dd.MM.yyyy" format).
- **Created by:** The creator of the translation package (User ID information or "automatic").
- **Package status:** The current status of the translation package (for example, "exported" or "reset", etc.).
- **Import date:** The date the translation package was imported (specification in "dd.MM.yyyy HH:mm:ss" format). Is only set when packages have the "imported" package status.
- **Number of TRADOS matches (GoCAT only): 100%/context matches/repetitions.** How many words fall under the 100%/context/repetitions category in GoCAT?
- **Number of TRADOS matches: 99% - 95%.** How many words fall under the 99% - 95% category in GoCAT?
- **Number of TRADOS matches: 94% - 75%.**How many words in the package fall under the 94% - 75% category in GoCAT?
- **Number of TRADOS matches: 74% - 0%.**How many words in the package fall under the 74% - 0% category in GoCAT?

<a id="figure.auftragsverwaltung.uebersetzung.exceldatei2"></a>

![Image: Excel file package content sheet](images/ExcelExport_Paket.jpg)

**Figure 170. Excel File Package Content**

An example detail information sheet of the Excel export can be seen in [Figure 170, “Excel File Package Content”](6-4-11-excel-export-of-translation-packages.md#figure.auftragsverwaltung.uebersetzung.exceldatei2 "Figure 170. Excel File Package Content"). There is only one detail sheet for each export in the Excel file, which contains all objects from the exported translation packages. The following information (in the respective column) will be given for each object (in the respective line).

- **Package name:** Name of the translation package in which the object is contained.
- **Package number:** The serial number of the translation package in which the object is contained. It is counted separately per target language and location and is displayed at the end of the package name.
- **Brand:** The brand of the responsible editing location for the translation package in which the object is contained.
- **Location:** The responsible editing location for the translation package in which the object is contained.
- **Source language:** The source language of the translation package (ISO code display).
- **Target language:** The target language of the translation package (ISO code display).
- **Order header:** The order header of the editorial object.
- **Order step:** The order step of the editorial object.
- **System name:** system name of the editorial object (without the location code specification).
- **System name addition:** location code as an addition to the editorial object system name (e.g. "@00011"). The location code given here does not have any relation to the location responsible for the translation package.
- **Version-specific ID:** ID of the object version of the editorial object.
- **Version-independent ID:** Global ID of the editorial object which is valid over all versions.
- **Used by:** Path in the editorial system to the editorial object.
- **Type:** Object type for the editorial object, for example FCL\_MEASUREMENT\_TABLE.
- **Initial deployment date:** The date the editorial object was initially deployed (data is in "dd.MM.yyyy" format). Is only set if the editorial object is contained in a scheduled order context. This column remains empty for objects from AdHoc orders.
- **Package creation date:** The creation date of the translation package is contained in the object (given in the format "dd.MM.yyyy").
- **Import date:** The date the translation package was imported which contains the object (given in "dd.MM.yyyy HH:mm:ss" format). Is only set when packages have the "imported" package status.
- **Package status:** Status of the translation package in which the object is contained.
- **Translation status:** The current translation status of the editorial object version listed here for the specified target language.
- **Object version:** The display version of the editorial object.
- **Author:** The last author, who has edited the version of the editorial object listed here.
- **Market name:** The respective market name from the editorial object header is in this field.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="6-4-10-translation-disputes.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="6-4-translation.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-odis-creator-editing-process.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">6.4.10. Translation Disputes </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7. ODIS Creator Editing Process</td></tr></table>
