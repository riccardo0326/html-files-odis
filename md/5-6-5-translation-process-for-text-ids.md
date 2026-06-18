[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.6. Text Library](5-6-text-library.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.6.5. Translation Process for Text IDs</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-6-4-sorting-and-filtering-in-the-text-library.md">Prev</a> </td><th align="center" width="60%">5.6. Text Library</th><td align="right" width="20%"> <a accesskey="n" href="5-7-remote-diagnosis-export.md">Next</a></td></tr></table>

---

#### <a id="textbib.uebersetzung"></a>5.6.5. Translation Process for Text IDs

The translation process for the text IDs from the text library has the following characteristics in contrast to the editorial translation process:

- The source language of the project package is German.
- The translation occurs into all of the languages currently in the master data of ODIS Creator.
- The translation requirements for the text library texts are assigned completely to the VW Wolfsburg location.
- The translation process for a version of a text library text begins only if this version has the "released" processing status.
- Every version of a text in the text library contains a separate translation status with the following range of values:

  - Empty (no display)
  - Ready for translation
  - In translation
  - Complete
- A version of a text ID in the text library has the translation status "Empty (no display)" as long as it was not released.
- A text ID version with the "released" processing status contains the translations status "ready for translation" and it will create translation requirements for all system languages.
- A text ID version with the "released" processing status receives the "in translation" translation status, if there is at least one translation requirement for a language that was transferred to the translation package, but translation requirements that have still not been transferred to a translation package are available for no language.
- A text ID version with the "released" processing status has the "complete" translation status, if the translation packages have been imported for all of the languages for this text version.

  A text ID in the text library can then only be used, if at least one version of this text has the "Complete" translation status. The newest version with the "Complete" translation status will then be used.
- After adding a new language in the ODIS Creator master data, the translation requirements for all text library text IDs are created when implementing a job. This can result in a portion of the text IDs changing from a translation status of "complete" to "ready for translation". These text IDs can however continue to be used.
- Text IDs from the text library, which have plain text that consists exclusively of elements that are not relevant to translation, are excluded from the translation process. Instead of an image of translation requirements, the translation status will be set directly to "Complete". This particularly applies to text IDs from the category type "text module", "text module (ANSI characters)" or "placeholder". The text IDs used in the text modules must have at least one version with the "complete" translation status, since this represents a requirement for its usability.
- There is also a feedback process for text IDs (see [Section 5.6.3.8, “Make a Text ID Complaint”](5-6-3-text-id.md#textbib.reklamation "5.6.3.8. Make a Text ID Complaint")).
- When copying a text ID from the text library, all of the translations already having the "complete" translation status will be applied to the copy. If the text ID content of the copy is not changed again before the release, then no translation requirements are created for the languages, in which the translation could be carried over from the source object. New translation requirements will be created for the remaining languages.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-6-4-sorting-and-filtering-in-the-text-library.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-6-text-library.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-7-remote-diagnosis-export.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.6.4. Sorting and Filtering in the Text Library </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.7. Remote diagnosis export</td></tr></table>
