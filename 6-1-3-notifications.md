[ODIS Creator Help](odis-creator-help.md) > [6. ODIS Creator Order Management Process](6-odis-creator-order-management-process.md) > [6.1. Tasks](6-1-tasks.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">6.1.3. Notifications</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="6-1-2-tasks-for-translation-coordinators.md">Prev</a> </td><th align="center" width="60%">6.1. Tasks</th><td align="right" width="20%"> <a accesskey="n" href="6-2-orders.md">Next</a></td></tr></table>

---

#### <a id="auftragsverwaltung.benachrichtigung"></a>6.1.3. Notifications

##### <a id="auftragsverwaltung.benachrichtigung.uebersicht"></a>6.1.3.1. Overview

Through the main entry **Notification** of the tasks or translation [navigator](3-2-3-navigator.md "3.2.3. Navigator"), messages about changes in the status of the orders can be displayed, if for example new tasks are created for an order or an editorial object was released. These notifications are triggered by various events and then automatically created. You cannot trigger the creation of a notification yourself.

The notifications are separated for a better overview. All notifications for translations are displayed under one separate structure node **Translation** ([1](6-1-3-notifications.md#figure.navigator.benachrichtigung "Figure 116. Navigator with Notification")) in the navigator for the tasks and in the navigator for the translation. All other notifications are displayed under one collective structure node **Order** ([2](6-1-3-notifications.md#figure.navigator.benachrichtigung "Figure 116. Navigator with Notification")) regardless of their type in the navigator for the tasks and in the navigator for the translation.

<a id="figure.navigator.benachrichtigung"></a>

![Image: navigator with notification](images/navigator_benachrichtigung.png)

**Figure 116. Navigator with Notification**

There are different types of notifications:

- **Standard notifications:** For notifications that do not fit into any of the other categories, for example for baselines, imports in the administration.
- **Translation notifications:** For translation notifications, for example erroneous import or complaint about an editorial object translation.
- **Object notifications:**  For notifications about editorial objects, for example, status changes or use of old control module descriptions. Is also used for the Excel export of market supply.

For example, the notifications appear as they do in [Figure 117, “Example of a Notification”](6-1-3-notifications.md#figure.navigator.benachrichtigungsfelder "Figure 117. Example of a Notification"):

<a id="figure.navigator.benachrichtigungsfelder"></a>

![Image: notification example](images/Benachrichtung.jpg)

**Figure 117. Example of a Notification**

Only one field is filled in per notification for the fields "for user" and "for team". If a notification goes to a user, for example as a response to an action by a user, then the field "for user" is filled in the notification. If a notification goes to an entire team, for example a notification for a team object, then the field "for team" is filled in.

##### <a id="auftragsverwaltung.benachrichtigung.filterfunktion"></a>6.1.3.2. Filter Function

The filter function for the notifications is structured similarly to the filter function for the tasks (see [Define filter function](3-2-3-navigator.md#navigator.filter.definieren "3.2.3.1. Defining the filter")). This means that there is a lock button ([3](6-1-3-notifications.md#figure.navigator.benachrichtigung "Figure 116. Navigator with Notification")) to activate and deactivate the filter function in the navigator for tasks and in the navigator for translation.

##### <a id="auftragsverwaltung.benachrichtigung.quittierung"></a>6.1.3.3. Confirmation for Notifications

If a message is clicked on, its content is displayed in the [Editor](3-2-5-editor.md "3.2.5. Editor"). A selected message can be deleted using the **Notification finished** [button](2-2-general-definitions-and-glossaries.md#schaltflaeche) in the [context menu](2-2-general-definitions-and-glossaries.md#kontextmenu) or the symbol ![](images/Benachricht_loeschen.png) in the [tool bar](2-2-general-definitions-and-glossaries.md#symbolleiste). If the main entry **notification** is selected, all included messages can be confirmed at once through the context menu ([4](6-1-3-notifications.md#figure.navigator.benachrichtigung "Figure 116. Navigator with Notification")). This means that all notifications are marked as done.

##### <a id="auftragsverwaltung.benachrichtigung.benachrichtigungsabonnenments"></a>6.1.3.4. Managing Notification Subscriptions

The **Edit subscriptions** [button](2-2-general-definitions-and-glossaries.md#schaltflaeche) in the [context menu](2-2-general-definitions-and-glossaries.md#kontextmenu) ([4](6-1-3-notifications.md#figure.navigator.benachrichtigung "Figure 116. Navigator with Notification")) for the main **Notification** entry or the symbol ![](images/Abos_bearbeiten_symbol.png) in the [tool bar](2-2-general-definitions-and-glossaries.md#symbolleiste) will open the **Subscription editor** ([Figure 118, “Editor for Subscriptions”](6-1-3-notifications.md#figure.abo.editor "Figure 118. Editor for Subscriptions")). It can be set here which type of changes for which objects should trigger notifications. By double clicking on a line, the dialog **change management** opens.

<a id="table.hinweis.Kontextmenue_Redaktion"></a>

<table border="1" summary="Note: Editing Context Menu"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note:</strong></span> The change management can also be opened using the <span class="bold"><strong>Change information... </strong></span> button in the context menu of the respective editorial object (e.g. <a class="xref" href="7-1-1-creating-a-new-editorial-object.md#figure.redaktion.kindelement" title="Figure 171. New Subnode">Figure 171, “New Subnode”</a>).</td></tr></tbody></table>

**Table 29. Note: Editing Context Menu**

<a id="figure.abo.editor"></a>

![Image: editor for subscriptions](images/abos.png)

**Figure 118. Editor for Subscriptions**

##### <a id="auftragsverwaltung.benachrichtigung.wiedervorlage"></a>6.1.3.5. Notification Reminder

Under the menu item **Help** under **Settings**, the user has the option to manage the time frames for a notification reminder ([Figure 119, “Configuration for Notifications”](6-1-3-notifications.md#figure.benachrichtigung.wiedervorlage "Figure 119. Configuration for Notifications")). There is one field for the settings for each notification type. The value shows the number of days until the reminder. A value of "0" days is given for this for the follow-up with the next notification. The time frame is set to "7" days as the default value for all types of notifications. The maximum value can be "365" days (one year). For the team settings, there is still the selection for the teams you are a part of in a similar display.

<a id="figure.benachrichtigung.wiedervorlage"></a>

![Image: configuration for the notification](images/benachrichtigung_wiedervorlage.png)

**Figure 119. Configuration for Notifications**

To arrange the amount of notifications more clearly, it will first be checked when a new notification is created, if there is already an active notification for the same procedure. If this is the case, then no notification will be created. If there is not a notification yet, then a new notification will be created. If there is a received notification, then it will check if the time frame between the receipt and the current time is larger than the maximum time frame saved in the system, based on the type of notification. If the time frame is greater than this, then the notification will be created and if the time frame is less than this, then no notification will be created.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="6-1-2-tasks-for-translation-coordinators.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="6-1-tasks.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="6-2-orders.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">6.1.2. Tasks for Translation Coordinators </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 6.2. Orders</td></tr></table>
