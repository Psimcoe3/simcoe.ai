[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementMulticategoryFilter Constructor (ICollection(ElementId), Boolean)

---



|  |
| --- |
| [ElementMulticategoryFilter Class](8d2774eb-3c47-5c3d-2866-8d4ab7408d2d.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of a filter to find elements whose category matches any of a given set of categories, with the option to instead match elements which are not of the given categories.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public ElementMulticategoryFilter( 	ICollection<ElementId> categoryIds, 	bool inverted ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	categoryIds As ICollection(Of ElementId), _ 	inverted As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementMulticategoryFilter( 	ICollection<ElementId^>^ categoryIds,  	bool inverted ) ``` |

#### Parameters

categoryIds
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The category ids to match.

inverted
:   Type:  System Boolean    
     True if the filter should match all elements which are not of the given categories.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | One or more categories was not valid for filtering. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ElementMulticategoryFilter Class](8d2774eb-3c47-5c3d-2866-8d4ab7408d2d.htm)

[ElementMulticategoryFilter Overload](12249cf2-5f4d-0d13-5f7f-b282ecbd4bac.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)