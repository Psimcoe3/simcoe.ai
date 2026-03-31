[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddFilter Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Adds a filter to the view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void AddFilter( 	ElementId filterElementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddFilter ( _ 	filterElementId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddFilter( 	ElementId^ filterElementId ) ``` |

#### Parameters

filterElementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     ElementId of the filter.

# Remarks

The filter will be added with default overrides, which means that there will be no change in the view's display. The filter is appended as the last filter in the order of filters applied to this view.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | ElementId is not associated with a FilterElement. -or- Filter is already applied to the view. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The element "this View" does not belong to a project document. -or- The view type does not support Visibility/Graphics Overriddes. |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)