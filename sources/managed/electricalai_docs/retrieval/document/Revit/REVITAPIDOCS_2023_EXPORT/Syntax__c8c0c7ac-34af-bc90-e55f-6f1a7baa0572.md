[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddCorrectionFactor Method (Double, Double)

---



|  |
| --- |
| [TemperatureRatingType Class](fe7e15d7-c31f-b24c-992f-332e54e9a5ba.htm)   [See Also](#seeAlsoToggle) |

Add a new electrical correction factor type to this temperature rating type. The given temperature value should be quantified in the document's selected unit of electrical temperature.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public CorrectionFactor AddCorrectionFactor( 	double temperature, 	double factor ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AddCorrectionFactor ( _ 	temperature As Double, _ 	factor As Double _ ) As CorrectionFactor ``` |

 

| Visual C++ |
| --- |
| ``` public: CorrectionFactor^ AddCorrectionFactor( 	double temperature,  	double factor ) ``` |

#### Parameters

temperature
:   Type:  System Double    
     Temperature of correction factor to be added in the document's selected unit of electrical temperature.

factor
:   Type:  System Double    
     Factor of correction factor to be added.

#### Return Value

New constructed correction factor.

# See Also

[TemperatureRatingType Class](fe7e15d7-c31f-b24c-992f-332e54e9a5ba.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)