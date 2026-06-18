[ODIS Creator Help](odis-creator-help.md) > [6. ODIS Creator Order Management Process](6-odis-creator-order-management-process.md) > [6.3. Text request](6-3-text-request.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">6.3.3. Text request status</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="6-3-2-text-request-filters.md">Prev</a> </td><th align="center" width="60%">6.3. Text request</th><td align="right" width="20%"> <a accesskey="n" href="6-4-translation.md">Next</a></td></tr></table>

---

#### <a id="d4e4499"></a>6.3.3. Text request status

If an action is performed on a text request using the context menu, the status changes according to the status model listed here when the action is performed successfully.

<a id="d4e4503"></a>

![Illustration: Text request status model for text requests with the “New” type](images/textbeauftragung_statusmodell_new.png)

**Figure 145. Text request status model: new**

<a id="d4e4511"></a>

![Illustration: Text request status model for text requests with the “Change” type](images/textbeauftragung_statusmodell_change.png)

**Figure 146. Text request status model: change**

<a id="d4e4519"></a>

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

**Table 32. Overview of the text request status**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="6-3-2-text-request-filters.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="6-3-text-request.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="6-4-translation.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">6.3.2. Text Request Filters </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 6.4. Translation</td></tr></table>
