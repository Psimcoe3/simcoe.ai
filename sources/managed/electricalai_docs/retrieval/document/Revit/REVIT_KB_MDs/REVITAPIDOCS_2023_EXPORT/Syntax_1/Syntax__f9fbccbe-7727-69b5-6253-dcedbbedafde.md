[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanLoadFamilies Method

---



|  |
| --- |
| [Family Class](f51d019d-6ff3-692b-d1d2-b497cab564de.htm)   [See Also](#seeAlsoToggle) |

Checks whether the document is in a state that allows the loading of families.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2020.1

# Syntax

| C# |
| --- |
| ``` public static bool CanLoadFamilies( 	Document document ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CanLoadFamilies ( _ 	document As Document _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool CanLoadFamilies( 	Document^ document ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document to check.

#### Return Value

True if loading of families is allowed, otherwise False.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Family Class](f51d019d-6ff3-692b-d1d2-b497cab564de.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)