[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetPointConstraintType Method

---



|  |
| --- |
| [AdaptiveComponentFamilyUtils Class](6fdc0a79-5217-21b2-122d-b1987180cc5b.htm)   [See Also](#seeAlsoToggle) |

Sets constrain type of an Adaptive Shape Handle Point.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static void SetPointConstraintType( 	Document doc, 	ElementId refPointId, 	AdaptivePointConstraintType constraintType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub SetPointConstraintType ( _ 	doc As Document, _ 	refPointId As ElementId, _ 	constraintType As AdaptivePointConstraintType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void SetPointConstraintType( 	Document^ doc,  	ElementId^ refPointId,  	AdaptivePointConstraintType constraintType ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The Document

refPointId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ReferencePoint id

constraintType
:   Type:  [Autodesk.Revit.DB AdaptivePointConstraintType](9aa479aa-36be-bf1b-7570-026afcd4d02e.htm)    
     Constraint type of the Adaptive Shape Handle Point.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The ElementId refPointId does not correspond to a valid ReferencePoint. -or- The Element corresponding to ElementId refPointId does not belong to an Adaptive Family. -or- The ElementId refPointId does not correspond to a Shape Handle Point. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This operation failed. |

# See Also

[AdaptiveComponentFamilyUtils Class](6fdc0a79-5217-21b2-122d-b1987180cc5b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)