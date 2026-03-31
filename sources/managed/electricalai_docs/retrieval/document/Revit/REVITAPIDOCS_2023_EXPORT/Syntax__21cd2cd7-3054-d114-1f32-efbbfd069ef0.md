[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemoveUnfilterableCategories Method

---



|  |
| --- |
| [ParameterFilterUtilities Class](50afdc29-3a0c-e3d9-c547-0fcdb40d3ce8.htm)   [See Also](#seeAlsoToggle) |

Removes from the given set the categories that are not filterable.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static ICollection<ElementId> RemoveUnfilterableCategories( 	ICollection<ElementId> categories ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function RemoveUnfilterableCategories ( _ 	categories As ICollection(Of ElementId) _ ) As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ICollection<ElementId^>^ RemoveUnfilterableCategories( 	ICollection<ElementId^>^ categories ) ``` |

#### Parameters

categories
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The set of categories to check.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ParameterFilterUtilities Class](50afdc29-3a0c-e3d9-c547-0fcdb40d3ce8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)