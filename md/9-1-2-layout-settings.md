[ODIS Creator Help](odis-creator-help.md) > [9. ODIS Creator Configuration](9-odis-creator-configuration.md) > [9.1. Settings](9-1-settings.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">9.1.2. Layout Settings</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="9-1-1-settings-default-value-for-the-maximum-wait-time.md">Prev</a> </td><th align="center" width="60%">9.1. Settings</th><td align="right" width="20%"> <a accesskey="n" href="9-2-collect-program-logs.md">Next</a></td></tr></table>

---

#### <a id="konfiguration.benutzervorgaben.layout"></a>9.1.2. Layout Settings

It is explained in the following section, which adjustments you are able to make to the layout and also what the limitations are. These adjustments can be made for the following editors:

- Ad hoc order header
- Adhoc order step
- Scheduled order header
- Scheduled order step
- Brand
- Vehicle type
- Model year
- Version
- Motor
- XOR Nodes
- Control Module Configuration
- Equipment without diagnostic interface
- Knowledge base
- Diagnostic Object
- Function test
- General test
- Measured Values Table
- Test Procedure
- Traversal test
- Default measurement
- Base control module
- Control module group for KWP and UDS
- Control module versions for KWP and UDS
- Functional control module group
- Control Module Version Groups
- Fault location
- Vehicle project
- Supplemental document
- XML Template
- Brand variable

Under settings, you can apply the following settings to the layout; these are saved specifically to the user.

- Showing and hiding attributes
- Changing the sequence of attributes
- Adjusting text fields
- Adjusting tables (directly in the editor)

##### <a id="d4e34762"></a>9.1.2.1. Layout Settings for the Object Editor

In [Figure 640, “Object Editor in Settings”](9-1-2-layout-settings.md#figure.config.benutzervorgaben.objekteditor "Figure 640. Object Editor in Settings"), you will see the editor for adjusting an object editor, for example, the editor of a knowledge base from editing. First select the editor, which you would like to change, in the selection field. Then you can show or hide the desired attributes with the option fields and set the sequence of attributes with the arrow buttons in the editor. As soon as you press the **Apply** button or switch the selection to another editor, the settings will be saved and immediately applied.

<a id="figure.config.benutzervorgaben.objekteditor"></a>

![Object Editor in Settings](images/objekteditor_benutzervorgaben.png)

**Figure 640. Object Editor in Settings**

You also have the option to reset the performed layout settings to the original condition. To do this, select the button **Reset all settings** or **Reset object type**.

**Reset all settings** causes all layout settings for all object editors to be reset. The option **Reset object type** only resets the settings of the selected object editor. This reset will not affect the settings for line height of the text fields, which is set in a separate tab in settings.

<a id="figure.config.benutzervorgaben.objekteditor.beispiel"></a>

![Knowledge Base Editor After Adjustments](images/objekteditor_benutzervorgaben.beispiel.jpg)

**Figure 641. Knowledge Base Editor After Adjustments**

In [Figure 641, “Knowledge Base Editor After Adjustments”](9-1-2-layout-settings.md#figure.config.benutzervorgaben.objekteditor.beispiel "Figure 641. Knowledge Base Editor After Adjustments"), you can see the knowledge base editor with a user-defined layout.

##### <a id="d4e34791"></a>9.1.2.2. Adjusting Text Fields

In the settings editor (see [Figure 642, “Text Field Editor in Settings”](9-1-2-layout-settings.md#figure.config.benutzervorgaben.textfeldeditor "Figure 642. Text Field Editor in Settings")), you can specify the desired line height or increase/decrease it with the buttons.

<a id="figure.config.benutzervorgaben.textfeldeditor"></a>

![Text Field Editor in Settings](images/textfeldeditor_benutzervorgaben.png)

**Figure 642. Text Field Editor in Settings**

The text fields have a minimum of 2 and a maximum of 40 lines. Three lines are set by default. The following text fields can be configured:

- Version comment
- Comment
- Tester description

##### <a id="d4e34812"></a>9.1.2.3. Adjusting Tables

Tables can be adjusted directly in the editor. The changes are then saved with the layout settings. Then the settings will be restored the next time it is started.

The following adjustments can be made for tables:

- **Table height adjustment:** you can adjust the table height separately using the buttons in every table. The number of lines per table is a minimum of one line and a maximum of 50 lines.
- **Changing the column sequence:** the column sequence can be set per drag and drop. To do this, pull the desired column to the desired position in the table.
- **Column sorting:** column sorting through the column header is likewise saved and restored the next time ODIS Creator starts.
- **Changing the column width:** you can change the column width by moving the edge of the column with the mouse.

These adjustments are possible for the following tables in the editors of the edition:

- Used
- Used by
- Suspicion rule/suspicion rule list
- Variant Rule
- Version history
- Market availability
- List of source EV
- Operation
- Parameters
- LogicalLinks
- Texts used from the text library
- Model name
- Test log

In [Figure 643, “Example of Table Adjustments”](9-1-2-layout-settings.md#figure.config.benutzervorgaben.tabelle "Figure 643. Example of Table Adjustments"), you can see the possible changes in the example of the used table.

<a id="figure.config.benutzervorgaben.tabelle"></a>

![Example of Table Adjustments](images/tabellen_anpassungen.jpg)

**Figure 643. Example of Table Adjustments**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="9-1-1-settings-default-value-for-the-maximum-wait-time.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="9-1-settings.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="9-2-collect-program-logs.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">9.1.1. Settings: Default Value for the Maximum Wait Time </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 9.2. Collect Program Logs</td></tr></table>
