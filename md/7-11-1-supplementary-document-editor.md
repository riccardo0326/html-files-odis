[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.11. Editors for Supplemental Documents](7-11-editors-for-supplemental-documents.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.11.1. Supplementary Document Editor</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-11-editors-for-supplemental-documents.md">Prev</a> </td><th align="center" width="60%">7.11. Editors for Supplemental Documents</th><td align="right" width="20%"> <a accesskey="n" href="7-11-2-hotspot-editor.md">Next</a></td></tr></table>

---

#### <a id="zdk"></a>7.11.1. Supplementary Document Editor

The supplementary document editor is an **internal OC editor** to create text content for supplemental documents. Document elements such as text, icons, and references can be added. In most cases, the editor will display the formatted result directly (“WYSIWYG” editor, "What you see is what you get”, similar to Microsoft Word).

##### <a id="zdk.oeffnen"></a>7.11.1.1. Opening A Document in the Supplementary Document Editor

In the **Editing** [view](3-2-1-views-bar.md "3.2.1. Views Bar"), click on the **Supplemental documents** action element. Select the desired document in the supplemental documents navigator and open the corresponding [revision editor](3-2-5-editor.md "3.2.5. Editor"). Click in the gray area of the editor with the right mouse button. Click on the **Text** and **Edit** [buttons](2-2-general-definitions-and-glossaries.md#schaltflaeche) in the context menu ([Figure 300, “Opening the Supplementary Document Editor”](7-11-1-supplementary-document-editor.md#figure.zdkeditor.oeffnen "Figure 300. Opening the Supplementary Document Editor")).

<a id="figure.zdkeditor.oeffnen"></a>

![Image: opening the supplementary document editor](images/epic_oeffnen.png)

**Figure 300. Opening the Supplementary Document Editor**

The document is opened in the supplementary document editor ([Figure 301, “Supplementary Document Editor”](7-11-1-supplementary-document-editor.md#figure.zdk.editor "Figure 301. Supplementary Document Editor")).

<a id="figure.zdk.editor"></a>

![Image: supplementary document editor](images/zdk_editor.png)

**Figure 301. Supplementary Document Editor**

The editor is divided into two sections. The upper section of the internal editor contains the field for editing the title (**Caption** XML element), while the lower section contains the field for editing the content. The font, style, color, and font size of the title can be formatted. In addition to the font type, style, color, and formatting, the following elements can be added in the content editor: Table, Anchor, AnchorRef, DocRef, List. Text is formatted and elements are added using buttons that are located to the left of and above the editor field. Many of the formatting options are similar to editing texts within function code dialogs (see [Section 7.14.7, “Editing Text”](7-14-7-editing-text.md "7.14.7. Editing Text")).

First, the **cursor** (insertion symbol) must be at the desired input location in the document. To do this, use the mouse to click at the respective point in the document.

###### <a id="zdk.transformation"></a>7.11.1.1.1. Conversion of Supplementary Document Content

When supplementary document content is opened in the internal editor for the first time, a conversion may be needed. The conversion ensures that certain XML elements are modified so that they can be processed by the internal editor. The display of texts in the diagnostic procedure is hardly changed during the conversion.

In detail, the conversion involves the following elements:

- ANSI characters instead of root elements

  The "Caution”, “Information”, and “Attention” XML elements that are defined in the upper location of the schema are replaced with ANSI symbols that have the same values. When this happens, the XML element

  - “Information” is replaced with the ANSI symbol “additional information”
  - “Caution” is replaced with the ANSI symbol “Note”
  - “Attention” is replaced with the ANSI symbol “Danger”

  The text that is present is carried over when these elements are replaced.
- Table layout information

  Cells that are combined into a row in a table using the “colspan” attribute cannot be edited in the internal editor. Therefore, this attribute is ignored. As a result, the display of table content may shift.

##### <a id="zdk.kombiniertesspeichern"></a>7.11.1.2. Combined Save for Supplementary Documents

This function is similar to the Save function, except the linked object properties editor is also saved. By saving the object properties editor, the supplementary document is saved on the ODIS Creator server. You can continue working directly after the combined save: the supplementary document remains open and in the "In editing" status.

To be able to perform a combined save on a supplementary document, all mandatory fields must be filled out and changes must be made to the supplementary document. If a supplementary document is open, a combined save can be performed using the file menu and the toolbar.

<a id="zdk.kombiniertesspeichern.image"></a>

![Illustration: combined save of supplementary documents](images/kombiniertes-speichern-zdk.png)

**Figure 302. Combined Save of Supplementary Documents**

##### <a id="zdk.textsize"></a>7.11.1.3. Changing Font Size

The text in auxiliary documents can be written in various font sizes. In contrast to texts in function codes (where only lower case and upper case font is possible), eleven different font sizes are available. The user can select any font size between 10 and 20 using a combo box.

The display in the combo box always represents the font size for the character to the left of the current cursor position. The exceptions to this are tables, special characters, and the cursor position 0 (at the beginning of a text field), where the selection will always show the value for the previous cursor position.

##### <a id="zdk.anchor"></a>7.11.1.4. Adding an Anchor

Pressing the “Anchor” button adds an anchor to the document. In the diagnostic process display, an anchor element serves as the target for a link within an document. The targets are not visible in the displayed document, but then can be focused on by selecting a corresponding anchor-ref.

<a id="figure.zdk.anchor"></a>

![Image: adding anchor](images/add_anchor.png)

**Figure 303. Adding Anchor**

  

The name of the anchor must be specified.

<a id="figure.zdk.anchor.name"></a>

![Image: anchor name](images/add_anchor_name.png)

**Figure 304. Anchor Name**

  

When the anchor name is entered, an anchor symbol appears in the editor interface.

<a id="figure.zdk.anchor.symbol"></a>

![Image: anchor symbol](images/add_anchor_symbol.png)

**Figure 305. Anchor Symbol**

  

To edit an anchor, you must click the element to be edited with the mouse, then right-click and select the command "Edit anchor” from the context menu. When a menu item is selected, the filled-in dialog in which the anchor will be edited appears. **Caution:** when an anchor ID is edited, anchor refs that already exist and that link to the anchor ID may be invalid. They must be edited or deleted before saving.

##### <a id="zdk.anchor.ref"></a>7.11.1.5. Adding an AnchorRef

To add an AnchorRef, first the anchor itself must be defined. Then, pressing the “AnchorRef” button adds an AnchorRef to the document. AnchorRef elements have displayed text and the ID of the referenced anchor that should be focused on when the link is used.

Any number of AnchorRefs can link to a single anchor, for example to allow the user to jump back to the beginning from certain places in the document.

<a id="figure.zdk.anchor.ref"></a>

![Image: adding AnchorRef](images/add_anchor_ref.png)

**Figure 306. Adding AnchorRef**

  

The "Reference” to the anchor that has already been created and the “Link text” must be specified in a separate dialog.

<a id="figure.zdk.anchor.ref.link"></a>

![Image: AnchorRef link](images/add_anchor_ref_link.png)

**Figure 307. AnchorRef Link**

  

If everything is entered correctly, an AnchorRef symbol will appear in the editor interface.

<a id="figure.zdk.anchor.ref.symbol"></a>

![Image: AnchorRef symbol](images/add_anchor_ref_symbol.png)

**Figure 308. AnchorRef Symbol**

  

To edit an AnchorRef, you must click the reference to be edited with the mouse, then right-click and select the command "Edit anchor reference” from the context menu. When a menu item is selected, the filled-in dialog in which the anchor reference will be edited appears.

##### <a id="zdk.doc.ref"></a>7.11.1.6. Adding a DocRef

Pressing the “DocRef” button adds a DocRef to the document. DocRef elements are used to generate references to external documents within a supplementary document. Currently, only WWW references are permitted.

<a id="figure.zdk.doc.ref"></a>

![Image: adding DocRef](images/add_docref.png)

**Figure 309. Adding DocRef**

  

The document category and the external reference target must be specified in a separate dialog.

<a id="figure.zdk.doc.ref.edit"></a>

![Image: DocRef category/reference](images/add_docref_edit.png)

**Figure 310. DocRef Category/Reference**

  

If everything is entered correctly, a DocRef symbol will appear in the editor interface.

<a id="figure.zdk.doc.ref.symbol"></a>

![Image: DocRef symbol](images/add_docref_symbol.png)

**Figure 311. DocRef Symbol**

  

To edit a DocRef, you must click the reference to be edited with the mouse, then right-click and select the command "Edit document reference” from the context menu.

<a id="figure.zdk.doc.ref.edit.docref.select"></a>

![Image: selecting the DocRef menu](images/docRef_edit_menu.png)

**Figure 312. Selecting the DocRef Menu**

  

When a menu item is selected, the filled-in dialog in which the anchor reference will be edited appears.

<a id="figure.zdk.doc.ref.edit.docref.window"></a>

![Image: DocRef editor window](images/docRef_edit_menu_window.png)

**Figure 313. DocRef Editor Window**

##### <a id="zdk.list"></a>7.11.1.7. Working with a List in the Supplementary Document Editor

Lists within supplementary documents are edited according to the WYSIWYG approach. This means that the visible elements in a list in the editor are also displayed that way in the operating system.

###### <a id="zdk.list.create"></a>7.11.1.7.1. Creating a New List

There is a button in the toolbar for creating a new list. Pressing this button declares the current line in the document where the cursor is located as a list. If more than one line is selected in the editor, then all lines will be declared as a list. Each of the lines will form its own entry in the list.

<a id="figure.zdk.list"></a>

![Image: adding a list](images/add_list.png)

**Figure 314. Adding a List**

  

The list is laid out with bullet points that follow one after the other.

The following items may not be used within a list:

- ANSI characters
- Tables
- Icons

Note: if tables are added into lists using “Default text with table”, this may shift the display of the list in the operating system.

<a id="figure.zdk.list.symbol"></a>

![Image: list symbol](images/add_list_symbol.png)

**Figure 315. List Symbol**

###### <a id="zdk.list.delete"></a>7.11.1.7.2. Deleting a List

A list and its content can be completely deleted To do this, the user must mark the entire list and press the Delete button. A list bullet may remain, depending on how much is marked (if the line break for the last list item is included or not). It can be used as the basis for a new list. To remove the last bullet, the user must place the cursor in the line with the bullet and press the “Delete” button. The "Backspace” button moves the bullet up on line, if that line was previously empty. Otherwise, the bullet will be deleted.

###### <a id="zdk.list.work"></a>7.11.1.7.3. Working with a List

- **New List Items**

  New list items can be created by pressing the Enter key. The bullets in the display indicate which lines are currently contained in the list. The lines directly below an existing list may be marked with a bullet to signal to the user that the line is empty and could possibly be used as a list item.

  If there is text in the line after the cursor when the Enter key is pressed, then that text will be turned into a new list item. You can also create empty list items. They will be kept and will then be displayed in the operating system as bullets without text. When creating empty list items, you must follow the requirements fro ending a list (see below).
- **Deleting List Items**

  List items can be deleted by pressing the delete keys (Delete or Backspace). The cursor must be at the beginning or end of the line when doing so. The text content of the lines will then be combined into a single list item.
- **Ending a List**

  In order to resume writing with normal text after the end of a list, the list must be ended. A list is ended when the user is in a blank line of the list and presses the Enter key again. If there are any items in the list after that, they will be “delisted”, meaning they will no longer be a part of the list and will not have bullets in front of them.
- **Copying a List**

  If text is copied from one or more list items, it can be pasted into another location. If the location where it is pasted is in the same document, then the text will be inserted as a list.
- **Formatting List Entries**

  Users can format the text in list elements as they like. The same options as with normal text are available, such as font type, font size, bold, italics, etc. The formatting can be applied before typing or by selecting existing text.

###### <a id="zdk.list.bullets"></a>7.11.1.7.4. Working with Different Bullets in a List

There are seven different bullets available in ODIS Creator For displaying lists. The default “dot” is always used in new lists. You can change that if desired using the context menu.

<a id="figure.zdk.list.bulletcontext"></a>

![Image: changing bullets](images/change_list_symbol.png)

**Figure 316. Context Menu: Changing Bullets**

  

The possible bullets are:

- Dot (default)
- Circle
- Square
- Arabic numerals
- Roman numerals
- Lower case letters
- Upper case letters

<a id="figure.zdk.list.bulletdialog"></a>

![Image: changing bullets](images/change_list_symbol_dialog.png)

**Figure 317. Dialog: Changing Bullets**

##### <a id="zdk.textlib"></a>7.11.1.8. Using the Text Library

The text library is available in the internal auxiliary document editor. They can be used to add TextIDs into the auxiliary document using a selection dialog.

The following restrictions apply:

- Placeholders cannot be used.
- TextIDs cannot be added within lists.

Otherwise, all text library functions, such as those available in the function test editor, are available. Adding new text or changing text is possible.

##### <a id="zdk.variables"></a>7.11.1.9. Using Variables in the Supplementary Document Editor

Variables (placeholders) for parameters (values from function codes) can be added in the internal auxiliary document editor (manually or using a dialog. Refer to [Figure 319, “Adding Placeholders with a Dialog”](7-11-1-supplementary-document-editor.md#figure.zdk.AssistentVar "Figure 319. Adding Placeholders with a Dialog")). The placeholders must be specified as follows: "%Placeholder" (for specifying leading zeros or also "%0.2Placeholder” for digits after the decimal point). Placeholders must begin with a letter. The rest may contain alphanumeric characters and “\_” (umlauts are not permitted).

If a percentage sign is placed in front of a “\”, it does not function as a placeholder.

Placeholder names can be ended with the following characters:

- Spaces
- Line break
- Tables
- Icons
- Symbols (alpha, beta, etc.)
- End of the document

Placeholders can be used in any location except within an AnchorRef and DocRef.

<a id="figure.zdk.variables"></a>

![Illustration: adding placeholders](images/add_variables_zdk.png)

**Figure 318. Adding Placeholders**

  

<a id="figure.zdk.AssistentVar"></a>

![Image: adding placeholders with a dialog](images/add_variables_dialog_zdk.png)

**Figure 319. Adding Placeholders with a Dialog**

  

When saving, placeholders with the same name are checked for the same formatting. Placeholders that have the same name but differing formatting are not permitted.

<a id="figure.zdk.validateFormat"></a>

![Image: validating placeholder formatting in the auxiliary document editor](images/zdk_var_validate_format.png)

**Figure 320. Validating Placeholder Formatting in the Auxiliary Document Editor**

Variables and default text links are checked for the correct formatting when saving. Only fully-formatted or unformatted variables and text links are permitted. For example, if a variable is formatted partially as "red” and partially as “blue", you will receive an error message and changes will not be saved.

<a id="figure.zdk.validate"></a>

![Illustration: validating variables in the supplementary document editor](images/zdk_var_validate.png)

**Figure 321. Validating Variables in the Supplementary Document Editor**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-11-editors-for-supplemental-documents.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-11-editors-for-supplemental-documents.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-11-2-hotspot-editor.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.11. Editors for Supplemental Documents </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.11.2. Hotspot Editor</td></tr></table>
