[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetCoordinateSystem Method

---



|  |
| --- |
| [ReferencePoint Class](b4b9baeb-2ec5-a2e1-1420-37f593d36aa4.htm)   [See Also](#seeAlsoToggle) |

The position and orientation of the ReferencePoint.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetCoordinateSystem( 	Transform coordinateSystem ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetCoordinateSystem ( _ 	coordinateSystem As Transform _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetCoordinateSystem( 	Transform^ coordinateSystem ) ``` |

#### Parameters

coordinateSystem
:   Type:  [Autodesk.Revit.DB Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)

# Remarks

The position of the point is given by CoordinateSystem.Origin, and the orientation is specified by the three unit vectors CoordinateSystem.BasisX, BasisY, BasisZ. The basis vectors must be unit length and mutually perpendicular. Whenever the Reference property is not    a null reference (  Nothing  in Visual Basic)  , changing the CoordinateSystem property has a compound effect. First the point is moved to the specified location. Then the point is moved to conform to its Reference, by the shortest possible distance.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when coordinateSystem does not specify an orthonormal basis. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when CoordinateSystem is set while the Reference property is not    a null reference (  Nothing  in Visual Basic)  , and the ReferencePoint is unable to move to the new location. |

# See Also

[ReferencePoint Class](b4b9baeb-2ec5-a2e1-1420-37f593d36aa4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)