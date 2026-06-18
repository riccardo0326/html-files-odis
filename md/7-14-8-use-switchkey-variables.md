[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.14. Function Test Editor](7-14-function-test-editor.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.14.8. Use SwitchKey Variables</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-14-7-editing-text.md">Prev</a> </td><th align="center" width="60%">7.14. Function Test Editor</th><td align="right" width="20%"> <a accesskey="n" href="7-14-9-desktop.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Allgemein.SwitchKey"></a>7.14.8. Use SwitchKey Variables

ODX control module answers can contain so-called MUX response parameters, that permit different response structures (cases) as response possibilities. However, exactly only one response structure (case) is returned from the control module in runtime.

In order to not analyze all case paths at the same time, the name of the case response parameter for runtime can be saved in a SwitchKey variable:

- First create an ASAM Ecukom with all input parameters to request the control module response.
- Then insert a response parameter with the path to the MUX response parameter (parent node above the case response parameters) in the ASAM Ecukom. Assign a SwitchKey variable to this MUX response parameter.
- Now insert an "expression" type switch instruction after the ASAM Ecukom. The SwitchKey variable is written in the expression field.
- You can now add switch cases for every MUX case under the switch instruction. The name of the case response parameter is inserted as a value in the case dialog. (Tip: to simplify the input of the MUX case name, you can use the button 'From ODX...'.)
- In every switch case, you can now analyze the response parameter under the MUX case with the ASAM result.

[Figure 373, “SwitchKey Example”](7-14-8-use-switchkey-variables.md#figure.Funktionstesteditor.Allgemeine_Funktionalitaet.SwitchKey.Beispiel "Figure 373. SwitchKey Example") shows an example for a process to analyze MUX case response structures with a SwitchKey variable.

<a id="figure.Funktionstesteditor.Allgemeine_Funktionalitaet.SwitchKey.Beispiel"></a>

![Image: SwitchKey example](images/fte_allgemein_switchkey_beispiel.png)

**Figure 373. SwitchKey Example**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-14-7-editing-text.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-14-function-test-editor.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-14-9-desktop.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.14.7. Editing Text </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.14.9. Desktop</td></tr></table>
