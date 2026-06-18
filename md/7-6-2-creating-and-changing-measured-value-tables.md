[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.6. Function Library](7-6-function-library.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.6.2. Creating and Changing Measured Value Tables</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-6-1-creating-and-changing-test-procedures.md">Prev</a> </td><th align="center" width="60%">7.6. Function Library</th><td align="right" width="20%"> <a accesskey="n" href="7-6-3-creating-and-changing-default-measurements.md">Next</a></td></tr></table>

---

#### <a id="messwertetabelle"></a>7.6.2. Creating and Changing Measured Value Tables<a id="d4e13411"></a>

Measured value tables are objects to bundle defined measuring points from control modules as well as to define specified values for these measuring points and have no display name. The ODIS Creator supports two different log types for control modules (UDS & KWP).

The new creation of UDS measured value tables is **not possible**, however can contain UDS measured value tables in ODIS Creator that are from the previous system, and can also continue to be used. These existing UDS measured value tables serve only as the supplement of the measured values for a UDS control module in the control module descriptions, which are prepared by the **specified values, the suspicion lists and the message texts**. For UDS control modules, all measured values in ODIS Creator are read through the ODX data set available in running time.

The creation of KWP measured value tables is possible. A KWP measured value table can be linked to a KWP control module, in which it is dragged from the control module tree navigator to the used list in the object editor of the measured values table per drag and drop. The purpose of a KWP measured values table is to compile and allocate the defined measured values to the KWP control module description assigned to the measured values table.

The description text or the message for a measured value can be created with assistance from the [rich text editor](7-1-16-creating-formatted-text.md "7.1.16. Creating Formatted Text").

Measured value tables can be created in the function library as subnodes of the 'measured value tables' group node or as a parallel node to already existing measured value tables. Simply select the corresponding object and select **New subnode >> Measured value table** or **New parallel node >> Measured value table** in the context menu.

A measured value within a measured value table can be inactive or active. Inactive means that the measured value cannot be offered for reuse and is not provided. A measured value can be set to (in)active in the measured value table editor. A measured value is set to active by default or when created.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-6-1-creating-and-changing-test-procedures.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-6-function-library.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-6-3-creating-and-changing-default-measurements.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.6.1. Creating and Changing Test Procedures </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.6.3. Creating and Changing Default Measurements</td></tr></table>
