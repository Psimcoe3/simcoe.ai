[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetProjectPosition Method

---



|  |
| --- |
| [ProjectLocation Class](1249d5fa-74f3-cf64-0a63-7ab370b67a5c.htm)   [See Also](#seeAlsoToggle) |

Sets the coordinates of a point in the ProjectLocation's coordinate system.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetProjectPosition( 	XYZ point, 	ProjectPosition position ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetProjectPosition ( _ 	point As XYZ, _ 	position As ProjectPosition _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetProjectPosition( 	XYZ^ point,  	ProjectPosition^ position ) ``` |

#### Parameters

point
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)

position
:   Type:  [Autodesk.Revit.DB ProjectPosition](249111cc-c1f3-d3e1-e7bf-dc791327fd4c.htm)

# Remarks

When setting this value, the transformations applied to the location are modified such that the passed point becomes the specified North/South, East/West and Elevation, and the coordinate transform will have the designated angular rotation. This is similar to the Revit command "Specify Coordinates at Point".

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Unable to use the project position's transform to calculate the point. |

# See Also

[ProjectLocation Class](1249d5fa-74f3-cf64-0a63-7ab370b67a5c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)