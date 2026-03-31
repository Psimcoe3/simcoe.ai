[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetArcTypeSpiral Method

---



|  |
| --- |
| [RebarShapeDefinitionByArc Class](a92742a5-9781-3691-ec78-5b318fbf5ad3.htm)   [See Also](#seeAlsoToggle) |

Set the RebarShapeDefinitionByArc.Type property to Spiral.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void SetArcTypeSpiral( 	double height, 	double pitch, 	int baseFinishingTurns, 	int topFinishingTurns ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetArcTypeSpiral ( _ 	height As Double, _ 	pitch As Double, _ 	baseFinishingTurns As Integer, _ 	topFinishingTurns As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetArcTypeSpiral( 	double height,  	double pitch,  	int baseFinishingTurns,  	int topFinishingTurns ) ``` |

#### Parameters

height
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The height of the spiral (assuming the spiral is vertical).

pitch
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The pitch, or vertical distance traveled in one rotation.

baseFinishingTurns
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The number of finishing turns at the lower end of the spiral.

topFinishingTurns
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The number of finishing turns at the upper end of the spiral.

# Remarks

In order to create a spiral definition, you must provide default values for height, pitch, and finishing turns.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | baseFinishingTurns is not between 0 and 100. -or- topFinishingTurns is not between 0 and 100. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for height must be greater than 0 and no more than 30000 feet. -or- The given value for pitch must be greater than 0 and no more than 30000 feet. |

# See Also

[RebarShapeDefinitionByArc Class](a92742a5-9781-3691-ec78-5b318fbf5ad3.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)