[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.11. Editors for Supplemental Documents](7-11-editors-for-supplemental-documents.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.11.2. Hotspot Editor</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-11-1-supplementary-document-editor.md">Prev</a> </td><th align="center" width="60%">7.11. Editors for Supplemental Documents</th><td align="right" width="20%"> <a accesskey="n" href="7-12-xml-templates.md">Next</a></td></tr></table>

---

#### <a id="hotspot"></a>7.11.2. Hotspot Editor

The hotspot editor offers the option to display image files in the editing system and to create new hotspots within an image and to change to a limited extent.

##### <a id="funktionalitaet"></a>7.11.2.1. Functionality

The hotspot editor can create and manage hotspots for pixel-oriented and vector-oriented graphics. The base graphic formats are PNG, JPG and SVG. For you as a user, the process does not vary for the different graphic types, since ODIS Creator calculates the marked areas for you according to the image type. You can perform the following actions:

- Create a hotspot with the mouse (drag a rectangle)

- Select individual hotspots (including multiple selection)

- Moving hotspots

- Deleting hotspots

- Allocation of document references through a list

##### <a id="anwendungsfaelle"></a>7.11.2.2. Use cases

###### <a id="bilddokument.oeffnen"></a>7.11.2.2.1. Opening an Image Document

To start the **Hotspot Editor**, press **Hotspots > Edit** in the context menu. This assumes that a link to an image object was already made (see [Section 7.10, “Supplemental documents”](7-10-supplemental-documents.md "7.10. Supplemental documents")).

<a id="hotspot.editor2"></a>

![Image: opening the Hotspot Editor](images/HotSpotEditorStarten.png)

**Figure 322. Opening the Hotspot Editor**

If the MOVE interface is available, images are no longer loaded from the file system but rather are looked up in the MOVE database. You can use the same image in different supplemental documents and create different hotspots respectively.

###### <a id="bilddokument.bearbeiten"></a>7.11.2.2.2. Editing an Image Document

<a id="hotspot.bearbeiten"></a>

![Image: editing image document](images/HotspotEditor.png)

**Figure 323. Editing Image Document**

Hotspots are defined by rectangles. To create a new hotspot, click at the point in the image where the left upper edge of the hotspot should be. Hold down the mouse button and pull the rectangle toward the right lower side. You will see the new hotspot with its coordinates on the right side of the table. You can now specify a destination for the hotspot in the table.

If you want to move a hotspot or change its size, click on the border of the rectangle so that it will change its color to red. If you position the cursor over one of the borderlines now, then the cursor symbol will change to a double arrow, and you can change the hotspot size by clicking on the border and pull it in the desired direction. Within the rectangle, the cursor changes its form to a crossed double arrow. If you press the left mouse button now, you can move the hotspot to another position.

If you want to delete a hotspot, then select a hotspot in the table and click on the ![](images/Minus01.png)-symbol on the right side above the table.

When you have created all necessary hotspots, click on the **Apply** button. The Hotspot Editor is closed and you will return back to the editor for the supplemental document administrative information. Save it and it will also save the hotspot information. If you want to discard your changes, close the editor and reject the request asking if you would like to save.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-11-1-supplementary-document-editor.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-11-editors-for-supplemental-documents.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-12-xml-templates.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.11.1. Supplementary Document Editor </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.12. XML Templates</td></tr></table>
