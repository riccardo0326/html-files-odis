[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.3. Search](7-3-search.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.3.2. Full Text Search</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-3-1-object-search.md">Prev</a> </td><th align="center" width="60%">7.3. Search</th><td align="right" width="20%"> <a accesskey="n" href="7-3-3-id-search.md">Next</a></td></tr></table>

---

#### <a id="redaktion.search.text"></a>7.3.2. Full Text Search

You can select which of the following areas should be searched in using the full text search (see [Figure 229, “Full Text Search”](7-3-2-full-text-search.md#figure.suche "Figure 229. Full Text Search")):

- **Metadata:** search in all object attributes, for example, the comments, version comments, etc.; exceptions are source language display names and the tester description for function codes

- **Source language content:** search in the content of all source-language objects

- **Source language display names:** search in the source language display names of all objects

- **Translated display names:** search in the translated display names of every object that has a translation

- **Translated content:** search in the content of every translated object

One or more areas can be selected for the full-text search. The search functions similar to a web search. There is the option to search for individual words or multiple words, each with and without placeholders, such as "\*". The search for an individual word only displays the results, if a field contains this individual word. It is important to note that when searching for an attribute text, such as the system name, words are separated by a special character (for example "-"). Excluded from this is the special character "\_", because this symbol is used very frequently in system names and will represent no word limitation there. For example, if a system name consists of multiple words that are connected with a "\_", then the character string will be recognized as one word in the full text search. When searching for multiple words, it can be decided to use a placeholder or not for each individual word.

If you would like to do a search with a placeholder, then the word must be placed in " " with the placeholders. It is important for the search that the string of characters without " " must consist of at least three characters (combination of a-z, A-Z and 0-9).

*Example:* the system name "Passat\_06" can be found by searching **"Passat\_06"**, **"Passat\*"** or **"Passat\*06"**, whereas the system name "Passat-06" can also be found when searching for **Passat**. However, if the system name "Passat06" is searched for, it will not be found with **Passat**, but rather only found with **"Passat\*"** or **"Passat06"**. The system name "AD-delete-read-DTC memory" can, for example, be found by searching for **Read DTC memory** or **Read DTC\***.

Texts that are not contained in the editorial object data are not included in the full-text search, but are rather just referenced:

- Texts from XML reference tables
- General system texts and vehicle status texts
- Default texts and texts from the text library
- Texts from the master component list
- EFA texts
- Texts from control module descriptions

<a id="figure.suche"></a>

![Image: full text search](images/volltextsuche.png)

**Figure 229. Full Text Search**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-3-1-object-search.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-3-search.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-3-3-id-search.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.3.1. Object Search </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.3.3. ID Search</td></tr></table>
