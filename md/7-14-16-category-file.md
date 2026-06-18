[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.14. Function Test Editor](7-14-function-test-editor.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.14.16. Category - File</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-14-15-category-ecukom.md">Prev</a> </td><th align="center" width="60%">7.14. Function Test Editor</th><td align="right" width="20%"> <a accesskey="n" href="7-14-17-category-connection.md">Next</a></td></tr></table>

---

#### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Datei"></a>7.14.16. Category - File

This category contains action elements for interaction with files. The following action elements are used:

- [Section 7.14.16.1, “Action Element - Read File”](7-14-16-category-file.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Datei.Lesen "7.14.16.1. Action Element - Read File")
- [Section 7.14.16.2, “Action Element - Write File”](7-14-16-category-file.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Datei.Schreiben "7.14.16.2. Action Element - Write File")
- [Section 7.14.16.3, “Action Element - Delete File”](7-14-16-category-file.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Datei.Loeschen "7.14.16.3. Action Element - Delete File")

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Datei.Lesen"></a>7.14.16.1. Action Element - Read File

The "Read file" action element can be seen in [Figure 474, “Read File Action Element”](7-14-16-category-file.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Datei.Lesen "Figure 474. Read File Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Datei.Lesen"></a>

![Image: read file action element](images/fte_arbeitsflaeche_datei_dateilesen.png)

**Figure 474. Read File Action Element**

Using this command, you can read data from a file in the function test. To do this, enter the file name, the read position within the file, the number of bytes, and a variable for the result. You can read variables from the "String" and "Byte" types. To read individual bytes one after the other, program a loop. Use the 'ASCII' option to read a string character-by-character from the file (coding: UTF 2-byte). Use the "Binary" option to read bytes from the file.

###### <a id="d4e24993"></a>7.14.16.1.1. File name

The file name is used for access to the files based on the argument "File name with VIN" in order to access the files for runtime. If "File name with VIN" is set, then the VIN is added to the file name as a prefix. The file extension ".tpr" is also added to the file name.

###### <a id="d4e24996"></a>7.14.16.1.2. Item

The "position" indicates the read position within the file.

###### <a id="d4e24999"></a>7.14.16.1.3. Number of Bytes

The "Number of bytes" specifies the number of bytes to read from the file.

###### <a id="d4e25002"></a>7.14.16.1.4. Result

Under "Result", a variable is specified in which the result of the read operation is stored.

###### <a id="d4e25005"></a>7.14.16.1.5. Type

Using the "Type" option, you can select the data to be read (ASCII/binary).

###### <a id="d4e25008"></a>7.14.16.1.6. File Name with VIN

The "File name with VIN" control field controls the file name prefix:

- If "File name with VIN" is set, then the VIN is added to the file name as a prefix. The VIN is separated from the rest of the file name with an underscore. The file extension ".tpr" is added to the file name. The final file name on the client is then as follows: '<VIN>\_<Filename>.tpr'
- Example: if the "foo" file name is used, then the resulting file will be named: 'WAUZZZ8R89A000675\_foo.tpr'.

###### <a id="d4e25017"></a>7.14.16.1.7. Variable

The description for selecting variables is found in [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables"). The definition of variables is found in [Section 7.14.11.1, “Action Element - Declare Variable”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen "7.14.11.1. Action Element - Declare Variable").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Datei.Schreiben"></a>7.14.16.2. Action Element - Write File

The "Write" action element can be seen in [Figure 475, “Write File Action Element”](7-14-16-category-file.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Datei.Schreiben "Figure 475. Write File Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Datei.Schreiben"></a>

![Image: write file action element](images/fte_arbeitsflaeche_datei_dateilschreiben.png)

**Figure 475. Write File Action Element**

Using this command, you can read data from a function test in a file. To do this, enter the file name, the write position within the file, the number of bytes, and a variable for the source. You can write variables from the "String" and "Byte" types. To write individual bytes one after the other, program a loop. Use the 'ASCII' option to write a string character-by-character in the file (coding: UTF 2-byte). Use the "Binary" option to write bytes in the file.

###### <a id="d4e25035"></a>7.14.16.2.1. File name

The file name is used for access to the files based on the argument "File name with VIN" in order to access the files for runtime. If "File name with VIN" is set, then the VIN is added to the file name as a prefix. The file extension ".tpr" is also added to the file name.

###### <a id="d4e25038"></a>7.14.16.2.2. Item

The "position" indicates the write position within the file.

###### <a id="d4e25041"></a>7.14.16.2.3. Number of Bytes

The "Number of bytes" specifies the number of bytes to written in the file.

###### <a id="d4e25044"></a>7.14.16.2.4. Source

A variable that will be written in the file is specified under "Source".

###### <a id="d4e25047"></a>7.14.16.2.5. Type

Using the "Type" option, you can select the data to be written (ASCII/binary).

###### <a id="d4e25050"></a>7.14.16.2.6. File Name with VIN

The "File name with VIN" control field controls the file name prefix:

- If "File name with VIN" is set, then the VIN is added to the file name as a prefix. The VIN is separated from the rest of the file name with an underscore. The file extension ".tpr" is added to the file name. The final file name on the client is then as follows: '<VIN>\_<Filename>.tpr'
- Example: if the "foo" file name is used, then the resulting file will be named: 'WAUZZZ8R89A000675\_foo.tpr'.

###### <a id="d4e25059"></a>7.14.16.2.7. Variable

The description for selecting variables is found in [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables"). The definition of variables is found in [Section 7.14.11.1, “Action Element - Declare Variable”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen "7.14.11.1. Action Element - Declare Variable").

##### <a id="Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Datei.Loeschen"></a>7.14.16.3. Action Element - Delete File

The "Delete file" action element can be seen in [Figure 476, “Delete File Action Element”](7-14-16-category-file.md#figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Datei.Loeschen "Figure 476. Delete File Action Element").

<a id="figure.Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Datei.Loeschen"></a>

![Image: delete file action element](images/fte_arbeitsflaeche_datei_dateiloeschen.png)

**Figure 476. Delete File Action Element**

You can delete a file using this action element.

###### <a id="d4e25077"></a>7.14.16.3.1. File name

The file name is used for access to the files based on the argument "File name with VIN" in order to access the files for runtime. If "File name with VIN" is set, then the VIN is added to the file name as a prefix. The file extension ".tpr" is also added to the file name.

###### <a id="d4e25080"></a>7.14.16.3.2. File Name with VIN

The "File name with VIN" control field controls the file name prefix:

- If "File name with VIN" is set, then the VIN is added to the file name as a prefix. The VIN is separated from the rest of the file name with an underscore. The file extension ".tpr" is added to the file name. The final file name on the client is then as follows: '<VIN>\_<Filename>.tpr'
- Example: if the "foo" file name is used, then the resulting file will be named: 'WAUZZZ8R89A000675\_foo.tpr'.

###### <a id="d4e25089"></a>7.14.16.3.3. Variable

The description for selecting variables is found in [Section 7.14.6, “Using Variables”](7-14-6-using-variables.md "7.14.6. Using Variables"). The definition of variables is found in [Section 7.14.11.1, “Action Element - Declare Variable”](7-14-11-category-definition.md#Funktionstesteditor.Arbeitsflaeche.Aktionselemente_Kategorie_Definition.Deklariere_Variablen "7.14.11.1. Action Element - Declare Variable").

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-14-15-category-ecukom.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-14-function-test-editor.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-14-17-category-connection.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.14.15. Category - Ecukom </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.14.17. Category - Connection</td></tr></table>
