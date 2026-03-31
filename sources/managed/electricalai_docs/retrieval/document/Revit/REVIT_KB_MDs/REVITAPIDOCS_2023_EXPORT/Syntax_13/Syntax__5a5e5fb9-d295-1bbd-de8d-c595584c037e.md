[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ThermalAsset Constructor

---



|  |
| --- |
| [ThermalAsset Class](c4dac7e3-96e2-bc6c-1299-f696a253e879.htm)   [See Also](#seeAlsoToggle) |

Constructs an instance of ThermalAsset.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ThermalAsset( 	string name, 	ThermalMaterialType materialType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	name As String, _ 	materialType As ThermalMaterialType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ThermalAsset( 	String^ name,  	ThermalMaterialType materialType ) ``` |

#### Parameters

name
:   Type:  System String    
     The name of the asset.

materialType
:   Type:  [Autodesk.Revit.DB ThermalMaterialType](73446ebc-6ebf-855c-aadc-a4d4291cc082.htm)    
     The type of thermal material that this asset will describe.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | name is an empty string. -or- name cannot include prohibited characters, such as "{, }, [, ], |, ;, less-than sign, greater-than sign, ?, `, ~". |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ThermalAsset Class](c4dac7e3-96e2-bc6c-1299-f696a253e879.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)