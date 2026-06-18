[ODIS Creator Help](odis-creator-help.md) > [6. ODIS Creator Order Management Process](6-odis-creator-order-management-process.md) > [6.4. Translation](6-4-translation.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">6.4.10. Translation Disputes</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="6-4-9-expert-functions-for-translation-management.md">Prev</a> </td><th align="center" width="60%">6.4. Translation</th><td align="right" width="20%"> <a accesskey="n" href="6-4-11-excel-export-of-translation-packages.md">Next</a></td></tr></table>

---

#### <a id="uebersetzung.reklamation"></a>6.4.10. Translation Disputes

A complaint in DELS or GOCAT can be started in the editing view (see [Section 7.1.14, “Editorial Object Complaints”](7-1-14-editorial-object-complaints.md "7.1.14. Editorial Object Complaints")) or in the text library view (see [Section 5.6.3.8, “Make a Text ID Complaint”](5-6-3-text-id.md#textbib.reklamation "5.6.3.8. Make a Text ID Complaint")). Complaint packages are created the same way as manually defined translation packages. A complaint package however only includes the selected object. The target date for the complaint package is determined based on the currently set order context.

Only objects that have already been translated with DELS can be complained about using DELS, and objects that have been translated with GOCAT can only be complained about with GOCAT.

Since more than one editorial object can be in a translation package, it is also possible to create more than one complaint package for an initial translation package. These complaint packages can exist simultaneously. Every complaint package contains only one editorial object respectively and has a unique number in the complaint counter.

If no initial translation package can be determined for a manual complaint, then translation requests are created. These translation requirements, as all other requirements, are listed in the translation management (see [Section 6.4.4, “Translation Requirements”](6-4-4-translation-requirements.md "6.4.4. Translation Requirements")). These translation requirements are packaged via the standard mechanism for translation packages. With this, the attached files and the complaint comments are not included in the translation package. The translation package created in this way does not have a special complaint package name and the complaint counter has a value of "0". GOCAT does not have an option to detect if one or more of the objects within a translation package deals with complaints.

<a id="table.hinweis.reklamation.farsi"></a>

<table border="1" summary="Note: Complaint of Translations in Farsi"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top">Due to the certain structure of the <span class="bold"><strong>fa-IR Farsi</strong></span> language, it is explicitly filtered out in the data language selection. Because Farsi cannot be selected as a data language, it is not possible to make complaints of translation packages in the Farsi language. However, translation packages in Farsi can be manually generated and imported in expert mode.</td></tr></tbody></table>

**Table 37. Note: Complaint of Translations in Farsi**

##### <a id="d4e5371"></a>6.4.10.1. Disputes for Translations with Clone Languages

If there is a dispute about a translation that has a clone language defined, the behavior may differ depending on the settings. If there are disputes about one or more objects, there may be a different result depending on the settings for the clone language and packages.

If a clone language is defined when there is a manual dispute regarding a cloned package, but there is no package available for the clone language, the translation requests for the cloned language will be created. These translation requests are listed in the translation management, as all other requests are.

If a clone language is defined for a target language and there is a package for the clone language, then a dispute package will only be created in the clone language if there is a dispute regarding the target language (cloned language) or the clone language.

The table that follows shows the various actions.

In the example, the clone language is “en\_US” and the language to be disputed is always “en\_GB”.

<a id="table.auftragsverwaltung.uebersetzung.reklamation"></a>

<table border="1" summary="Example of Translation Disputes with and without a Clone Language"><colgroup><col align="center"/><col align="center"/><col align="center"/><col align="center"/></colgroup><thead><tr><th align="center">Paket1</th><th align="center">Paket2</th><th align="center">Clone language defined</th><th align="center">Result</th></tr></thead><tbody valign="top"><tr><td align="center" valign="top">en_GB</td><td align="center" valign="top"> </td><td align="center" valign="top">No</td><td align="center" valign="top">en_GB</td></tr><tr><td align="center" valign="top">en_GB</td><td align="center" valign="top"> </td><td align="center" valign="top">Yes</td><td align="center" valign="top">en_GB requirement</td></tr><tr><td align="center" valign="top">en_GB</td><td align="center" valign="top">en_US</td><td align="center" valign="top">No</td><td align="center" valign="top">en_GB</td></tr><tr><td align="center" valign="top">en_GB</td><td align="center" valign="top">en_US</td><td align="center" valign="top">Yes</td><td align="center" valign="top">en_US</td></tr><tr><td align="center" valign="top">en_US</td><td align="center" valign="top"> </td><td align="center" valign="top">No</td><td align="center" valign="top">en_GB requirement</td></tr><tr><td align="center" valign="top">en_US</td><td align="center" valign="top"> </td><td align="center" valign="top">Yes</td><td align="center" valign="top">en_US</td></tr><tr><td align="center" valign="top">en_US</td><td align="center" valign="top">en_GB</td><td align="center" valign="top">No</td><td align="center" valign="top">en_GB</td></tr><tr><td align="center" valign="top">en_US</td><td align="center" valign="top">en_GB</td><td align="center" valign="top">Yes</td><td align="center" valign="top">en_US</td></tr></tbody></table>

**Table 38. Example of Translation Disputes with and without a Clone Language**

##### <a id="d4e5435"></a>6.4.10.2. Automatic Complaint During the Import

Various checks are run on the translation package to be imported during the import process. If one of these checks fails, then the translation package will be declined and stored in the error folder. If a translation package suitable for the current import object is determined in the ODIS Creator system and one of the checks fails, then the corresponding translation package will be stored in the ODIS Creator system with the "OC import error" status. An automatic complaint is initiated for this translation package status.

Automatic complaint means that the translation package is stored under a new name as a complaint package in the "export folder". The new name follows the format of other translation packages with the addition of "\_R<complaint counter>\_<orderNo.>" instead of the package number. All parameters, especially the deadline of a complaint package are identical to the original package. Only the complaint counter will increase by one, the cause of the malfunction in the metadata is stored and the last change date is set to the current time stamp. The "last change date" is used for the complaint date display.

The automatic complaint works exclusively on the existing object in the database. No unique, new object will be created for this. Conditional on the status "OC import error", the representation of the translation package changes in the translation view.

When a complaint automatically occurs for faulty imports, the location administrator and group administrator teams will receive a notification with the reason for rejection. In the properties window for translation packages with the status "OC import error", there is the entry "reason" and "complaint date". The reason message will be displayed as a value, that is also written in the "error.xml" file. If multiple entries are in the error file, then only the first entry will be displayed here.

For the "complaint date" field, the time of the last failed attempt to import this package is displayed.

##### <a id="d4e5442"></a>6.4.10.3. Importing Complaint Packages

There is no difference between complaint packages and normal translation packages when importing the translation packages. The processing is exactly the same in both cases.

When importing translation packages to the ODIS Creator system, the handling of packages with the "OC import error" status is identical to the handling when the status is "exported" or "in translation". This means the text information contained in the answer package is transferred to the ODIS Creator system after the corresponding checks. Transferring text information overwrites any previously imported text information for the corresponding objects in the respective target language. Since objects are always disputed as a "whole" (for example, function tests or supplemental documents), then the results will also be valued as a "whole" when importing. This means that any previously translated text information for these objects will also be overwritten with the actual delivered texts during the import.

The translation package will be given the "Imported" status at the end, when everything was processed correctly. If an error occurs, then the relative status will be given to the error.

From version OC-22.1.0 and higher the behavior is as follows: after successfully importing packages for complaints that were generated automatically, the corresponding initial translation packages will be set to the “Imported” status (instead of “OC import error”).

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="6-4-9-expert-functions-for-translation-management.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="6-4-translation.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="6-4-11-excel-export-of-translation-packages.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">6.4.9. Expert Functions for Translation Management </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 6.4.11. Excel Export of Translation Packages</td></tr></table>
