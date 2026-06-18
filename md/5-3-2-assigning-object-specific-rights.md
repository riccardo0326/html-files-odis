[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.3. Rights](5-3-rights.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.3.2. Assigning Object-Specific Rights</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-3-1-assignment-of-technical-rights.md">Prev</a> </td><th align="center" width="60%">5.3. Rights</th><td align="right" width="20%"> <a accesskey="n" href="5-3-3-assignment-of-meta-roles.md">Next</a></td></tr></table>

---

#### <a id="objektspezifische.rechte"></a>5.3.2. Assigning Object-Specific Rights

<a id="d4e2207"></a>

<table border="1" summary="Note for Assigning Object-Specific Rights"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Symbol: Note" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Note:</strong></span> When assigning object-specific rights, you must proceed very carefully so that the ODIS Creator process will not be affected and is able to continue operating. You should only apply changes if you have received extensive training for this function and you must always make sure that only the intended adjustments which you have made are saved.</td></tr></tbody></table>

**Table 20. Note for Assigning Object-Specific Rights**

  

To display the allocation of object-specific rights for a roll, the respective roll must be clicked on in the rights management navigator ([Figure 60, “Rights Management Navigator”](5-3-1-assignment-of-technical-rights.md#administration.rechte "Figure 60. Rights Management Navigator")). The corresponding editor will open for display in the right section. To change the allocation of object rights, the editor must be opened in [edit mode](3-2-5-editor.md "3.2.5. Editor") ([Figure 64, “Object Rights”](5-3-2-assigning-object-specific-rights.md#figure.objektrechte "Figure 64. Object Rights")). It will display which roll is currently opened at the top of the editor, for example, "author". The object type names, attribute names and the status labels cannot be changed and only internal names are available in ODIS Creator. This is generally an abbreviation of the full English name.

<a id="figure.objektrechte"></a>

![Image: editing object rights](images/objektrechte.png)

**Figure 64. Object Rights**

Only object types that are consistent with the functional rights of the role can be selected in the **Object type** [selection field](2-2-general-definitions-and-glossaries.md#auswahlfeld). For example, the **order header** entry can only be selected if the roll of a functional right is assigned, such as **New order header**, **Change order header** or **Delete order header** If the editor view was accessed through a [function editor](5-3-1-assignment-of-technical-rights.md#zuordnung.funktionale.rechte "5.3.1.2. Allocation of Functional Rights (Function Editor)") link, the corresponding object type is already preselected.

In the **Condition** [selection field](2-2-general-definitions-and-glossaries.md#auswahlfeld), the conditions that the object type can assume can be selected.

In the **Object type rights** table, the object type attributes are displayed. In two other columns, two rights (none, read, version, write, delete) can be specified respectively per attribute and condition for the roll. The **right (default)** is applied if a user's team does not have the role responsible for the object. In contrast, the **right (responsible)** is applied if the user's team has the role responsible for the object.

The selection fields for the **Rights (responsible)** column are dynamically influenced by the implementation of rights in the **Rights (default)** column. Only the same right or a higher level right will be offered for selection. They will also be set to the default rights, if they were still not set to any rights or a lower right.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-3-1-assignment-of-technical-rights.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-3-rights.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-3-3-assignment-of-meta-roles.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.3.1. Assignment of Technical Rights </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.3.3. Assignment of Meta Roles</td></tr></table>
