[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetBarIncluded Method

---



|  |
| --- |
| [Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)   [See Also](#seeAlsoToggle) |

Sets if the bar at the desired index is included or not.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public void SetBarIncluded( 	bool include, 	int barPositionIndex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetBarIncluded ( _ 	include As Boolean, _ 	barPositionIndex As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetBarIncluded( 	bool include,  	int barPositionIndex ) ``` |

#### Parameters

include
:   Type:  System Boolean    
     True to include the bar, false to exclude the bar.

barPositionIndex
:   Type:  System Int32    
     The bar index.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barPositionIndex is not in the range [ 0, NumberOfBarPositions-1 ]. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)