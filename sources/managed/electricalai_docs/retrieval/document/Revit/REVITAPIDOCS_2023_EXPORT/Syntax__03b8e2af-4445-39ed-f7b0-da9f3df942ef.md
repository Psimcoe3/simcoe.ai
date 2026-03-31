[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewFamilyInstanceCreationData Method (FamilySymbol, IList(XYZ))

---



|  |
| --- |
| [Application Class](5e11e5bf-82da-ae9b-1c52-95d0e9f28c96.htm)   [See Also](#seeAlsoToggle) |

Creates an object which wraps the arguments of NewFamilyInstance() for batch creation.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FamilyInstanceCreationData NewFamilyInstanceCreationData( 	FamilySymbol symbol, 	IList<XYZ> adaptivePoints ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewFamilyInstanceCreationData ( _ 	symbol As FamilySymbol, _ 	adaptivePoints As IList(Of XYZ) _ ) As FamilyInstanceCreationData ``` |

 

| Visual C++ |
| --- |
| ``` public: FamilyInstanceCreationData^ NewFamilyInstanceCreationData( 	FamilySymbol^ symbol,  	IList<XYZ^>^ adaptivePoints ) ``` |

#### Parameters

symbol
:   Type:  [Autodesk.Revit.DB FamilySymbol](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)    
     A FamilySymbol object that represents the type of the instance that is to be inserted.

adaptivePoints
:   Type:  [System.Collections.Generic IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The adaptive point location where the adaptive instance is to be placed.

# See Also

[Application Class](5e11e5bf-82da-ae9b-1c52-95d0e9f28c96.htm)

[NewFamilyInstanceCreationData Overload](8f899df7-9949-9839-35f7-4092a6e70e20.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)