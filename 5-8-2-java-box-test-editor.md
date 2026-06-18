[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.8. Java Box Test](5-8-java-box-test.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.8.2. Java Box Test Editor</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-8-1-java-box-test-navigation-tree.md">Prev</a> </td><th align="center" width="60%">5.8. Java Box Test</th><td align="right" width="20%"> <a accesskey="n" href="5-8-3-status-model.md">Next</a></td></tr></table>

---

#### <a id="javabox.editor"></a>5.8.2. Java Box Test Editor

The editor contains a list of Java boxes for the function code/object to be tested.

When a list element is selected, the corresponding Java box content is displayed, and the list shows which Java boxes have been tested (status accepted or declined) and which must still be tested (status untested).

<a id="figure.javabox.editor"></a>

![Image: Java box test editor](images/javabox_editor.png)

**Figure 108. Java Box Test Editor**

The editor can be put into editing by double-clicking in order to be able to perform a test. Only a tester who was not the last editor of a test object can set the editor to editing.

<a id="figure.javabox.prueferbearbeiter"></a>

![Image: tester may not be the last editor](images/javabox_pruefer_bearbeiter.png)

**Figure 109. Tester May Not Be the Last Editor**

For each list element (Java box), the content of the Java box can be accepted or declined. To decline, the comment field must be filled out (see [Figure 108, “Java Box Test Editor”](5-8-2-java-box-test-editor.md#figure.javabox.editor "Figure 108. Java Box Test Editor")).

The test request can be completed once all Java boxes that needed to be tested have been tested (accepted or declined). Then the status of the test request will be set to completed and it will no longer be visible in the navigation tree.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-8-1-java-box-test-navigation-tree.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-8-java-box-test.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-8-3-status-model.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.8.1. Java Box Test Navigation Tree </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.8.3. Status Model</td></tr></table>
