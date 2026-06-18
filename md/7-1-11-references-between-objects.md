[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.1. Editorial Object General Information](7-1-editorial-object-general-information.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.1.11. References Between Objects</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-1-10-editorial-object-brand-codes.md">Prev</a> </td><th align="center" width="60%">7.1. Editorial Object General Information</th><td align="right" width="20%"> <a accesskey="n" href="7-1-12-delete-editorial-objects.md">Next</a></td></tr></table>

---

#### <a id="redaktion.referenzen"></a>7.1.11. References Between Objects

When deleting editorial objects and when creating references between editorial objects, an order context is always required in the foreground. Even if it turns out that this will not be used in a later process. The order context is necessary, since a reference between the parent object and the reused or moved editorial object is created respectively. If the parent object is released, then this will be set in the currently set order context with a new working version. The released parent object will likewise be taken into processing, if a reference is deleted.

The following apply as a parent object:

- a structuring node (documentation category, function library, etc.)
- a root node
- an object from a vehicle project, control module or fault location tree.
- its reference is a content reference, for which there is already a working version of the parent object by definition.

**Example:** a working version of a vehicle model references a released version of a model year. If the working version of the vehicle model is deleted now, then one does not need an order context for this. This will also cause the released version of the model year to be deleted. However, an order context is now mandatory for this deletion process of a released version.

If no order context is set when creating a reference, then the order context dialog appears to select an order.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-1-10-editorial-object-brand-codes.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-1-editorial-object-general-information.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-1-12-delete-editorial-objects.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.1.10. Editorial Object Brand Codes </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.1.12. Delete Editorial Objects</td></tr></table>
