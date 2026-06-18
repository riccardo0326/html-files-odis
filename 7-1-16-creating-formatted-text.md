[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.1. Editorial Object General Information](7-1-editorial-object-general-information.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.1.16. Creating Formatted Text</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-1-15-cardinalities-of-editorial-objects.md">Prev</a> </td><th align="center" width="60%">7.1. Editorial Object General Information</th><td align="right" width="20%"> <a accesskey="n" href="7-1-17-using-text-ids-in-editing.md">Next</a></td></tr></table>

---

#### <a id="formatiertertext"></a>7.1.16. Creating Formatted Text<a id="d4e6604"></a>

Formatted texts can be created at various locations in ODIS Creator. A central component is used for this: the rich text editor (RTE). The rich text editor is available in the following subcomponents:

- Default text editor
- Auxiliary Document Editor
- Usage Locations of Text IDs:

  - Message editor for measured values in the measured values tables (KWP)
  - Various commands (message, help, etc.) in the function test editor
  - Display names of editorial objects
  - Editor for auxiliary documents

The display of texts within multi-line RTE text files contains an automatic line break so that the texts are always completely legible. For longer text entries, there is also a vertical scroll bar.

Table displays contained in texts are not divided with breaks. When there are large numbers of columns, the table may not be displayed completely in the text field. If this is the case, you need to expand the window or editor sideways. If that is not possible, then reduce the width of the columns so that the entire table is visible.

The additional rich text editor functions are described in the following.

##### <a id="d4e6629"></a>7.1.16.1. Text Formats

Various buttons are available in RTE to format texts. In addition to the font selection (Arial/Courier), the font size (small/large), the font style (italic/bold), and the font color (black/red/blue) can also be applied to the text. [Figure 200, “Format Options for Text in the Rich Text Editor”](7-1-16-creating-formatted-text.md#figure.redaktion.funktionsbibliothek.rte.format "Figure 200. Format Options for Text in the Rich Text Editor") gives an overview of the buttons.

<a id="figure.redaktion.funktionsbibliothek.rte.format"></a>

![Image: format options for text in the rich text editor](images/textformat.png)

**Figure 200. Format Options for Text in the Rich Text Editor**

##### <a id="d4e6641"></a>7.1.16.2. Graphics and Symbols

Graphics and symbols can be inserted with special buttons in the text. The insertion is made at the active cursor position and is possible within the running text. The row height aligns itself automatically to the highest element. The red attention symbol, for example, enlarges the row respectively to its dimensions: the following text is not enlarged, however is displayed with the respective row height. The following images ([Figure 201, “Buttons to Insert Graphics”](7-1-16-creating-formatted-text.md#figure.redaktion.funktionsbibliothek.rte.grafiken "Figure 201. Buttons to Insert Graphics") and [Figure 202, “Buttons to Insert Symbols”](7-1-16-creating-formatted-text.md#figure.redaktion.funktionsbibliothek.rte.symbole "Figure 202. Buttons to Insert Symbols")) show the buttons to add graphics and symbols.

<a id="figure.redaktion.funktionsbibliothek.rte.grafiken"></a>

![Image: buttons to insert graphics](images/symbole1.png)

**Figure 201. Buttons to Insert Graphics**

<a id="figure.redaktion.funktionsbibliothek.rte.symbole"></a>

![Image: buttons to insert symbols](images/symbole2.png)

**Figure 202. Buttons to Insert Symbols**

##### <a id="d4e6661"></a>7.1.16.3. Tables<a id="d4e6663"></a>

The RTE assists the creation of tables with various functions. Tables can have a minimum of one and a maximum of 60 columns/lines. Because the RTE wraps automatically everywhere except in the supplementary document editor content editor (based on the ODIS Service processing components) and a large number of very wide columns cannot be displayed, you are responsible for setting up the layout of the tables so that they are correctly displayed in the processing system. Due to technical reasons, a table has a header row that is not displayed in the processing system, and is only used for the parameterization of the column width. The [Figure 203, “Table in Rich Text Editor”](7-1-16-creating-formatted-text.md#figure.redaktion.funktionsbibliothek.rte.tabellenbeispiel "Figure 203. Table in Rich Text Editor") shows a table in RTE.

<a id="figure.redaktion.funktionsbibliothek.rte.tabellenbeispiel"></a>

![Image: table in rich text editor](images/tabellen_beispiel.png)

**Figure 203. Table in Rich Text Editor**

The [Figure 204, “Buttons to Parameterize Tables”](7-1-16-creating-formatted-text.md#figure.redaktion.funktionsbibliothek.rte.tabellenschaltflaechen "Figure 204. Buttons to Parameterize Tables") shows the buttons to parameterize the tables.

<a id="figure.redaktion.funktionsbibliothek.rte.tabellenschaltflaechen"></a>

![Image: buttons to parameterize tables](images/tabellen_schaltflaechen.png)

**Figure 204. Buttons to Parameterize Tables**

Tables can be inserted directly into the running text and expands a line correspondingly. No other table elements (tables or special characters) can be in a table cell.

###### <a id="d4e6687"></a>7.1.16.3.1. Horizontal Orientation

The orientation of cells can be aligned to the left or right, or centered. The orientation can be applied to multiple cells, depending on the selection.

###### <a id="d4e6690"></a>7.1.16.3.2. Expansion

Rows/columns can be expanded in existing tables using two buttons Rows/columns are always added after the current selected item in a table.

###### <a id="d4e6693"></a>7.1.16.3.3. Frames

The table frame can be turned on or off. It surrounds the entire table. Due to technical circumstances, the frame is always displayed around the table regardless of the parameterization.

###### <a id="d4e6696"></a>7.1.16.3.4. Cell Editor

The editing of a table cell occurs in a separate window, the cell editor. This is opened per double clicking and is a full-fledged rich text editor (without table function). If the cell editor is closed, an automatic table orientation occurs (as long as no fixed column width is specified)

###### <a id="d4e6699"></a>7.1.16.3.5. Column/Row Size

The size of a column/row depends on its content and is automatically determined. However, the column width can also be manually set. To do this, a column in the upper, labeled header line, can be made wider or more narrow. Once dragged to the header line, the column is provided with a fixed width. To return to the automatic size adjustment, the context menu can be used in the header area of the affected column.

###### <a id="d4e6702"></a>7.1.16.3.6. Applying Formats Directly to Cell

Text formats can be applied directly to table cells. The format is applied to the entire content of the cell for this. If additive formats, such as the font style (bold/italic) are applied to a cell that already contains font styles in the text portions, then the formats will be partially set and partially removed. Due to different formats within a cell, the format button stays in its last condition and does not adjust.

###### <a id="d4e6705"></a>7.1.16.3.7. Deleting Tables and Structures

Deleting tables can be done directly by entering text using the keyboard or the context menu. Individual rows/columns can also be removed through the context menu. Note: it is not possible to undo these actions.

###### <a id="d4e6708"></a>7.1.16.3.8. Copy

A table can be copied either using the context menu or using the button combination CTRL C (copy table) or CTRL E (copy table (XML)) when the table (or a cell) is marked. Inserting a table is only possible in the RTE. Other applications are not supported. The insertion is prevented if the clipboard has a table and for example, should be added to a cell editor, since no inner tables are supported.

##### <a id="d4e6711"></a>7.1.16.4. ANSI Special Characters<a id="d4e6713"></a>

The RTE supports the creation of ANSI special characters according to the ANSI standard Z535.6. The special characters consist of a split display whereby the first area, called heard area in the following, contains a standardized graphic and if necessary, a standardized text and the second section has a parameterized text. The following special characters are supported:

- ![Additional information symbol](images/redaktion_allgemein_rte_sonderzeichen_infonew_32x32.png) Additional information
- ![Note symbol](images/redaktion_allgemein_rte_sonderzeichen_ansi-s4_32x32.png) Note
- ![Caution symbol](images/redaktion_allgemein_rte_sonderzeichen_ansi-s3_32x28.png) Caution
- ![Warning symbol](images/redaktion_allgemein_rte_sonderzeichen_ansi-s2_32x28.png) Warning
- ![Danger symbol](images/redaktion_allgemein_rte_sonderzeichen_ansi-s1_32x28.png) Danger

Inserting special characters can be done through five icons, that are placed in the left tool bar in the rich text editor. Pressing a button in the tool bar will add the special character to the position where the cursor is active. The buttons are designed with the respective characters. The following images show the message dialog with the buttons to insert the special characters and examples for the special characters.

<a id="figure.redaktion.funktionsbibliothek.rte.sonderzeichen"></a>

![Image: special characters in the rich text editor: note and caution](images/redaktion_allgemein_rte_sonderzeichen_beispiel.png)

**Figure 205. Special Characters in the Rich Text Editor: Note and Caution**

<a id="figure.redaktion.funktionsbibliothek.rte.sonderzeichen2"></a>

![Image: special characters in the rich text editor: warning and danger](images/redaktion_allgemein_rte_sonderzeichen_beispiel2.png)

**Figure 206. Special Characters in the Rich Text Editor: Warning and Danger**

<a id="figure.redaktion.funktionsbibliothek.rte.sonderzeichen3"></a>

![Image: special characters in the rich text editor: additional information](images/redaktion_allgemein_rte_sonderzeichen_beispiel3.png)

**Figure 207. Special Characters in the Rich Text Editor: Additional Information**

The special characters can be added directly to the running text and expand a line correspondingly. A special character is used like a table element. Table elements cannot contain other table elements.

<a id="formatierungenansisonderzeichen"></a>Because ANSI characters must be displayed in a specified format, formatting, such as that contained in formatted TextIDs, does not have any effect on ANSI characters. Formatted TextIDs lose their formatting when used in an ANSI special character.

<a id="festebreiteansizeichen"></a>In the rich text editor display, all ANXI characters have a fixed width so that editing is easier. Line breaks are added to the text automatically and the height of the ANSI characters increases. There is no width restriction in the actual display on the tester (also in HTML in auxiliary documents).

###### <a id="d4e6781"></a>7.1.16.4.1. Cell Editor

The editing of a text cell in the special characters occurs in a separate window, the cell editor. This is opened per double clicking and is a full-fledged rich text editor (without table function). Furthermore, the formats for the use of special characters are limited: Arial, black, bold, aligned to the left. If the cell editor is closed, the special character is automatically aligned. The column width is automatically adjusted.

###### <a id="d4e6784"></a>7.1.16.4.2. Applying Formats Directly to Cell

The large/small font text formats can be applied directly to the special character cell. The format is applied to the entire content of the cell.

###### <a id="d4e6787"></a>7.1.16.4.3. Deleting Special Characters

Deleting special characters can be done directly by entering text using the keyboard or the context menu. The form of the special character cannot be changed. Note: it is not possible to undo these actions.

###### <a id="d4e6790"></a>7.1.16.4.4. Copy

A special character can be copied either using the context menu or using the button combination CTRL C (copy table) or CTRL E (copy special character (XML)) when the table (or a cell) is marked. Inserting a special character is only possible in the RTE. Other applications are not supported. The insertion is prevented if the clipboard contains a table element (special character or table) and for example, should be inserted in a cell editor, since no inner table elements are supported.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-1-15-cardinalities-of-editorial-objects.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-1-editorial-object-general-information.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-1-17-using-text-ids-in-editing.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.1.15. Cardinalities of Editorial Objects </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.1.17. Using Text IDs in Editing</td></tr></table>
