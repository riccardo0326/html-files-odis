[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.1. Editorial Object General Information](7-1-editorial-object-general-information.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.1.1. Creating a New Editorial Object</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-1-editorial-object-general-information.md">Prev</a> </td><th align="center" width="60%">7.1. Editorial Object General Information</th><td align="right" width="20%"> <a accesskey="n" href="7-1-2-revising-an-editorial-object.md">Next</a></td></tr></table>

---

#### <a id="redaktionsobjekt.erstellen"></a>7.1.1. Creating a New Editorial Object

Editorial objects are information carriers for the entire system, which are created and managed by authors. The author creates a new, empty object in the editing system. ODIS Creator assigns a unique ID. The author can change the system name and the display name.

The system name of editorial objects is limited to the following characters: "+.-\_/0123456789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ".

This character set applies to the following editorial objects:

- Brand
- Vehicle type
- Model year
- Version
- Motor
- Control Module Configuration
- Equipment without diagnostic interface
- XOR node
- Knowledge base
- Diagnostic Object
- Measured Values Table
- Default measurement
- Supplemental document

There is another restriction for function code system names (see [Section 7.6.4.2, “Unique System Name for Function Tests”](7-6-4-function-code-objects.md#funktionscode.eindeutigesystemnamen "7.6.4.2. Unique System Name for Function Tests")). There is also a limitation for the XML templates; these may only contain the characters "\_0123456789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ".

The author has the option to declare the created object as a template. The template differs from the actual editorial object, in that it is not subject to a version, does not need to be complete, is not verified, and is never processed. A new editorial object is generated in the database the first time it is saved.

To create a new editorial object, you have two options: if the current editorial object should used the new object, select **New subnodes**. ODIS Creator assists you during the creation and offers the editorial objects permitted at this location in the submenu. The new object is added at this location directly under the editorial object, that was marked during the creation.

<a id="figure.redaktion.kindelement"></a>

![Image: new subnode](images/RedaktionKindelement.png)

**Figure 171. New Subnode**

If you want to insert another element on the same level next to the currently selected object, then select **New parallel node**. In this scenario, ODIS Creator also gives you possible objects to be selected for this location. The parallel node is added according to the editorial object, that was marked during creation.

<a id="figure.redaktion.nachbarelement"></a>

![Image: new parallel node](images/RedaktionNachbarelement.png)

**Figure 172. New Parallel Node**

In both cases, you can change the order at a later time. To do this, click on the editorial object in the navigator, hold the mouse button down and the shift button on the keyboard. Now pull the object to the desired location and release it. ODIS Creator also assists you here and shows the unpermitted positions at the mouse cursor.

Alternatively, you can also create a new editorial object through the menu bar under **Insert >> Parallel node** or **Insert >> Subnode**

Every editorial object has a system name<a id="d4e5819"></a>and most also have a display name<a id="d4e5822"></a>. The system name is always used in ODIS Creator for displays in navigators or references. The system name can only be newly created within the first version and can only be changed until the editorial object is risk-released<a id="d4e5825"></a>for the first time. This way ODIS Creator ensures that all references of the editorial objects also then fit together, if only the newest changes are already provided (**incremental [baseline](11-appendix.md#baselines "Baseline")**)<a id="d4e5829"></a>. The system name and display name, if necessary, must be specified before the editorial object can be saved for the first time.

For versioning,<a id="d4e5832"></a>ODIS Creator has three input fields available. The version itself is given in three digits. ODIS Creator makes sure that for every new version, the last position of the version is at least incremented. You can also increment the version yourself at the first and second position, if for example, your changes are so extensive that you think a new main version is justified. Exact definitions for versioning can be defined in the editing repair manual. You must give a version comment for each new version<a id="d4e5835"></a>. Specify the changes and the reason for change here, so that you and your colleagues can understand why a revision was necessary. In the version history,<a id="d4e5838"></a>you will see the version, date and comments from the previous versions. You can therefore understand the previous revision cycles of the respective editorial object.

If the **migration protection** checkbox is enabled,<a id="d4e5843"></a>this prevents the overwriting of an editorial object during a data migration. The migration protection<a id="d4e5845"></a>can be enabled or deleted by clicking on it or through the editorial object context menu or through the menu bar under **File**.

<a id="d4e5850"></a>

![Image: new creation of editorial object](images/RedaktionVersionierung.png)

**Figure 173. New Creation of Editorial Object**

ODIS Creator saves all released versions of an object. If processing steps are still necessary during a revision cycle after completion, then this will be differentiated by a new version number. This also allows colleagues that have already used the confirmed completed object and that must verify a corrected version to determine the difference. In contrast to the released versions, ODIS Creator does not store this working version separately. Add the version comments<a id="d4e5858"></a>if you revise an object again after completion. ODIS Creator always provides the version matching a baseline. Version comments are only intended for the internal use within editing. Thus they are not translated and are not visible in the [processing system](10-odis-creator-affiliated-systems.md#vaudas).

If you want to archive information for an editorial object, then use the comment input field for this.<a id="d4e5863"></a>. The comments will be transferred to each new version. It is also only intended for internal use and will therefore not be translated nor exported to the processing system.

All editorial objects have ultimately three tables still. You can see from the **used** table, which other editorial objects are being used from the editorial object just displayed. You will always see all used objects here, even if you have filtered out specific objects in the navigator, you have not opened the default filter, or the usage is content-related and not structural. This allows you to easily see which objects have been affected by the changes you have just made to the edited editorial object. This is even possible if a reusable editorial object is used by other editing locations or group brands.

The **used by** table allows you to see an overview in the opposite direction: this table shows you all editorial objects that reference the object just displayed. It also applies here that all used editorial objects will be displayed regardless of the filter settings, so that you can always quickly assess the effects of changes.

You have the option in both of these tables to display the respective object by double clicking on an entry. If this object is only used at one position, then the editor will be opened directly and the object is selected in the navigator. If the object is reused at multiple locations, then a use location dialog will be displayed as an interim step; you can select here in which context the object should be displayed. For performance reasons, it tries to load as little data as possible when opening the entire structure. Therefore the following features apply when opening the tree structure:

- If the child objects have already been loaded for a superordinate node and the corresponding path element is included in there, then this node will remain unchanged and the path is retained.
- If the child objects have already been loaded for a superordinate node, but the corresponding path element is not included in there, then the existing child objects will be completely deleted and replaced by the respective path element. If this is the case, the superordinate node will be displayed in italics to indicate that this node does not contain every child object.
- Since it is possible that the elements on the last level of the object to be selected may be significant for other procedures, it deviates from the process described thus far. If child objects for a node on the level before the last have not loaded yet or the object to be selected is not included in the child objects, then the child objects will be entirely reloaded. If then the object to be selected is still not in the list based on the results hit list limit (see [Section 7.1.5, “Apply Filter”](7-1-5-apply-filter.md "7.1.5. Apply Filter")), it will be added at the end and the object will be displayed in gray font in the tree.

The brand allocations for the different objects can be seen in these two “Used” and “Used by” tables. It is possible to filter the objects by context menu in each column in the tables.

<a id="d4e5881"></a>

![Image: Filters in tables](images/RedaktionFiltern.png)

**Figure 174. Filters in Tables**

The last table shows you the type, name and date of all test logs, which the displayed editorial object version has gone through. The last log for the consistency check is always<a id="d4e5889"></a>kept since the last release. You can initiate the consistency check through the menu bar under **Extras** or the context menu.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-1-editorial-object-general-information.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-1-editorial-object-general-information.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-1-2-revising-an-editorial-object.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.1. Editorial Object General Information </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.1.2. Revising an Editorial Object</td></tr></table>
