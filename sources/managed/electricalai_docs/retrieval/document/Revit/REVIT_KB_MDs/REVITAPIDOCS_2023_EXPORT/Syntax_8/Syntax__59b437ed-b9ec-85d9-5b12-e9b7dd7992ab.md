[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetThermalAsset Method

---



|  |
| --- |
| [PropertySetElement Class](dd2c8fbb-98ec-7249-87f0-542401f490dd.htm)   [See Also](#seeAlsoToggle) |

Sets a copy of the given ThermalAsset to be used in the PropertySetElement.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void SetThermalAsset( 	ThermalAsset thermalAsset ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetThermalAsset ( _ 	thermalAsset As ThermalAsset _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetThermalAsset( 	ThermalAsset^ thermalAsset ) ``` |

#### Parameters

thermalAsset
:   Type:  [Autodesk.Revit.DB ThermalAsset](c4dac7e3-96e2-bc6c-1299-f696a253e879.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the name of the asset is empty, contains prohibited characters, or is not unique |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PropertySetElement Class](dd2c8fbb-98ec-7249-87f0-542401f490dd.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)