[ODIS Creator Help](odis-creator-help.md) > [6. ODIS Creator Order Management Process](6-odis-creator-order-management-process.md) > [6.2. Orders](6-2-orders.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">6.2.1. Scheduled Orders</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="6-2-orders.md">Prev</a> </td><th align="center" width="60%">6.2. Orders</th><td align="right" width="20%"> <a accesskey="n" href="6-2-2-ad-hoc-orders.md">Next</a></td></tr></table>

---

#### <a id="geplante.auftraege"></a>6.2.1. Scheduled Orders

Scheduled orders are created and managed by the editing coordinators and worked on by the authoring teams. These enable a long-term plan and coordination of the editorial process with external deadlines, such as the staggered market introduction of a vehicle in specific target markets.

##### <a id="geplante.auftraege.anlegen"></a>6.2.1.1. Creating Orders

An order consists of an **order header**, that contains all of the fundamental information for a topic. This includes the start and end deadline, the market introduction deadline for individual markets, the market name, and a comment. Besides the name, only the start deadline, end deadline and the market name must be entered. All other information can be entered when necessary. To create a new order header, click on the **Insert** and then **Scheduled order header** [buttons](2-2-general-definitions-and-glossaries.md#schaltflaeche) in the [menu bar](2-2-general-definitions-and-glossaries.md#menuleiste) ([Figure 120, “Inserting Order Headers”](6-2-1-scheduled-orders.md#figure.auftragskopf.einfuegen "Figure 120. Inserting Order Headers")). A corresponding button can also be accessed through the [context menu](2-2-general-definitions-and-glossaries.md#kontextmenu) for the order navigator ([Figure 121, “Order Header Context Menu”](6-2-1-scheduled-orders.md#figure.auftragskopf.kontext "Figure 121. Order Header Context Menu")).

<a id="figure.auftragskopf.einfuegen"></a>

![Image: inserting order headers](images/auftragskopf_einfuegen.png)

**Figure 120. Inserting Order Headers**

Additional **order steps** can be assigned to a scheduled order. Each order step can therefore contain other deadlines within the deadline time frame given in the order header and can be assigned to another authoring team to be processed. This makes it possible to coordinate the work of a specialized authoring team within an order. A scheduled order step is only visible to the authoring team if the start date has been reached. If the order step has not been completed yet by the end deadline, this is specifically highlighted. To create an order step, mark the order header in the order navigator and click on the **Insert** and **Scheduled order step** [buttons](2-2-general-definitions-and-glossaries.md#schaltflaeche) in the [menu bar](2-2-general-definitions-and-glossaries.md#menuleiste). A corresponding button can also be accessed from the [context menu](2-2-general-definitions-and-glossaries.md#kontextmenu) for the order header ([Figure 121, “Order Header Context Menu”](6-2-1-scheduled-orders.md#figure.auftragskopf.kontext "Figure 121. Order Header Context Menu")).

<a id="figure.auftragskopf.kontext"></a>

![Image: order header context menu](images/auftragskopf_kontext.png)

**Figure 121. Order Header Context Menu**

##### <a id="geplante.auftraege.abschliessen"></a>6.2.1.2. Finalize Order Definition

After an order has been created, it will have the status ["Defining"](6-2-3-order-status.md#table.auftragsstatus "Table 30. Order Status Overview"). To complete the order definition of an order header, click on the symbol in the [tool bar](2-2-general-definitions-and-glossaries.md#symbolleiste) ![](images/set_defined.png) ([1](6-2-1-scheduled-orders.md#figure.auftragskopf.abschliessen "Figure 122. Finalize Order Definition")). A corresponding button can also be accessed through **Complete order definition** in the [context menu](2-2-general-definitions-and-glossaries.md#kontextmenu) for the order navigator ([2](6-2-1-scheduled-orders.md#figure.auftragskopf.abschliessen "Figure 122. Finalize Order Definition")).

<a id="figure.auftragskopf.abschliessen"></a>

![Image: finalize order definition](images/auftragskopf_abschliessen.png)

**Figure 122. Finalize Order Definition**

  

A test will take place if the entered data is correct. So, for example, the date in the **"Scheduled start date"** selection field should be before the date in the **"Scheduled end date"** selection field ([3](6-2-1-scheduled-orders.md#figure.auftragskopf.abschliessen "Figure 122. Finalize Order Definition")), otherwise an error message will appear.

##### <a id="auftraege.ueberwachen"></a>6.2.1.3. Monitoring Orders

The status of an order is not only displayed in the properties of an order header or order step, but also in the [navigator](3-2-3-navigator.md "3.2.3. Navigator") given by symbols. An overview of symbols for orders can be found under [order status](6-2-3-order-status.md "6.2.3. Order Status").

For deadline monitoring, the order objects in the navigator are highlighted in color which has a scheduled completion that is critical or overdue. If the due date and the current date match and the order has not been completed yet, it will be marked in yellow. If the due date has already passed, then the order will be marked in red. Orders that have not started yet or that have completion deadlines set in the future, are not highlighted in any color.

Authors and editing coordinators can find a quick tool in the "[Orders](6-1-tasks.md "6.1. Tasks")" view, since all of the time-critical orders are directly displayed there.

##### <a id="autraege.anpassen"></a>6.2.1.4. Adjusting the Initial Deployment Date

When revising scheduled orders in the "processing" status, changes to initial introduction dates can only be given if it is the current day or in the future. Specifications of dates in the past are not allowed for this. It is possible to revise and save the other parameters of scheduled order headers, for example the comments, even if the currently set initial deployment date is in the past.

If the scheduled order is already completed, then the initial deployment date can no longer be adjusted. There is then the option to change the [translation requirements target date](6-4-4-translation-requirements.md#zieltermin.uebersetzungsbedarfe "6.4.4.1. Changing the Deadline of Translation Requirements").

##### <a id="start.enddatum.anpassen"></a>6.2.1.5. Changing Planned Start or End Date of Order Headers

Changes to the start or end date in order headers will also be applied in order steps. The following applies:

- Change in the order header with the "Defined” status: the end and start date of the order header and order steps in the (“In Definition”, “Defined”) status can be changed.
- Change in the order header with the "In progress” status: only the end date of the order header and order steps in the (“In Definition”, “Defined", "In progress") status can be changed.

However, to avoid conflicts with the consistency requirements, changes to the start or end date can only be applied to the order steps if:

- the start date is moved back.
- the end date is moved forward.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="6-2-orders.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="6-2-orders.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="6-2-2-ad-hoc-orders.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">6.2. Orders </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 6.2.2. Ad Hoc Orders</td></tr></table>
