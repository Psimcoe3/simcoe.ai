[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetButton Method

---



|  |
| --- |
| [FabricationService Class](e29ecbb2-7de0-c341-0db0-9f77bd0f5543.htm)   [See Also](#seeAlsoToggle) |

Gets the service button for a given palette index and button index from the service.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public FabricationServiceButton GetButton( 	int paletteIndex, 	int buttonIndex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetButton ( _ 	paletteIndex As Integer, _ 	buttonIndex As Integer _ ) As FabricationServiceButton ``` |

 

| Visual C++ |
| --- |
| ``` public: FabricationServiceButton^ GetButton( 	int paletteIndex,  	int buttonIndex ) ``` |

#### Parameters

paletteIndex
:   Type:  System Int32    
     The palette index.

buttonIndex
:   Type:  System Int32    
     The button index.

#### Return Value

The service button

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | the index paletteIndex is not larger or equal to 0 and less than PaletteCount |

# See Also

[FabricationService Class](e29ecbb2-7de0-c341-0db0-9f77bd0f5543.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)