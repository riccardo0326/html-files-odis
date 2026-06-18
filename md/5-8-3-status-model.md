[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.8. Java Box Test](5-8-java-box-test.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.8.3. Status Model</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-8-2-java-box-test-editor.md">Prev</a> </td><th align="center" width="60%">5.8. Java Box Test</th><td align="right" width="20%"> <a accesskey="n" href="6-odis-creator-order-management-process.md">Next</a></td></tr></table>

---

#### <a id="javabox.statusmodell"></a>5.8.3. Status Model

The process for a function code that contains Java boxes is as follows:

<a id="figure.javabox.statusmodell"></a>

![Image: Java box test status model](images/javabox_statusmodell.png)

**Figure 110. Status Model for Function Code with Java Boxes**

When the “Confirmed completed” status is reached, the check for untested Java boxes is triggered:

- If there is an untested Java box, a test request is generated and the function code is set to the “In testing” status.
- If there are no untested Java boxes, then the function code status will be set to "Confirmed completed” or “Risk released”

When the check is completed:

- If all Java boxes were accepted, the function code status will change to “Confirmed completed” or “Risk released”.
- If at least one Java box was not accepted, the function code status will change to “In processing” and an entry will be created in the consistency check. See [Figure 111, “Function Code with Java Box Consistency Check”](5-8-3-status-model.md#figure.javabox.consistecy "Figure 111. Function Code with Java Box Consistency Check").

<a id="figure.javabox.consistecy"></a>

![Image: function code with Java box consistency check](images/javabox_consistency_check.png)

**Figure 111. Function Code with Java Box Consistency Check**

The author has the ability to change a function code status from “In testing” back to “In processing”. The following information window is displayed.

<a id="figure.javabox.incheck"></a>

![Image: processing function code in testing](images/javabox_inPruefung_inBearbeitung.png)

**Figure 112. Processing Function Code In Testing**

If the processing is forced, the test request will be deleted. If the test request cannot be deleted, the forced processing will be declined and an error dialog will be generated.

<a id="figure.javabox.delete"></a>

![Image: processing function code in testing, test request cannot be deleted](images/javabox_inBearbeitung_nichtLoeschen.png)

**Figure 113. Processing Function Code In Testing, Test Request Cannot Be Deleted**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-8-2-java-box-test-editor.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-8-java-box-test.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="6-odis-creator-order-management-process.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.8.2. Java Box Test Editor </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 6. ODIS Creator Order Management Process</td></tr></table>
