[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.7. Control Module Tree](7-7-control-module-tree.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.7.9. Control Module Version Groups</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-7-8-using-control-module-descriptions.md">Prev</a> </td><th align="center" width="60%">7.7. Control Module Tree</th><td align="right" width="20%"> <a accesskey="n" href="7-7-10-error-types.md">Next</a></td></tr></table>

---

#### <a id="sgbaum.sgvariantengruppe"></a>7.7.9. Control Module Version Groups

##### <a id="sgbaum.sgvariantengruppe.anlage"></a>7.7.9.1. Creating a Control Module Version Group

Control module version groups are treated the same as a standard editorial object. It is created by an author within an order context under the base version. The system name receives the prefix **"Group\_"** by default before the name of the base version. You can change this. There are no other required fields besides the version comments. The control modules version group is to make sure that all DTC memories of a control module version are referenced in one or more sections of a diagnostic object.

<a id="figure.sg-baum.sgvargruppe"></a>

![Image: control module version group while editing](images/sg_vargruppe_undefiniert.png)

**Figure 275. Control Module Version Group while Editing**

To be able to make a comparison between the use of fault locations in a knowledge base and the fault locations of control module versions, you must first collect them. To do this, you can drag the control module versions and the diagnostic objects per drag and drop to a control module version group. The DTC memories that are assigned to the control module versions will be automatically transferred with. The outcome of these operations can be seen under [Figure 275, “Control Module Version Group while Editing”](7-7-9-control-module-version-groups.md#figure.sg-baum.sgvargruppe "Figure 275. Control Module Version Group while Editing").

##### <a id="sgbaum.sgvariantengruppe.anwendung"></a>7.7.9.2. Application of a Control Module Version Group

An analysis is performed after the release of the control module version group. All diagnostic objects given within a control module version group and their subordinate diagnostic objects are searched for fault locations from the control module versions that are included in their suspicion rules. The results are portrayed with colored markings, which can also be seen in [Figure 276, “Control Module Version Group After the Analysis”](7-7-9-control-module-version-groups.md#figure.sg-baum.sgvargruppe.analyse "Figure 276. Control Module Version Group After the Analysis"). Fault locations without a fill color are used by at least one diagnostic object. Fault locations with a red fill color are not used by any diagnostic objects. Fault locations with a blue fill color were marked by an author as intentionally not linked.

<a id="figure.sg-baum.sgvargruppe.analyse"></a>

![Image: control module version group after the analysis](images/sg_vargruppe_definiert.png)

**Figure 276. Control Module Version Group After the Analysis**

You can provide a comment for each linked fault location. The comments can be viewed in the “Used” table in the editor of the control unit for the variant group. The dialog for editing the comment is displayed when you select the fault location in the navigator below the control unit for the variant group, and then select the value **“Edit comment”** in the context menu. If only one fault location is selected, the existing comment is displayed in the dialog for revision. If multiple selections are made, an empty comment field is always displayed after opening the dialog, regardless of whether any comments have previously been entered.

<a id="figure.sg-baum.sgvargruppe.kommentar"></a>

![Image: editing the context menu at the fault location for comment](images/sg_vargruppe_kommentar.png)

**Figure 277. Editing the Context Menu at Fault Location For Comment**

You can set the mark **“intentionally not linked”** if you select the fault location in the navigator under the control module version group and then select the value **“intentionally not linked”** in the context menu. This is shown in [Figure 278, “Context Menu at Fault Location for Intentionally Not Linked”](7-7-9-control-module-version-groups.md#figure.sg-baum.sgvargruppe.nicht.verlinkt "Figure 278. Context Menu at Fault Location for Intentionally Not Linked"). When setting the status, there is the option to write a comment (see [Figure 279, “Comment Dialog for Intentionally Not Linked Action”](7-7-9-control-module-version-groups.md#figure.sg-baum.sgvargruppe.nicht.verlinkt.kommentar "Figure 279. Comment Dialog for Intentionally Not Linked Action")). If you insert a comment and confirm the dialog by clicking “OK”, the comment is applied to all selected relationships. This overwrites any previously inserted comments. If you confirm the dialog by clicking “Status change only”, only the status is updated and the comments remain as before.

<a id="figure.sg-baum.sgvargruppe.nicht.verlinkt"></a>

![Image: context menu at fault location for intentionally not linked](images/sg_vargruppe_nicht_verlinkt.png)

**Figure 278. Context Menu at Fault Location for Intentionally Not Linked**

<a id="figure.sg-baum.sgvargruppe.nicht.verlinkt.kommentar"></a>

![Figure: comment dialog for intentionally not linked action](images/sg_vargruppe_nicht_verlinkt_kommentar.png)

**Figure 279. Comment Dialog for Intentionally Not Linked Action**

Since the background job for the analysis of the fault location usage may run into an error, you also have the option to start the test process actively. To do this, select the value **usage calculation** in the context menu in the navigator on the control module version group, as seen in [Figure 280, “Context Menu at the Control Module Version Group to Initiate the Analysis of Fault Location Usage”](7-7-9-control-module-version-groups.md#figure.sg-baum.sgvargruppe.ermitteln "Figure 280. Context Menu at the Control Module Version Group to Initiate the Analysis of Fault Location Usage").

<a id="figure.sg-baum.sgvargruppe.ermitteln"></a>

![Image: context menu on the control module version group to initiate the analysis of fault location usage](images/sg_vargruppe_ermitteln.png)

**Figure 280. Context Menu at the Control Module Version Group to Initiate the Analysis of Fault Location Usage**

##### <a id="sgbaum.sgvariantengruppe.ueberpruefen"></a>7.7.9.3. Checking Fault Location Usage

###### <a id="sgbaum.sgvariantengruppe.ueberpruefen.dialog"></a>7.7.9.3.1. Dialog for the Usage Status of Fault Locations

In the main menu under **File > Check DTC usage**, you have the option to search for the fault location usage independent of the navigator (see [Figure 281, “Menu for Checking Fault Location Usage”](7-7-9-control-module-version-groups.md#figure.sg-baum.sgvargruppe.verwendung.menu "Figure 281. Menu for Checking Fault Location Usage")).

<a id="figure.sg-baum.sgvargruppe.verwendung.menu"></a>

![Image: menu for checking fault location usage](images/dtc_verwendungen.png)

**Figure 281. Menu for Checking Fault Location Usage**

In the dialog for checking fault location usage, you have the option to select through vehicle projects (see [Figure 282, “Dialog for Fault Location Usage based on a Vehicle Project”](7-7-9-control-module-version-groups.md#figure.sg-baum.sgvargruppe.verwendung.fzp "Figure 282. Dialog for Fault Location Usage based on a Vehicle Project")) and/or base control modules (see [Figure 283, “Dialog for Fault Location Usage based on a Base Control Module”](7-7-9-control-module-version-groups.md#figure.sg-baum.sgvargruppe.verwendung.sg "Figure 283. Dialog for Fault Location Usage based on a Base Control Module")). You must perform one of the two selection options. You can set the status in the other selection field. You will initiate the search by pressing the **Display** button. By double clicking on a line in the results, you can jump directly to the corresponding location in the control module navigator.

<a id="figure.sg-baum.sgvargruppe.verwendung.fzp"></a>

![Image: menu for checking fault location usage](images/dtc_verwendungsstatus_fzp.png)

**Figure 282. Dialog for Fault Location Usage based on a Vehicle Project**

<a id="figure.sg-baum.sgvargruppe.verwendung.sg"></a>

![Image: menu for checking fault location usage](images/dtc_verwendungsstatus_sg.png)

**Figure 283. Dialog for Fault Location Usage based on a Base Control Module**

###### <a id="sgbaum.sgvariantengruppe.ueberpruefen.excel"></a>7.7.9.3.2. Excel Export for Fault Location Usage Status

You can export the current display for Excel with the button **Export** from [Figure 282, “Dialog for Fault Location Usage based on a Vehicle Project”](7-7-9-control-module-version-groups.md#figure.sg-baum.sgvargruppe.verwendung.fzp "Figure 282. Dialog for Fault Location Usage based on a Vehicle Project"). The export runs in the background and the dialog from [Figure 284, “Completion Message for the Excel Export of the Usage Status”](7-7-9-control-module-version-groups.md#figure.sg-baum.sgvariantengruppe.ueberpruefen.excel.fertig "Figure 284. Completion Message for the Excel Export of the Usage Status") will notify you when it has ended. You will find the results in your notifications in the task navigator (see [Figure 285, “Notification for the Excel Export of the Usage Status”](7-7-9-control-module-version-groups.md#figure.sg-baum.sgvariantengruppe.ueberpruefen.excel.benachrichtigung "Figure 285. Notification for the Excel Export of the Usage Status")). Here you can download it using the entry **Save results** from the context menu.

<a id="figure.sg-baum.sgvariantengruppe.ueberpruefen.excel.fertig"></a>

![Image: completion message for the usage status Excel export](images/dtc_excel_export_fertig.png)

**Figure 284. Completion Message for the Excel Export of the Usage Status**

<a id="figure.sg-baum.sgvariantengruppe.ueberpruefen.excel.benachrichtigung"></a>

![Image: notification for the usage status Excel export](images/dtc_excel_export_benachrichtigung.png)

**Figure 285. Notification for the Excel Export of the Usage Status**

The Excel export, as seen in [Figure 286, “Excel Export of Usage Status”](7-7-9-control-module-version-groups.md#figure.sg-baum.sgvariantengruppe.ueberpruefen.excel "Figure 286. Excel Export of Usage Status"), also contains the fault location and the IDs of objects in separate columns, in addition to the information from the dialog. You will find information about the selected content at the top.

<a id="figure.sg-baum.sgvariantengruppe.ueberpruefen.excel"></a>

![Image: Excel export of usage status](images/dtc_excel_darstellung.png)

**Figure 286. Excel Export of Usage Status**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-7-8-using-control-module-descriptions.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-7-control-module-tree.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-7-10-error-types.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.7.8. Using Control Module Descriptions </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.7.10. Error Types</td></tr></table>
