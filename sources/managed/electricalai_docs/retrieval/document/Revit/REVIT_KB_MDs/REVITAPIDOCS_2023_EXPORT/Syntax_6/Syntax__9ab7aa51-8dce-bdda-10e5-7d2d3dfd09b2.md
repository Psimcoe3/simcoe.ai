[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsViewIdValidForViewport Method

---



|  |
| --- |
| [Viewport Class](5991dc40-234a-4835-cc06-07524d2e61a4.htm)   [See Also](#seeAlsoToggle) |

Verifies that the Viewport can change it's view id to the input %viewId%.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public bool IsViewIdValidForViewport( 	ElementId viewId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsViewIdValidForViewport ( _ 	viewId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsViewIdValidForViewport( 	ElementId^ viewId ) ``` |

#### Parameters

viewId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The view which will be checked to see if it can be applied to Viewport.

#### Return Value

True if the %viewId% is valid for the viewport, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Viewport Class](5991dc40-234a-4835-cc06-07524d2e61a4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)