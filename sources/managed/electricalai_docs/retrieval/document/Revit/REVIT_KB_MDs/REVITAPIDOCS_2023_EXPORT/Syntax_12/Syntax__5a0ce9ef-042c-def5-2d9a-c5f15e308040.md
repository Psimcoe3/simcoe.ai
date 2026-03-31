[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OverrideServiceButtonExclusion Method

---



|  |
| --- |
| [FabricationService Class](e29ecbb2-7de0-c341-0db0-9f77bd0f5543.htm)   [See Also](#seeAlsoToggle) |

Overrides the default service button exclusions, used by Route and Fill, Design to Fabrication, or Multi Point Routing for the current user and session only.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017 Subscription Update

# Syntax

| C# |
| --- |
| ``` public void OverrideServiceButtonExclusion( 	int paletteIndex, 	int buttonIndex, 	bool exclude ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub OverrideServiceButtonExclusion ( _ 	paletteIndex As Integer, _ 	buttonIndex As Integer, _ 	exclude As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void OverrideServiceButtonExclusion( 	int paletteIndex,  	int buttonIndex,  	bool exclude ) ``` |

#### Parameters

paletteIndex
:   Type:  System Int32    
     The index of the service palette to exclude the service button from.

buttonIndex
:   Type:  System Int32    
     The index of the service button to exclude.

exclude
:   Type:  System Boolean    
     Pass true to exclude from being used by Route and Fill or Design to Fabrication.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | the index paletteIndex is not larger or equal to 0 and less than PaletteCount |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also

[FabricationService Class](e29ecbb2-7de0-c341-0db0-9f77bd0f5543.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)