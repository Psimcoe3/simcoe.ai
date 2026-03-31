[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetIsFilterEnabled Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Sets the filter enabled flag.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public void SetIsFilterEnabled( 	ElementId filterElementId, 	bool enable ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetIsFilterEnabled ( _ 	filterElementId As ElementId, _ 	enable As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetIsFilterEnabled( 	ElementId^ filterElementId,  	bool enable ) ``` |

#### Parameters

filterElementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ElementId of the filter.

enable
:   Type:  System Boolean    
     True if the specified filter should be enabled in this view, false otherwise.

# Remarks

Several filters can be applied to a view in a sertain order. This enable/disable flag allows one to quickly turn on/off the action of a particular filter in this view (without removing the filter from the set of applied filters and loosing the corresponding overrides). By default, all the filters applied to a view are enabled.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Filter is not applied to the view. -or- ElementId is not associated with a FilterElement. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The element "this View" does not belong to a project document. -or- The view type does not support Visibility/Graphics Overriddes. |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)