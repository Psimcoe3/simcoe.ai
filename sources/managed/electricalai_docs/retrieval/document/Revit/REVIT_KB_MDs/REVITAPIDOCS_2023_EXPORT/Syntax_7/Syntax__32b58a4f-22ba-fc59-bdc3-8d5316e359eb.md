[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetDefaultEntity Method

---



|  |
| --- |
| [PipeFittingAndAccessoryPressureDropData Class](83417712-9a53-53da-62ca-2a8fed96c875.htm)   [See Also](#seeAlsoToggle) |

Stores the default entity in the data.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void SetDefaultEntity( 	Entity defaultEntity ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetDefaultEntity ( _ 	defaultEntity As Entity _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetDefaultEntity( 	Entity^ defaultEntity ) ``` |

#### Parameters

defaultEntity
:   Type:  [Autodesk.Revit.DB.ExtensibleStorage Entity](cf17f0e8-33bd-ef95-bf4b-e6298406f29b.htm)    
     The Entity to be stored.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Writing of Entities of this Schema is not allowed to the current add-in. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PipeFittingAndAccessoryPressureDropData Class](83417712-9a53-53da-62ca-2a8fed96c875.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)