[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.14. Function Test Editor](7-14-function-test-editor.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.14.1. Introduction</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-14-function-test-editor.md">Prev</a> </td><th align="center" width="60%">7.14. Function Test Editor</th><td align="right" width="20%"> <a accesskey="n" href="7-14-2-menus-and-tool-bars.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Einleitung"></a>7.14.1. Introduction

With the function test editor (FTE), you can create, edit, and check function test modules, that are inserted for automatic identification of equipment, to execute functions in the OBD and for fault finding on the vehicle using the tester. Test modules are created in three steps in a graphic user interface:

1. Step: summarized display of the test module in the "test steps" area,
2. Step: analysis of every test step with its separate instructions in the "commands" area and
3. Step: parameterization of separate commands in dialogs.

All function tests are managed in the ODIS Creator editing system.

##### <a id="Funktionstesteditor.Einleitung.Kurzbeschreibung_der_Anwendung"></a>7.14.1.1. Brief description

The function test editor is a graphic editor. This serves to process function tests that are in an XML format. The function tests are transferred and compiled in the testing language. The Java Code created like this is then used by the processing system to conduct tests. In addition to the graphic desktop, on which the action elements are organized in test steps and can be edited through dialogs, FTE uses different views, see also [Figure 334, “Function Test Editor”](7-14-1-introduction.md#figure.Funktionstesteditor.Einleitung.Kurzbeschreibung_der_Anwendung "Figure 334. Function Test Editor"); these fulfill the following purpose:

- **Test steps:** display of test steps in a selected function test, creation, deletion and edit of new test steps, test selection or accessing sub-programs.
- **Properties:** display of all properties of a selected element in the function test.
- **XML:** display of the function tests saved in the XML.
- **Java code:** display of the function tests converted to the testing language (Java Code).
- **Problems:** display of problems occurred, for example, during programming
- **Break points:** activation or deactivation of break points inserted into test steps

The views can be hidden separately and be displayed again through the **View** menu item.

<a id="figure.Funktionstesteditor.Einleitung.Kurzbeschreibung_der_Anwendung"></a>

![Image: function test editor](images/fte_Funktionstesteditor.png)

**Figure 334. Function Test Editor**

The desktop serves to edit the separate test step contents of a function test: inserting action elements from the lineup; moving, deleting and editing action elements. The desktop is not one view in the proper sense, it cannot be hidden corresponding to that. Closing it will cause the function test to close. The **palette** is available as a separate view.

The status bar at the lower edge contains the current view and any additional information, similar to the current function test to be processed.

<a id="table.hinweis.fte.zahlen"></a>

<table border="1" summary="Note for Numbers in the Function Test Editor"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note:</strong></span> In contrast to other editing systems, th decimals in all numbers are separated by a period in FTE. Therefore, the numbers are not localized in FTE.</td></tr></tbody></table>

**Table 68. Note for Numbers in the Function Test Editor**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-14-function-test-editor.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-14-function-test-editor.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-14-2-menus-and-tool-bars.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.14. Function Test Editor </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.14.2. Menus and Tool Bars</td></tr></table>
