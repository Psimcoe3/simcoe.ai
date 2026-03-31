[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TemperatureRatingType Class

---



|  |
| --- |
| [Members](6a6ae4fb-4c5b-cfd3-1eb6-7cdee0745550.htm)   [See Also](#seeAlsoToggle) |

Represents temperature rating type definition information.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class TemperatureRatingType : ElementType ``` |

 

| Visual Basic |
| --- |
| ``` Public Class TemperatureRatingType _ 	Inherits ElementType ``` |

 

| Visual C++ |
| --- |
| ``` public ref class TemperatureRatingType : public ElementType ``` |

# Remarks

Temperature rating type is defined based on corresponding wire material type. It includes type information such as wire size, insulation type, correction factor, etc. Only the temperature rating types which are retrieved from WireMaterialType can work well, so don't retrieve it from Revit document directly.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  Autodesk.Revit.DB.Electrical TemperatureRatingType

# See Also

[TemperatureRatingType Members](6a6ae4fb-4c5b-cfd3-1eb6-7cdee0745550.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)