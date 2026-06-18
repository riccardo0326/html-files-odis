[ODIS Creator Help](odis-creator-help.md) > [3. ODIS Creator Basic Information](3-odis-creator-basic-information.md) > [3.2. Program Structure](3-2-program-structure.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">3.2.3. Navigator</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="3-2-2-edited-order-order-context.md">Prev</a> </td><th align="center" width="60%">3.2. Program Structure</th><td align="right" width="20%"> <a accesskey="n" href="3-2-4-properties-window.md">Next</a></td></tr></table>

---

#### <a id="navigator"></a>3.2.3. Navigator

In the navigator,<a id="d4e727"></a>all entries are hierarchically sorted in a structure tree (for example [Figure 27, “Order Navigator”](3-2-3-navigator.md#figure.navigator "Figure 27. Order Navigator")). An entry can contain additional entries, which can be shown or hidden by clicking on the main entry. Displayed before a main entry that can be opened. ![](images/Plus01.png) Displayed before a main entry that is open. ![](images/minus.png) . If you click on an entry, its properties will be shown underneath it in the [properties window](3-2-4-properties-window.md "3.2.4. Properties window") and the [editor](3-2-5-editor.md "3.2.5. Editor") view with the details will be opened in the right [frame](2-2-general-definitions-and-glossaries.md#rahmen).

<a id="figure.navigator"></a>

![Image: order navigator](images/Navigator.png)

**Figure 27. Order Navigator**

The navigator is configured so that when it starts, it displays the entries that are most helpful for you in the open view. Some navigators have a separate tool bar (green border in [Figure 27, “Order Navigator”](3-2-3-navigator.md#figure.navigator "Figure 27. Order Navigator")). There you can define the filter to limit or expand the displayed entries and retrieve a table overview of the entries.

##### <a id="navigator.filter.definieren"></a>3.2.3.1. Defining the filter

With a filter,<a id="d4e751"></a>you can limit or expand the number of entries displayed in the navigator. You can specify criteria in the filter, which the displayed entries must fulfill. If the navigator displays multiple different types of entries, you can define a separate filter for each type.

<a id="figure.benachrichtigungsfilter"></a>

![Image: notification filter](images/benachrichtigungsfilter.png)

**Figure 28. Notification filter**

So that entries do not appear without reference in the navigator structure tree, ODIS Creator makes sure that superordinate entries are also then displayed only if their subordinate entries match the filter criteria. In this context, the filter in the [editing](7-odis-creator-editing-process.md "7. ODIS Creator Editing Process") process represents an exception, which only applies to the already expanded navigator entries (see [Section 7.1.5, “Apply Filter”](7-1-5-apply-filter.md "7.1.5. Apply Filter")).

For each type of entry, you can specify which of their attributes must conform to which criteria. To do this, press the button, ![Symbol: Add button](images/plus.png)to create a new condition. You can link these conditions through the logical AND or OR. When the logical link is the same, the filter conditions are strictly analyzed in the order they are displayed. When there are a number of logical conditions, the AND has a stronger functional effect than the OR and will be analyzed first according to that. This is always comparable to the multiplication before addition rule. The first condition in a table or parentheses may not contain an AND or OR, since no condition is given that can be linked to this condition.

To clarify the function, filter functions based on a simple but atypical example (types of fruit) are illustrated in the following.

If you give the condition [Fruit = Apple][OR Fruit = Pear AND Color = Green], pears and apples of every color will be filtered but not green apples or green pears.

<a id="d4e776"></a>

<table border="1" summary="Defining a Filter - Example 1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr bgcolor="#EEEEEE"><th>AND/OR</th><th>Attribute name</th><th>Condition</th><th>Value</th></tr></thead><tbody valign="top"><tr><td valign="top"> </td><td valign="top">Fruit</td><td valign="top">=</td><td valign="top">Apple</td></tr><tr><td valign="top">OR</td><td valign="top">Fruit</td><td valign="top">=</td><td valign="top">Pear</td></tr><tr><td valign="top">AND</td><td valign="top">Color</td><td valign="top">=</td><td valign="top">Green</td></tr></tbody></table>

**Table 7. Defining a Filter - Example 1**

You can put parentheses in the filter dialog, in which you specify either only AND or OR and then include the first filter condition within the parentheses in the next line. The parentheses are automatically closed with the next AND/OR line or with the last line.

If you would like to filter apples or pears and both types of fruit should be green, then specify the following conditions:

<a id="d4e807"></a>

<table border="1" summary="Defining a Filter - Example 2"><colgroup><col/><col/><col/><col/></colgroup><thead><tr bgcolor="#EEEEEE"><th>AND/OR</th><th>Attribute name</th><th>Condition</th><th>Value</th></tr></thead><tbody valign="top"><tr><td valign="top"> </td><td valign="top">Fruit</td><td valign="top">=</td><td valign="top">Apple</td></tr><tr><td valign="top">OR</td><td valign="top">Fruit</td><td valign="top">=</td><td valign="top">Pear</td></tr><tr><td valign="top">AND</td><td valign="top"> </td><td valign="top"> </td><td valign="top"> </td></tr><tr><td valign="top"> </td><td valign="top">Color</td><td valign="top">=</td><td valign="top">Green</td></tr></tbody></table>

**Table 8. Defining a Filter - Example 2**

  

If the placement of parentheses is too complicated, you can also simply remove the parentheses for this simple example based on the rule:

[(Apple OR Pear) AND green =]

[Apple AND green OR Pear AND green]

<a id="d4e847"></a>

<table border="1" summary="Defining a Filter - Example 3"><colgroup><col/><col/><col/><col/></colgroup><thead><tr bgcolor="#EEEEEE"><th>AND/OR</th><th>Attribute name</th><th>Condition</th><th>Value</th></tr></thead><tbody valign="top"><tr><td valign="top"> </td><td valign="top">Fruit</td><td valign="top">=</td><td valign="top">Apple</td></tr><tr><td valign="top">AND</td><td valign="top">Color</td><td valign="top">=</td><td valign="top">Green</td></tr><tr><td valign="top">OR</td><td valign="top">Fruit</td><td valign="top">=</td><td valign="top">Pear</td></tr><tr><td valign="top">AND</td><td valign="top">Color</td><td valign="top">=</td><td valign="top">Green</td></tr></tbody></table>

**Table 9. Defining a Filter - Example 3**

It is always possible to omit the parentheses. However, it will cause complex filters to be composed of a lot of conditions.

Different conditions can be selected based on the selected attribute. The following list explains the available conditions.

<a id="table.filterbedingungen"></a>

<table border="1" summary="Filter Conditions"><colgroup><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left"><span class="bold"><strong>Condition</strong></span></th><th align="left"><span class="bold"><strong>Description</strong></span></th></tr></thead><tbody valign="top"><tr><td align="left" valign="top">=</td><td align="left" valign="top">
<p>Filters all entries in which the attribute matches the specified value exactly:</p>
<p>the condition [<span class="citation">= Apple</span>] will find every [Apple] but not [apple], [apples], [applesauce], [pineapple], [scrapple], [grapple]</p>
</td></tr><tr><td align="left" valign="top">&lt;&gt;</td><td align="left" valign="top">
<p>Filters all entries in which the attribute does not match the specified value:</p>
<p>The condition [<span class="citation">!= Apple</span>] finds [pears], [cherries] and also [apple], [apples], [applesauce], [pineapple], [scrapple], [grapple], but not [Apple].</p>
</td></tr><tr><td align="left" valign="top">&lt;</td><td align="left" valign="top">
<p>Filters all entries in which the attribute is less than the specified value:</p>
<p>the condition [<span class="citation">&lt; 01.02.2008</span>] will find every date that comes before 01.02.2008, but not 01.02.2008 itself.</p>
</td></tr><tr><td align="left" valign="top">&gt;</td><td align="left" valign="top">
<p>Filters all entries in which the attribute is greater than the specified value:</p>
<p>the condition [<span class="citation">&lt; 01.02.2008</span>] will find every date that comes after 01.02.2008, but not 01.02.2008 itself.</p>
</td></tr><tr><td align="left" valign="top">&lt;= , &gt;=</td><td align="left" valign="top">Behaves like &lt; and &gt;, however it will also find the specified value.</td></tr><tr><td align="left" valign="top">like</td><td align="left" valign="top">
<p>Filters all entries in which the attribute contains the specified value: * marks the place in the value where any symbols could be:</p>
<p>the condition [<span class="citation">like Apple*</span>] finds [Apple] and [Applesauce] but not [apple], [apples], [scrapple]</p>
<p>the condition [<span class="citation">like*Apple</span>] will only find [Apple] but not [apple], [apples], [applesauce], [pineapple], [scrapple], [grapple]</p>
<p>the condition [<span class="citation">like *apple</span>] finds [apple] and [pineapple] but not [Apple], [apples], [applesauce].</p>
<p>the condition [<span class="citation">like *pple*</span>] will find [Apple], [apple], [apples], [applesauce], [pineapple], [scrapple], [grapple]</p>
</td></tr></tbody></table>

**Table 10. Filter Conditions**

  

As you saw in the examples, the values are case sensitive. If you would like to find both upper case and lower case values, formulate two equal conditions and link them with OR. Alternatively, you can also formulate a like-condition and replace the first letter with \*.

If you would like to find an [Apple] as well as [apple], enter

[Fruit = Apple OR Fruit = apple] or

[Fruit like \*pple].

##### <a id="navigator.filter.speichern"></a>3.2.3.2. Saving a Filter

As seen in the previous [Section 3.2.3.1, “Defining the filter”](3-2-3-navigator.md#navigator.filter.definieren "3.2.3.1. Defining the filter"), defined filters can definitely assume complex sizes. So that you do not have to define a filter again every time ODIS Creator restarts, there is the option to save a defined filter.

To save a defined filter, use the 'Save' button that is above the table in every filter dialog (see [Figure 28, “Notification filter”](3-2-3-navigator.md#figure.benachrichtigungsfilter "Figure 28. Notification filter")). After pressing the 'Save' button, it will offer for you to enter a filter name (see [Figure 29, “Save Dialog for Filters”](3-2-3-navigator.md#figure.filterspeichern "Figure 29. Save Dialog for Filters")). The entered name should be as informative as possible so that you can quickly identify the saved filter for later use. The name of the saved filter can be changed at any time in the [filter administration](3-2-3-navigator.md#navigator.filter.speichern.administration "3.2.3.4. Saved Filter Administration").

<a id="figure.filterspeichern"></a>

![Image: save dialog](images/filterdialog_speichern.png)

**Figure 29. Save Dialog for Filters**

  

Filters that have already been saved can be selected using the selection field, which is provided in every filter dialog above the table (see [Figure 28, “Notification filter”](3-2-3-navigator.md#figure.benachrichtigungsfilter "Figure 28. Notification filter")). Since the filter is saved based on the tree type, you can, for example, also reuse a saved notification filter only in the notification filter dialog. Filters from different tree types are not displayed in the selection field.

If you use a previously defined filter, then it can also be revised within the filter dialog. If you press the 'Save' button again after revising, you will receive the option to overwrite the previously saved filter or to enter a new name to save the filter under a new name.

Saved filters can also be released for other users. You must enable the checkbox for this with the name entry during the save process. The release of a filter can be changed at any time in the [filter administration](3-2-3-navigator.md#navigator.filter.speichern.administration "3.2.3.4. Saved Filter Administration").

##### <a id="navigator.filter.memento"></a>3.2.3.3. Filter Reminder

If you use a saved filter in a navigation tree and this filter is still active when closing the navigation tree or when ending the ODIS Creator Client, then this setting will be stored in the local Windows user folder on the computer. When the corresponding navigation tree is next opened, ODIS Creator will recognize that a previously saved filter was set and reactivates it again. Therefore you can reuse the filter that was used and saved in the last session, without having the additional step of selecting it through the filter dialog and setting it.

##### <a id="navigator.filter.speichern.administration"></a>3.2.3.4. Saved Filter Administration

You can open the filter administration at any time by clicking on the **Help** and then **Settings** [buttons](2-2-general-definitions-and-glossaries.md#schaltflaeche) in the [menu bar](2-2-general-definitions-and-glossaries.md#menuleiste). If necessary, you must select the entry **Filter settings** on the left side to go to [Figure 30, “Filter Administration”](3-2-3-navigator.md#figure.filteradministration "Figure 30. Filter Administration").

You can change the name and the release of the saved filter in the filter administration. Filters that are no longer required can be deleted by pressing the button ![Symbol: Delete button](images/minus.png) .

<a id="figure.filteradministration"></a>

![Image: filter administration](images/Filteradministration.png)

**Figure 30. Filter Administration**

  

If you select the button '**Display available filters**', then you will receive an overview of all saved filters that were released by other users (see [Figure 31, “Filters Released by Other Users”](3-2-3-navigator.md#figure.filteradministration.copy "Figure 31. Filters Released by Other Users")). Here you can see the filters from other users and if desired, you can copy it using the button '**Apply filter**'. When it is copied, the current status of the other user's filter is copied to the appropriate filters. The copy is a snapshot, a later comparison between the original and the copy is not planned. The name of the copied filter is preceded by 'Copy-' in order to indicate the copied filter in the particular overview. This addition is only set initially and can be removed at any time.

<a id="figure.filteradministration.copy"></a>

![Image: filters released by other users](images/Filteradministration_Copydialog.png)

**Figure 31. Filters Released by Other Users**

##### <a id="navigator.listenansicht"></a>3.2.3.5. List View

The list view displays the entries in the navigator in a [table](3-2-6-tables-and-lists.md "3.2.6. Tables and Lists"). The list view is useful if you could like to compare the details of many different entries at a glance. The entries displayed in the list are the same as what you see in the navigator. The filter also applies to the list.

##### <a id="navigatoren.sync"></a>3.2.3.6. Multiple Navigators with the Same Type

When two navigators are the same in editing (see [Section 7.1, “Editorial Object General Information”](7-1-editorial-object-general-information.md "7.1. Editorial Object General Information")), the difference is made between the primary and secondary navigator. The primary navigator is the navigator on the left side and the secondary navigator is opened on the right side next to the primary navigator. A navigator instance can be opened through the view bar or through the global menu **Insert > Reference**.

Both these navigators can be used independently from each other. All functions of the respective navigator are available for the primary and secondary navigator.

The path of an editorial object is selected in the navigator from which the editor was originally opened. The link function from a used/used by table affects the navigator from which the object was originally opened, as long as the usage location remains in the same type context.

The editors for editorial objects are always opened in the primary instance through operations that are independent of a navigator; for example, restoring from the recycle bin, display from the search result or link functions from outside the editing view.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="3-2-2-edited-order-order-context.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="3-2-program-structure.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="3-2-4-properties-window.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">3.2.2. Edited Order (Order Context) </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 3.2.4. Properties window</td></tr></table>
