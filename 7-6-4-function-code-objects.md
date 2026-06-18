[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.6. Function Library](7-6-function-library.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.6.4. Function Code Objects</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-6-3-creating-and-changing-default-measurements.md">Prev</a> </td><th align="center" width="60%">7.6. Function Library</th><td align="right" width="20%"> <a accesskey="n" href="7-7-control-module-tree.md">Next</a></td></tr></table>

---

#### <a id="funktionscode"></a>7.6.4. Function Code Objects

Function code objects is the general term for objects that describe a function process. [Function tests](7-6-4-function-code-objects.md#funktionscode.funktionstest "7.6.4.3. Creating and Changing a Function Test"), [general tests](7-6-4-function-code-objects.md#funktionscode.generellertest "7.6.4.5. Creating and Changing General Tests") and [traversal tests](7-6-4-function-code-objects.md#funktionscode.traversierungstest "7.6.4.4. Creating and Changing a Traversal Test") are associated with this group of objects. The actual content in these objects is edited using the function test editor (see [Section 7.14, “Function Test Editor”](7-14-function-test-editor.md "7.14. Function Test Editor")).

Function code objects can, like all objects in the function library, be created directly below the respective group node in the function library or parallel to the already existing objects. Simply select the corresponding object and select **New subnode >> ...test** or **New parallel node >> ...test** in the context menu.

##### <a id="funktionscode.funktiontesteditor.oeffnen"></a>7.6.4.1. Opening the Function Test Editor

After opening the function code object, you can select the entry **test sequence** through the context menu in the editor. With that, the content of the function code object is opened for editing in the [function test editor](7-14-function-test-editor.md "7.14. Function Test Editor"). If a function code object is opened in “read-only mode,” the background (instruction and test step page) is shown in gray. The background is shown in white in "edit mode.”

To replace content with new content, the entry **Replace content** is available in the context menu. You can then select the corresponding content file in the dialog.

<a id="table.hinweis.fkb.inhaltersetzen"></a>

<table border="1" summary='Note for the "Replace Content" Function'><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note: </strong></span>it is checked when replacing the content of a function code, if 1. the schema version of the FTE file matches that of the XML file and if 2. the new content file is compatible with the schema <span class="emphasis"><em>VAUDES_Funktionstest.xsd</em></span> (VAUDES_Function_test.xsd) and with the schema version. Content can only be successfully replaced if both tests are successful.</td></tr></tbody></table>

**Table 59. Note for the "Replace Content" Function**

If you want to use function code content with an outdated schema version, you have to adjust the original function code relevant to translation, and save it. The old schema version is updated to the newest version when it is saved. Then you can use the function code content in another one.

If the function code object still has no content, because, for example, it was just created by you, then you will be notified of this through an additional query and you can open the [function test editor](7-14-function-test-editor.md "7.14. Function Test Editor") with no content. As an alternative to the context menu, these functions are also available in the menu under **Extras >> Editor menu**.

##### <a id="funktionscode.eindeutigesystemnamen"></a>7.6.4.2. Unique System Name for Function Tests

System names of all four function test types ([function tests](7-6-4-function-code-objects.md#funktionscode.funktionstest "7.6.4.3. Creating and Changing a Function Test"), [general tests](7-6-4-function-code-objects.md#funktionscode.generellertest "7.6.4.5. Creating and Changing General Tests"), [traversal tests](7-6-4-function-code-objects.md#funktionscode.traversierungstest "7.6.4.4. Creating and Changing a Traversal Test") and [test procedures](7-6-1-creating-and-changing-test-procedures.md "7.6.1. Creating and Changing Test Procedures")) must be clear throughout the system. The background for this is that the processing system does not assume a difference in test types and therefore, can push ambiguous system names to problems during processing. Therefore, the consistency check checks the system names for uniqueness.

The function code system name may only consist of the character set "\_0123456789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ". The function code may only begin with a letter or an underscore.

##### <a id="funktionscode.funktionstest"></a>7.6.4.3. Creating and Changing a Function Test<a id="d4e13480"></a>

To create a new function test in the context of a knowledge base or a diagnostic object, select **New subnode > Function test** or **New parallel node > Function test** in the knowledge base navigator context menu.

##### <a id="funktionscode.traversierungstest"></a>7.6.4.4. Creating and Changing a Traversal Test<a id="d4e13487"></a>

The purpose of traversal tests is for the control module identification. They are tied to a control module in the equipment network. It is determined if this control module is also available. To create a new traversal test in the context of equipment network objects, select **New subnode > Traversal test** or **New parallel node > Traversal test** in the equipment network navigator context menu.

##### <a id="funktionscode.generellertest"></a>7.6.4.5. Creating and Changing General Tests<a id="d4e13494"></a>

The purpose of general tests is to describe frequently recurring functions. These descriptions are stored there and can be opened from function tests and traversal tests as a subprogram if necessary. They can consist of multiple test steps. To create a new general test, select **New subnode > General test** or **New parallel node> General test** in the function library navigator context menu. Alternatively, a new general test can also be created through the action element subprogram (see [Section 7.14.20.4, “Action Element - Sub-Program”](7-14-20-category-miscellaneous.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Aufruf_Testprozedur "7.14.20.4. Action Element - Sub-Program")) in the function test editor.

##### <a id="funktionscode.remoterepair"></a>7.6.4.6. Remote Repair<a id="d4e13502"></a>

In the function test object, there is the option to set parameters for Remote Repair. The “Remote Repair” checkbox can be activated to do this. Once the checkbox is activated, additional input fields and tables in the Editor are displayed, as shown in [Figure 268, “Function Library Navigation Tree”](7-6-4-function-code-objects.md#figure.redaktion.funktionscode.remoterepair "Figure 268. Function Library Navigation Tree"). Parameters can be set for them. After saving and checking in, the data is transferred and will be available the next time it is opened (read or write).

Because this information is not relevant for everyone, this area can be hidden when the checkbox is activated by changing the layout settings (refer to [Section 9.1.2, “Layout Settings”](9-1-2-layout-settings.md "9.1.2. Layout Settings")). If the checkbox is deactivated, the Remote Repair area will be hidden. The data will be kept for the time being if the checkbox is unintentionally deactivated. The data will be displayed again if the checkbox is activated again. When the object is saved temporarily or permanently, the data in the Remote Repair area will be deleted.

<a id="figure.redaktion.funktionscode.remoterepair"></a>

![Image: Remote Repair area](images/RedaktionFunktionstestRemoteRepair.png)

**Figure 268. Function Library Navigation Tree**

  

The following parameters are available in the Remote Repair area and can be adjusted:

<a id="d4e13516"></a>

<table border="1" summary="Remote Repair Parameters"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Name</th><th align="left">Explanation</th></tr></thead><tbody valign="top"><tr><td align="left" valign="top">Script name</td><td align="left" valign="top">The name of the script to be run is entered here. It is a required field where free text can be entered.</td></tr><tr><td align="left" valign="top">Job ID</td><td align="left" valign="top">The ID of the script to be run is entered here as free text.</td></tr><tr><td align="left" valign="top">Runtime in seconds</td><td align="left" valign="top">This is the expected time that the script will need to run. Only numbers are permitted. Using other errors will cause a validation error.</td></tr><tr><td align="left" valign="top">Access parameter</td><td align="left" valign="top">The access parameters for the script can be specified here. One name and the type of access parameter can be entered in each line. Both fields are free text fields. The values are assigned using the “used” table of the diagnostic object that the function test uses.</td></tr><tr><td align="left" valign="top">Requirements</td><td align="left" valign="top">Requirements for running the script can be specified here. The requirements must be defined first in Administration (refer to <a class="xref" href="5-2-1-group-data.md" title="5.2.1. Group Data">Section 5.2.1, “Group Data”</a>) and are then available as a selection field. In the Requirements field, a condition is selected and the number is then set automatically.</td></tr><tr><td align="left" valign="top">Description</td><td align="left" valign="top">Descriptions for the script can be specified here. Texts from the text library, free text, or a combination of both can be used here. If free text is used, a translation will be initiated after release or completion.</td></tr><tr><td align="left" valign="top">Follow-up activities OK</td><td align="left" valign="top">Follow-up activities for the script can be specified here if the execution is successful. Texts from the text library, free text, or a combination of both can be used here. If free text is used, a translation will be initiated after release or completion.</td></tr><tr><td align="left" valign="top">Follow-up activities not OK</td><td align="left" valign="top">Follow-up activities for the script can be specified here if the execution is not successful. Texts from the text library, free text, or a combination of both can be used here. If free text is used, a translation will be initiated after release or completion.</td></tr><tr><td align="left" valign="top">Safety precautions</td><td align="left" valign="top">Safety precautions for the script can be specified here. They must be followed when running the script. Texts from the text library, free text, or a combination of both can be used here. If free text is used, a translation will be initiated after release or completion.</td></tr><tr><td align="left" valign="top">Target systems</td><td align="left" valign="top">Target systems on which the scripts can be run can be specified here. The target systems must be defined first in Administration (refer to <a class="xref" href="5-2-1-group-data.md" title="5.2.1. Group Data">Section 5.2.1, “Group Data”</a>) and are then available through a selection field.</td></tr></tbody></table>

**Table 60. Remote Repair Parameters**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-6-3-creating-and-changing-default-measurements.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-6-function-library.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-7-control-module-tree.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.6.3. Creating and Changing Default Measurements </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.7. Control Module Tree</td></tr></table>
