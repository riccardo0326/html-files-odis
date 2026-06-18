[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.1. Editorial Object General Information](7-1-editorial-object-general-information.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.1.15. Cardinalities of Editorial Objects</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-1-14-editorial-object-complaints.md">Prev</a> </td><th align="center" width="60%">7.1. Editorial Object General Information</th><td align="right" width="20%"> <a accesskey="n" href="7-1-16-creating-formatted-text.md">Next</a></td></tr></table>

---

#### <a id="redaktion.kardinalitaet"></a>7.1.15. Cardinalities of Editorial Objects

The creation, copy and usage of editorial objects under other editorial objects causes references to be made between the respective objects. These references are subject to the so-called cardinality conditions. This will regulate which object types may form references. Furthermore the amount will be set there of how often an editorial object may reference another of a certain type. For example, a vehicle model may only be referenced by a knowledge base. However, a knowledge base may reference any number of vehicle models. Thereby, the following three cardinalities are distinguished in ODIS Creator, whereby the mentioned error messages contain example data and may read differently in the specific error scenario.

##### <a id="redaktion.kardinalitaet.standard"></a>7.1.15.1. Normal Cardinality Condition

It is simply defined here, which object types may be in direct relationship to each other. This also regulates how often which object types are referenced, or how often this may be used under another object type.

- Normally, the ODIS Creator interface is designed so that the user can only create references between object types that are permitted. However, if an action causes two editorial objects to create a reference that is not allowed despite the design, then it will be blocked by the system and the user will be given one of the following error messages:

  The editorial object 'Combi' with the 'Variant' type cannot be assigned to an object with the 'Brand' type.

  No object from the 'Variant' type can be assigned under the editorial object 'Volkswagen' wit the 'Brand' type.
- The amount of times an editorial object of a specific type is used may also be limited under editorial object types.

  Example: a vehicle model may only be assigned one time to a knowledge base.

  Error message: the 'remaining vehicles' editorial object with the 'vehicle model' type can only be assigned a maximum of 1 time to an object from the 'knowledge base' type.
- The minimum amount of object types to which an editorial object must be assigned is also set.

  Example: in the equipment network, it is always necessary that an editorial object is assigned to the type on the next-highest level. For example, an engine object must always be assigned to one variant.

  Error message: the editorial object 'Engine XY' with the 'Engine' type must be assigned at least one time to an object with the 'Variant' type.
- The same also applies to the minimum amount of object types that must be subordinate to an editorial object.

  Example: a measured value table must always be assigned to a control module description.

  Error message: the editorial object 'Get\_02\_\_\_\_0AM\_1\_1007\_11' with the 'measured value table' type must have at least one subordinate object with the 'control module group' type.
- Finally, the maximum amount of object types that can be subordinate to an editorial object is limited.

  Example: only one control module description can be assigned to one control module configuration.

  Error message: the editorial object 'BV\_DashBoardUDS/MultipleBrands' with the 'control module configuration' type may only have a maximum of one subordinate object with the 'control module group' type.

##### <a id="redaktion.kardinalitaet.or"></a>7.1.15.2. Or-Cardinality Condition

For an Or-condition, an editorial object must be assigned to at least one other editorial object from a specific type set.

Example: a diagnostic object must always be assigned to at least one knowledge base object or diagnostic object. This however also permits that the diagnostic object is assigned to one knowledge base object and multiple diagnostic objects at the same time.

Error message: for the editorial object '17\_instrument cluster', none of the following alternative cardinality conditions were met for one sub(/super)ordinate object:

Knowledge base: 1..1

Diagnostic object: 1..\*

##### <a id="redaktion.kardinalitaet.xor"></a>7.1.15.3. Exclusive-Or Cardinality Condition

An exclusive-or condition then exists, if a complete group of object types would be permitted under or above an editorial object. However, as soon as an editorial object with a type from this group is assigned, other objects of this type can only be assigned still and the remaining types are excluded.

Example: control module configurations can be assigned in principle to ODX/KWP control module groups. However, only one control module description from the 4 categories mentioned may be assigned to one specific control module configuration.

Error message: the editorial object 'BV\_DashBoardUDS/Mehrmarke' ('BV\_DashBoardUDS/MultipleBrands') must exclusively be assigned to or be superordinate to an editorial object from the following types: UDS control module group, KWP control module group, UDS control module variants, KWP control module variants

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-1-14-editorial-object-complaints.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-1-editorial-object-general-information.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-1-16-creating-formatted-text.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.1.14. Editorial Object Complaints </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.1.16. Creating Formatted Text</td></tr></table>
