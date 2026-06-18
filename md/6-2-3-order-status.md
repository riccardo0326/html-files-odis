[ODIS Creator Help](odis-creator-help.md) > [6. ODIS Creator Order Management Process](6-odis-creator-order-management-process.md) > [6.2. Orders](6-2-orders.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">6.2.3. Order Status</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="6-2-2-ad-hoc-orders.md">Prev</a> </td><th align="center" width="60%">6.2. Orders</th><td align="right" width="20%"> <a accesskey="n" href="6-2-4-usage-locations-dialog-in-order-management.md">Next</a></td></tr></table>

---

#### <a id="auftragsstatus"></a>6.2.3. Order Status

Order headers and order steps can run through various statuses while being processed by the "author" and "editing coordinator". The current status is displayed in the navigator by an additional symbol in the small box on the lower left side. This small symbol is the same for ad hoc orders, scheduled orders and order steps. The complete symbols in the "display" column in the following table are displayed for ad hoc orders (left), scheduled orders (right) and order steps (second line).

<a id="table.auftragsstatus"></a>

<table border="1" summary="Order Status Overview"><colgroup><col align="left"/><col align="left"/><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Display</th><th align="left">Status</th><th align="left">Description</th><th align="left">Editor</th></tr></thead><tbody valign="top"><tr><td align="left" valign="top">
<p><span class="inlinemediaobject"><img src="images/taskhead_adhoc_inDef.gif"/></span> <span class="inlinemediaobject"><img src="images/taskhead_planed_inDef.gif"/></span></p>
<p><span class="inlinemediaobject"><img src="images/taskstep_adhoc_inDef.gif"/></span> <span class="inlinemediaobject"><img src="images/taskstep_planed_inDef.gif"/></span></p>
</td><td align="left" valign="top">Defining</td><td align="left" valign="top">The orders was just created. In this status, only a name must be given.</td><td align="left" valign="top">Authors for ad hoc orders and editing coordinators for scheduled orders</td></tr><tr><td align="left" valign="top">
<p><span class="inlinemediaobject"><img src="images/taskhead_adhoc_def.gif"/></span> <span class="inlinemediaobject"><img src="images/taskhead_planed_def.gif"/></span></p>
<p><span class="inlinemediaobject"><img src="images/taskstep_adhoc_def.gif"/></span> <span class="inlinemediaobject"><img src="images/taskstep_planed_def.gif"/></span></p>
</td><td align="left" valign="top">Defined</td><td align="left" valign="top">
<p>No other specifications are necessary for this status for ad hoc orders. So that a scheduled order can be set to this status [defined], the start and end date as well as the responsible team must be specified in addition to the name. A defined scheduled order is visible for authors from the scheduled start date.</p>
</td><td align="left" valign="top">Authors for ad hoc orders and editing coordinators for scheduled orders</td></tr><tr><td align="left" valign="top">
<p><span class="inlinemediaobject"><img src="images/taskhead_adhoc_inProcess.gif"/></span> <span class="inlinemediaobject"><img src="images/taskhead_planed_inProcess.gif"/></span></p>
<p><span class="inlinemediaobject"><img src="images/taskstep_adhoc_inProcess.gif"/></span> <span class="inlinemediaobject"><img src="images/taskstep_planed_inProcess.gif"/></span></p>
</td><td align="left" valign="top">In processing</td><td align="left" valign="top">As soon as an editorial object is worked on within an order, ODIS Creator automatically sets the status to "processing".</td><td align="left" valign="top">Authors when editing an editorial object within a specific order</td></tr><tr><td align="left" valign="top">
<p><span class="inlinemediaobject"><img src="images/taskhead_adhoc_finished.gif"/></span> <span class="inlinemediaobject"><img src="images/taskhead_planed_finished.gif"/></span></p>
<p><span class="inlinemediaobject"><img src="images/taskstep_adhoc_finished.gif"/></span> <span class="inlinemediaobject"><img src="images/taskstep_planed_finished.gif"/></span></p>
</td><td align="left" valign="top">Complete</td><td align="left" valign="top">Order steps are reported as finished by the authors if all required editorial objects are created or changed and a risk release was performed. If the last order step in an order header is completed, the order header is also completed.</td><td align="left" valign="top">Authors</td></tr></tbody></table>

**Table 30. Order Status Overview**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="6-2-2-ad-hoc-orders.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="6-2-orders.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="6-2-4-usage-locations-dialog-in-order-management.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">6.2.2. Ad Hoc Orders </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 6.2.4. Usage Locations Dialog in Order Management</td></tr></table>
