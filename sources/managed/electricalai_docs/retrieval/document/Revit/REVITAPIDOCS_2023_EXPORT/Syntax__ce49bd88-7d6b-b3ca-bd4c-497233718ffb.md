[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewSpace Method (Level, Phase, UV)

---



|  |
| --- |
| [Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)   [See Also](#seeAlsoToggle) |

Creates a new space element on the given level, at the given location, and assigned to the given phase.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Space NewSpace( 	Level level, 	Phase phase, 	UV point ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewSpace ( _ 	level As Level, _ 	phase As Phase, _ 	point As UV _ ) As Space ``` |

 

| Visual C++ |
| --- |
| ``` public: Space^ NewSpace( 	Level^ level,  	Phase^ phase,  	UV^ point ) ``` |

#### Parameters

level
:   Type:  [Autodesk.Revit.DB Level](577e5d4e-a558-118c-9dea-3b810b061775.htm)    
     The level on which the room is to exist.

phase
:   Type:  [Autodesk.Revit.DB Phase](ab01f390-a8e8-c21c-b2d0-6dd21056cdec.htm)    
     The phase in which the room is to exist.

point
:   Type:  [Autodesk.Revit.DB UV](1724be37-059b-91ff-aa74-d1508082f76d.htm)    
     A 2D point that dictates the location on that specified level.

#### Return Value

If successful a new Space element within the project, otherwise    a null reference (  Nothing  in Visual Basic)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when level, phase or point is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the space cannot be created. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if the level does not exist in the given document. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if the phase does not exist in the given document. |

# See Also

[Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)

[NewSpace Overload](d72124de-64a9-56ca-b310-6856c507e647.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)