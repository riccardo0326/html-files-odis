[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.2. Recently used objects</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-1-19-additional-functions.md">Prev</a> </td><th align="center" width="60%">7. ODIS Creator Editing Process</th><td align="right" width="20%"> <a accesskey="n" href="7-3-search.md">Next</a></td></tr></table>

---

### <a id="zvo"></a>7.2. Recently used objects

The “Recently used objects” view (see [Figure 220, “Recently Used Objects View”](7-2-recently-used-objects.md#figure.zvo.view "Figure 220. Recently Used Objects View")) lists all editorial objects (for all sessions) in reverse order based on when they were used, meaning the most recently used editorial objects are listed at the top. Only editorial objects for the OC environment that has been opened are displayed. The layout settings can be used to specify how many editorial objects should be displayed. The view consists of the following columns:

- Order step
- Name
- Status
- Object type
- Version
- Brand
- Last revision
- Consistency
- Context

<a id="figure.zvo.view"></a>

![Image: Recently used objects view](images/view_zvo.png)

**Figure 220. Recently Used Objects View**

By simply selecting the “Order step” icon (first column) for an editorial object, the corresponding order step will open in the Editor and be selected in the order navigation tree. By simply selecting the other columns for an editorial object, the corresponding Editor will open in read-only mode. If an auxiliary document editor or function test is selected, the preview or test sequence will also open in read-only mode. Double-clicking opens the editors in editing mode. If an editorial object opens in editing mode to which no context has been assigned yet, the dialog for defining a context opens. In all cases, the selected editorial object moves into the first position. If the user tries to open an editorial object from a view that is in the recycle bin or that has been deleted completely, then the user will be notified of this with an information dialog (see [Figure 221, “Recently Used Objects Info Dialog”](7-2-recently-used-objects.md#figure.dialog.zvo.deleted "Figure 221. Recently Used Objects Info Dialog")) and this editorial object will be removed from the list.

<a id="figure.dialog.zvo.deleted"></a>

![Image: Recently used objects info dialog](images/info_dialog_zvo_deleted.png)

**Figure 221. Recently Used Objects Info Dialog**

The “Recently used objects” view is only available in editing and oder management and is initially displayed in the View area under the Editor area when the OC is started (see [Figure 222, “Recently Used Objects when Starting OC”](7-2-recently-used-objects.md#figure.zvo.ocstart "Figure 222. Recently Used Objects when Starting OC")).

<a id="figure.zvo.ocstart"></a>

![Image: Recently used objects when starting OC](images/perspective_zvo.png)

**Figure 222. Recently Used Objects when Starting OC**

The “Recently used objects” view closes automatically when switching to a view from Preparation or Administration. It opens automatically when switching back to a view from "Editing” or “Order management”. If the view is closed, it can be opened again using the icon, the selection menu under **View >> Recently used objects**, or using the **Ctrl+D** keyboard shortcut (see [Figure 223, “Recently Used Objects Menu Item”](7-2-recently-used-objects.md#figure.zvo.menu "Figure 223. Recently Used Objects Menu Item")).

<a id="figure.zvo.menu"></a>

![Image: Recently used objects menu item](images/menu_entry_zvo.png)

**Figure 223. Recently Used Objects Menu Item**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-1-19-additional-functions.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-odis-creator-editing-process.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-3-search.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.1.19. Additional Functions </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.3. Search</td></tr></table>
