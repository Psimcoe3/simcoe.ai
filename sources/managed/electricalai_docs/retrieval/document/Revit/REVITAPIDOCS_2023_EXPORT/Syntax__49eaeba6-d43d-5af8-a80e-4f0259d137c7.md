[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddVoltageType Method

---



|  |
| --- |
| [ElectricalSetting Class](d0c5bb12-7cf7-35e0-fc72-51e491c56bc2.htm)   [See Also](#seeAlsoToggle) |

Add a new type definition of voltage into project.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public VoltageType AddVoltageType( 	string name, 	double actualValue, 	double minValue, 	double maxValue ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AddVoltageType ( _ 	name As String, _ 	actualValue As Double, _ 	minValue As Double, _ 	maxValue As Double _ ) As VoltageType ``` |

 

| Visual C++ |
| --- |
| ``` public: VoltageType^ AddVoltageType( 	String^ name,  	double actualValue,  	double minValue,  	double maxValue ) ``` |

#### Parameters

name
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     Specify voltage type name

actualValue
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Specify actual value of voltage type.

minValue
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Specify acceptable minimum value of the voltage type.

maxValue
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Specify acceptable maximum value of the voltage type.

#### Return Value

New added voltage type object.

# See Also

[ElectricalSetting Class](d0c5bb12-7cf7-35e0-fc72-51e491c56bc2.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)