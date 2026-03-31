[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DWFImportOptions Constructor (IList(ElementId))

---



|  |
| --- |
| [DWFImportOptions Class](8465ab77-dc06-79c2-4bed-e17a564adb22.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of DWFImportOptions with an array of imported sheet views.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public DWFImportOptions( 	IList<ElementId> views ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	views As IList(Of ElementId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: DWFImportOptions( 	IList<ElementId^>^ views ) ``` |

#### Parameters

views
:   Type:  System.Collections.Generic IList   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     These sheet views where DWF markups are imported.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DWFImportOptions Class](8465ab77-dc06-79c2-4bed-e17a564adb22.htm)

[DWFImportOptions Overload](0c06c09f-098a-d7e8-87a6-fa7e44ae6386.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)