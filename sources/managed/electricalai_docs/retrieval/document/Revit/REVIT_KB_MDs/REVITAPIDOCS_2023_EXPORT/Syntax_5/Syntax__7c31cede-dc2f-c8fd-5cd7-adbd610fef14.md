[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSegment Method

---



|  |
| --- |
| [RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.htm)   [See Also](#seeAlsoToggle) |

Return a reference to one of the segments in the definition.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public RebarShapeSegment GetSegment( 	int segmentIndex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSegment ( _ 	segmentIndex As Integer _ ) As RebarShapeSegment ``` |

 

| Visual C++ |
| --- |
| ``` public: RebarShapeSegment^ GetSegment( 	int segmentIndex ) ``` |

#### Parameters

segmentIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Index of the segment (0 to NumberOfSegments - 1).

#### Return Value

The requested segment.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | segmentIndex is not between 0 and NumberOfSegments. |

# See Also

[RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)