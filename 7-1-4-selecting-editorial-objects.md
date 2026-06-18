[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.1. Editorial Object General Information](7-1-editorial-object-general-information.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.1.4. Selecting Editorial Objects</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-1-3-editorial-object-status.md">Prev</a> </td><th align="center" width="60%">7.1. Editorial Object General Information</th><td align="right" width="20%"> <a accesskey="n" href="7-1-5-apply-filter.md">Next</a></td></tr></table>

---

#### <a id="redaktion.selektion"></a>7.1.4. Selecting Editorial Objects

While creating content for an editorial object, more frequent relationships to other editorial objects are constructed. When creating a variant rule, for example, objects from the equipment network must be selectable. In general, this selection can be made up to three ways in ODIS Creator, which is further explained in the following using the variant rule as an example:

- **Drag and drop:** you can select an equipment network object in the navigator and with the mouse button pressed down, you can pull this object over the desired table entry in the diagnostic object variant rule table. As soon as you release the mouse button, the equipment network object is entered into the table.
- **Auto completion:** In the case of the variant rule table, it is possible to enter an equipment network object directly. To do this, you must first select an object type in the table. Then you can enter a combination of letters in the value field, that should appear in the name of the desired object. The position of where the letter combination is in the name does not play a role. When entering 'ddy', for vehicle models for example, the entries '2K\_Caddy\_2004' and '2C\_Caddy\_2011' will be found. It will check if the combination in the input also produces a result. If the input of another letter would cause the hit list to be empty, then the input will be rejected and the letter will not be considered.
- **Dialog selection:** If the respective value field in the table is clicked in, then a button with an ellipses appears at the right edge of the field. After clicking on the button, a selection dialog will open, which you can use to select the desired type of object. The dialog ensures that only permitted object types can be selected or applied. The filter function is also available within the dialog, which is explained further in [Section 7.1.5, “Apply Filter”](7-1-5-apply-filter.md "7.1.5. Apply Filter"). Defining and activating a filter can be done through the dialog context menu.

These three selection methods are however not available in every scenario. The selection of a fault location is, for example, not possible through auto completion in a suspicion rule, since the context for a control module description is also always required here, and this can only be ensured per drag and drop or with the selection dialog.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-1-3-editorial-object-status.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-1-editorial-object-general-information.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-1-5-apply-filter.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.1.3. Editorial Object Status </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.1.5. Apply Filter</td></tr></table>
