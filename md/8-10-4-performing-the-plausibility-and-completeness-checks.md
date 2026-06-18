[ODIS Creator Help](odis-creator-help.md) > [8. ODIS Creator Preparation Process](8-odis-creator-preparation-process.md) > [8.10. Plausibility and Completeness Checks](8-10-plausibility-and-completeness-checks.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">8.10.4. Performing the Plausibility and Completeness Checks</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="8-10-3-placeholder.md">Prev</a> </td><th align="center" width="60%">8.10. Plausibility and Completeness Checks</th><td align="right" width="20%"> <a accesskey="n" href="8-10-5-test-status.md">Next</a></td></tr></table>

---

#### <a id="prozess.bereitstellung.pruefung.durchfuehrung"></a>8.10.4. Performing the Plausibility and Completeness Checks

The individual tests are described in detail in the following. These may or may not be performed depending on the selected setting.

##### <a id="prozess.bereitstellung.pruefung.durchfuehrung.fehlerfreiheit"></a>8.10.4.1. Checking Editorial Objects for Correctness

The following items are checked during an editorial object consistency check:

1. Checks if used objects exist in ODIS Creator.
2. It checks in every editorial object that contains images, if the referenced images are in the MOVE database with the correct status
3. The used text entries are checked for validity.
4. A check ensures the EFA codes for the editorial objects have a valid usage status (meaning if they have valid elements and assignments from the perspective of EFA maintenance). The editorial objects that contain usage relationships to EFA codes, that are declared as invalid in the ODIS Creator EFA master data status, may not be provided. The EFA codes dependent on the editorial object are then implicitly labeled with the status isValid = false.
5. Compatibility test between the used DTCs and control module descriptions in the function tests and diagnostic objects.
6. The test for the usage of old or deleted control module descriptions. This test matches the test from [Section 8.10.4.4, “ECU Variant Usage Test”](8-10-4-performing-the-plausibility-and-completeness-checks.md#prozess.bereitstellung.pruefung.durchfuehrung.ecu "8.10.4.4. ECU Variant Usage Test").
7. Tests for the system names
8. Checking the filling in of required fields in the editorial objects
9. Checking the combination of the vehicle model name, model year and the assigned vehicle project
10. Validation of diagnostic address in the control module configuration
11. Calculation of Logical Links
12. Checking the conformity to the XML schema for supplemental documents and function tests
13. Checking the conformity to the DSGVO match word list for supplemental documents and function tests
14. Special checks for the function tests:

    - Checking if the content file is compilable
    - Validity check of the EFA codes included in the content file using the EFA components of the ODIS Creator
    - Checking the existence of the indirect references to diagnostic objects
15. When saving diagnostic objects, the system will check if cyclone and non-cyclone data are present in the suspicion rules as mixed data. If there is mixed data, it will not be possible to save if the brand settings do not allow mixed data. An error message will inform the user of this. Saving will occur if there is no mixed data or if mixed data is allowed in the suspicion rules for the brand. In the latter case, the mixed data will be documented as a note in the consistency check log for the editorial object.

All consistency checks are performed for the working versions of editorial objects. In contrast to the normal consistency checks that are performed for the completion message, it is in this case, not saved itself in the editorial object. For example, the Logical Links are calculated but not saved.

For completed or risk-released editorial objects, the consistency checks have already been successfully performed with the completion message. However, deleting or editing referenced editorial objects may cause inconsistencies in the editorial objects. Therefore, the tests 1 through 4 are performed again for the confirmed completed or risk-released editorial objects. The warnings included in the consistency checks are displayed in the log as errors that do not prevent the deployment.

It is checked for every relevant supplemental document that contains a hotspot, if the referenced documents are available with the corresponding status for the deployment.

After a defined time interval after an order step deadline, it will also be checked for the test if all editorial objects are released in the relevant order steps.

##### <a id="prozess.bereitstellung.pruefung.durchfuehrung.move"></a>8.10.4.2. Checking Content of Used MOVE Objects

For every relevant supplemental document that contains images, it is checked if the referenced images are available with their contents in the MOVE database, in which one tries to download the respective images. If the MOVE database cannot be reached, the test is not performed. The respective message is described in the overview sheet in the test log.

##### <a id="prozess.bereitstellung.pruefung.durchfuehrung.referenz"></a>8.10.4.3. Completeness Check of Referenced Objects

It is checked for every relevant editorial object, if all editorial objects for which it references, are released and are valid for the initial deployment date respective to the performed test.

It tries to uncover the spaces for the deployment in relation to the child objects. The last versions of the child objects are considered for this:

- If the initial deployment deadline for all versions of the child object is after the initial deployment date of the performed test, then an error is given.
- If the initial deployment deadline of the last version of the child object is before the initial deployment deadline of the performed test and the version is not released, then an error is given.

The connection between the equipment network (vehicle model) and the knowledge base is checked in both orientations.

##### <a id="prozess.bereitstellung.pruefung.durchfuehrung.ecu"></a>8.10.4.4. ECU Variant Usage Test

This checks if the ECU variants (EVs) used in the function tests, control module configurations or measured value tables, are available and current in ODIS Creator. If the used ECU variants are not current, the status of the ECU variants as well as the name of the applicable vehicle project are described in the created error message. The test matches the consistency check 6 from [Section 8.10.4.3, “Completeness Check of Referenced Objects”](8-10-4-performing-the-plausibility-and-completeness-checks.md#prozess.bereitstellung.pruefung.durchfuehrung.referenz "8.10.4.3. Completeness Check of Referenced Objects").

##### <a id="prozess.bereitstellung.pruefung.durchfuehrung.verwendung"></a>8.10.4.5. Use of editorial objects from other brands

It will check here if the editorial object of the brand to be checked references an editorial object of another brand.

There are two options for defining the relationship between an editorial object and a brand.

- Allocation of the editorial object to a brand by the link in the equipment network
- Determining the brand reference of an editorial object by the responsible team

For this test, the allocation of the editorial object for a brand by the responsible team is meant with brand allocation.

The editorial objects are taken in the outgoing quantity, that are considered in the test and that are assigned to the specified brand at the time of the test. Valid object versions of the child objects are then gathered that do not belong to the specified brand. Only object references are considered for reuse.

Name references are not considered in this test. The following apply as name references:

- Diagnostic objects to equipment network with exception of the knowledge base
- Function codes to equipment network
- Function codes to diagnostic objects
- Measured value tables to diagnostic objects

For this, references to control modules as well as other imported base objects (vehicle projects, fault locations) are not considered.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="8-10-3-placeholder.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="8-10-plausibility-and-completeness-checks.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="8-10-5-test-status.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">8.10.3. Placeholder </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 8.10.5. Test Status</td></tr></table>
