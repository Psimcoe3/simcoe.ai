[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetSegmentFixedDirection Method

---



|  |
| --- |
| [RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.htm)   [See Also](#seeAlsoToggle) |

Fix the direction of a segment.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetSegmentFixedDirection( 	int iSegment, 	double vecCoordX, 	double vecCoordY ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetSegmentFixedDirection ( _ 	iSegment As Integer, _ 	vecCoordX As Double, _ 	vecCoordY As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetSegmentFixedDirection( 	int iSegment,  	double vecCoordX,  	double vecCoordY ) ``` |

#### Parameters

iSegment
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Index of the segment (0 to NumberOfSegments - 1).

vecCoordX
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The x-coordinate of a 2D vector specifying the segment direction.

vecCoordY
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The y-coordinate of a 2D vector specifying the segment direction.

# Remarks

The centerline of the segment will be constrained to be parallel to the vector. The segment must have at least one constraint.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | iSegment is not between 0 and NumberOfSegments. -or- The length of the vector (vecCoordX, vecCoordY) is too close to zero. |

# See Also

[RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)