[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.5. Default Texts](5-5-default-texts.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.5.2. Manage Default Texts</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-5-1-manage-text-groups.md">Prev</a> </td><th align="center" width="60%">5.5. Default Texts</th><td align="right" width="20%"> <a accesskey="n" href="5-6-text-library.md">Next</a></td></tr></table>

---

#### <a id="standard.bearbeiten"></a>5.5.2. Manage Default Texts

The editor can be seen in [Figure 76, “Default text editor”](5-5-2-manage-default-texts.md#figure.standard.neu "Figure 76. Default text editor"). The user must give a text ID for the default text and can specify the default text content in the lower field.

<a id="figure.standard.neu"></a>

![Default text editor](images/neuerStandardtext.png)

**Figure 76. Default text editor**

[Table 22, “Default Text Functions”](5-5-2-manage-default-texts.md#table.standard "Table 22. Default Text Functions") describes the possible functions of the default texts.

<a id="table.standard"></a>

<table border="1" summary="Default Text Functions"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Function</th><th align="left">Description</th></tr></thead><tbody valign="top"><tr><td align="left" valign="top">New default text</td><td align="left" valign="top">If you have selected a specific text group or a default text, then you can create a new default text through the "Default text" context menu. This action is also available in the global menu under "Insert &gt; Default text".</td></tr><tr><td align="left" valign="top">New default text with table</td><td align="left" valign="top">With this action you can create an enhanced default text with tables and special characters. This action has the same conditions as "New default text". You can also find this action in the global menu under "Insert &gt; Default text with table".</td></tr><tr><td align="left" valign="top">Editing a default text</td><td align="left" valign="top">By double clicking on an entry in the navigator, you can overwrite the text. In addition to double clicking, this functionality can be accessed through the menu item "File &gt; Edit".</td></tr><tr><td align="left" valign="top">Deactivating/activating the default text</td><td align="left" valign="top">Existing default texts can be made inactive. This function can be found in the context menu "Set to inactive", if one or more default texts are marked. It can be reached in the global menu under "Edit" &gt; "Set to inactive". Inactive default texts are no longer available to the author in the selection dialog. Inactive texts will now be grayed out in the navigator. Inactive default texts can also be reset to active at any time.</td></tr></tbody></table>

**Table 22. Default Text Functions**

  

Default texts are differentiated by "simple default texts" and "default texts with tables". The simple default texts only contain text, formatting, symbols and icons. The default texts with tables can also contain tables and special characters.

<a id="figure.standard.mittabelle"></a>

![Default text with table](images/Administration_standardtextverwaltung_standardtext_mit_tabelle.png)

**Figure 77. Default text with table**

Both default text types can be added through the context menu and the menu. You can differentiate the default text types based on their icons.

<a id="figure.standard.einfuegen"></a>

![Insert default text](images/Administration_standardtextverwaltung_standardtext_einfuegen.png)

**Figure 78. Insert default text**

Default texts with tables cannot be used and inserted at every place in ODIS Creator, in comparison to the simple default texts. For example, ODIS Creator blocks the insertion of these default texts into another table. They can also not be used in one-line text fields in the function editor.

<a id="table.hinweis.administration.standardtextverwaltung.standardtextmittabelle"></a>

<table border="1" summary="Note for Default Text with Table"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top">
<p><span class="bold"><strong>Note:</strong></span> Please check if the default text is being correctly displayed in the processing system at each location a default text is used with a table. Along with other functions, you can use the 'Print Preview" function for this in the function test.</p>
</td></tr></tbody></table>

**Table 23. Note for Default Text with Table**

<a id="figure.standard.inaktiv"></a>

![Setting Default Text to Inactive/Active](images/Standard_in_aktiv_setzen.png)

**Figure 79. Setting Default Text to Inactive/Active**

Using inactive default texts is still possible and is not completely prevented. For example, you can enter the ID of the inactive default text directly in the text editor or copy an existing function test with inactive default texts. Default texts will not be checked during a release. [Figure 79, “Setting Default Text to Inactive/Active”](5-5-2-manage-default-texts.md#figure.standard.inaktiv "Figure 79. Setting Default Text to Inactive/Active") shows the function for setting default texts to inactive/active.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-5-1-manage-text-groups.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-5-default-texts.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-6-text-library.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.5.1. Manage Text Groups </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.6. Text Library</td></tr></table>
