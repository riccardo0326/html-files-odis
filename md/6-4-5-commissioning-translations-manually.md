[ODIS Creator Help](odis-creator-help.md) > [6. ODIS Creator Order Management Process](6-odis-creator-order-management-process.md) > [6.4. Translation](6-4-translation.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">6.4.5. Commissioning Translations Manually</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="6-4-4-translation-requirements.md">Prev</a> </td><th align="center" width="60%">6.4. Translation</th><td align="right" width="20%"> <a accesskey="n" href="6-4-6-translation-jobs.md">Next</a></td></tr></table>

---

#### <a id="uebersetzung.manuell.beauftragen"></a>6.4.5. Commissioning Translations Manually

Translation coordinators can also define translation packages manually at any time. Select the translation objects that should be translated and define a translation package from that. Now enter a deadline when you would like the translation to be delivered and click the **Commission translation package** [button](2-2-general-definitions-and-glossaries.md#schaltflaeche) (see [Figure 147, “Translation Overview”](6-4-translation.md#figure.auftragsverwaltung.uebersetzung "Figure 147. Translation Overview")). A warning message will be given in the following scenarios:

- The selected deadline does not correlate to the expected initial deployment deadline of the editorial object.
- The selected deadline does not match the range of time needed for the translation [Section 6.4.1, “Define Translation Parameters”](6-4-1-define-translation-parameters.md "6.4.1. Define Translation Parameters").

The translation package is exported anyway after confirming the warning message. In this case, it is the translation coordinator's responsibility to ensure the translation packages are translated on time and imported into the ODIS Creator system.

The translation coordinator will be informed if clone languages are included when manually building packages.

<a id="figure.auftragsverwaltung.uebersetzung.clone"></a>

![Image: clone language translation note](images/uebrestzung_beauf_clone_hinweis.png)

**Figure 156. Clone Language Translation Note**

To optimize the timing when manually ordering translation packages, a dialog with a note that the package was created is displayed. The dialog gives the user the option to display the package that was just created in the navigator or to continue working with the current display. It may take longer to display the new package in the navigator. This can depend on the number of existing packages in the target language for the editing location.

<a id="figure.auftragsverwaltung.uebersetzung.jump"></a>

![Image: translation note for completed package](images/uebersetzung_beauf_jump_hinweis.png)

**Figure 157. Translation Note for Completed Package**

##### <a id="uebersetzung.export"></a>6.4.5.1. Exporting Translation Packages with Clone Languages

If the target language of the translation package is defined as a clone language in the location of the package, then the translation requests for all languages in the clone language group will be considered. The translation status for all requests that are considered will be set to “In translation”.

If one or more objects in the clone language are packaged manually, the requirements from the cloned language will be removed after the action is completed. On the other hand, if one or more objects in the cloned language are packaged manually, the package will be created in the clone language and the requirements will be removed from the clone language.

The languages in the clone language group that are valid at the time of the export will be stored in the translation package.

The clone language settings for the Wolfsburg location are considered for administrative translation packages.

##### <a id="uebersetzung.import"></a>6.4.5.2. Importing Translation Packages with Clone Languages

If cloned languages are included in imported translation packages, the imported texts in all of the cloned languages contained in the package will be used as the translation and their translation status will be changed to Completed (translated).

When importing using the expert function, the clone languages contained in the package are not considered.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="6-4-4-translation-requirements.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="6-4-translation.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="6-4-6-translation-jobs.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">6.4.4. Translation Requirements </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 6.4.6. Translation Jobs</td></tr></table>
