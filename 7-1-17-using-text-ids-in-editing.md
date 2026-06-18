[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.1. Editorial Object General Information](7-1-editorial-object-general-information.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.1.17. Using Text IDs in Editing</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-1-16-creating-formatted-text.md">Prev</a> </td><th align="center" width="60%">7.1. Editorial Object General Information</th><td align="right" width="20%"> <a accesskey="n" href="7-1-18-templates.md">Next</a></td></tr></table>

---

#### <a id="textIdVerwenden"></a>7.1.17. Using Text IDs in Editing

Text IDs from the text library (see [Section 5.6, “Text Library”](5-6-text-library.md "5.6. Text Library")) can be used in editing.

##### <a id="texteinfuegen"></a>7.1.17.1. Using Texts

Free text entries can be made to use a text ID. If a space is entered within a free text entry, an auto-completion dialog will open. Based on the text input, suggestions from the text library (see [Section 5.6, “Text Library”](5-6-text-library.md "5.6. Text Library")) are listed, and you can select a text from this list (by double clicking). If none of the suggested text IDs work, you can continue to write and use the free text.

The auto-complete dialog (selection dialog) for entries in the text library is initially paired directly with the dialog that is opened (main dialog). The effect of this pairing is that the selection dialog is connected to the upper right corner of the main dialog so that the main dialog is not covered by the selection dialog. The pairing also ensures that the selection dialog will change its position parallel to the main dialog when the main dialog is moved. The pairing can be ended if the user moves the selection dialog away from its location next to the main dialog. At this point, both dialogs are separated, meaning the selection dialog will no longer change its position when the main dialog does. The pairing will be restored if the selection dialog is closed and then opened again. The selection dialog can be closed separately from the main dialog. However, if the author closes the main dialog, then the selection dialog will automatically close. This also occurs even if the two dialogs were separated from each other.

In general: the auto-complete dialog (selection dialog) for text library entries is only visible if text library entries are also permitted in the field that is currently in focus. In particular, this means that an open selection dialog will close automatically if the author switches the focus from a text field that allows text library entries to another interface element in the GUI (such as a drop-down box).

If you use a text from the text library, you will recognize the text based on the background color. In [Figure 208, “Display of a Used Text ID”](7-1-17-using-text-ids-in-editing.md#figure.redaktion.text.hintergrund "Figure 208. Display of a Used Text ID"), you will see an example for text ID usage in a diagnostic object. You can also see additional information about the text ID in the associated tool tip, such as the ID or the author of the text ID.

<a id="figure.redaktion.text.hintergrund"></a>

![Image: display of a used text ID](images/textbib_verwendung_hintergrund_tooltip.jpg)

**Figure 208. Display of a Used Text ID**

Texts can also be placeholders. If you have inserted a placeholder, you can assign the placeholder a variable, a keyword or a value using the interface table (see [Section 7.1.17.5, “Change Text ID Variable/Keyword”](7-1-17-using-text-ids-in-editing.md#text.schnittstellentabelle "7.1.17.5. Change Text ID Variable/Keyword")).

A special feature is the expression being in the function editor (see [Section 7.14.12.1.3, “Text Library”](7-14-12-category-mapping.md#ausdruck.textbibliothek "7.14.12.1.3. Text Library")). A text ID is added there with the **Text library** function.

It acts similarly to the locations where no free text is entered, however variables or codes cannot be used, for example. In the instruction dialogs with tables, there is the **"..."** button and the menu item **text library** under that (see [Figure 209, “Text Selection in Table Cells”](7-1-17-using-text-ids-in-editing.md#figure.redaktion.text.tabellen "Figure 209. Text Selection in Table Cells")); the selection dialog with the search field will also open at these locations.

<a id="figure.redaktion.text.tabellen"></a>

![Image: text selection in table cells](images/fte_deklarieren_textbib.png)

**Figure 209. Text Selection in Table Cells**

##### <a id="textekopieren"></a>7.1.17.2. Reusing Texts

It is possible to copy text IDs from one editorial object to another. To do this, select the text ID to be copied and select copy in the context menu. Select paste in the new editorial object, where this text ID should be used. Now you have more options of how the text ID should be pasted.

- **Paste text ID as reference:** the text ID reference is pasted in the new editorial object with the ID of the selected text ID. For example, @[txt]123.123456.
- **Paste:** the plain text of the text ID is pasted in the new editorial object. The formatting is transferred with this, however the reference to the text ID is no longer at the pasted location.

##### <a id="d4e6841"></a>7.1.17.3. Usage Locations of Text IDs

There are different usage locations for text IDs, which are defined by the respective superordinate category (see [Figure 82, “Category properties”](5-6-1-category.md#figure.admin.textbib.kategorie_einstellen "Figure 82. Category properties")). The text IDs used in an editorial object are listed in the table "used texts from text library" (see [Figure 210, “"Used Texts from Text Library" Table”](7-1-17-using-text-ids-in-editing.md#figure.redaktion.tabelle.verwendeteTexte "Figure 210. \"Used Texts from Text Library\" Table")).

<a id="figure.redaktion.tabelle.verwendeteTexte"></a>

![Image: "used texts from text library" table](images/textbib_tabelle_verwendete_texte.jpg)

**Figure 210. "Used Texts from Text Library" Table**

In the used texts table, you will see the text ID with the version, the category it belongs to and the content. The content is not displayed immediately, but rather can be loaded using the context menu.

Usage in the function test editor is somewhat extensive compared to the rest of editing, therefore the following table gives an overview of the usage locations in the function test editor of text IDs as well as the type of usage and insertion.

<a id="d4e6857"></a>

<table border="1" summary="Usage Locations of Text IDs in the Function Test Editor"><colgroup><col align="left"/><col align="left"/><col align="left"/><col align="left"/><col align="left"/><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Location/action element</th><th align="left">Type</th><th align="left">Text ID selection</th><th align="left">ANSI characters permitted</th><th align="left">Special characters permitted</th><th align="left">Formatting permitted</th><th align="left">Text ID category</th></tr></thead><tbody valign="top"><tr><td align="left" valign="top">Title</td><td align="left" valign="top">one line</td><td align="left" valign="top">Auto complete</td><td align="left" valign="top">No</td><td align="left" valign="top">No</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Function test title</td></tr><tr><td align="left" valign="top">Tester description</td><td align="left" valign="top">Multi-line</td><td align="left" valign="top">Auto complete</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Tester description</td></tr><tr><td align="left" valign="top">Test step title</td><td align="left" valign="top">one line</td><td align="left" valign="top">Auto complete</td><td align="left" valign="top">No</td><td align="left" valign="top">No</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Test step title</td></tr><tr><td align="left" valign="top">Sub-Program</td><td align="left" valign="top">Expression (translatable)</td><td align="left" valign="top">Button</td><td align="left" valign="top">No</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Sub-Program</td></tr><tr><td align="left" valign="top">Set test module title</td><td align="left" valign="top">one line</td><td align="left" valign="top">Auto complete</td><td align="left" valign="top">No</td><td align="left" valign="top">No</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Set test module title</td></tr><tr><td align="left" valign="top">Question - Text</td><td align="left" valign="top">Multi-line</td><td align="left" valign="top">Auto complete</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Question</td></tr><tr><td align="left" valign="top">Question - Answer</td><td align="left" valign="top">Expression (translatable)</td><td align="left" valign="top">Button</td><td align="left" valign="top">No</td><td align="left" valign="top">No</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Question</td></tr><tr><td align="left" valign="top">Input</td><td align="left" valign="top">Multi-line</td><td align="left" valign="top">Auto complete</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Input</td></tr><tr><td align="left" valign="top">Help</td><td align="left" valign="top">Multi-line</td><td align="left" valign="top">Auto complete</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Help</td></tr><tr><td align="left" valign="top">Message</td><td align="left" valign="top">Multi-line</td><td align="left" valign="top">Auto complete</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Message</td></tr><tr><td align="left" valign="top">Make declaration</td><td align="left" valign="top">Expression (translatable)</td><td align="left" valign="top">Button</td><td align="left" valign="top">No</td><td align="left" valign="top">No</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Make declaration</td></tr><tr><td align="left" valign="top">Expression</td><td align="left" valign="top">Expression (translatable)</td><td align="left" valign="top">Button</td><td align="left" valign="top">No</td><td align="left" valign="top">No</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Expression</td></tr><tr><td align="left" valign="top">Measuring equipment - supplemental text</td><td align="left" valign="top">Multi-line</td><td align="left" valign="top">Auto complete</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Measuring channel, voltage, current, resistance, diode, temperature, oscilloscope, high-voltage block</td></tr><tr><td align="left" valign="top">Measuring equipment - Vehicle test point/text</td><td align="left" valign="top">one line</td><td align="left" valign="top">Auto complete</td><td align="left" valign="top">No</td><td align="left" valign="top">No</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Measuring channel, voltage, current, resistance, diode, temperature, oscilloscope, high-voltage block</td></tr><tr><td align="left" valign="top">Ecukom - output text</td><td align="left" valign="top">Multi-line</td><td align="left" valign="top">Auto complete</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Ecukom, ASAM Ecukom</td></tr><tr><td align="left" valign="top">Read measured values</td><td align="left" valign="top">Multi-line</td><td align="left" valign="top">Auto complete</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Read measured values</td></tr><tr><td align="left" valign="top">Documents</td><td align="left" valign="top">Expression (translatable)</td><td align="left" valign="top">Button</td><td align="left" valign="top">No</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Documents</td></tr><tr><td align="left" valign="top">All/ table cell / ANSI cell content</td><td align="left" valign="top">Multi-line</td><td align="left" valign="top">Auto complete</td><td align="left" valign="top">No</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Yes</td><td align="left" valign="top">All</td></tr></tbody></table>

**Table 43. Usage Locations of Text IDs in the Function Test Editor**

Key:

- **Location/action element**: instruction and if necessary, rich text editor attribute
- **Type**: rich text editor type (one line/multiple lines)
- **Text ID selection**: selection type (auto population/button)
- **ANSI characters permitted**: use of ANSI characters permitted (yes/no)
- **Special characters permitted**: use of special characters (icons) permitted (yes/no)
- **Formatting permitted**: text IDs with special characters permitted (yes/no)
- **Text ID category**: category name from the text library

##### <a id="aktionen.verwendete.Texte"></a>7.1.17.4. Actions on Used Text IDs

If you use a text ID in an editorial object, you can perform various actions using the context menu on the text ID plain text. These are explained in the following.

In [Figure 211, “Context Menu of a Used Text ID”](7-1-17-using-text-ids-in-editing.md#figure.redaktion.kontext_textid "Figure 211. Context Menu of a Used Text ID"), you will see an example for a text ID context menu in a diagnostic object.

<a id="figure.redaktion.kontext_textid"></a>

![Image: context menu of a used text ID](images/textbib_kontext_verwendungsstelle.jpg)

**Figure 211. Context Menu of a Used Text ID**

- **Copy:** this copies the text ID to the clipboard and it can be pasted at another location.
- **Paste:** pastes a copied text ID as plain text to the desired location. As long as a text ID can be used at this location, the reference to the text ID will remain there, otherwise only the plain text is inserted.
- **Cut:** this copies the text ID to the clipboard and it can be pasted at another location. The text ID is then no longer present in the original field.
- **Undo/Repeat:** this can undo or repeat changes. An action can only be redone if it was previously undone.
- **Copy XML:** this function copies the XML structure for the text ID reference to the clipboard.
- **Paste XML:** this function pastes the XML structure for the text ID reference from the clipboard.
- **Change text ID variable/keyword:** this function opens the interface table in which a variable, a keyword or a value can be set for every placeholder. (see [Section 7.1.17.5, “Change Text ID Variable/Keyword”](7-1-17-using-text-ids-in-editing.md#text.schnittstellentabelle "7.1.17.5. Change Text ID Variable/Keyword"))
- **Display text IDs:** this function allows the IDs of the used text IDs to be displayed. The function is a switch and can be activated and deactivated through the context menu.
- **Paste text ID reference:** this function pastes a copied text ID as a reference at another location.

##### <a id="text.schnittstellentabelle"></a>7.1.17.5. Change Text ID Variable/Keyword

In the function test editor, a variable, a keyword or a value can be assigned to a text ID that is a placeholder. In [Figure 212, “Text ID Interface Table”](7-1-17-using-text-ids-in-editing.md#figure.redaktion.schnittstellentabelle "Figure 212. Text ID Interface Table"), you will see the interface table, that is accessed when you select **Change text ID variable/keyword** in the context menu for a text ID placeholder. In the **Value/variable/function test keyword** column, you can specify the desired value or the variable or the keyword.

<a id="figure.redaktion.schnittstellentabelle"></a>

![Image: text ID interface table](images/textbib_schnittstellentabelle.jpg)

**Figure 212. Text ID Interface Table**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-1-16-creating-formatted-text.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-1-editorial-object-general-information.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-1-18-templates.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.1.16. Creating Formatted Text </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.1.18. Templates</td></tr></table>
