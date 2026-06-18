[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.1. Editorial Object General Information](7-1-editorial-object-general-information.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.1.13. Branching Editorial Objects</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-1-12-delete-editorial-objects.md">Prev</a> </td><th align="center" width="60%">7.1. Editorial Object General Information</th><td align="right" width="20%"> <a accesskey="n" href="7-1-14-editorial-object-complaints.md">Next</a></td></tr></table>

---

#### <a id="redaktion.branchen"></a>7.1.13. Branching Editorial Objects

While continuing to develop an editorial object, it may be necessary under certain circumstances to perform a quick adjustment due to responses from other systems. At the same time, the new adjustments to this editorial object are not scheduled for a publication yet, and therefore the editorial object cannot be released simply by the normal workflow. For this scenario, there is the option to create a branch for an editorial object.

As the foundation for a branch, every release version of the editorial object can be used.

##### <a id="redaktion.branchen.start"></a>7.1.13.1. Start Branching

To be able to start the branch for an editorial object, there must already be at least one released version for this editorial object. Based on the last released version, a new working version must still exist and this must be in the "in processing" status.

If all these conditions are met, "Create branch object" can be initiated through the context menu in the navigator. This will start the branching and a dialog will open to select the base version.

<a id="figure.branch.dialog"></a>

![Image: selection dialog for creating a branch object](images/Auswahl_Branch_Basisobjekt.png)

**Figure 196. Selection Dialog for Creating a Branch Object**

If the current version is already a branch version, then a dialog will appear indicating that the editorial object is already a branch version.

<a id="figure.branch.hinweis"></a>

![Image: message dialog for revised branch](images/hinweis_branchen.png)

**Figure 197. Message Dialog for Revised Branch**

The current working version is shaded in the background. This makes it no longer visible to the author. A new working version is created based on the selected released version.

The branch object is assigned to the currently set context. If no order context is set when creating a branch object, then the order context dialog appears to select an order.

##### <a id="redaktion.branchen.durchfuehren"></a>7.1.13.2. Executing the Branching Process

After starting the branching process, the author can make all desired changes to the editorial object as usual. The usual processes from the workflow of the editorial object, such as complete and release, are available as before.

While the working version is shaded and the branch version is not released, the branch object will be rebuilt in test baselines. Furthermore, the last released version that has reached its market introduction date, is included in the production baseline.

##### <a id="redaktion.branchen.end"></a>7.1.13.3. Ending the Branching Process

Branching is normally ended automatically. Through the risk-release of the branch version, the original working version, that was shaded until now and therefore not visible, is reactivated and can be viewed as the current working version in the navigator. The branch version will be the last released version of the editorial object.

Branch objects are each arranged at the end of the version history, even if they relate to another previously released version (base version). The version from which the branch object was created is also displayed in the editorial object history.

If other released versions are located between the branch version and the base version, then this does not change. The changes applied in the branch version are not transferred to these versions. The transfer of changes to the subsequent restored version is also still the responsibility of the appropriate author. The restored working version is ordered in the version history at the end, thus behind the branch version.

Now the working version, which was previously shaded, is not contained in test baselines. The released branch version is first included in the production baselines when the market introduction date is reached.

The branching will manually end, if you discard and delete the branch version. This will automatically make the shaded old version active again and will display in the navigator.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-1-12-delete-editorial-objects.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-1-editorial-object-general-information.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-1-14-editorial-object-complaints.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.1.12. Delete Editorial Objects </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.1.14. Editorial Object Complaints</td></tr></table>
