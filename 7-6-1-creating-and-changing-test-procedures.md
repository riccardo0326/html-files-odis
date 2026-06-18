[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.6. Function Library](7-6-function-library.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.6.1. Creating and Changing Test Procedures</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-6-function-library.md">Prev</a> </td><th align="center" width="60%">7.6. Function Library</th><td align="right" width="20%"> <a accesskey="n" href="7-6-2-creating-and-changing-measured-value-tables.md">Next</a></td></tr></table>

---

#### <a id="testprozedur"></a>7.6.1. Creating and Changing Test Procedures<a id="d4e13400"></a>

Test procedures portray small, reusable pieces of the program. In contrast to function code objects, test procedures have no global pre-run and post-run, but rather only consist of one test step. Test procedures can be accessed within function codes by inserting the procedure node in the test process.

Test procedures can be created in the function library as subnodes of the 'test procedures' group node or as a parallel node to already existing test procedures. Simply select the corresponding object and select **New subnode >> Test procedure** or **New parallel node >> Test procedure** in the context menu. Alternatively, a new test procedure can also be created through the action element subprogram (see [Section 7.14.20.4, “Action Element - Sub-Program”](7-14-20-category-miscellaneous.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Sonstige.Aufruf_Testprozedur "7.14.20.4. Action Element - Sub-Program")) in the function test editor.

The system name of test procedures is subject to the limitations described under [Section 7.6.4.2, “Unique System Name for Function Tests”](7-6-4-function-code-objects.md#funktionscode.eindeutigesystemnamen "7.6.4.2. Unique System Name for Function Tests").

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-6-function-library.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-6-function-library.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-6-2-creating-and-changing-measured-value-tables.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.6. Function Library </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.6.2. Creating and Changing Measured Value Tables</td></tr></table>
