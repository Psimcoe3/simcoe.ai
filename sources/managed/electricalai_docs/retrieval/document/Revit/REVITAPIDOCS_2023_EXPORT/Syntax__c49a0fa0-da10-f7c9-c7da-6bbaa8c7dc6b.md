[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalyticalModelSelector Constructor (Curve)

---



|  |
| --- |
| [AnalyticalModelSelector Class](d286b023-8822-10ad-6702-53c86a6c9e70.htm)   [See Also](#seeAlsoToggle) |

Creates a selector based on a specific analytical curve.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public AnalyticalModelSelector( 	Curve curve ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	curve As Curve _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: AnalyticalModelSelector( 	Curve^ curve ) ``` |

#### Parameters

curve
:   Type:  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     The curve upon which this selector acts.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input curve points to a helical curve and is not supported for this operation. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[AnalyticalModelSelector Class](d286b023-8822-10ad-6702-53c86a6c9e70.htm)

[AnalyticalModelSelector Overload](9e76852b-a21f-b2d7-93a3-66b844047368.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)