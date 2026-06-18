[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.2. Managing Master Data](5-2-managing-master-data.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.2.2. Importing URL Addresses</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-2-1-group-data.md">Prev</a> </td><th align="center" width="60%">5.2. Managing Master Data</th><td align="right" width="20%"> <a accesskey="n" href="5-2-3-configuredidentdata.md">Next</a></td></tr></table>

---

#### <a id="administration.servicereferences"></a>5.2.2. Importing URL Addresses

The URL addresses are imported from the servicereference.xml file. The servicereference.xml file is saved and versioned in a GIT repository on a Bitbucket server. The individual versions are provided with a tag there, which includes the version number.

When importing the URL addresses, the desired version of the servicereference.xml file is first selected and then this version is exported from the Bitbucket server to the ODIS Creator server and the required information is read out from there with an XML parser. The communication between the ODIS Creator server and the Bitbucket server occurs via synchronous REST requests (Representational State Transfer) to the Bitbucket repository set up in the server configuration.

To determine the desired version, all of the tags and commit data contained in the GIT repository are first read out with a REST request and listed in the selection dialog “Import new URL addresses”. (See [Figure 48, ““Import new URL addresses” Selection Dialog”](5-2-2-importing-url-addresses.md#figure.url.adressen.importieren "Figure 48. “Import new URL addresses” Selection Dialog")).

<a id="figure.url.adressen.importieren"></a>

![Figure: “Import new URL addresses” selection dialog](images/administation_url_adressen_importieren.png)

**Figure 48. “Import new URL addresses” Selection Dialog**

If the user selects a tag name, the associated version of the servicereference.xml from the Bitbucket server is loaded onto the ODIS Creator server via REST call-up and the required information is read out from there with an XML parser.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-2-1-group-data.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-2-managing-master-data.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-2-3-configuredidentdata.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.2.1. Group Data </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.2.3. ConfiguredIdentData</td></tr></table>
