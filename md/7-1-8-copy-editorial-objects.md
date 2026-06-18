[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.1. Editorial Object General Information](7-1-editorial-object-general-information.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.1.8. Copy Editorial Objects</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-1-7-editorial-object-history.md">Prev</a> </td><th align="center" width="60%">7.1. Editorial Object General Information</th><td align="right" width="20%"> <a accesskey="n" href="7-1-9-location-assignment-of-editorial-objects.md">Next</a></td></tr></table>

---

#### <a id="redaktion.kopieren"></a>7.1.8. Copy Editorial Objects

For your daily work, you will often require similar editorial objects that you have already created. You do not need to always rebuild it from the beginning, but rather you can copy it. ODIS Creator offers you highly efficient functions for this. You can not only copy individual objects but also entire structures and not the attached objects.

In addition to the copy function, most of the editorial objects can also be reused. Your decision of when you would like to copy and when you would like to reuse should be based on the following criteria:

- If you assume that an object or an object structure can be used as a good base, but it still needs an extensive revision, then you should copy it. You can then perform all of your changes on the source objects without effects.
- If the objects can currently be used the same way, but you expect that they should be developed differently, then you should copy.
- If you can use an object and all objects used by it exactly the same, then you should reuse the objects. If this is the case, then you only need to set up one reference. If the reused objects are already released, you must not perform any other procedures. You can also subscribe to change notifications, so that you will be notified if the reused object is changed.
- You can likewise subscribe to change notifications for every copy. You can survey changes to the original without direct pressure to act and, if necessary, apply them to your copy.

<a id="table.hinweis.redaktionsobjekt.wiederverwenden"></a>

<table border="1" summary="Note for the Reuse of Editorial Objects"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note: </strong></span>if an editorial object is reused by a user, then the corresponding translation requirements can be pulled to the object to be used for the user's location. You can find more information under <a class="xref" href="6-4-4-translation-requirements.md#uebersetzungsbedarfe.berechnen" title="6.4.4.3. Determining Translation Requirements">Section 6.4.4.3, “Determining Translation Requirements”</a>.</td></tr></tbody></table>

**Table 40. Note for the Reuse of Editorial Objects**

To make the copying easier, ODIS Creator offers two options of how you can copy multiple objects.

In the default view of the navigators, select one or more objects by clicking on them. You can initiate the copying process two ways. Either you can select the **copy** command in the context menu or you can pull the selected objects with the mouse while the left mouse button is pressed down (initiate a drag and drop operation). Then select the corresponding command from the **Insert** menu or press the CTRL button if using drag and drop and release the left mouse button over the target object. In both cases, you can select between the following copy variants in the context menu:

- **Only object without subobjects**

  Only the selected objects without their sub-structures are copied.
- **Only object with maximum reuse**

  The selected objects are copied. All child objects of the respective object are reused as much as possible, otherwise they will be likewise copied (for example, equipment network objects cannot be used again).
- **Copy of all objects**

  The selected objects and their child objects including the secondary objects (objects that belong to another tree type) are copied.
- **Copy of primary objects / reference of secondary objects**

  The selected objects and their child primary objects are copied. The used secondary objects are only referenced.
- **Only primary objects copy**

  The selected objects and their child primary objects are copied. Any subordinate secondary objects are neither copied nor referenced.

Copies of editorial objects which require the uniqueness of system names (see [Table 41, “System Name Uniqueness Test Overview”](7-1-8-copy-editorial-objects.md#table.systemnameeindeutigkeit "Table 41. System Name Uniqueness Test Overview")) already receive a new system name with the prefix "Copy\_of\_".

<a id="table.systemnameeindeutigkeit"></a>

<table border="1" summary="System Name Uniqueness Test Overview"><colgroup><col/><col/><col/><col/><col/></colgroup><tbody valign="top"><tr><td align="left" valign="top"><span class="bold"><strong>Object type</strong></span></td><td align="left" valign="top"><span class="bold"><strong>Case sensitive</strong></span></td><td align="left" valign="top"><span class="bold"><strong>Location code</strong></span></td><td align="left" valign="top"><span class="bold"><strong>Status</strong></span></td><td align="left" valign="top"><span class="bold"><strong>Special Features</strong></span></td></tr><tr><td align="left" valign="top">Brands, knowledge base, preset measurement, measured values table, supplemental document, XML template, base control module</td><td align="left" valign="top">No</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Release version</td><td align="left" valign="top"> </td></tr><tr><td align="left" valign="top">Fault location</td><td align="left" valign="top">No</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Release version</td><td align="left" valign="top">Search string only consists of Dez code and SAE code and it will be search with LIKE.</td></tr><tr><td align="left" valign="top">Function test, traversal test, general test, test procedure</td><td align="left" valign="top">No</td><td align="left" valign="top">Yes</td><td align="left" valign="top">Release version</td><td align="left" valign="top">It will search across types. The name must be unique within all 4 categories.</td></tr></tbody></table>

**Table 41. System Name Uniqueness Test Overview**

The prefix "Copy\_of\_" can be later changed or deleted by the author. With this, duplicate system names continue to be possible also for the object types listed in the [Table 41, “System Name Uniqueness Test Overview”](7-1-8-copy-editorial-objects.md#table.systemnameeindeutigkeit "Table 41. System Name Uniqueness Test Overview"). The uniqueness test continues to occur during the completion.

When copying an editorial object, it will receive "New creation as copy of <system name> <version>" in the version comments regardless of the system name uniqueness test.

<a id="figure.KopierenPerKontextmenue"></a>

![Image: Insert menu when copying with the context menu](images/KopierenEinfuegenKontextmenue.png)

**Figure 182. Insert Menu**

<a id="figure.KopierenPerDragAndDrop"></a>

![Image: Insert menu when copying using drag and drop method](images/Kopieren_KontextmenueBeiDrop.png)

**Figure 183. Insert Menu with Drag And Drop**

Switch using the **Mark** entry in the navigator menu or by pressing the key ![](images/markieren_icon.png) in the menu bar in the marked view of the navigator. It is possible in this view to only copy parts of an object structure. While only the objects explicitly marked with a check mark are copied. ODIS Creator offers the convenience function, that if an object was already marked with a check mark and a second object is marked, then all objects between them in the hierarchy are also marked. All associated objects are always copied as a complete structure. Two separate structures are marked in the [Figure 185, “Copying with Single Selection”](7-1-8-copy-editorial-objects.md#figure.KopierenMitAuswahl "Figure 185. Copying with Single Selection"), that are copied. Firstly, the diagnostic object ODIS\_TEST\_Object types is considered as one structure with the subordinate diagnostic object function1 and all objects subordinate to that. Secondly, the diagnostic object assembly group under the diagnostic object function2 is considered as the second structure to be copied. For the target object, both the diagnostic objects ODIS\_TEST\_Object types and assembly group are copied to one level.

The **context menu** and drag and drop methods are also available to initiate the copying process for this second copying option. The 5 functionalities already described are also offered when inserting. In contrast to inserting in the default navigator view, not all child objects are included here, but rather only those explicitly marked.

<a id="figure.WiederverwendeteObjekte"></a>

![Image: reused diagnostic objects](images/WiederverwendeteObjekte.png)

**Figure 184. Reused Editorial Objects**

Reused diagnostic objects are indicated by an icon at the upper right of the symbol. This allows them to be recognized at first glance in the tree view.

<a id="figure.KopierenMitAuswahl"></a>

![Image: copying with single selection](images/KopierenCheckBoxBaum.png)

**Figure 185. Copying with Single Selection**

As previously stated, the selected objects can also be reused. At locations in the target object structure, where a reuse of the selected object is permitted, another menu item **Reuse** is given in addition to the context menu item **Insert**. When using drag and drop, the respective **Ctrl** key must be pressed before releasing the mouse button. Doing this forces the selected object and all subordinate objects to be reused.

It should be noted that only the copying process of the object marking is influenced in the marked view. All other menu functions, such as filter, complete, and delete, also affect only the selected editorial objects in the marked view.

A copying process often includes many objects. Thus the procedure will generally take longer. Copying is performed asynchronously, so that you can continue to work at other locations in ODIS Creator in the meantime. As soon as the procedure is completed, the new objects are inserted in the open navigators and you will be prompted whether notifications should be set up for the copied objects, which would indicate that the copying process is complete. While the asynchronous process runs, "Copying editorial objects" is displayed on the right side in the lower status line. This can remind you that the process is not completed yet. There is another button to the right of this, with which you can open a progress indicator in which all asynchronous processes currently running are displayed. You can also cancel the asynchronous processes in this view. However, the server process will not be canceled here, but rather only the response to the client will be stopped with this. This ensures that the copying process is completed entirely and consistently. The number of copying processes permitted to occur at the same time can be set by your group administrator. The default value is 1, so that only one copying process can be started at a time. Other processes will then be prevented with an error message.

<a id="d4e6235"></a>

![Image: progress indicator](images/Fortschrittsanzeige.png)

**Figure 186. Progress Indicator**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-1-7-editorial-object-history.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-1-editorial-object-general-information.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-1-9-location-assignment-of-editorial-objects.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.1.7. Editorial Object History </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.1.9. Location Assignment of Editorial Objects</td></tr></table>
