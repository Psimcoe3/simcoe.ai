[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OrderedViewList Property

---



|  |
| --- |
| [InSessionViewSheetSet Class](61a44d58-c862-5fb6-6a06-dd3d3abac585.htm)   [See Also](#seeAlsoToggle) |

Ordered views.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual IReadOnlyList<View> OrderedViewList { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Property OrderedViewList As IReadOnlyList(Of View) 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property IReadOnlyList<View^>^ OrderedViewList { 	IReadOnlyList<View^>^ get (); 	void set (IReadOnlyList<View^>^ value); } ``` |

#### Implements

 [IViewSheetSet OrderedViewList](fd9a9560-5984-91ee-f888-6550524215b9.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input ordered view list is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the set operation failed due to invalid view which cannot be printed. |

# See Also

[InSessionViewSheetSet Class](61a44d58-c862-5fb6-6a06-dd3d3abac585.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)