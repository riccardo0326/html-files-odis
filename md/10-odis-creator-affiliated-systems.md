[ODIS Creator Help](odis-creator-help.md) >

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">10. ODIS Creator Affiliated Systems</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="9-5-didb.md">Prev</a> </td><th align="center" width="60%"> </th><td align="right" width="20%"> <a accesskey="n" href="11-appendix.md">Next</a></td></tr></table>

---

## <a id="umfeldsysteme"></a>10. ODIS Creator Affiliated Systems

In this section, the affiliated systems are only described with the properties that are relevant in the ODIS Creator context. The affiliated systems relevant to the ODIS Creator business process are (alphabetical order):

<a id="efa"></a>**EFA (Standard Fault Description Language)**

In the EFA system, error symptoms are depicted in a complex structure together with their dependencies for the error analysis.

<a id="gocat"></a>**GOCAT**

GOCAT is a group-wide translation portal, that supports the process for all document translations given by Volkswagen AG in an order. The software organizes all steps of the document translation. This begins when a translation order is manually or automatically created, the optional addition of the settings relevant to translation, with the order placement to an agency, assigning to a translation, performing the translation up to quality control and creation of a delivery order as a PDF.

<a id="dels"></a>**DELS**

DELS is a new group-wide translation portal that supports the process for all document translations commissioned by Volkswagen AG. DELS is a successor to GoCAT and organizes all steps of document translation. The main difference between DELS and GoCAT is the API interface. From a user perspective, the translation process remains the same.

<a id="internet"></a>**Internet**

The interface makes the link of editorial objects to documents, that are available on the Internet, possible.

<a id="livas3"></a>**LIVAS3 (literature, information, processing and handling system)**

LIVAS3 is the editing system for workshop information (for example, repair manuals). LIVAS3 currently contains the MOVE component to manage multimedia objects. So that you can look up LIVAS document and can look up and commission MOVE images and objects, you must be recognized with your user name in LIVAS3.

<a id="move"></a>**MOVE (multimedia object management)**

MOVE is a component to manage the multimedia objects that are currently integrated in LIVAS3.

<a id="TPS/CONNECT"></a>**TPS/CONNECT**

CONNECT is a REST API that can be used to make requests to access image objects in the TPS database. The actual search for images is facilitated by a separate REST API named CORA that processes the search request for image data.

TPS/CONNECT is the successor system to LIVAS3. In the future, images will no longer be referenced from the MOVE database, but rather from the TPS database and assigned to the supplementary documents. You can search for image objects in a dialog window using the image number. A successful login to the CONNECT interface is required to do this.

<a id="ria"></a>**Mirror Server 2 (formerly RIA Retail Integration Architecture)**

Mirror Server 2 is the distribution system, from which the customers can obtain the diagnostic data online.

<a id="tpi"></a>**TSB Repository**

From the TSB repository from the [HST](11-appendix.md#HST "HST") (Technical Service Handbook) system, the available Technical Service Bulletins are determined to assist in fault repairs in the workshop. The Technical Service Bulletins can either correlate to DISS codes or give general information, that is separate from the DISS code (for example, messages for reporting requirement, message for software updates).

<a id="vaudas"></a>**ODIS Service**

The diagnostic processing system ODIS Service assists the technician in the workshop with the instruments of Guided Fault Finding (GFF) and the Guided Functions (GF), to identify the fault source based on the error codes read from the vehicle and error symptoms detected by the technician during the service process. In the ODIS Creator context, ODIS Service is only directly addressed in the scope of development-related tests for the created function test that incorporates a vehicle.

<a id="anmerkungen"></a>**Comments**

Comments on systems, rolls, and concepts in the extended peripherals of ODIS Creator:

- The Technical Service Bulletins, from the [HST](11-appendix.md#HST "HST") (Technical Service Handbook) editing system required to correct faults in the workshop, are determined and displayed based on the DISS codes at the diagnostic object being transferred by ODIS Service into the **ELSA** service information system.
- The service information system **ELSA (electronic service information system)** supports the mechanics in the workshop when correcting an identified error. The applicable repair manuals, wiring diagrams, and Technical Service Bulletins are displayed corresponding to any fault sources identified in the off-board diagnosis by the ODIS Service processing system and the linking information from ODIS Creator.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="9-5-didb.md">Prev</a> </td><td align="center" width="20%"> </td><td align="right" width="40%"> <a accesskey="n" href="11-appendix.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">9.5. DIDB </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 11. Appendix</td></tr></table>
