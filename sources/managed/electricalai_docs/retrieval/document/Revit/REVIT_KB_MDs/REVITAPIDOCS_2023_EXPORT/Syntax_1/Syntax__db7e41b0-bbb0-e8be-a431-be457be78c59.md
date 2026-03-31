[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReportLinkLoadResults Method

---



|  |
| --- |
| [RevitLinkUIUtils Class](09f5f83f-201a-fb39-5187-24c27bc3ff33.htm)   [See Also](#seeAlsoToggle) |

This function reports any errors which were encountered when loading the Revit links represented by the given LinkLoadResult map.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static void ReportLinkLoadResults( 	Document doc, 	IDictionary<string, LinkLoadResult> loadResults ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub ReportLinkLoadResults ( _ 	doc As Document, _ 	loadResults As IDictionary(Of String, LinkLoadResult) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void ReportLinkLoadResults( 	Document^ doc,  	IDictionary<String^, LinkLoadResult^>^ loadResults ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document containing the links.

loadResults
:   Type:  System.Collections.Generic IDictionary   String  ,  [LinkLoadResult](f846bfb0-b047-9332-567f-75ae880d8359.htm)    

    A map from the display name of a link to the LinkLoadResult for that link.

# Remarks

If all links succeeded in loading, the function does nothing. If any links failed to load, this function will display the Unresolved References dialog, giving the user the option to open the Manage Links dialog to correct any problems.

To ensure the dialog fits on the screen, Revit will only list up to ten link names. Additional links will be mentioned as, "And >number< additional links." This is the same behavior Revit's user interface uses.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RevitLinkUIUtils Class](09f5f83f-201a-fb39-5187-24c27bc3ff33.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)