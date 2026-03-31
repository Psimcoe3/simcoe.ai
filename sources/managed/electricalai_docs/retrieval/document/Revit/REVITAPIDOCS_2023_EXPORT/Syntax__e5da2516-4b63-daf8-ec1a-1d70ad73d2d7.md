[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetInstanceFlipped Method

---



|  |
| --- |
| [AdaptiveComponentInstanceUtils Class](786db8ac-a051-37e4-7b4c-dbf286fe9a7c.htm)   [See Also](#seeAlsoToggle) |

Sets the value of the flip parameter on the adaptive instance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static void SetInstanceFlipped( 	FamilyInstance famInst, 	bool flip ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub SetInstanceFlipped ( _ 	famInst As FamilyInstance, _ 	flip As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void SetInstanceFlipped( 	FamilyInstance^ famInst,  	bool flip ) ``` |

#### Parameters

famInst
:   Type:  [Autodesk.Revit.DB FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)    
     The FamilyInstance

flip
:   Type:  System Boolean    
     The flip flag

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The FamilyInstance famInst is not an Adaptive Family Instance. -or- The FamilyInstance famInst does not have an Adaptive Family Symbol. -or- The FamilyInstance famInst cannot be flipped or unflipped. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This operation failed. |

# See Also

[AdaptiveComponentInstanceUtils Class](786db8ac-a051-37e4-7b4c-dbf286fe9a7c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)