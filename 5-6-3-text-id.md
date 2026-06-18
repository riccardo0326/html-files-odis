[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.6. Text Library](5-6-text-library.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.6.3. Text ID</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-6-2-requests.md">Prev</a> </td><th align="center" width="60%">5.6. Text Library</th><td align="right" width="20%"> <a accesskey="n" href="5-6-4-sorting-and-filtering-in-the-text-library.md">Next</a></td></tr></table>

---

#### <a id="textbib.textID"></a>5.6.3. Text ID

A text ID contains text, other text IDs or a placeholder for a variable or keyword. Special characters and ANSI characters are controlled by the category above the text ID.

##### <a id="textbib.textid.anlegen"></a>5.6.3.1. Creating a Text ID

A text ID can be created through the category node or a text ID with the **text ID** context menu entry. You can also select the **Add -> Text ID** entry in the menu instead. It will open in the [Figure 89, “Text ID Object Editor”](5-6-3-text-id.md#figure.admin.textbib.textid_anlegen "Figure 89. Text ID Object Editor") editor shown. You must specify a version comment and text content.

<a id="figure.admin.textbib.textid_anlegen"></a>

![Text ID Object Editor](images/textbib_textid_anlegen.jpg)

**Figure 89. Text ID Object Editor**

The text ID receives a text ID number from the system when saving. The number will be created according to the scheme <category number>.<serial number>.

A text ID can be copied from one category to another. In the menu, select **Edit > Copy** to do this. This is however only possible if both categories use the same additional options. For example, it is not possible to copy a text ID from a category with ANSI characters to a category without ANSI characters. A text ID can likewise not be added to a category, which contains text IDs from automatic population (for example, from a master component list import).

<a id="table.hinweis.3"></a>

<table border="1" summary="Text ID Note"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note:</strong></span> Text IDs cannot be created under categories that are automatically populated, for example, from a master component list import.</td></tr></tbody></table>

**Table 25. Text ID Note**

If you open the text ID editor in read mode, then you will see the entered text content in a preview field with the format of the superordinate category.

<a id="figure.admin.textbib.vorschau"></a>

![Text ID Content Preview](images/textbib_vorschau_textinhalt.jpg)

**Figure 90. Text ID Content Preview**

No formatting is displayed while editing text content. For text IDs in a category with additional functions ("text module", "text module (ANSI characters)" and "placeholder"), the text cannot be edited when the editor is open in write mode. Here, only used text IDs can then be replaced or be added to, or the placeholder can be changed.

In the read or write mode of a text ID, you can view the entered text with formatting and any special characters in a separate dialog through the **Preview** button in the editor. You can take the text content preview dialog out of the ODIS Creator as its own window and thus compare the different text content.

##### <a id="textbib.textid.zusatzfunktion"></a>5.6.3.2. Text ID Editor

There are different buttons in the editor for a text ID depending on the selected additional function for the category.

- **Text module:** the additional "text module" function in the text ID editor allows the **text library** and **preview** buttons to appear.
- **Text module (ANSI characters):** the additional "text module (ANSI characters)" function in the text ID editor allows the **text library** and **preview** buttons to appear.
- **Placeholder:** the additional "placeholder" function in the text ID editor allows the **placeholder** and **preview** buttons to appear.

You can select other text IDs through the **text library** button, which should be used in the current text ID. You can create a new placeholder in the text ID using the **placeholder** button.

The tables "used", "used by" and "details for translation" are given in the text ID editor. The "used" table contains text IDs that are used by the currently selected text ID. This table is only for texts IDs from a category with the additional functions "text module" and "text module (ANSI characters). The "used by" table contains text IDs which use the currently selected text ID.

Like at other locations in ODIS Creator, it is also possible to jump to the objects from the "used" and "used by" tables. For this, you will select the desired object in the respective table and it opens the corresponding navigator with the object and the object editor in read mode. It is necessary that you have the necessary rights to the target object for this.

The "details for translation" table will display the current translation status for each target language. For text modules, the respective lowest status of the corresponding, used text IDs is displayed.

##### <a id="textbib.textbaustein"></a>5.6.3.3. Using Text IDs in Text Modules

A text ID from a category with the additional "text module" function consists of various text IDs. To add a text ID to a text module, open the text module in the editor and select the "text library" button. In the open dialog, you can enter a text and text IDs will be suggested per auto completion.

<a id="figure.admin.textbib.ansi"></a>

![Dialog for editing a text module (ANSI characters)](images/textbib_textid_ansi.jpg)

**Figure 91. Dialog for editing a text module (ANSI characters)**

For a category with "text module (ANSI characters) as the additional function, you can specify the desired ANSI characters in the dialog (see [Figure 91, “Dialog for editing a text module (ANSI characters)”](5-6-3-text-id.md#figure.admin.textbib.ansi "Figure 91. Dialog for editing a text module (ANSI characters)")). You can also select text IDs through auto completion, where text content should be added.

In [Figure 91, “Dialog for editing a text module (ANSI characters)”](5-6-3-text-id.md#figure.admin.textbib.ansi "Figure 91. Dialog for editing a text module (ANSI characters)"), you will see the editing dialog for a "text module (ANSI characters)" with the applicable preview in the text ID editor.

For a category with "text module" as the additional function, you can select the desired text ID through auto completion and insert additional content separated by spaces and breaks.

<a id="figure.admin.textbib.textbaustein"></a>

![Dialog for editing a text module](images/textbib_textid_textbaustein.jpg)

**Figure 92. Dialog for editing a text module**

In [Figure 92, “Dialog for editing a text module”](5-6-3-text-id.md#figure.admin.textbib.textbaustein "Figure 92. Dialog for editing a text module"), you will see the editing dialog for a "text module" with the applicable preview in the text ID editor.

The text content of the text ID cannot be changed in the text module. You only have the option to replace the used text IDs with others or to expand it. These adjustments can be performed again through the "text library" interface.

##### <a id="textbib.platzhalter"></a>5.6.3.4. Using Placeholders in Text IDs

You can add a placeholder to a text ID. Select the **placeholder** button when text ID editor is open in write mode. The dialog to be seen will open in [Figure 93, “Dialog for editing a placeholder”](5-6-3-text-id.md#figure.admin.textbib.platzhalter "Figure 93. Dialog for editing a placeholder"), in which the placeholder name as well as a German and English comment must be entered.

<a id="figure.admin.textbib.platzhalter"></a>

![Dialog for editing a placeholder](images/textbib_textid_platzhalter.jpg)

**Figure 93. Dialog for editing a placeholder**

%<VariableName> is then used in the text ID preview instead of the text, which is also seen in the above image.

##### <a id="textbib.autovervollstaendigung"></a>5.6.3.5. Auto Completion

The selection of a text ID through auto completion is given as an independent dialog (see [Figure 94, “Dialog for Auto Completion Results”](5-6-3-text-id.md#figure.admin.textbib.autov "Figure 94. Dialog for Auto Completion Results")), that will open at the same time. Functionalities, such as favorites and bookmarking, are available per the context menu for the text library.

<a id="figure.admin.textbib.autov"></a>

![Dialog for Auto Completion Results](images/textbib_textid_autovervollstaendig_ergebnis.jpg)

**Figure 94. Dialog for Auto Completion Results**

In [Figure 94, “Dialog for Auto Completion Results”](5-6-3-text-id.md#figure.admin.textbib.autov "Figure 94. Dialog for Auto Completion Results"), you will see an input dialog for a text module and the applicable auto completion list.

If the dialog is not open, it will open automatically as soon as something is typed in either of the dialogs for recording a text module or an ANSI text module. The following rules apply for this:

- A search will always start if the user has entered at least one word or word fragment followed by a space. The space will always act as the trigger.
- All search terms that begin with # are interpreted as a category name or part of a category name. This allows the text ID to be narrowed down even more to one or more categories. Depending on the set user interface language, it will search for the German or English category names for this. Example: the author enters "#F component #Ha". It will search for all text IDs that contain the word component as a word or portion of the word and is assigned to a category that begins with F or Ha. The search for text IDs and categories is not case sensitive.
- All words left of the current cursor position are always entered as the search parameter. It only ever considers the words that are after the last period, line break or the last text ID.
- There are three adjusters that the group administrator can use to set parameters, which can be used to adjust settings for individual brands.

  - **Linking of search terms:** you can select if search terms should be linked with “AND” (the text ID must contain all terms) or with “OR” (the text ID must contain at least one of the terms). The default setting is to list both search options.
  - **Automatic use of wildcards:** you can select if wildcards should be added before and after each search automatically. The default setting is to list both search options.
  - **Maximum number of hits:** you can select the maximum number of hits (including entries in favorites) that should be displayed as search results.
- If present, results will always be shown in the dialog even if the number of hits without favorites includes more elements than the limit that is set. If the search finds too many hits, only the X hits with the highest score are shown (X is the selected limit).
- It will automatically search for text IDs that contain the entered terms. Depending on the setting (“automatic use of wildcards”, see above), this also applies for part of a word. Entering additional wildcards is not necessary. Entered wildcards are understood as standard search symbols, for example, "steered" and "understeered" will be found with "steer".
- The search is not case-sensitive, meaning it does not differentiate between capital and lower case letters. For example, depending on the setting (“automatic use of wildcards”, see above), the search will find both “control module” and “engine control module” if you search for “control”.
- The terms can be entered in any order, but depending on the setting (“linking of search terms” and “automatic use of wildcards”, see above), either all (partial) terms may need to be present in a text ID. For example, “component follow” will also find “following illustrated component”.
- The user can apply a text ID by double clicking.
- When transferring a text ID, only the characters from the cursor position up to the last period, line break or text ID will be replaced by the selected text ID text. If a text area is marked, then only the marked text will be replaced, regardless of any periods, line breaks, or text IDs that are marked.
- The opening of the dialog will not inhibit typing. Therefore, the focal point remains in the current input field and the dialog at the same time as when the non-modal dialog opens.

Only text IDs that are active, approved and completely translated are available for selection in the auto completion. Text requests are an exception to this. They can be used by their author directly after creating them. If this dialog is called up when authoring a "text module" or "text module (ANSI character)", then the displayed text IDs may also be only default text IDs or placeholders, however no "text modules" or "text modules (ANSI characters)".

All found text IDs are displayed in a tree diagram. The upper level represents categories and the second represents text IDs. In contrast to the "text library" navigator, the text ID numbers are not displayed but rather the plain text in the data language currently set is displayed here. Only category nodes are displayed, for which text IDs were found. These are closed when opening the dialog, however they can be individually opened when needed.

You can move the selection of a text ID upward or downward in the tree structure using both arrow buttons. If the tree structure is too large for the current view, then a scroll bar will appear. If this is the case, you can move the structure with the mouse upward or downward. The current selection will remain selected during this. You can change the size of the whole dialog, however there is a set minimum size that you cannot go below.

<a id="table.hinweis.Autovervollstaendigung"></a>

<table border="1" summary="Data Language Note"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note: </strong></span> in the auto propagation dialog, the text IDs are displayed in the data language set in ODIS Creator (see <a class="xref" href="9-3-data-language.md" title="9.3. Data Language">Section 9.3, “Data Language”</a>).</td></tr></tbody></table>

**Table 26. Data Language Note**

###### <a id="antrag.textbib"></a>5.6.3.5.1. Requests

In the text library selection dialog, authors have the option of using their own newly-created text IDs without having them go through the approval process. When selecting a requested text in the text selection dialog, the free text will be entered in the usage location accordingly. Replacing the requested text with a text ID results in replacing the text in all areas where it used with the text ID.

<a id="table.hinweis.Antragautovervollstaendigung"></a>

<table border="1" summary="Request Notes"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note: </strong></span>the auto-complete dialog only shows the author’s own texts that they have requested, not those from other authors.</td></tr></tbody></table>

**Table 27. Request Notes**

###### <a id="fav.textbib"></a>5.6.3.5.2. Favorites

There is the option to mark text IDs as favorites (see [Figure 95, “Favorites in the Auto Completion Results”](5-6-3-text-id.md#figure.admin.textbib.autov.fav "Figure 95. Favorites in the Auto Completion Results")). These will always be displayed in the dialog at the topmost position. Otherwise, all entries shown (category and text IDs) are sorted according to their score (or alphanumerically for those with identical scores), with text IDs being sorted within their respective category. The currently set "favorites" are always saved when the dialog is closed and will be displayed again when the next selection is made. They were also be saved when ODIS Creator restarts. The text IDs for the favorite nodes are always displayed regardless of the search parameters. Text IDs that are set to inactive are no longer displayed in the favorites, however will remain stored as a favorite in case it is reactivated later.

<a id="figure.admin.textbib.autov.fav"></a>

![Favorites in the Auto Completion Results](images/textbib_autovervollstaendigen_favoriten.JPG)

**Figure 95. Favorites in the Auto Completion Results**

You can manage your favorites under **Help > Settings > Text ID Favorites Settings**. There you can remove favorites using the context menu or add new ones using the search function.

<a id="figure.admin.textbib.fav"></a>

![Managing Favorites](images/benutzervorgaben_favoriten.png)

**Figure 96. Managing Favorites**

###### <a id="d4e3214"></a>5.6.3.5.3. Pin Function

In addition to marking favorites, there is also the "Pin" function (see [Figure 97, “Pinning Results in the Auto Completion”](5-6-3-text-id.md#figure.admin.textbib.autov.festp "Figure 97. Pinning Results in the Auto Completion")). When pinning, the selected text IDs within the category will be moved upward. In the image, the first three text IDs are pinned under the components category (code behind). This resorting is only temporary for the currently open selection dialog and will be discarded when the dialog is closed or when conducting a new search. A new search will then begin when the user starts the auto completion of a text ID in a different input field than the current one. Until then the bookmarked entries will be kept even if they are no longer in the results after the search parameters have changed. The “permanently pinned” text IDs are sorted among themselves based on their score.

<a id="figure.admin.textbib.autov.festp"></a>

![Pinning Results in the Auto Completion](images/textbib_autovervollstaendigen_festpinnen.JPG)

**Figure 97. Pinning Results in the Auto Completion**

##### <a id="textbib.statusmodell"></a>5.6.3.6. Text ID Status Model

A text ID can assume different statuses. A newly created text ID has the status "in progress". As soon as the text administrator completes the compilation, they can start the release process. First of all, a text ID completion message is given when all tests have been successfully performed. Then the text administrator can release the text ID. The completion message and release can also be initiated in one step by the text administrator; this will also release the text ID immediately when there is a successful completion message.

A text ID can be edited when in the "released" status and then reverts to the "in progress" status, and the version is automatically increased by one. The old version can continue to be used in the released status.

A consistency check will be performed when a completion message for a text ID is given. During this consistency check, which can also be initiated manually by the text administrator, the following items will be checked:

- Check if all required data is in place. => If negative, this test receives the "Error" status for consistency.
- It checks if all the used text IDs are sill active for text modules and ANSI text modules. => If negative, this test receives the "Warning" status for consistency.
- It checks if only text IDs without a special function, placeholders, spaces, tabs and line breaks are used in text modules and ANSI text modules. => If negative, this test receives the "Error" status for consistency.

If separate consistency check steps for an error, a warning or a note occurs, then a corresponding entry will be made in a test log. The created test log matches the layout and appearance of that in editing. If no discrepancies result from this check, then no test log will be created.

##### <a id="textbib.deaktivieren"></a>5.6.3.7. Deactivating/Activating Text IDs

A text ID can be deactivated and activated. To do this, select "Activate" or "Deactivate" in the text ID context menu. A text ID that is inactive will no longer be available at the usage locations. Usage continues to be allowed at the usage locations still available.

##### <a id="textbib.reklamation"></a>5.6.3.8. Make a Text ID Complaint

The translation of a text ID can be contested like that of an editorial object. See [Section 7.1.14, “Editorial Object Complaints”](7-1-14-editorial-object-complaints.md "7.1.14. Editorial Object Complaints"). Note that the rolls and the teams refer to the [text administrator](3-3-1-description-of-roles.md "3.3.1. Description of Roles") here.

##### <a id="textbib.textid.beantragen"></a>5.6.3.9. Request Text IDs

New text IDs can be requested using the text library selection dialog. The dialog for requesting a new text ID is reached using the “New” button in the text library selection dialog.

<a id="figure.auswahldialogneu"></a>

![Illustration: Selection dialog with “New” option](images/textbib_textid_neu_option.png)

**Figure 98. New Button in the Selection Dialog**

Note: a text entry can only be created or linked in objects that have been saved at least once and that were opened in write mode. For example, if a function test is open in read-only mode, the “New” button will be inactive. If a diagnostic object is still not saved, there will first be a dialog asking if the object should be saved.

Note: replacing a free text with a text ID using a text entry is subject to certain rules. The replacement will *not* be made if the following characters directly follow or are after the text to be replaced (without spaces between):

- Numbers
- Letters (upper case or lower case)
- ,
- „
- "
- (
- )
- <
- >

The “Text ID to be requested” field in the “Requesting a Text ID” dialog is mandatory. The content of the new text ID is specified here. The usage locations can also be selected in the “Usage location” area. It is an optional field, so it is also possible to leave it blank. The “Comments” field is also optional. The “Request type”, “Text type”, and “Text ID in OC” fields are automatically populated.

<a id="figure.beantragungsdialog"></a>

![Illustration: Dialog for requesting a new text ID](images/textbib_textid_neu_dialog.png)

**Figure 99. Request Dialog for New Text IDs**

##### <a id="textbib.textid.aenderung"></a>5.6.3.10. Requesting a Text ID Change

Changes to text IDs can be requested using the text library selection dialog. The dialog for requesting a text ID change is reached using the “Change” button in the text library selection dialog.

<a id="figure.auswahldialogaendern"></a>

![Illustration: Selection dialog with “Change” option](images/textbib_textid_aenderungsoption.png)

**Figure 100. Change Button in the Selection Dialog**

The “Text ID to be requested” field in the “Requesting a Text ID” dialog is mandatory. The content of the desired change to the text ID is specified here. The “Comments” field is optional. The “Request type”, “Text type”, and “Text ID in OC” fields are automatically populated.

<a id="figure.aenderungsdialog"></a>

![Illustration: Dialog for requesting a text ID change](images/textbib_textid_aenderungsdialog.png)

**Figure 101. Request Dialog for a Text ID Change**

##### <a id="textbib.textid.beantragen.ausdruck"></a>5.6.3.11. Request Text IDs in Expressions

New text IDs are added to expressions using the text library selection dialog. This does not occur using the auto-complete feature, but is triggered using the text library button in the expression dialog. If the text library button is selected in the expression dialog, the text library expression dialog will appear in a new window. A text ID can be entered using the New button (changing a text ID is similar). To use the new text ID, it must be selected from the selection dialog by double-clicking to have it displayed within the expression dialog.

##### <a id="textbib.textid.loeschen"></a>5.6.3.12. Deleting Text IDs

Text IDs that are no longer used in any version and were deactivated, are regularly deleted from the system through a job.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-6-2-requests.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-6-text-library.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-6-4-sorting-and-filtering-in-the-text-library.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.6.2. Requests </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.6.4. Sorting and Filtering in the Text Library</td></tr></table>
