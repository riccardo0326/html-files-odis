[ODIS Creator Help](odis-creator-help.md) > [8. ODIS Creator Preparation Process](8-odis-creator-preparation-process.md) > [8.10. Plausibility and Completeness Checks](8-10-plausibility-and-completeness-checks.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">8.10.7. Plausibility and Completeness Check Log</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="8-10-6-test-object-editor.md">Prev</a> </td><th align="center" width="60%">8.10. Plausibility and Completeness Checks</th><td align="right" width="20%"> <a accesskey="n" href="8-10-8-notification.md">Next</a></td></tr></table>

---

#### <a id="prozess.bereitstellung.pruefung.protokoll"></a>8.10.7. Plausibility and Completeness Check Log

As soon as the plausibility and completeness check is completed and the respective test object has one of the final statuses "Completed" or "Error", the location administrator can view the progression of the test with the log files. To do this, select the respective test object in the navigator. The button "Download log" is now available in the editor. As with the deployment, the user can thereby download the log file as a zip file.

When the automatic tests are performed after the deployment, the log is also stored in the log folder of the respective baseline on the server.

For the manual test, the log is also stored in the specified folder on the replacement drive. The log is stored in the sub-folder with the name of the respective test type.

For each test, a log in the form of an Excel table is created with the same name as the corresponding test object. This Excel file will always contain the following data sheets:

- One [overview sheet](8-10-7-plausibility-and-completeness-check-log.md#prozess.bereitstellung.pruefung.protokoll.uebersicht "8.10.7.1. Overview Sheet")
- One for those ["With errors"](8-10-7-plausibility-and-completeness-check-log.md#prozess.bereitstellung.pruefung.protokoll.fehler "8.10.7.2. \"With Errors\" Table Sheet"), thus the list of all checked editorial objects for which an error was created
- One for those ["Without errors"](8-10-7-plausibility-and-completeness-check-log.md#prozess.bereitstellung.pruefung.protokoll.fehlerfrei "8.10.7.3. \"Without Errors\" Table Sheet"), thus the list of all checked editorial objects for which no error was created
- One for the ["order headers and order steps"](8-10-7-plausibility-and-completeness-check-log.md#prozess.bereitstellung.pruefung.protokoll.auftrag "8.10.7.4. \"Order Headers And Order Steps\" Table Sheet"), thus the list of all order headers and order steps for all included editorial objects.
- One for the ["references to other brands"](8-10-7-plausibility-and-completeness-check-log.md#prozess.bereitstellung.pruefung.protokoll.verwendung "8.10.7.5. \"References to other brands\" Table Sheet"), therefore the list of all editorial objects, which reference editorial objects of other brands.

##### <a id="prozess.bereitstellung.pruefung.protokoll.uebersicht"></a>8.10.7.1. Overview Sheet

The overview sheet includes a summary of the performed test. These include:

- [Imported Data Information](8-10-7-plausibility-and-completeness-check-log.md#prozess.bereitstellung.pruefung.protokoll.uebersicht.daten "8.10.7.1.1. Imported Data Information")
- [Test information](8-10-7-plausibility-and-completeness-check-log.md#prozess.bereitstellung.pruefung.protokoll.uebersicht.info "8.10.7.1.2. Test Object Information")
- [Statistics for the Considered Editorial Objects](8-10-7-plausibility-and-completeness-check-log.md#prozess.bereitstellung.pruefung.protokoll.uebersicht.statistik "8.10.7.1.3. Statistics for the Considered Editorial Objects")
- [Test Overview](8-10-7-plausibility-and-completeness-check-log.md#prozess.bereitstellung.pruefung.protokoll.uebersicht.pruefungen "8.10.7.1.4. Test Overview")

###### <a id="prozess.bereitstellung.pruefung.protokoll.uebersicht.daten"></a>8.10.7.1.1. Imported Data Information

Among other information, the date and the version of the data that data was imported into ODIS Creator are entered in the first worksheet. For most of this data, the date of the last change or the import date and the version are saved. This date is then displayed in the log. This applies to the following data:

- Reference table
- Measured value default display
- Document categories
- Vehicle status texts
- System texts
- Service references
- Master components list

###### <a id="prozess.bereitstellung.pruefung.protokoll.uebersicht.info"></a>8.10.7.1.2. Test Object Information

The following information in relation to the test itself is added to the worksheet:

- Name of test
- Test type
- Test trigger
- Test sort
- Provision date

  The simulated deployment deadline for the plausibility and completeness check started manually for the production baseline. Otherwise „n/a“ is entered.
- Order step deadline

  The deadline used when tests are automatically started after reaching the deadline of the test order step. Otherwise „n/a“ is entered.
- Start time (date and time) of the baseline creation when tests are automatically started after a baseline creation
- End time (date and time) of the baseline creation for which the ODIS Creator has ended the storage of baseline data on the replacement drive
- Baseline version
- Baseline creation date
- Test started
- Test ended

###### <a id="prozess.bereitstellung.pruefung.protokoll.uebersicht.statistik"></a>8.10.7.1.3. Statistics for the Considered Editorial Objects

During the test, the statistics are compiled for the considered editorial objects. The statistics are listed for the following editorial objects:

- Diagnostic objects per knowledge base
- Equipment network objects per vehicle model
- Function tests
- General tests
- Traversal tests
- Test procedures
- Measured values tables
- Default measurements
- XML Templates
- Supplemental documents

The following values are listed for these objects:

- **Total:** the total amount of the tested objects
- **No error:** number of objects, for which no errors were detected.
- **Error:** number of objects, for which separate errors were detected, but do not prevent the deployment.
- **Not deployed:** number of objects, for which at least one error was detected that prevents the deployment

###### <a id="prozess.bereitstellung.pruefung.protokoll.uebersicht.pruefungen"></a>8.10.7.1.4. Test Overview

This section gives an overview of the tests performed and the log worksheet, in which the results of the respective tests are given. Only the tests are listed that were selected when it was prepared. A direct correlation of a test to a log worksheet is not always possible.

###### <a id="prozess.bereitstellung.pruefung.protokoll.uebersicht.testbaseline"></a>8.10.7.1.5. Note for the Test Baseline Check

When performing the plausibility and completeness check after a baseline is created for the test baseline, it may occur that there are different separate working versions of the considered editorial objects at the time of the provision and the time of the test. The user will be informed of this status in the test log with the following message:

"The status of the checked objects can differ between the test baseline and the validation check because the validation check occurs later. The log entries for the test baseline contain a time stamp indicating when the object was provided. The worksheets with the list of all the checked editorial objects contain the time stamp for the last change of the object at the time of the test.

###### <a id="prozess.bereitstellung.pruefung.protokoll.uebersicht.move"></a>8.10.7.1.6. Notes for Unavailable Connection to the MOVE Database

If the connection to the MOVE database could not be established while the plausibility and completeness check is being performed, the user is notified of this status with the following message:

"The connection to the MOVE database could not be established. The test for the used MOVE objects was not performed."

##### <a id="prozess.bereitstellung.pruefung.protokoll.fehler"></a>8.10.7.2. "With Errors" Table Sheet

All editorial objects are logged here that were considered and for which as least one error was detected.

The „With errors“ table sheet contains a total of 15 columns. The first 12 columns are the same is in [Section 8.10.7.3, “"Without Errors" Table Sheet”](8-10-7-plausibility-and-completeness-check-log.md#prozess.bereitstellung.pruefung.protokoll.fehlerfrei "8.10.7.3. \"Without Errors\" Table Sheet"). The last columns are listed below with title and description:

- **Test:** name of the test
- **Error:** the reason for an entry with details
- **Relevant to deployment:** flag if the error prevented the deployment or not. If the flag is set (“Yes”), then there may be two causes for this. One cause is that the editorial object may not be present. The other cause is that the editorial object may be present, but referenced objects (child objects) are not present, so the relationships to the references objects cannot be prepared.

Applies to the filling of the table: there is one separate row for each error in an editorial object. Multiple errors can be detected for one editorial object through multiple tests. If this is the case, multiple entries for one editorial object are included in the worksheet.

##### <a id="prozess.bereitstellung.pruefung.protokoll.fehlerfrei"></a>8.10.7.3. "Without Errors" Table Sheet

All editorial objects are logged here that were considered and for which no error was detected.

The „Without errors“ table sheet contains a total of 12 columns. The columns are labeled as follows:

- **Object type:** object type of the considered object
- **Object path:** the path of the considered brand-specific object in the primary tree of the object type. Only one path is always given
- **System name:** the system name of the considered object
- **Object status:** object status of the considered object
- **Object version:** object version of the considered object
- **Version comments:** version comments of the affected version
- **Team:** team of the last editor of the considered object version
- **Last author:** last editor of the considered object version
- **Last context:** order context (name of the order head and step, separated by " |-| ") of the considered object version
- **Version-specific ID:** version-specific ID of the considered object version
- **Version-independent ID:** version-independent ID of the considered object
- **Last change:** time stamp of the last change of the considered object

Applies to the filling of the table: there is one separate row for each editorial object. The columns are filled in with the respective values.

##### <a id="prozess.bereitstellung.pruefung.protokoll.auftrag"></a>8.10.7.4. "Order Headers And Order Steps" Table Sheet

Here all order headers and order steps are listed, which contain editorial objects with errors.

The "Order headers and order steps" table sheet contains a total of 13 columns. The columns are labeled as follows:

- **Order header label:** name of the order header
- **Order step label:** name of the order step
- **Order header status:** object status of the order header
- **Order step status:** object status of the order step
- **Start date:** scheduled start date of the scheduled order
- **End date:** scheduled end date of the scheduled order
- **Initial deployment date:** initial deployment date of the scheduled order
- **Market name:** market name from the applicable order header
- **Author of the last order header change:** the user responsible for the last order header change
- **Responsible order header team:** the team responsible for the last order header change
- **Order step end date:** scheduled end date of the scheduled order step
- **Responsible order step team:** the team responsible for the last order step change
- **Contains no released objects:** it is noted if unreleased objects are included

Applies to the filling of the table: there is one row for each order step. Then the information for the applicable order header is included in the row. The columns are filled with the respective values, as long as they exist for the corresponding object. If the values for the respective object do not exist, then the Excel table cells are not filled in.

##### <a id="prozess.bereitstellung.pruefung.protokoll.verwendung"></a>8.10.7.5. "References to other brands" Table Sheet

All editorial objects are logged here that were considered and that reference editorial objects of other brands.

The „Without errors“ table sheet contains a total of 13 columns. The columns are labeled as follows:

- **Source object system name:** the system name of the considered object
- **Source object object type:** the object type of the considered object
- **Source object path:** the path of the considered brand-specific object in the primary tree of the object type. Only one path is always given.
- **Reference object system name:** the system name of the referenced non-brand object
- **Source object version:** the object version of the considered object
- **Source object status:** the object status of the considered object
- **Source object ID:** version-specific ID of the considered object version
- **Version-independent ID of source object:** version-independent ID of the considered object
- **Reference object ID:** version-specific ID of the referenced non-brand object
- **Version-independent ID of reference object:** version-independent ID of the referenced non-brand object
- **Last author of source object:** last editor of the considered object version
- **Last context of source object:** order context (name of the order head and step, separated by " |-| ") of the considered object version
- **Action element:** the path to the action elements in the function test content, that references the non-brand object.
- **Reference object type:** the object type of the referenced non-brand object
- **Reference object brand:** the brand of the referenced non-brand object
- **Reference object location:** the location of the referenced non-brand object

Applies to the filling of the table: there is one separate row for each editorial object. The columns are filled in with the respective values.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="8-10-6-test-object-editor.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="8-10-plausibility-and-completeness-checks.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="8-10-8-notification.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">8.10.6. Test Object Editor </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 8.10.8. Notification</td></tr></table>
