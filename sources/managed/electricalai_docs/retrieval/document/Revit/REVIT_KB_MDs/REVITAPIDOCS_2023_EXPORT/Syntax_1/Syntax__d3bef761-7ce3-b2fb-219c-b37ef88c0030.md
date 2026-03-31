[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetMinSymbolWidth Method

---



|  |
| --- |
| [ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)   [See Also](#seeAlsoToggle) |

Obtains the minimum width of the given FamilySymbol.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static double GetMinSymbolWidth( 	FamilySymbol symbol ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetMinSymbolWidth ( _ 	symbol As FamilySymbol _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: static double GetMinSymbolWidth( 	FamilySymbol^ symbol ) ``` |

#### Parameters

symbol
:   Type:  [Autodesk.Revit.DB FamilySymbol](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)    
     The family symbol.

#### Return Value

The minimum width.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)