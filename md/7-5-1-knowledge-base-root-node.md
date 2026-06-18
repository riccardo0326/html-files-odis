[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.5. Knowledge base](7-5-knowledge-base.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.5.1. Knowledge Base Root Node</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-5-knowledge-base.md">Zurück</a> </td><th align="center" width="60%">7.5. Knowledge base</th><td align="right" width="20%"> <a accesskey="n" href="7-5-2-diagnostic-objects.md">Weiter</a></td></tr></table>

---

#### <a id="wissesbasis.wurzelknoten"></a>7.5.1. Knowledge Base Root Node

Every knowledge base has a knowledge base root node. This root node always represents the first level in the knowledge base navigation tree. The respective diagnostic object tree is then spread out under this root node. The function test, that can be in a child relationship to this root node, is declared as a module start and/or module end test (see [Abbildung 263, „Specifying Start/Start (background)/End Module“](7-5-3-specify-the-used-relationship.md#figure.redaktion.wissensbasis.verwendetbeziehung.wbs.funktionstest "Abbildung 263. Specifying Start/Start (background)/End Module")). These function tests are then used as initial or final tests on a vehicle.

##### <a id="wissensbasis.anlegen"></a>7.5.1.1. Creating a New Knowledge Base Root Node<a id="d4e11829"></a>

You can create a new knowledge base root node by selecting an already existing knowledge base root node and then clicking on the menu item **New parallel node > Knowledge base** in the context menu or click on **Parallel node > Knowledge base** in the Insert selection menu.

A new knowledge base root node can also be created without selecting an already existing knowledge base object. For this, the menu item **Subnode > Knowledge base** must be selected in the context menu or in the selection menu.

The system name of the knowledge base may not contain any special characters, but rather only consists of the letters A-Z, numbers and underscores. Otherwise, it can cause problems in further processing when resolving the name (for example, when using it as a directory name).

##### <a id="wissensbasis.attribute"></a>7.5.1.2. Knowledge Base Root Node Attributes<a id="d4e11840"></a>

<a id="figure.redaktion.wissensbasis.attribute"></a>

![Image: attribute of a knowledge base root node](images/wbs_attribute.png)

**Abbildung 248. Knowledge Base Root Node Attributes**

  

**Migration protection:**

This attribute is explained in [Section 7.1.1, “Creating a New Editorial Object”](7-1-1-creating-a-new-editorial-object.md "7.1.1. Creating a New Editorial Object").

**Internal:**

The object is indeed prepared, however it is not displayed in ODIS Service on the interface or in the selection of components.

**P-differ:**

Specifically, if referenced test programs have been collected at this diagnostic object for a P-differ export.

**Remote diagnosis:**

Specifies if the knowledge base should be marked for usage in remote diagnosis. If the attribute is set, the respective object can be included in the export scope for remote diagnosis.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-5-knowledge-base.md">Zurück</a> </td><td align="center" width="20%"><a accesskey="u" href="7-5-knowledge-base.md">Nach oben</a></td><td align="right" width="40%"> <a accesskey="n" href="7-5-2-diagnostic-objects.md">Weiter</a></td></tr><tr><td align="left" valign="top" width="40%">7.5. Knowledge base </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Zum Anfang</a></td><td align="right" valign="top" width="40%"> 7.5.2. Diagnostic objects</td></tr></table>
