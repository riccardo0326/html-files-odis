[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.1. Editorial Object General Information](7-1-editorial-object-general-information.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.1.12. Delete Editorial Objects</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-1-11-references-between-objects.md">Prev</a> </td><th align="center" width="60%">7.1. Editorial Object General Information</th><td align="right" width="20%"> <a accesskey="n" href="7-1-13-branching-editorial-objects.md">Next</a></td></tr></table>

---

#### <a id="redaktion.loeschen"></a>7.1.12. Delete Editorial Objects

Required editorial objects can no longer be deleted from the ODIS Creator system. Deleting objects in ODIS Creator is a multi-step process. As soon as you delete an object in an editing navigation tree, the object will first be moved to the recycle bin. The deletion of objects is subject to certain conditions. You then have the option in the recycle bin to permanently deleted a deleted object or to restore it to the original position from the recycle bin.

If a released editorial object is deleted, then it is required that an order context is set. The deleted editorial object then appears in the table "Deleted release versions" in the respective order.

##### <a id="redaktion.loeschen.papierkorb"></a>7.1.12.1. Recycle Bin

The recycle bin can be accessed in the editing view through the menu **Extras >> Recycle bin**. The deleted objects in the recycle bin are organized in the list by types (see [Figure 191, “Recycle Bin”](7-1-12-delete-editorial-objects.md#figure.redaktion.papierkorb "Figure 191. Recycle Bin")).

<a id="figure.redaktion.papierkorb"></a>

![Image: recycle bin](images/papierkorb.png)

**Figure 191. Recycle Bin**

The deleted objects are under the type nodes. The objects for this are not structured in parallel, but rather are hierarchically structured. Deleted child nodes are under the likewise deleted parent nodes. If no deleted parent node is in the recycle bin, then the deleted object is listed directly under the node type.

To give a complete summary of the context of a deleted node in relation to its used child objects, the recycle bin not only shows the deleted child objects under a deleted object but also the objects not deleted. The objects not deleted are displayed in gray font in the recycle bin (see [Figure 192, “Recycle Bin Display of Undeleted Child Objects”](7-1-12-delete-editorial-objects.md#figure.redaktion.papierkorb_ungeloescht "Figure 192. Recycle Bin Display of Undeleted Child Objects")). With the additional display of the undeleted editorial objects, you are given a better view of which editorial objects were actually deleted during the last deleting process and which were kept.

<a id="figure.redaktion.papierkorb_ungeloescht"></a>

![Image: recycle bin display of undeleted child objects](images/papierkorb_ungeloescht.png)

**Figure 192. Recycle Bin Display of Undeleted Child Objects**

##### <a id="redaktion.loeschen.vorgang"></a>7.1.12.2. Deleting Process

The open views are kept current when a deleting process occurs, therefore if an editorial object in the navigation tree is deleted, it will automatically be added to the recycle bin. If the deleted editorial object was previously displayed in the recycle bin as an undeleted object in gray, it will then be displayed correctly after the deleting process as a deleted editorial object in black front. The update occurs so that the "Filter again" function is executed by the system on the respective root element. The current open status will be restored as long as it is possible after deleting. This action is necessary, since deleting superordinate editorial objects can change the tree structure considerably. Example: the open status cannot be restored if a diagnostic object is deleted, that is superordinate to an editorial object, that was previously on the highest level. If this is the case, the function „Filter again“ must be executed on the root element. If this is the case, this will add the deleted object to the recycle bin at the first level and then will remove the other object from this level. With this, the open status of the previous object is however lost. If the recycle bin view is closed and reopened again, then the view will be reset the same way as the navigation trees. If an editorial object is permanently deleted from the recycle bin, then it will be immediately removed from the current recycle bin.

As with other navigation trees, filters can be defined in the recycle bin in order to limit the number of visible elements on the interface. After setting a new filter, this filter must be applied to elements in the tree through the context menu **Filter again**.

All deleted editorial objects are displayed in the recycle bin regardless of their original status. If the selected editorial object to be deleted is present at one or more other locations, then you will be informed of this through the existing usage locations dialog. Only the usage locations are displayed in this dialog for your information. There is no direct relationship to the deleting process. Because of this, the following message will appear after closing the usage locations dialog: „Are you sure you want to delete the editorial object?“. You will then still be able to cancel the deleting process, if the editorial object still needs to be used in another context. If the editorial object to be deleted is not used at another location, then the usage dialog is not displayed, and the message of whether you want to delete the editorial object is displayed immediately.

###### <a id="uebersetzungsbedarfe.redaktionsobjekte.loeschen"></a>7.1.12.2.1. Deleting Translation Requirements for Deleted Editorial Objects

If you move released editorial objects to the recycle bin, then the existing translation requirements that were not packaged in the translation packages yet, will be removed from the ODIS Creator system. If translation requirements were still not present, then it will also be ensured that no new translation requirements are generated afterward.

Many versions may exist in the ODIS Creator system for a released editorial object. Since only the last released version of an editorial object is visible, then also only the last released version of an editorial object can be moved to the recycle bin. However for all versions of an editorial object, the translation requirements, that have not been packed in the translation packages yet, can still exist. If you move the last released version of the editorial object to the recycle bin, then the translation requirements for all versions of the editorial object are also removed from the ODIS Creator system.

Some versions of the editorial object can already be contained in an old deployment. All versions of the editorial object that are already in a deployment, are exported when a baseline is rebuilt again, regardless of if the last released version was deleted or not. For such versions of the editorial object, translation requirements may still exist in the ODIS Creator system, that have not been sent to translation yet. The ODIS Creator system will provide that the translations for such versions of the editorial object can be retrieved later and they are exported when the old baseline is rebuilt again. To ensure this, the translation requirements for the versions of editorial objects are not deleted, if they are included in deployments as well as all previous versions.

The [Figure 193, “Deleting Translation Requirements for Deleted Editorial Objects”](7-1-12-delete-editorial-objects.md#figure.bedarfe.loeschen.redaktionsobjekt "Figure 193. Deleting Translation Requirements for Deleted Editorial Objects") clarifies this process. If the user moves the last released version of editorial object A into the recycle bin (version 1.0.3), the translation marker and the translation requirements, that have not yet been sent to translation, are deleted (particularly for version 1.0.3 and version 1.0.2). From version 1.0.1 of the editorial object, the translation requirements and translation markers are no longer deleted.

<a id="figure.bedarfe.loeschen.redaktionsobjekt"></a>

![Image: deleting translation requirements of deleted editorial objects](http://127.0.0.1:55991/help/topic/MasterData_Client_Control/html/images/Bedarfe_gel%C3%83%C2%B6schter_redaktionsobjekte_entfernen.jpg)

**Figure 193. Deleting Translation Requirements for Deleted Editorial Objects**

If you restore an editorial object that was previously moved into the recycle bin, then a new working version of the editorial object is created. If you release this version of the editorial object, then a translation marker is generated for this version of the editorial object. After this, the translation requirements will also be generated, if changes to the translation-relevant components of the editorial object were made relating to the existing translations or translation requirements of the earlier versions of the editorial object.

##### <a id="papierkorb.loeschen.redaktionsobjekte.regeln"></a>7.1.12.3. Rules for Deleting Editorial Objects

1. Only subordinate editorial objects are deleted that match the same primary type as the selected root element.
2. Editorial objects can only be deleted in the context in which they can also be created. For example, a model year can also be deleted in the knowledge base navigator, since it can be created in the knowledge base navigator under a vehicle model that is linked to a knowledge base.
3. All subordinate editorial objects are deleted in cascading order if they are not used at any other location. Therefore the cascading deletion is also applied to the reusable editorial objects. However only subordinate objects are deleted, which have the same processing status as the editorial object to be deleted. Here it is only differentiated, in summary, according to a release status (includes the status „In review“, „Risk-released“, „Released and tested“ or „Reviewed with errors“) and to a working status that includes all of the remaining statuses. The situation is explained again in more detail in [Section 7.1.12.4, “Status Consideration for Cascade Delete”](7-1-12-delete-editorial-objects.md#papierkorb.loeschen.kaskadierend "7.1.12.4. Status Consideration for Cascade Delete").
4. Editorial objects, that are linked to the content of another editorial object through the ID, cannot be deleted. For example, when using a measured values table in a function test. If this is the case, the entire deleting process is canceled and you will receive the following error message: „The "system name" object cannot be deleted, because it is still being used in the following objects: systemname1, systemname2.“

   Diagnostic objects that are used in a function test are the exception hare. Diagnostic objects can be referenced within function tests by name (for example, in suspicion lists) and by ID (as "indirectDO" in document nodes). Deleting is permitted in both cases, because it cannot be determined which type of reference is being used during the deletion.
5. Editorial objects, that are only linked by a name reference to the content of another editorial object, are deleted and the deleting process will not be canceled. For example, when using an equipment network object in a variant rule.

<a id="figure.papierkorb.loeschen.redaktionsobjekt"></a>

![Image: example scenario for deleting an editorial object](images/papierkorb_loeschen_redaktionsobjekt.png)

**Figure 194. Example Scenario for the Deletion of an Editorial Object**

##### <a id="papierkorb.loeschen.kaskadierend"></a>7.1.12.4. Status Consideration for Cascade Delete

The cascade delete is performed depending on the processing status of the output object to be deleted. If the object is in one of the release statuses „In review“, „Risk released“, „Released tested“ or „Reviewed with errors“, then only the child objects that are in one of these statuses are also deleted. Several deleting scenarios are portrayed in the [Table 42, “Cascade Delete Explanation for Editorial Objects”](7-1-12-delete-editorial-objects.md#table.papierkorb.loeschen.kaskadierend "Table 42. Cascade Delete Explanation for Editorial Objects"), in order to illustrate the situation. It is still determined for the deletion, if the subordinate editorial object will be reused at another located. In the table, a version number 1 or 2 means this is the first version of this object, whereas a version number 1.1 or 2.1 implies that there is indeed an earlier release version. If a version is marked with an asterisk, then it is a working version. The original scenario is portrayed as follows: DGO1->DGO2 means that the diagnostic object 2 was subordinate to diagnostic object 1. DGO1=>DGO1.1\*->DGO2 means that DGO2 was first subordinate to the working version DGO1.1\*. The deletion process always stems from DGO1(\*), or DGO1.1(\*).

<a id="table.papierkorb.loeschen.kaskadierend"></a>

<table border="1" summary="Cascade Delete Explanation for Editorial Objects"><colgroup><col align="center"/><col align="left"/><col align="left"/></colgroup><thead><tr><th align="center">Initial situation</th><th align="left">Resulting situation with single use of DGO2.x</th><th align="left">Resulting situation with multiple use of DGO2.x</th></tr></thead><tbody valign="top"><tr><td align="center" valign="top">DGO1 -&gt; DGO1.1* -&gt; DGO2</td><td align="left" valign="top">Cancellation, because DGO2 is not assigned to a knowledge base or DGO -&gt; DGO1.1*-&gt;DGO2</td><td align="left" valign="top">Only DGO1.1* deleted -&gt; DGO1</td></tr><tr><td align="center" valign="top">DGO1-&gt;DGO2 -&gt; DGO1.1* -&gt; DGO2</td><td align="left" valign="top">Only DGO1.1* deleted -&gt; DGO1-&gt;DGO2</td><td align="left" valign="top">Only DGO1.1* deleted -&gt; DGO1-&gt;DGO2</td></tr><tr><td align="center" valign="top">DGO1-&gt;DGO2 -&gt; DGO1.1* -&gt; DGO2.1*</td><td align="left" valign="top">DGO1.1* and DGO2.1* are deleted -&gt; DGO1-&gt;DGO2</td><td align="left" valign="top">Only DGO1.1* deleted -&gt; DGO1-&gt;DGO2.1*</td></tr><tr><td align="center" valign="top">DGO1-&gt;DGO2 -&gt; DGO1 -&gt; DGO2.1*</td><td align="left" valign="top">Cancellation, because DGO2.1* is not assigned to a knowledge base or DGO -&gt; DGO1-&gt;DGO2.1*</td><td align="left" valign="top">Only DGO1 deleted -&gt; WBx/DGOx-&gt;DGO2.1*</td></tr><tr><td align="center" valign="top">DGO1-&gt;DGO2</td><td align="left" valign="top">Both objects deleted</td><td align="left" valign="top">Only DGO1 deleted -&gt; WBx/DGOx-&gt;DGO2</td></tr><tr><td align="center" valign="top">DGO1*-&gt;DGO2*</td><td align="left" valign="top">Both objects deleted</td><td align="left" valign="top">Only DGO1* deleted -&gt; WBx/DGOx-&gt;DGO2*</td></tr><tr><td align="center" valign="top">DGO1*-&gt;DGO2-&gt;DGO3*</td><td align="left" valign="top">Cancellation, because DGO2 is not assigned to a knowledge base or DGO -&gt; DGO1*-&gt;DGO2-&gt;DGO3*</td><td align="left" valign="top">DGO1* and DGO3* are deleted as long as DGO3* is not used multiple times -&gt; WBx/DGOx-&gt;DGO2</td></tr></tbody></table>

**Table 42. Cascade Delete Explanation for Editorial Objects**

##### <a id="papierkorb.wiederherstellen.redaktionsobjekte"></a>7.1.12.5. Restoring Editorial Objects

You can restore deleted editorial objects located in the recycle bin at any time. You have the option for this to only restore the selected editorial object itself or include all of its subnodes. For this selection option, there are two menu items („object only“ and „object structure“) given under the „Restore“ menu item. If you select the „object structure“ menu item, then the editorial object will be restored with the deleted subnodes subordinate to it. The corresponding menu item is deactivated for the displayed editorial objects that are not deleted. The recycle bin display will refresh after restoring, in which the „Filter again“ function is performed by the system at the superordinate element of the restored editorial object. In other words: regardless of whether you have selected the „object only“ or „object structure“ function, the root element will always be taken from the element, that you have previously selected to restore.

In both the „object only“ and „object structure“ cases, each individual restored editorial object again will be inserted at its original usage location; therefore all references are restored to the condition before deleting, as long as the linked editorial objects were not deleted in the meantime. Since the links were not changed by the deletion, the links also appear respectively at the newest object version after restoring. The content matches the editorial object in the version before the deletion, including its variants and suspicion rules, except for the version and the properties „Creator“, „Creation date“, „Status date“ and „Last change“.

Every restored editorial object is set to the „in processing“ status, regardless of its status when it was deleted. The current date is set as the editorial object creation date, if it has to do with an already published object. The original creation date does not change for unpublished objects. In every case, the version of the restored editorial object will be increased by one in the third position.

##### <a id="papierkorb.loeschen.endgueltig"></a>7.1.12.6. Deleting Editorial Objects Permanently

You can select the deleted editorial objects in the recycle bin. Through a corresponding context menu item „Delete permanently“, you can delete these editorial objects permanently and thus remove it from the recycle bin. The deletion process takes place asynchronously in the background, so that you will not be prevented from continuing your work. As long as the progress bar (see [Figure 195, “Progress Bar – Delete from the Recycle Bin”](7-1-12-delete-editorial-objects.md#figure.redaktion.progressbar "Figure 195. Progress Bar – Delete from the Recycle Bin")) appears, the deletion process is active. Two sub-menu items “Object only” and “Object structure” will be given at the context menu item to decide, if you would also like to delete all subordinate editorial objects with the editorial object or just the editorial object itself. If you select the option, that all subordinate editorial objects should be permanently deleted, then all subnodes marked for deletion will be permanently deleted. All grayed-out objects not marked for deletion will be kept. The recycle bin update after a deleting process occurs that same as updating after restoring.

<a id="figure.redaktion.progressbar"></a>

![Image: progress bar – delete from the recycle bin](images/papierkorb_progressbar.jpg)

**Figure 195. Progress Bar – Delete from the Recycle Bin**

**Attention!** Permanently deleted objects cannot be restored!“. You can close this dialog with „OK“ or „Cancel“. „Cancel“ will cancel the deleting process and the recycle bin will not change.

##### <a id="papierkorb.sonderfall"></a>7.1.12.7. Special Case for Control Module Descriptions

The previous information relating to deleting and restoring editorial objects in an editing operation also applies the same way to control module descriptions (functional groups, control module groups and control module versions). However, the system behaves differently in the following ways:

- A control module description that is linked to editorial object content by the ID can still be deleted, as opposed to an editorial object.
- Corresponding to their status before the deletion, all control module descriptions receive the status „In processing“ or „Risk released“.
- The control module description version stays the same when restored and is not increased.
- If a control module description version that was marked as deleted in ODIS Creator is imported again, then this version marked for deletion will be restored and updated (if necessary) corresponding to the imported data.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-1-11-references-between-objects.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-1-editorial-object-general-information.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-1-13-branching-editorial-objects.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.1.11. References Between Objects </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.1.13. Branching Editorial Objects</td></tr></table>
