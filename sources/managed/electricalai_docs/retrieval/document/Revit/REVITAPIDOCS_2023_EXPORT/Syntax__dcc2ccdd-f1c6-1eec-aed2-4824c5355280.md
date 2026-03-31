[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetApparentPhaseValue Method

---



|  |
| --- |
| [PanelScheduleView Class](ef4390e8-5a93-fe7f-580b-c8ec297f6b52.htm)   [See Also](#seeAlsoToggle) |

Gets the apparent load for the given phase for the given slotted circuit

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public double GetApparentPhaseValue( 	ElementId circuitId, 	ElementId apparentLoadParam ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetApparentPhaseValue ( _ 	circuitId As ElementId, _ 	apparentLoadParam As ElementId _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetApparentPhaseValue( 	ElementId^ circuitId,  	ElementId^ apparentLoadParam ) ``` |

#### Parameters

circuitId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Circuit id for the apparent phase value

apparentLoadParam
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The requested apparent load phase parameter

#### Return Value

The value of the apparent phase

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PanelScheduleView Class](ef4390e8-5a93-fe7f-580b-c8ec297f6b52.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)