[ODIS Creator Help](odis-creator-help.md) > [3. ODIS Creator Basic Information](3-odis-creator-basic-information.md) > [3.2. Program Structure](3-2-program-structure.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">3.2.5. Editor</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="3-2-4-properties-window.md">Prev</a> </td><th align="center" width="60%">3.2. Program Structure</th><td align="right" width="20%"> <a accesskey="n" href="3-2-6-tables-and-lists.md">Next</a></td></tr></table>

---

#### <a id="editor"></a>3.2.5. Editor

The editor<a id="d4e1025"></a>in the right frame is your main work window. If an entry is clicked on in the structure tree in the [navigator](3-2-3-navigator.md "3.2.3. Navigator"), the details for this entry is displayed in a separate editor window in the editor. Editor windows can be opened for viewing or for editing.

##### <a id="editor.oeffnen"></a>3.2.5.1. Opening the Editor Window

**Click once** on the entry in the navigator structure tree to open the editor window just **to view**. If another entry is clicked on in the navigator, its details will be displayed **in the same editor window**.

**Click twice** on the entry in the navigator structure tree to open the editor window **for editing**. If the editor is already open for viewing, then click on the button ![Symbol: Edit mode](images/bearbeitungsmodus.png) in the [tool bar](2-2-general-definitions-and-glossaries.md#symbolleiste) or in the [context menu](2-2-general-definitions-and-glossaries.md#kontextmenu) for the open entry in order to edit in the displayed editor.

If another entry is opened from the navigator structure tree for editing, then an **additional editor window** is opened. Multiple editor window can be open for editing at the same time, however only one editor window can be open for viewing. All open editor window are displayed and selected through the [tabs](2-2-general-definitions-and-glossaries.md#reiterkarten) ([Figure 33, “Editor with Tabs”](3-2-5-editor.md#figure.editoren "Figure 33. Editor with Tabs")). The open [windows](2-2-general-definitions-and-glossaries.md#fenster) inside the right frame can be organized next to each other or behind each other.

<a id="figure.editoren"></a>

![Image: editor with tabs](images/Editor.png)

**Figure 33. Editor with Tabs**

While an editor window is open for editing, an asterisk is given before the window title in the tab ([1](3-2-5-editor.md#figure.editable.editor "Figure 34. Editor in Edit Mode")). Entries can be handled and changed in the separate editor fields ([Figure 34, “Editor in Edit Mode”](3-2-5-editor.md#figure.editable.editor "Figure 34. Editor in Edit Mode")). The editor is locked from editing for all other users and can only be opened for viewing.

<a id="figure.editable.editor"></a>

![Image: editor in edit mode](images/EditableEditor.png)

**Figure 34. Editor in Edit Mode**

<a id="table.hinweis.editor_bearbeitung"></a>

<table border="1" summary="Editing Note for Open Editor"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note:</strong></span> Only have an editor open for editing as long as necessary, since other users cannot edit this editor during this time.</td></tr></tbody></table>

**Table 11. Editing Note for Open Editor**

##### <a id="editor.speichern"></a>3.2.5.2. Save Changes

To save the changes in the editing window, click on the buttons **File** and then **Save** in the [menu bar](2-2-general-definitions-and-glossaries.md#menuleiste), or go to the [tool bar](2-2-general-definitions-and-glossaries.md#symbolleiste) ![Save](images/save.png) . If you save the changes in this way, then the editor is locked from editing for all other users and can only be opened to be viewed.

To remove the lock from the object being edited, you should check in the object. To do this, use the buttons **File** in the [menu bar](2-2-general-definitions-and-glossaries.md#menuleiste) and then click on **Check in and close** or the corresponding button ![Checks the object in and closes the active editor](images/save_and_close.png) in the [tool bar](2-2-general-definitions-and-glossaries.md#symbolleiste). Then the editor stays open only for viewing (an asterisk is no longer displayed in front of the window title in the tab).

##### <a id="r%C3%BCckg%C3%A4ngig.wiederherstellen"></a>3.2.5.3. Undo / Restore

There are corresponding options in the menu structure and in the ODIS Creator tool bar for the undo and restore functionalities. There are two buttons in the tool bar ([Figure 36, “Undo / Restore Button”](3-2-5-editor.md#figure.rueckgaengig.wiederherstellen.button "Figure 36. Undo / Restore Button")) for both the editing and order management views. There are two entries in the global menu for both views under the Edit menu ([Figure 35, “Undo / Restore Menu”](3-2-5-editor.md#figure.rueckgaengig.wiederherstellen.menu "Figure 35. Undo / Restore Menu")). There is a history for the order management or editing editors.

Each editor has its own history (also the sub-editors). If an editor is closed or saved, then the respective history is deleted. The buttons or the menu always reflect the history of the editor that was just active. If no actions could be undone for an editor, then the button is deactivated. The same applies to the restore button. If you click on the menus, then the last action in the undo/restore list in the history is undone or restored. As an alternative, you can use "CTRL-Z" or "CTRL-Y". The buttons can be used in several ways. By clicking on the black triangle next to the button one time, up to 15 of the last entries on the undo / restore list in the history is opened. You will always find the last performed as well as the last undone action at the top of the list. Multiple actions can be undone or restored by selecting them in the open history list. All entries in the history are then affected up to and including the selected action. A change in the editor occurs so that all actions that are in the restore list in the history are removed from the history. The newly performed change is then given as the last action in the history.

<a id="figure.rueckgaengig.wiederherstellen.menu"></a>

![Image: undo / restore menu](images/menu_rueckgaengig.png)

**Figure 35. Undo / Restore Menu**

<a id="figure.rueckgaengig.wiederherstellen.button"></a>

![Image: undo / restore button](images/button_rueckgaengig.png)

**Figure 36. Undo / Restore Button**

###### <a id="r%C3%BCckg%C3%A4ngig.wiederherstellen.aktionen"></a>3.2.5.3.1. Actions in the History

Generally, actions in the history are seen with the name of the changed interface elements. This designation of the history elements can be seen in the open lists as well as a tool tip in the toolbar and as a general rule, they will read as follows: "Edit comments", "Activate migration protection" based on the partially generic orientation of the editors, it is not always possible to clearly name the elements in the history. Universally where this is not possible, generic names for the elements in the history are used, for example "Text field edits", "Cell edits".

###### <a id="r%C3%BCckg%C3%A4ngig.wiederherstellen.einschr%C3%A4nkungen"></a>3.2.5.3.2. Restrictions

There are some restrictions on the enhancement of the "Undo / Restore" functionality for the views mentioned. These restrictions are listed in the following:

- Only actions which you have performed can be undone. Actions automatically performed by the system cannot be undone individually and therefore, they are not recorded as entries in the history. The actions performed automatically by the system are undone together with their triggering action by the system.
- Actions that include a status change of an object cannot be undone. These are therefore not recorded in the history.
- The only actions that can be undone are those that you have performed since the last time the object was saved. Saving or closing the editor deletes the respective history.
- Actions that cause saving to occur cannot be undone and are therefore not recorded in the history.
- Only actions can be restored that were also previously undone, thus those that are stored in the editor history.
- Histories are only recorded for editors. There is no history for actions in dialogs.

###### <a id="r%C3%BCckg%C3%A4ngig.wiederherstellen.elemente"></a>3.2.5.3.3. Supported Interface Elements

- **Text field:** As an action, text content changes are recorded here in the history. If you just changed the content in the text field, then the following difference applies when pressing "CTRL-Z": if you already made changes then the changes in the current text field will be undone. If no change was made, then the last entry in the history will be undone.
- **Selection field:** The selection of a value in a selection field is recorded as a change in the history. This only applies if the value differs from the previous selection. The change of a selection in selection fields often results in a cascade of actions, for example, changing the range of values for another selection field or filling a text field with a specific value. These cascading actions are not listed as independent entries in the history, but rather are stored as invisible sub actions in the history. Since these actions run automatically and are linked directly to your previous action, they can also not be undone separately. The sub-actions not visible to you are likewise reset if the "main" action is undone.
- **Date field:** here date changes are recorded in the history as an action. A trigger for this is the positive confirmation (OK button) of the date selection dialog applies, or if a manual date input has occurred, exiting the date field with the cursor.
- **Checkbox:** Setting or removing the check mark in a check box is recorded as an action in the history.
- **Options field:** Options fields are used in editors to select exclusively between different options. Setting an options field always causes the other options fields in the group to be deactivated. This collective action will be recorded in the history as one thing.
- **Table:** Tables are inserted in the ODIS Creator system in two different ways. On the one hand, the rows in a table can be ["edited"](3-2-5-editor.md#r%C3%BCckg%C3%A4ngig.wiederherstellen.elemente.tabelle.editierbar) directly in the editor and on the other hand, there are tables where you can only ["add or delete"](3-2-5-editor.md#r%C3%BCckg%C3%A4ngig.wiederherstellen.elemente.tabelle.hinzuf%C3%BCgen) rows, but the content of a row is edited using a sub-editor. The actions to add or delete lines in the table are recorded separately from the above mentioned applications in the history. The actions to revise an existing line are different from both applications.

  - **Use of table that can be edited in the editor:**

    This form of table usage can be found mostly in the sub-editors. The lines of the tables in this form can be changed directly in the editor. For example, this applies to the variant rule in the diagnostic object editor or the suspicion/variant rule in the sub-editor. This means that the changes to individual cells in a table are also recorded as actions in the editor history.

    The table cells are edited using selection fields or text fields. The changes are almost always applied first as an action in the history, if you exit the cells with the cursor. To some extent, you can also change cells through drag and drop. After dropping objects in a cell, the cursor will automatically be removed from the cell and the action will be recorded in the history as described above (exiting the cell).
  - **Use of table where lines can only be added or deleted:**

    The lines of tables in this usage form can only be changed using a sub-editor. For example, this applies to the suspicion rule list in the diagnostic object editor or the measured values in a measured values table editor. This means that only the change to a complete line is stored as an action to be undone for the history. Trigger for recording the action in the history is the positive confirmation of the sub-editor, for example using the "Apply" button. Closing a sub-editor using the "Cancel" button, for example, causes no change in the history of the main editor, which the edited table is in.

    There is the option in diagnostic objects to create new table lines per drag and drop to the suspicion rule list table. After dropping objects in the table, an entry in the history will be created. This entry includes all new suspicion rules created by the drop. The automatic creation of suspicion rules by dragging and dropping to the suspicious rules list table can be undone by pressing "CTRL-Z" one time. It does not matter if only one new suspicion rule or multiple suspicion rules were created automatically; there is always only one single action in the history.
- **List:** In relation to the history, the properties are the same for lists as they are for tables. Both buttons to add or delete entries are also here with one exception: the elements from the lists cannot be revised, therefore a list is, in principle, a one-column table for which the entries cannot be revised.

###### <a id="r%C3%BCckg%C3%A4ngig.wiederherstellen.bef%C3%BCllung"></a>3.2.5.3.4. Populating the History

- **Text field:** when entering texts, it does not make sense to undo the entry of an individual letter. For this reason, the typing of letters on the keyboard is not considered an event for text fields. The only clear indication that you have completed editing a text field is that the cur exits the edited text field. This result is used to record the change of text field content in the history. An exception for text fields is pressing "CTRL-Z" while the cursor is in the text field and the content was already changed. By pressing "CTRL-Z", the changed content of the text field is first stored in the history. Then the actual execution of the action "CTRL-Z" occurs and the text field is reset back to the original condition. This intricate process is technically necessary, so that the history is complete.
- **Date field:** a date field is set up as a text field. For this reason, it also "inherits" the behavior when exiting the field with the cursor as well as when pressing "CTRL-Z". This event also occurs for date fields when confirming the closing of the date selection dialog. This event is also used here to record the content change in the history.
- **Table:** For tables in ODIS Creator, there are three use cases in total. Adding as well as deleting lines in a table can be done using the buttons at the right upper edge. For both these actions, the action to add an entry in the history is clearly defined - pressing on one of the buttons.

  The third use case is the revision of an existing line within a table. A difference must be made here again between both table usage options in ODIS Creator. In tables where the lines can only be changed using a sub-editor, closing the sub-editor is used as an event in order to enter an action into the history. For this type of table, the whole line is always considered a unit in the history. For tables where the lines can be edited directly in the editor, changes are not considered as the whole line, but rather as individual cells. Changes to a cell are recorded as individual actions in the history. The event applied to this is exiting the cell with the cursor.
- **Lists:** Lists are identical in their properties to the tables described above, but the entries in the lists cannot be revised themselves.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="3-2-4-properties-window.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="3-2-program-structure.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="3-2-6-tables-and-lists.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">3.2.4. Properties window </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 3.2.6. Tables and Lists</td></tr></table>
