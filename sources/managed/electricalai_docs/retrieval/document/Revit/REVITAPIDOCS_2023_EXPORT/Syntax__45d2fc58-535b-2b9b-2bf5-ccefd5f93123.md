[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanElementsBeAddedToDisplacementSet Method

---



|  |
| --- |
| [DisplacementElement Class](08113547-eaaa-5ec1-5ff1-de609fe7c29c.htm)   [See Also](#seeAlsoToggle) |

Indicates if these elements can be displaced by this DisplacementElement.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool CanElementsBeAddedToDisplacementSet( 	ICollection<ElementId> toDisplace ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanElementsBeAddedToDisplacementSet ( _ 	toDisplace As ICollection(Of ElementId) _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanElementsBeAddedToDisplacementSet( 	ICollection<ElementId^>^ toDisplace ) ``` |

#### Parameters

toDisplace
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The elements to displace.

#### Return Value

True if the elements can be displaced by this DisplacementElement.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DisplacementElement Class](08113547-eaaa-5ec1-5ff1-de609fe7c29c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)