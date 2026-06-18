[ODIS Creator Help](odis-creator-help.md) > [3. ODIS Creator Basic Information](3-odis-creator-basic-information.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">3.1. Starting ODIS Creator</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="3-odis-creator-basic-information.md">Prev</a> </td><th align="center" width="60%">3. ODIS Creator Basic Information</th><td align="right" width="20%"> <a accesskey="n" href="3-2-program-structure.md">Next</a></td></tr></table>

---

### <a id="vaudes.starten"></a>3.1. Starting ODIS Creator

ODIS Creator is installed using a setup program. The setup program is provided on a server and can be downloaded using a browser application. Open your Internet browser and enter the application web address (for example, http://odis\_creator\_server/creator\_start). You can get the exact address from your system administrator/HelpDesk.

The ODIS Creator homepage appears with the download link for downloading the setup program.

<a id="figure.startseite"></a>

![Image: ODIS Creator homepage](images/Startseite.png)

**Figure 20. ODIS Creator Homepage**

You can download the setup program setupODIS.exe to the client computer and start running it there either by clicking the “Download and run ODIS Creator Setup” link or the ODIS Creator logo.

A language selection appears first when starting the setup program. You can use this language selection to specify the following:

- The language that will be used in the setup program
- The interface language for ODIS Creator

The setup program installs the ODIS Creator Client on your computer in the folder "C:\webApps\ODISC\_<Umgebung>\".

The “ODIS Creator Terms of Use” dialog appears when starting the application.

<a id="figure.nutzungsbedingungen"></a>

![Image: ODIS Creator Terms of Use Dialog](images/Nutzungsbedingungen.png)

**Figure 21. ODIS Creator terms of use**

Agree to the terms of use by pressing the “OK” button. The login dialog will then appear. Otherwise the application’s start process will be canceled.

The login dialog requests you authenticate yourself with the PKI smartcard PIN. After the PIN is entered successfully, you will be logged in with the user ID linked to the PKI smartcard. Each user ID is assigned to the individual [views](3-2-1-views-bar.md "3.2.1. Views Bar") corresponding to the roles and access rights management (see [Section 3.3, “Roles and Teams”](3-3-roles-and-teams.md "3.3. Roles and Teams")).

<a id="figure.anmelden"></a>

![Image: dialog for requesting the PKI smartcard PIN](images/PKI_Pin_Dialog.jpg)

**Figure 22. Logging in with the PKI Smartcard PIN**

After logging in, the application will load with the views according to the access rights.

It is possible when there is an update from ODIS Creator that a login is not possible despite having the correct login data. For example, if the service components to which you want to log in cannot be reached or has a different version as the client. In both cases, you will receive a related message and the login will be canceled.

If the server cannot be reached, you will receive the following message: "You cannot log in, because the server currently cannot be reached."

If the client and server have different versions, you will receive the following message: "You cannot log in, because the client version is different from the server version." In this case, enter the URL for the ODIS Creator homepage in the Internet browser and then run the setup again in order to update the application on the client computer.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="3-odis-creator-basic-information.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="3-odis-creator-basic-information.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="3-2-program-structure.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">3. ODIS Creator Basic Information </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 3.2. Program Structure</td></tr></table>
