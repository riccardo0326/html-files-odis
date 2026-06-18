[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.4. Equipment Network](7-4-equipment-network.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.4.7. Country Sessions in the Equipment Network</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-4-6-vehicle-recognition-in-equipment-network.md">Prev</a> </td><th align="center" width="60%">7.4. Equipment Network</th><td align="right" width="20%"> <a accesskey="n" href="7-4-8-determining-the-engine-code-from-the-engine-control-module.md">Next</a></td></tr></table>

---

#### <a id="ausstattungsnetz.landessetzung"></a>7.4.7. Country Sessions in the Equipment Network

It is possible to specify country sessions in the equipment network.<a id="d4e11634"></a>They can then be used to automatically fill in the vehicle features dialog in the operating system. (see [Figure 241, “Country session”](7-4-7-country-sessions-in-the-equipment-network.md#figure.redaktion.ausstattungsnetz.landessetzung "Figure 241. Country session"))<a id="d4e11637"></a>

<a id="figure.redaktion.ausstattungsnetz.landessetzung"></a>

![Image: country session](images/landessetzung.png)

**Figure 241. Country session**

One or more country sessions can be specified for an editorial object in the “Vehicle type” in an input field designed for this. Entering a country session is optional. It consists of three characters, such as “X0A”.

A “negation” (minus symbol) is permitted when specifying the country version. Multiple country versions that are not permitted should be enclosed in parentheses with the minus symbol in front of the parentheses. A negative or positive list must be specified in the field. Multiple country sessions should be separated by a comma or blank space, regardless of whether the list is a positive list or negative list.

The following characters may be entered:

- A through Z
- Capital and lower case letters
- 0 through 9
- ?
- ,
- ()
- - (minus)

Examples of entries in the "Country session” field:

- X0A
- -X0A
- X0?
- X??
- ?0?
- X0A,X2A,X3A
- -(X0A,X2A,X3A)
- -(X0A,?2?,X?A,???)
- X0A,?2?,X?A,???

If information is entered incorrectly, there will be an error message. The vehicle type editor is not stored and also not closed.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-4-6-vehicle-recognition-in-equipment-network.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-4-equipment-network.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-4-8-determining-the-engine-code-from-the-engine-control-module.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.4.6. Vehicle Recognition in Equipment Network </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.4.8. Determining the Engine Code from the Engine Control Module</td></tr></table>
