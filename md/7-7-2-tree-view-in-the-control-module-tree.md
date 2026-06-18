[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.7. Control Module Tree](7-7-control-module-tree.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.7.2. Tree View in the Control Module Tree</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-7-1-importing-control-module-descriptions.md">Prev</a> </td><th align="center" width="60%">7.7. Control Module Tree</th><td align="right" width="20%"> <a accesskey="n" href="7-7-3-object-editor-in-control-module-tree.md">Next</a></td></tr></table>

---

#### <a id="sgbaum.baumansicht"></a>7.7.2. Tree View in the Control Module Tree

The control module tree lists all vehicle projects existing in the group under the structure node „base control modules“. The base control modules of the respective vehicle project are listed under a vehicle project and are sorted by the diagnostic address. The system name in the tree depends on the abbreviation according to the ASAM standard, for example, „0001\_EnginContrModul1“. The **0001** represents the diagnostic address and is displayed as a 4-digit hexadecimal number; migrated control module descriptions are an exception to this rule. These can also be 5 digits.

The control module versions are listed under the base control modules. The base versions of UDS as well as KWP control modules can be seen on the same level here. The level underneath it contains the ECU versions.

You can create any number of additional control module version groups under the UDS base version. This is to check the full use of DTC memories in the knowledge base. You can find additional information about this under [Section 7.7.9, “Control Module Version Groups”](7-7-9-control-module-version-groups.md "7.7.9. Control Module Version Groups").

With the equal treatment of the KWP control modules and the UDS control modules, there is a difference now also made between the base and ECU versions. The classification of levels artificially produced here was described by the definition of the keyword log on the base versions level as well as by the definition of the transport log on the ECU versions level. The base version of a KWP control module is here, for example, the version "BV\_EinginContrModul1KWP2000", the ECU version of this control module is then for example the version "EV\_EnginContrModul1KWP2000CAN20".

<a id="table.hinweis.sgbaum_benennung"></a>

<table border="1" summary="KWP Name"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note:</strong></span> The name of control modules, services, and parameters in KWP have changed completely!</td></tr></tbody></table>

**Table 61. KWP Name**

The control module descriptions with the **„in processing“** status ([1](7-7-2-tree-view-in-the-control-module-tree.md#figure.sgbaum_in_progress "Figure 269. Structure Tree for Control Module Descriptions")) are offered in a separate structure tree comparable to the tree for Logical Links ([2](7-7-2-tree-view-in-the-control-module-tree.md#figure.sgbaum_in_progress "Figure 269. Structure Tree for Control Module Descriptions")).

<a id="figure.sgbaum_in_progress"></a>

![Image: the structure tree for control module descriptions](images/sgbaum_in_bearbeitung.png)

**Figure 269. Structure Tree for Control Module Descriptions**

There are very many control module descriptions in the structure tree from the creation of new versions with every import of UDS control module descriptions. To make the search and use of the current version easier for you, there is the additional filter item **„Current“** (see [Figure 270, “Structure Tree for Current Control Module Descriptions”](7-7-2-tree-view-in-the-control-module-tree.md#figure.sgbaum_aktuell "Figure 270. Structure Tree for Current Control Module Descriptions")) in the structure tree tool bar for the control module descriptions. With the activation, the display of control module descriptions is reduced to what is valid at that time. With the deactivation, all control module descriptions referenced in the last productive baseline are displayed. In the test log for the finishing of editorial objects, an entry is composed when control module descriptions are used that are no longer current.

<a id="figure.sgbaum_aktuell"></a>

![Image: the structure tree for current control module descriptions](images/sgbaum_aktuell.png)

**Figure 270. Structure Tree for Current Control Module Descriptions**

By selecting **Validity** in the navigator menu ([Figure 271, “Structure Tree for Current Control Module Descriptions with Menu Selection”](7-7-2-tree-view-in-the-control-module-tree.md#figure.sgbaum_aktuell.menu "Figure 271. Structure Tree for Current Control Module Descriptions with Menu Selection")), a combined display of control module descriptions currently valid and used in the last production baseline can be seen when **All** is selected.

<a id="figure.sgbaum_aktuell.menu"></a>

![Image: the structure tree for current control module descriptions with menu selection](images/sgbaum_aktuell_alles.png)

**Figure 271. Structure Tree for Current Control Module Descriptions with Menu Selection**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-7-1-importing-control-module-descriptions.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-7-control-module-tree.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-7-3-object-editor-in-control-module-tree.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.7.1. Importing Control Module Descriptions </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.7.3. Object Editor in Control Module Tree</td></tr></table>
