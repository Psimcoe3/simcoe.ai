[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetRodEndPosition Method

---



|  |
| --- |
| [FabricationRodInfo Class](b52fe314-2639-a697-cf97-b3e4824818f8.htm)   [See Also](#seeAlsoToggle) |

Sets the position of the rod end. The method is applicable only for bearer hanger.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void SetRodEndPosition( 	int rodIndex, 	XYZ position ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetRodEndPosition ( _ 	rodIndex As Integer, _ 	position As XYZ _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetRodEndPosition( 	int rodIndex,  	XYZ^ position ) ``` |

#### Parameters

rodIndex
:   Type:  System Int32    
     The index of the rod.

position
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The position of the rod end.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Invalid rod position. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | the index rodIndex is should be in range of rod count. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The hanger is not a bearer hanger. |

# See Also

[FabricationRodInfo Class](b52fe314-2639-a697-cf97-b3e4824818f8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)