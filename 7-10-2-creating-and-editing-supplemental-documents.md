[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.10. Supplemental documents](7-10-supplemental-documents.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.10.2. Creating and Editing Supplemental Documents</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-10-1-supplemental-document-categories.md">Prev</a> </td><th align="center" width="60%">7.10. Supplemental documents</th><td align="right" width="20%"> <a accesskey="n" href="7-11-editors-for-supplemental-documents.md">Next</a></td></tr></table>

---

#### <a id="zusatzdokumente.anlegen"></a>7.10.2. Creating and Editing Supplemental Documents

You can create supplemental documents by clicking on an element with the right mouse button, when you are in the **editing** view of a navigator. Then select **New subnode** or **New parallel node**, depending on if the supplemental document should be added next to the selected object or be assigned to it. ODIS Creator assists you in the allocation by checking at which locations supplemental documents are permitted, and the respective commands are also only then offered.

<a id="figure.zusatzdokumente.anlegen"></a>

![Image: creating a supplemental document](images/Neuanlage.png)

**Figure 293. Create Supplemental Document**

  

As soon as you have selected the menu command, an editor will open on the right side where you can specify the administrative information for the supplemental document (metadata). The context menu will be display depending on the switch that is set (CONNECT\_TO\_TPS) in vaudes\_server.properties. Click on the editor with the right mouse button, then a context menu will appear with commands for editing the supplemental document content. Please note that this context menu is only available, if the editor is in edit mode.

<a id="d4e14102"></a>

![Image: LIVAS supplementary documents context menu](images/ZusatzdokumentKontextMenu.png)

**Figure 294. Supplementary Documents Context Menu (LIVAS Image Selection)**

<a id="figure.zusatzdokumente.tps.kontextmenu.zuordnen"></a>

![Image: TPS supplementary documents context menu](images/ZusatzdokumentKontextMenuTps.png)

**Figure 295. Supplementary Documents Context Menu (TPS Image Selection)**

Using the menu item **Text > Edit**, you can load and edit an additional text into the internal OC editor.

The menu items **Image > Assign** and **Media > Assign** each open a dialog, through which you can search for and link targeted objects from the multimedia object management MOVE. If necessary, you can also give new image or media objects using the **Assign...** button.

<a id="d4e14124"></a>

![Image: MOVE search](images/MoveSuche.png)

**Figure 296. MOVE Search**

After selecting the **Assign** context menu (see [Figure 295, “Supplementary Documents Context Menu (TPS Image Selection)”](7-10-2-creating-and-editing-supplemental-documents.md#figure.zusatzdokumente.tps.kontextmenu.zuordnen "Figure 295. Supplementary Documents Context Menu (TPS Image Selection)")), the TPS search dialog will open as long as the login to the CONNECT interface was successful. The TPS search dialog can be used to search for and find images using their image number. The user can filter the results list by image format to narrow down the display.

<a id="d4e14135"></a>

![Image: TPS search](images/TpsSuche.png)

**Figure 297. TPS Search**

The context menu item **Media > Assign** gives you the option to search for other media types and link them. Furthermore, you have the option to import new media objects (**Import...** button). Please note, that these media objects are indeed stored in the MOVE, however are not checked for visibility before storing.

<a id="d4e14146"></a>

![Image: importing a media object](images/ImportMedienobjekte.png)

**Figure 298. Importing a Media Object**

After a link to an image was made, you can create hotspots in this image (see [Section 7.11.2, “Hotspot Editor”](7-11-2-hotspot-editor.md "7.11.2. Hotspot Editor")).

A login to the LIVAS3 / MOVE server must take place the first time the **Image > Assign** or **Media > Assign** menu item is selected. The following login window is displayed for this:

<a id="figure.zusatzdokumente.livas.anmeldung"></a>

![Image: LIVAS3 / MOVE login](images/LivasAnmeldung.png)

**Figure 299. LIVAS3 / MOVE Login**

In addition to the user ID and password, you must select the brand under which you would like to work in LIVAS3/MOVE in the login window. The user ID and brand are saved locally on the computer so that both values will be preselected in future sessions.

With the **Edit MOVE server connection** menu item, you can display the login window with current connection status again in order to change the ID or the brand under which you would like to work in LIVAS 3 / MOVE.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-10-1-supplemental-document-categories.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-10-supplemental-documents.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-11-editors-for-supplemental-documents.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.10.1. Supplemental Document Categories </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.11. Editors for Supplemental Documents</td></tr></table>
