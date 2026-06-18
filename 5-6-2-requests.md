[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.6. Text Library](5-6-text-library.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.6.2. Requests</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-6-1-category.md">Prev</a> </td><th align="center" width="60%">5.6. Text Library</th><td align="right" width="20%"> <a accesskey="n" href="5-6-3-text-id.md">Next</a></td></tr></table>

---

#### <a id="textbib.textbeauftragungsantr%C3%A4ge"></a>5.6.2. Requests

The parent node of the various text request orders is called “Orders”.

The Text Administrator can perform the following actions on a text request:

- Text request:<a id="d4e2821"></a>accept. The Text Administrator can accept a text request. The “Accept request” context menu must be used for this. A text request can only be accepted if the Admin has not made any changes to the content.
- Text request:<a id="d4e2825"></a>decline. The “Decline request” context menu must be used for this. When declining, the Text Administrator must enter a reason for declining in the comments.

##### <a id="textbib.textbeauftragungsantragsfilter"></a>5.6.2.1. Text Request Filters

Filtering of text requests is possible in the “text library” navigator.

The filter for text requests functions the same as in other locations, such as the [editor](7-1-5-apply-filter.md "7.1.5. Apply Filter"). In the illustration that follows, the button for filtering text requests is highlighted.

<a id="figure.textbib_textantrag_filter"></a>

![Illustration: filter for text requests.](images/textbeauftragung_admin_editor.png)

**Figure 83. Text Requests Filter**

  

Entries can be filtered by the following criteria:

- Brand
- Creator (name of the creator of the entry)
- Last editor
- Editing date
- Creation date
- Status
- Status date
- Type (new entry or edited entry)

##### <a id="textbib.suche"></a>5.6.2.2. Search Function

A search function can be used to easily search for content in the text library. The illustration that follows shows the button for the search function in the library.

<a id="figure.textbib_suche"></a>

![Illustration: filter for text requests.](images/textbeauftragung_admin_editor_suche.png)

**Figure 84. Text Library Search Function**

  

The search function searches for the search term in text IDs (also working versions) and text requests (regardless of status) and displays the results. The following image shows the search dialog.

<a id="figure.textbib_suche.ergebnis"></a>

![Illustration: text library search results](images/textbeauftragung_admin_editor_suche_ergebnis.png)

**Figure 85. Text Library Search Results**

  

Double-clicking on a search result selects the associated object in the navigation tree and opens it in the corresponding editor.

##### <a id="textbib.autoerstellung"></a>5.6.2.3. Creating New Text IDs from a Text Request

The administrator has the ability to create a new Text ID directly in the text request editor using the “New Text ID” button and to automatically link it to the request. When the button is pressed, a selection dialog opens for selecting the category in which the new Text ID should be created. After confirming the selection dialog (see [Figure 86, “Category Selection Dialog”](5-6-2-requests.md#figure.textbib_kategory_auswahl "Figure 86. Category Selection Dialog")), the corresponding editor for Text IDs will open (see [Figure 89, “Text ID Object Editor”](5-6-3-text-id.md#figure.admin.textbib.textid_anlegen "Figure 89. Text ID Object Editor")). By saving the editor for the Text ID, the reference is automatically stored in the editor for the entry (similar to a drag and drop action).

<a id="figure.textbib_kategory_auswahl"></a>

![Illustration: category selection dialog for a new Text ID](images/textbib_kategorie_auswahl.png)

**Figure 86. Category Selection Dialog**

**WARNING:** the reference between the new Text ID that was created and the request only remains if the editor for the request was saved.

##### <a id="textbib.sprungtextid"></a>5.6.2.4. Jumping to a Linked Text ID

If a text ID is linked with a text request, you can jump directly to the Text ID from the text request editor. To do this, double-click the mouse in the “Text ID in OC” field.

##### <a id="d4e2894"></a>5.6.2.5. Text request status

If an action is performed on a text request using the context menu, the status changes according to the status model listed here when the action is performed successfully.

<a id="d4e2898"></a>

![Illustration: Text request status model for text requests with the “New” type](images/textbeauftragung_statusmodell_new.png)

**Figure 87. Text request status model: new**

<a id="d4e2906"></a>

![Illustration: Text request status model for text requests with the “Change” type](images/textbeauftragung_statusmodell_change.png)

**Figure 88. Text request status model: change**

<a id="d4e2914"></a>

<table border="1" summary="Overview of the text request status"><colgroup><col align="left"/><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Display</th><th align="left">Status</th><th align="left">Description</th></tr></thead><tbody valign="top"><tr><td align="left" valign="top">
<span class="inlinemediaobject"><img src="images/textorder_inpruefung.png"/></span>
</td><td align="left" valign="top">In testing</td><td align="left" valign="top">A new text request was created and is in testing for both roles. If the Text Administrator and author each decline an order or contradict when it is declined, it will change back to the “In Review” status.</td></tr><tr><td align="left" valign="top">
<span class="inlinemediaobject"><img src="images/textorder_angenommen.png"/></span>
</td><td align="left" valign="top">Accepted</td><td align="left" valign="top">The text request was accepted by the Text Administrator. The author can now definitively accept or decline a text request. If the author declines it, the status goes back to “In Review”. If the author selects the option “Keep free text” in the decline dialog, the status changes to "Discarded”. If both roles accept the text change, the status changes to “Approved”.</td></tr><tr><td align="left" valign="top">
<span class="inlinemediaobject"><img src="images/textorder_verworfen.png"/></span>
</td><td align="left" valign="top">Discarded</td><td align="left" valign="top">If a text request is discarded, the status can no longer be changed. The author can only delete the request.</td></tr><tr><td align="left" valign="top">
<span class="inlinemediaobject"><img src="images/textorder_freigegeben.png"/></span>
</td><td align="left" valign="top">Released</td><td align="left" valign="top">The “approved” status is reached if the Admin and author confirm a new text ID and a text ID is assigned to this order. If a text request is approved, the status can no longer be changed. The author can only delete the request. Text orders in this status are taken into considered during the process for automatic text substitution.</td></tr><tr><td align="left" valign="top">
<span class="inlinemediaobject"><img src="images/textorder_edit.png"/></span>
</td><td align="left" valign="top">Edit</td><td align="left" valign="top">If the Text Administrator accepts a text request with the “Change” type, the status will change to "Edit”. This status functions a type of work queue for the Administrator.</td></tr><tr><td align="left" valign="top">
<span class="inlinemediaobject"><img src="images/textorder_referenz.png"/></span>
</td><td align="left" valign="top">Add reference</td><td align="left" valign="top">If the Text Administrator and the text author accept a text request or linked text ID, the status will change to “Add reference”. This status is set to “Approved” status after a reference is set to a text ID and this is confirmed by the Administrator.</td></tr><tr><td align="left" valign="top">
<span class="inlinemediaobject"><img src="images/textorder_abgelehnt.png"/></span>
</td><td align="left" valign="top">Declined</td><td align="left" valign="top">If the Text Administrator declines a text request, the status will change to "Declined”. The author can accept or object to the declining of the text request. If there is an objection, the reason for declining must be given.</td></tr><tr><td align="left" valign="top">
<span class="inlinemediaobject"><img src="images/textorder_replace_rejected.png"/></span>
</td><td align="left" valign="top">Replacement error</td><td align="left" valign="top">If a text is not automatically replaced, the text request will have the Replacement error status. In this status, authors have the option to re-order automatic substitution by resetting the text order to the “Approved” status.</td></tr><tr><td align="left" valign="top">
<span class="inlinemediaobject"><img src="images/textorder_fertig.png"/></span>
</td><td align="left" valign="top">Complete</td><td align="left" valign="top">Editing completed. The TextID is available and free text was replaced.</td></tr></tbody></table>

**Table 24. Overview of the text request status**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-6-1-category.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-6-text-library.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-6-3-text-id.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.6.1. Category </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.6.3. Text ID</td></tr></table>
