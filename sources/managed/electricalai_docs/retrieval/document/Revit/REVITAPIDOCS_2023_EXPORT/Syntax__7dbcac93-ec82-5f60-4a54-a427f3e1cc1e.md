[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRoomAtPoint Method (XYZ, Phase)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Gets a room containing the point.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Room GetRoomAtPoint( 	XYZ point, 	Phase phase ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRoomAtPoint ( _ 	point As XYZ, _ 	phase As Phase _ ) As Room ``` |

 

| Visual C++ |
| --- |
| ``` public: Room^ GetRoomAtPoint( 	XYZ^ point,  	Phase^ phase ) ``` |

#### Parameters

point
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     Point to be checked.

phase
:   Type:  [Autodesk.Revit.DB Phase](ab01f390-a8e8-c21c-b2d0-6dd21056cdec.htm)    
     Phase in which the room exists.

#### Return Value

The room containing the point.

# Remarks

If phase is    a null reference (  Nothing  in Visual Basic)  , it will get the room of the last phase.The first one found will be returned. If there is no room containing the point, it returns    a null reference (  Nothing  in Visual Basic)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the point is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the coordinates of the point are not number or are Double::MaxValue or Double::MinValue. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[GetRoomAtPoint Overload](abe7af79-92f3-be8e-595f-8666dc6ba86b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)