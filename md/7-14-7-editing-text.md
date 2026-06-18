[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.14. Function Test Editor](7-14-function-test-editor.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.14.7. Editing Text</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-14-6-using-variables.md">Prev</a> </td><th align="center" width="60%">7.14. Function Test Editor</th><td align="right" width="20%"> <a accesskey="n" href="7-14-8-use-switchkey-variables.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Allgemeine_Funktionalitaet.TexteBearbeiten"></a>7.14.7. Editing Text

The text editor is shown in [Figure 370, “Text Editor”](7-14-7-editing-text.md#figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Richtexteditor "Figure 370. Text Editor"). It is used in multiple command dialogs.

<a id="figure.Funktionstesteditor.Allgemeine_Funktionalitaet.Richtexteditor"></a>

![Image: text editor](images/fte_allgemein_richtexteditor.png)

**Figure 370. Text Editor**

<a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Standardbutton"></a>**Standard**

A default text can be added using the **Default** button. See also [Section 7.14.3.12, “Default Texts”](7-14-3-use-cases.md#Funktionstesteditor.Allgemeine_Funktionalitaet.Standardtexte "7.14.3.12. Default Texts").

<a id="Funktionstesteditor.Allgemeine_Funktionalitaet.Expandbutton"></a>**Expand**

References are triggered in expanded mode. This mode is activated and deactivated using the Expand button (see [Figure 371, “Expand Button”](7-14-7-editing-text.md#figure.Funktionstesteditor.Allgemeine_Funktionalitaet.RTE.Expand "Figure 371. Expand Button")). The expanded mode is like a preview of the content: the names of default and vehicle status texts are switched with their text content. The remaining content of the RTE is not touched. The text cannot be edited in expanded mode.

<a id="figure.Funktionstesteditor.Allgemeine_Funktionalitaet.RTE.Expand"></a>

![Image: expand button](images/fte_expand.png)

**Figure 371. Expand Button**

**Vehicle Status**

Vehicle statuses can be added using the button with the vehicle symbol.

**Variable**

Variables can be inserted using this button in the text field.

**Keyword**

Keywords can be inserted using the button in the text field.

**Text Field**

The text is created using the [rich text editor](7-1-16-creating-formatted-text.md "7.1.16. Creating Formatted Text").

<a id="richtextbezeichner"></a>Variables, keywords, and references to vehicle status texts and default texts can either be entered directly in the text field or inserted at the respective cursor position by using the buttons in the lower section. For number variables, you can set and specify the number of places before and after the decimal, if the values should be formatted with leading or subsequent zeros. Please note that the space behind these three special strings is not removed. If a special string is inserted manually, then a space must be inserted behind it.

<a id="richtextbezeichner.hinweis"></a>Note: there is a unique feature for texts with references. If you add only one separate reference to a vehicle status or default text and remove all other characters (including spaces and breaks), then this text is not relevant to translation. This function allows additional translation costs to be avoided.

<a id="d4e16176"></a>

%01.01myvariable, %1.1myvariable, %myvariable

**Example 1. Variable**

  

<a id="d4e16179"></a>

$mykeyword

**Example 2. Keyword**

  

<a id="d4e16182"></a>

@[std]question\_1\_TST\_ODIS\_variantrule\_3, @[srv]TAN

References are triggered in expanded mode. This mode is activated and deactivated using the Expand button (see [Figure 371, “Expand Button”](7-14-7-editing-text.md#figure.Funktionstesteditor.Allgemeine_Funktionalitaet.RTE.Expand "Figure 371. Expand Button")). The expanded mode is like a preview of the content: the names of default and vehicle status texts are switched with their text content. The remaining content of the RTE is not touched. The text cannot be edited in expanded mode.

**Example 3. References**

  

<a id="d4e16187"></a>

%string\_resp\_array[int\_ctr[0, index]]

The use of variables/arrays as an array index represents a special case. In this scenario, identifications with '%' are not allowed. The function to insert variables automatically detects if the cursor is located within array brackets, and will add the variable name without the percent sign. If inserting manually, you must make sure not to use percent signs. Information about places before and after the decimal as well as about leading and/or subsequent zeros is not permitted in indexes.

**Example 4. Special Case of Array Indexes**

  

Variables and default text links are checked for the correct formatting when saving. Only fully-formatted or unformatted variables and text links are permitted. For example, if a variable is formatted partially as "red” and partially as “blue", you will receive an error message and changes will not be saved.

<a id="figure.Funktionstesteditor.Allgemeine_Funktionalitaet.RTE.Validate"></a>

![Illustration: validating variables in the FTE](images/fte_var_validate.png)

**Figure 372. Validating Variables in the FTE**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-14-6-using-variables.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-14-function-test-editor.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-14-8-use-switchkey-variables.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.14.6. Using Variables </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.14.8. Use SwitchKey Variables</td></tr></table>
