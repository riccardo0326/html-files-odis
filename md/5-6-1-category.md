[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.6. Text Library](5-6-text-library.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.6.1. Category</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-6-text-library.md">Prev</a> </td><th align="center" width="60%">5.6. Text Library</th><td align="right" width="20%"> <a accesskey="n" href="5-6-2-requests.md">Next</a></td></tr></table>

---

#### <a id="textbib.kategorie"></a>5.6.1. Category

A category is the parent node of various text IDs. All text IDs for a category have a standard format and the same permitted usage locations.

##### <a id="textbib.kategorieanlegen"></a>5.6.1.1. Create Category

A category can be created using the text library navigator in the category editor. To do this, select **Insert > Category** in the menu or **Category** in the context menu.

In the open editor (see [Figure 81, “Object editor for a category”](5-6-1-category.md#figure.admin.textbib.kategorie_anlegen "Figure 81. Object editor for a category")), you must enter a name in German as well as English and give a description. Furthermore, you can select if the text IDs from this category should have an additional function. To activate the additional function, select the checkbox and one of the three additional functions:

- Text Module
- Text Module (ANSI Characters)
- Placeholder

The description entered for a category will be displayed as a tool tip for the category in the "text library" and "text library settings" navigator.

<a id="figure.admin.textbib.kategorie_anlegen"></a>

![Object editor for a category](images/textbib_kategorie_anlegen.jpg)

**Figure 81. Object editor for a category**

In a category editor, you will see the text IDs assigned to this category. The following information is displayed for each text ID:

- Text ID
- Plain text
- Status
- Status date
- Consistency status
- Translation status
- Last revision
- Last editor
- Creation date
- Creator

The plain text is displayed in the corresponding data language that is set as long as it is available. Otherwise the plain text will be displayed in the authoring language.

##### <a id="textbib.zusatzfunktion"></a>5.6.1.2. Additional Functions for a Category

A category with the additional function option possesses one of the following three functions:

- Text Module
- Text Module (ANSI Characters)
- Placeholder

The features of these additional functions for categories and the associated text IDs are described in the following.

###### <a id="textbibi.textbaustein"></a>5.6.1.2.1. Text Module

If the "text module" additional function was selected in a category, then the values for text format are set to the default settings (front = Arial, small, black) and no changes are permitted. If the "text module" additional function in the editor category is selected later, then the format values already set are automatically reset to the default values by the system. The reason is that text IDs for a text module category are not given a unique format, but rather the format of the used individual text IDs is kept. However, the selection of a special character is still allowed.

If a text ID for a text module category (see [Figure 92, “Dialog for editing a text module”](5-6-3-text-id.md#figure.admin.textbib.textbaustein "Figure 92. Dialog for editing a text module")) is edited, then editing the text content is not possible in the editor, however the **text library** interface is active. The user can record free text in the dialog that opens and thus initiate the auto population (see [Section 5.6.3.5, “Auto Completion”](5-6-3-text-id.md#textbib.autovervollstaendigung "5.6.3.5. Auto Completion")) to select a text ID. In the dialog that opens for selecting existing text IDs, only text IDs will be offered that are released and fully translated and are neither text modules nor ANSI text modules. Double-clicking on a text ID will transfer it to the position where the cursor was beforehand. The text ID will not be abbreviated, but rather will be displayed as text in the data language that is currently set. It is not possible to edit this text. Any character input within the text ID will be ignored. However, you can layout multiple text IDs among each other according to your preferences by inputting spaces, tabs and line breaks. No formatting is used for this however.

When transferring the new text, all text IDs are replaced by their respective plain text and formatted in the preview. Thereby every text ID maintains their unique format that corresponds to its category, including any special characters. Since a special character can be selected in the text module category, this is likewise also displayed in the preview.

###### <a id="textbib.zusatz.ansi"></a>5.6.1.2.2. Text Module (ANSI Characters)

If the "text module" additional function was selected in a category, then the values for text format are set to the default settings (font = Arial, small, black) and no changes are permitted. The text administrator can change this value at any time. However no special characters are permitted and the corresponding checkboxes and option fields are deactivated. If the "text module (ANSI characters)" additional function should be selected later, then the format values already set are maintained and special characters are automatically reset by the system.

Only existing text IDs without a special function or placeholder can be used in text modules (see [Figure 91, “Dialog for editing a text module (ANSI characters)”](5-6-3-text-id.md#figure.admin.textbib.ansi "Figure 91. Dialog for editing a text module (ANSI characters)")). These must be released and translated. Only then are they available in the text ID selection dialog. For ANSI text modules, the format of the used text ID is ignored and replaced by the ANSI text module format.

The edit corresponds exactly to that of the text modules (see [Section 5.6.1.2.1, “Text Module”](5-6-1-category.md#textbibi.textbaustein "5.6.1.2.1. Text Module")) with the following differences:

- In addition to the conditions given in the text ID selection dialog, only text IDs from categories are given, that do not use special characters or they use either a period or an ellipsis.

- In the editor dialog, you can also select one of the ANSI characters: danger, warning, caution, note or information. The corresponding label for the icons is displayed as the tool tip.

- When applying the compiled ANSI text modules, the format of the used text IDs is ignored in the text ID editor preview and instead of that, all texts are displayed according to the format of the ANSI text module and of the selected text ID-specific ANSI character.

###### <a id="textbib.zusatz.platzhalter"></a>5.6.1.2.3. Placeholder

If the "placeholder" additional function was selected in a category, then the values for text format are set to the Arial, small and black font settings. The text administrator can change these values to anything, however no special characters are permitted and the respective checkboxes and option fields are deactivated. If the "placeholder" additional function should be selected later, then the format values already set are maintained and special characters are automatically reset by the system. Placeholders are not allowed at every usage location that can be selected in the editor view. Therefore the following usage locations cannot be selected:

- Equipment Network
- Knowledge base
- Knowledge base/Questions
- Function Library
- Supplemental documents

If a text ID for a placeholder category is edited, then editing the text content is not possible in the editor, however the placeholder button is active. When activated, the dialog opens (see [Figure 93, “Dialog for editing a placeholder”](5-6-3-text-id.md#figure.admin.textbib.platzhalter "Figure 93. Dialog for editing a placeholder")), in which you have to specify the name of the placeholder. Furthermore, you must still give a German and an English comment. All three fields are required fields. The placeholder does not rely on a type, so that no further specification is possible.

##### <a id="textbib.einstellungen"></a>5.6.1.3. Editing Category Settings

After you have created the category in the "text library" navigator, then you can define the text format and the usage locations in the "text library settings". The category settings editor will open when you double click on a category.

<a id="figure.admin.textbib.kategorie_einstellen"></a>

![Category properties](images/textbib_kategorie_einstellungen.png)

**Figure 82. Category properties**

You will see the editor in [Figure 82, “Category properties”](5-6-1-category.md#figure.admin.textbib.kategorie_einstellen "Figure 82. Category properties"), in which you can define the text format and the usage locations for a category. The default values for the text format when creating a new category are font = Arial, font size = small and font color = black, as long as no additional function was selected. To some extent, there are other default formats when there are additional functions in categories. See [Section 5.6.1.2, “Additional Functions for a Category”](5-6-1-category.md#textbib.zusatzfunktion "5.6.1.2. Additional Functions for a Category").

It is not possible to select the usage locations of the editing view, if the format deviates from the default format. As long as you have selected the editing view usage locations and have set another format, then the editing view usage locations will be deactivated.

##### <a id="textbib.kategorieloeschen"></a>5.6.1.4. Deleting a Category

A category can only be deleted if it does not contain any text IDs. The categories can then be removed in the "text library" navigator using the **Delete** entry in the context menu.

##### <a id="textbib.vorbefuelltekategrien"></a>5.6.1.5. Preset Categories

There are several categories which will automatically contain text IDs from the master components list import. For these categories, you cannot create any additional text IDs manually. The following categories cannot be added to manually:

- "Components (code in front)" (Category - Number: 016)
- "Components (code behind)" (Category - Number: 017)
- "Assembly (code in front)" (Category - Number: 021)
- "Assembly (code behind)" (Category - Number: 022)
- "Tools (code in front)" (Category - Number: 023)
- "Tools (code behind)" (Category - Number: 024)

The translations of the master component list terms are inserted as translations for the corresponding texts. The translation status created during the master component list import or changed texts is always set to "Done" regardless of the amount of existing translations in the master component list.

For the subsequent master component list imports, the changes are applied to the corresponding categories in the text library:

- If an existing component designation contains changed source language text content during a master component list import, the corresponding texts in the text library are also updated. A new version with the changed source language text is created respectively. If the source language portion of the master component designation does not change and only the changes were applied to the translations, then no new version is created and the adjustments in the translations will be applied to the current version.
- For new master component designations of the component and assembly type, new texts will be created in the associated text library categories.

"System (automatic)" is entered for the attributes "Last editor" and "Creator" for all texts in the text library that were created or changed automatically by ODIS Creator during the master component list import.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-6-text-library.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-6-text-library.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-6-2-requests.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.6. Text Library </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.6.2. Requests</td></tr></table>
