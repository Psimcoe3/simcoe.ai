[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidHub Method

---



|  |
| --- |
| [AnalyticalLink Class](b552fb54-8dff-6690-e16e-cc46cbc46d6b.htm)   [See Also](#seeAlsoToggle) |

Checks whether input hub is valid for an AnalyticalLink.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static bool IsValidHub( 	Document doc, 	ElementId hubId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidHub ( _ 	doc As Document, _ 	hubId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidHub( 	Document^ doc,  	ElementId^ hubId ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Hubs's document.

hubId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Hub to test for validity.

#### Return Value

True is returned when provided hubId points hub that is valid for AnalyticalLink, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[AnalyticalLink Class](b552fb54-8dff-6690-e16e-cc46cbc46d6b.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)