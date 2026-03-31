[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemoveWireMaterialType Method

---



|  |
| --- |
| [ElectricalSetting Class](d0c5bb12-7cf7-35e0-fc72-51e491c56bc2.htm)   [See Also](#seeAlsoToggle) |

Remove the wire material type from project.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void RemoveWireMaterialType( 	WireMaterialType materialType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub RemoveWireMaterialType ( _ 	materialType As WireMaterialType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void RemoveWireMaterialType( 	WireMaterialType^ materialType ) ``` |

#### Parameters

materialType
:   Type:  [Autodesk.Revit.DB.Electrical WireMaterialType](3d05ec79-0289-c6d1-2a13-7e6b07241afd.htm)    
     The wire material type to be removed.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Wire material type can be removed only if it is not currently assigned to any wire type, and the last one wire material type can't be removed, otherwise an exception will be thrown. |

# See Also

[ElectricalSetting Class](d0c5bb12-7cf7-35e0-fc72-51e491c56bc2.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)