[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.1. Editorial Object General Information](7-1-editorial-object-general-information.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.1.5. Apply Filter</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-1-4-selecting-editorial-objects.md">Prev</a> </td><th align="center" width="60%">7.1. Editorial Object General Information</th><td align="right" width="20%"> <a accesskey="n" href="7-1-6-sorting-subnodes.md">Next</a></td></tr></table>

---

#### <a id="redaktion.filter"></a>7.1.5. Apply Filter

As opposed to the [filter concept](3-2-3-navigator.md#navigator.filter.definieren "3.2.3.1. Defining the filter") in the [order management](6-2-1-scheduled-orders.md#auftraege.ueberwachen "6.2.1.3. Monitoring Orders"), the filters in the editing module do not apply to all elements in the structure tree, but rather only to the already expanded navigator elements from the time they were created.

You have the option to use the saved filter for a changed selection using **Filter again**. Editorial objects, to which **Filter again** has been applied to, are displayed in italics. However **Refresh** will refresh all objects currently visible in the navigator, while maintaining the respective filter settings so that no other nodes are displayed. However, deleted objects are removed through the refresh function.

##### <a id="redaktion.standardfilter"></a>7.1.5.1. Default Filter

If no user-defined filter is set, then the default filter is always active. This limits the displayed objects based on the structure tree type. For the equipment network tree or knowledge base structure tree, all objects that were not edited at your location will be filtered out. So that you can see the object in the default filter, the responsible team and your team must be assigned to the same location. The brand creates an exception here. All brands, that you are responsible for, are displayed in the structure tree. However, in the function library structure tree and supplemental document structure tree, only objects are displayed where the team responsible for it is the same team you are assigned to. For all other structure trees (control module tree, DTC memory, vehicle project and XML template), all working versions of the individual team are displayed if a working version is permitted. Only the objects released by other teams are displayed, regardless of the brand allocation.

This default filter can be switched off by opening the filter and removing all restrictions there, or confirm the empty filter and then select the **Filter again** command. The closer you use this filter to the root of the displayed navigator, the more objects you can see. You can copy objects from other brands and reuse them, if permitted. However, you can only then edit these objects, if they are used exclusively or among other objects that are assigned to the brand that is processed at your editing location.

##### <a id="redaktion.primaerfilter"></a>7.1.5.2. Filter for Primary Objects

ODIS Creator also still has a predefined filter for primary objects. In contrast to the previous editing system, ODIS Creator can also display every direct dependency in the navigators. For example, you can directly see which traversal test or which supplemental document is used at a specific location in the equipment network and you can also create a new one, edit and delete it directly at this location. This makes it much easier for you to see the attachments and dependencies at a glance, and you can create objects with all sub-objects directly at a location, without constantly switching to the respective work area.

However, if you prefer to work with the previous process, then perhaps interrupt the additionally displayed objects. If this is the case, activate the primary object filter (see [Figure 178, “Primary Filter”](7-1-5-apply-filter.md#figure.primaerfilter "Figure 178. Primary Filter")) and you will only see the equipment network objects in the equipment network, only diagnostic objects in the knowledge base, only function tests in the various values in the function test library, as well as preset measurements and measurement value tables. The control module tree and the supplemental documents are always sorted correctly, since no other references from these objects are possible.

<a id="figure.primaerfilter"></a>

![Image: primary filter](images/primaerfilter.png)

**Figure 178. Primary Filter**

Under the menu item **Help >> Settings**, you have the option in every editor navigator to set if the primary objects filter is active or inactive when opening. (see [Figure 179, “Primary Filter Settings”](7-1-5-apply-filter.md#figure.benutzervorgaben.primaerfilter "Figure 179. Primary Filter Settings"))

<a id="figure.benutzervorgaben.primaerfilter"></a>

![Image: Primary filter settings](images/benutzervorgaben_primaerfilter.png)

**Figure 179. Primary Filter Settings**

##### <a id="redaktion.filter.menge"></a>7.1.5.3. Filter Results

Regardless of the filter setting, the number of objects that can be loaded and displayed is limited. The group administrator can set a value. The default value is 500. If more child objects are found when opening an object node, then an applicable message will be displayed, in which you can select between three processes:

- **Load all:** Despite the limit given by the group administrator, this makes it possible to also display all found objects. Note: depending on the amount of results, the display may take some time.
- **Load:** All objects up to the permitted maximum amount will be loaded. If it is 500, for example, then the first 500 hits will be returned and displayed. The sorting of loaded objects deviates in this case from the default sorting. To offer you a logical object selection, the objects are loaded here in the order of their editing date. The last edited object will therefore be displayed first.
- **Filter:** The filter dialog will open automatic and you can set a filter or add to the existing filter. When closing the filter dialog with **OK**, the child objects will begin to load again. If the setting of the filter was not sufficient, then the corresponding message will display again.

<a id="figure.maximum_exceeded"></a>

![Image: message when permitted maximum amount is exceeded](images/Objekt_Hoechstanzahl.png)

**Figure 180. Message when Permitted Maximum Amount is Exceeded**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-1-4-selecting-editorial-objects.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-1-editorial-object-general-information.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-1-6-sorting-subnodes.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.1.4. Selecting Editorial Objects </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.1.6. Sorting Subnodes</td></tr></table>
