[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasOpenConnector Method

---



|  |
| --- |
| [PlumbingUtils Class](958a3fa2-eb4b-2814-f674-42cac98f4910.htm)   [See Also](#seeAlsoToggle) |

Checks if there is open piping connector for the given element - object of pipe curve, pipe fitting or pipe accessory.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static bool HasOpenConnector( 	Document document, 	ElementId elemId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function HasOpenConnector ( _ 	document As Document, _ 	elemId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool HasOpenConnector( 	Document^ document,  	ElementId^ elemId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

elemId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Element id to check.

#### Return Value

True if given element has open piping connector, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PlumbingUtils Class](958a3fa2-eb4b-2814-f674-42cac98f4910.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)