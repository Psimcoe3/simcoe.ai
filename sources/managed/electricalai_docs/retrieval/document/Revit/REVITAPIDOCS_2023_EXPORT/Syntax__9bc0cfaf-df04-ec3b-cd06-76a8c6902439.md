[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetConfiguration Method

---



|  |
| --- |
| [FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.htm)   [See Also](#seeAlsoToggle) |

Set the fabrication configuration with global profile.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void SetConfiguration( 	FabricationConfigurationInfo fabricationConfigurationInfo ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetConfiguration ( _ 	fabricationConfigurationInfo As FabricationConfigurationInfo _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetConfiguration( 	FabricationConfigurationInfo^ fabricationConfigurationInfo ) ``` |

#### Parameters

fabricationConfigurationInfo
:   Type:  [Autodesk.Revit.DB FabricationConfigurationInfo](c4977168-c9d5-73a7-328c-902330e638c7.htm)    
     The desired fabrication configuration.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The fabrication configuration cannot be swapped because the exiting fabrication configuration has already been used in the document. -or- Cannot set the configuration. |

# See Also

[FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.htm)

[SetConfiguration Overload](a673e26e-f398-6f07-3589-351835a7aa27.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)