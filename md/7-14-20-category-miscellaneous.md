[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.14. Function Test Editor](7-14-function-test-editor.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.14.20. Category - Miscellaneous</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-14-19-category-flash.md">Prev</a> </td><th align="center" width="60%">7.14. Function Test Editor</th><td align="right" width="20%"> <a accesskey="n" href="7-14-21-properties-view.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige"></a>7.14.20. Category - Miscellaneous

The following action elements are in this category:

- [Section 7.14.20.1, “Action Element - Comment”](7-14-20-category-miscellaneous.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Kommentar "7.14.20.1. Action Element - Comment")
- [Section 7.14.20.2, “Action Element - JavaBox”](7-14-20-category-miscellaneous.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.JavaBox "7.14.20.2. Action Element - JavaBox")
- [Section 7.14.20.3, “Action Element - Documents”](7-14-20-category-miscellaneous.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Dokumente "7.14.20.3. Action Element - Documents")
- [Section 7.14.20.4, “Action Element - Sub-Program”](7-14-20-category-miscellaneous.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Aufruf_Testprozedur "7.14.20.4. Action Element - Sub-Program")
- [Section 7.14.20.5, “Action Element - Log”](7-14-20-category-miscellaneous.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Protokoll "7.14.20.5. Action Element - Log")

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Kommentar"></a>7.14.20.1. Action Element - Comment

The "Comment" action element can be seen in [Figure 526, “Comment Action Element”](7-14-20-category-miscellaneous.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Kommentar "Figure 526. Comment Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Kommentar"></a>

![Image: comment action element](images/fte_arbeitsflaeche_sonstige_kommentar.png)

**Figure 526. Comment Action Element**

A comment that is not displayed when the test runs can be added using this action element.

###### <a id="d4e27711"></a>7.14.20.1.1. Text

Please enter the comment text in the text field.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.JavaBox"></a>7.14.20.2. Action Element - JavaBox

The "JavaBox" action element can be seen in [Figure 527, “JavaBox Action Element”](7-14-20-category-miscellaneous.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.JavaBox "Figure 527. JavaBox Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.JavaBox"></a>

![Image: JavaBox action element](images/fte_arbeitsflaeche_sonstige_javabox.png)

**Figure 527. JavaBox Action Element**

This action element is used to add Java<a id="d4e27727"></a>Source code in the function test.

###### <a id="d4e27729"></a>7.14.20.2.1. Source Text

Please enter the Java source text in the text field. The source text is added to the test program process. Then please check the JavaBox using the "Compile function test" function.

###### <a id="d4e27732"></a>7.14.20.2.2. Java Box Action Element Validation

An additional test must be performed for Java box action elements (4-eye principle). In addition to the author, an authorized person (tester) must review each Java box (see [Section 5.8, “Java Box Test”](5-8-java-box-test.md "5.8. Java Box Test")).

This additional test is documented with the status, comments, test date, and tester in the properties window for the Java box action element.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.javabox_properties"></a>

![Image: Java box properties](images/javabox_eigenschaften_pruefer.png)

**Figure 528. Java Box Properties**

The “Comments” and “Tester” attributes are automatically removed when a Java box is accepted.

If a Java box is declined, the comment and tester information is listed in the “Issues” tab.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.javabox_problem"></a>

![Image: Java box issues tab](images/javabox_problem_pruefer.png)

**Figure 529. Java Box Issues Tab**

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Dokumente"></a>7.14.20.3. Action Element - Documents

The "Documents" action element can be seen in [Figure 530, “Documents Action Element”](7-14-20-category-miscellaneous.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Dokumente "Figure 530. Documents Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Dokumente"></a>

![Image: documents action element](images/fte_arbeitsflaeche_sonstige_dokumente_dialog.png)

**Figure 530. Documents Action Element**

Documents can be managed using the "Documents" action element. A document is defined by the document type and the name of the reference with which it is linked.

###### <a id="d4e27768"></a>7.14.20.3.1. Document type

Organizing the documents into groups based on their content. The document type set here is specified in "Reference".

###### <a id="d4e27771"></a>7.14.20.3.2. Reference Type

You can select from a list for the "Reference type". The following are available: EFA, external, indirect DO, and internal

###### <a id="d4e27774"></a>7.14.20.3.3. Reference

The required supplemental document is selected in this location. This is done using the tree structure in the editing selection. The document type is specified using this selection.

###### <a id="d4e27777"></a>7.14.20.3.4. Print

A document that should be printed out on paper at the tester can be specified here. The user can control the printing using the function "Force display", "Display", "Hide", "Force printing", and "Print".

###### <a id="d4e27780"></a>7.14.20.3.5. Placeholder

The placeholder field shows the number of available placeholders in the linked document.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Dokumente_Dialog"></a>

![Illustration: document dialog](images/fte_arbeitsflaeche_sonstige_dokumente_dialog.png)

**Figure 531. Document dialog**

  

The placeholders can only be defined for the “Internal” link type. The placeholder dialog can be opened using the input field in order to edit values for the placeholders. The placeholders are read out of the linked document.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Dokumente_Platzhalter_Dialog"></a>

![Illustration: placeholder dialog](images/fte_arbeitsflaeche_sonstige_dokumente_platzhalter_dialog.png)

**Figure 532. Placeholder Dialog**

  

Placeholders can have a defined format that defines the type and display type of the value for the respective placeholder.

The tooltip display the placeholders and their numbers.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Dokumente_Tooltip"></a>

![Illustration: placeholder tooltip](images/fte_arbeitsflaeche_sonstige_dokumente_tooltip.png)

**Figure 533. Placeholder Tooltip**

  

The consistency check is run against the last version of the supplementary document. The differences in the placeholder assignment are found and are displayed as notes in the Info level. The info notes do not prevent completion of an object. The differences are also shown in the FTE syntax check.

<a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Dokumente.PlatzhalterFormatierungen"></a>Any formatting differences from the function test editor will be interpreted during the test program runtime and transferred to the auxiliary document in HTML format. In this way, the font style, color, type, and size can affect the placeholders in the auxiliary document.

The following table shows the available formatting characters.

<a id="d4e27811"></a>

<table border="1" summary="Formatting Characters"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Symbol</th><th align="left">Effect</th></tr></thead><tbody><tr><td align="left">\A</td><td align="left">Bold font</td></tr><tr><td align="left">\I</td><td align="left">Italic font</td></tr><tr><td align="left">\U</td><td align="left">Underlined font</td></tr><tr><td align="left">\S</td><td align="left">Black font</td></tr><tr><td align="left">\B</td><td align="left">Blue font</td></tr><tr><td align="left">\R</td><td align="left">Red font</td></tr><tr><td align="left">\H</td><td align="left">Green font</td></tr><tr><td align="left">\L</td><td align="left">Arial font</td></tr><tr><td align="left">\C</td><td align="left">Courier font</td></tr><tr><td align="left">\K</td><td align="left">Lower case font</td></tr><tr><td align="left">\G</td><td align="left">Upper case font</td></tr><tr><td align="left">\N</td><td align="left">Reset the font</td></tr></tbody></table>

**Table 124. Formatting Characters**

###### <a id="d4e27857"></a>7.14.20.3.6. Display preview

This button can open the selected document as read-only in a preview dialog (see [Figure 534, “Preview Dialog”](7-14-20-category-miscellaneous.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Dokumente_vorschau "Figure 534. Preview Dialog")). To be able to open the preview, the following conditions must be met:

- Only one document was selected.
- The selected document has the "Internal" reference type.

If the conditions are not met, the button will be inactive.

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Dokumente_vorschau"></a>

![Image: preview dialog](images/fte_arbeitsflaeche_sonstige_dokumente_vorschau.png)

**Figure 534. Preview Dialog**

  

The "OK" button closes the preview dialog.

###### <a id="d4e27876"></a>7.14.20.3.7. Alternative: Adding with Drag and Drop

In addition to editing document action elements using the dialog, you can also add supplementary documents and diagnostic objects by dragging and dropping. To do this, select one or more objects from a navigation tree and pull them over onto the action element using the drag and drop function. The previously selected objects are added to the list of action element documents. The following presets apply for the values of an entry in the documents list:

<a id="d4e27879"></a>

<table border="1" summary="Default Values for Supplementary Documents"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Column</th><th align="left">Basic Setting</th></tr></thead><tbody><tr><td align="left">Document Type</td><td align="left">Determined based on the document type of the select supplementary document</td></tr><tr><td align="left">Reference Type</td><td align="left">Contains the value "internal"</td></tr><tr><td align="left">Reference</td><td align="left">System name for the selected supplementary document</td></tr><tr><td align="left">Print</td><td align="left">Contains the value "Display"</td></tr><tr><td align="left">Parameters</td><td align="left">Contains the value "0"</td></tr></tbody></table>

**Table 125. Default Values for Supplementary Documents**

  

<a id="d4e27904"></a>

<table border="1" summary="Default Values for Diagnostic Objects"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Column</th><th align="left">Basic Setting</th></tr></thead><tbody><tr><td align="left">Document Type</td><td align="left">Contains the value "Component description"</td></tr><tr><td align="left">Reference Type</td><td align="left">Contains the value "Indirect DO"</td></tr><tr><td align="left">Reference</td><td align="left">System name for the selected diagnostic object</td></tr><tr><td align="left">Print</td><td align="left">Contains the value "Display"</td></tr><tr><td align="left">Parameters</td><td align="left">Contains the value "0"</td></tr></tbody></table>

**Table 126. Default Values for Diagnostic Objects**

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Aufruf_Testprozedur"></a>7.14.20.4. Action Element - Sub-Program

The "Sub-program" action element can be seen in [Figure 535, “Sub-Program Action Element”](7-14-20-category-miscellaneous.md#figure.Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen.Aufruf2 "Figure 535. Sub-Program Action Element").

<a id="figure.Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen.Aufruf2"></a>

![Image: sub-program call](images/fte_arbeitsflaeche_sonstige_unterprogramm.png)

**Figure 535. Sub-Program Action Element**

A sub-program is called up for runtime using this action element.

Using the dialog screen is similar to what is described in [Section 7.14.5.3.1, “Sub-Program”](7-14-5-test-steps-view.md#Funktionstesteditor.Testschritte_View.Testschritte_Erzeugen.Aufruf "7.14.5.3.1. Sub-Program"). One specific differences is that this command can also call up test procedures in addition to general tests and function tests.

The sub-program status (such as OK and Selection) is read out after running the sub-program and assigned to the test step status. The action elements can then be checked to see if a sub-program ran successfully.

Not every type of function code can be used in every function code. The following table shows which function codes can be selected on the command page for a sub-program.

<a id="d4e27947"></a>

<table border="1" summary="Sub-Program Calls in Function Codes"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Source</th><th align="left">Objective</th></tr></thead><tbody><tr><td align="left">Function test</td><td align="left">Function test, general test, test procedure</td></tr><tr><td align="left">Traversal test</td><td align="left">General test, test procedure</td></tr><tr><td align="left">General test</td><td align="left">Function test, general test, test procedure</td></tr><tr><td align="left">Test Procedure</td><td align="left">Test Procedure</td></tr></tbody></table>

**Table 127. Sub-Program Calls in Function Codes**

When using an incorrect function test, a fatal error will be displayed in the problems view. It is then not possible to close the sub-program dialog or save the function code.

###### <a id="d4e27970"></a>7.14.20.4.1. Alternative: Adding with Drag and Drop

In addition to editing the subroutine action element via the dialog, you can add new function tests, general tests or test procedures by dragging and dropping them to an instruction connection or to an empty “Subroutine” action element. To do this, select one or more objects from a navigation tree of your choice and add them to the action element using drag and drop. Only the first selected object is added to the “Subprogram” action element. This inserts the previously selected object into the subprogram of the action element and the subprogram dialog opens automatically.

In the command view, subprogram calls can be changed or replaced by dragging and dropping the function tests, general tests or test procedures onto an existing “Subprogram” action element. To do this, select one or more objects from a navigation tree of your choice and move them using drag and drop. The sub-program dialog is opened automatically. The existing interface table is compared with the new interface tables and is updated:

- Identical variables/key words will remail as they were.
- Old variables/key words that are not in the new sub-program will be deleted.
- New variables/key words that are not in the old sub-program are added.

Drag and drop is not possible if a sub-program editor is already open.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Protokoll"></a>7.14.20.5. Action Element - Log

The "Log" action element can be seen in [Figure 536, “Log Action Element”](7-14-20-category-miscellaneous.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Protokoll "Figure 536. Log Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Protokoll"></a>

![Image: action element categories - miscellaneous.log](images/fte_arbeitsflaeche_sonstige_protokoll.png)

**Figure 536. Log Action Element**

This action element activates (**on (for loops: only first/last cycle)**), (**on (for loops: all cycles\* [according to the setting in the operating system])**) or deactivates (**off**) the inclusion of the diagnostic log in the standard process.

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Volt_Erkennung"></a>7.14.20.6. Action Element - 12V Detection

The action element “12V detection” can be seen in [Figure 537, “12V Detection Action Element”](7-14-20-category-miscellaneous.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Volt_Erkennung "Figure 537. 12V Detection Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Volt_Erkennung"></a>

![Figure: action element categories - Other.12volt-detection](images/fte_arbeitsflaeche_sonstige_12volt_erkennung.png)

**Figure 537. 12V Detection Action Element**

This command can be used to suppress the error message **"No vehicle connected"** during the **"12V detection"** check in the processing system. The radio button **"on"** switches the error message on and the radio button **“off"** switches it off.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-14-19-category-flash.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-14-function-test-editor.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-14-21-properties-view.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.14.19. Category - Flash </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.14.21. Properties (View)</td></tr></table>
