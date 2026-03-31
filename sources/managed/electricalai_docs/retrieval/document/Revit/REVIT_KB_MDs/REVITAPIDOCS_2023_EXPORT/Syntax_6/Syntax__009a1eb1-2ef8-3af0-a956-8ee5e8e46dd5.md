[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricationPartSizeMap Constructor (String, Double, Double, Boolean, ConnectorProfileType, Int32, Int32)

---



|  |
| --- |
| [FabricationPartSizeMap Class](b4be4ccc-ac6d-bb65-ef61-a41713b2916f.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of the FabricationPartSizeMap class.

**Namespace:**   [Autodesk.Revit.DB.Fabrication](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018.2

# Syntax

| C# |
| --- |
| ``` public FabricationPartSizeMap( 	string size, 	double widthDiameter, 	double depth, 	bool isProductList, 	ConnectorProfileType profileType, 	int serviceId, 	int paletteId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	size As String, _ 	widthDiameter As Double, _ 	depth As Double, _ 	isProductList As Boolean, _ 	profileType As ConnectorProfileType, _ 	serviceId As Integer, _ 	paletteId As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: FabricationPartSizeMap( 	String^ size,  	double widthDiameter,  	double depth,  	bool isProductList,  	ConnectorProfileType profileType,  	int serviceId,  	int paletteId ) ``` |

#### Parameters

size
:   Type:  System String    
     The size display string for the straight that can be used by the user interface.

widthDiameter
:   Type:  System Double    
     The width or diameter of the straight.

depth
:   Type:  System Double    
     The depth of the straight.

isProductList
:   Type:  System Boolean    
     Set if the straight a product list or not.

profileType
:   Type:  [Autodesk.Revit.DB ConnectorProfileType](94482e32-e0e3-2340-c23c-6cef9348434e.htm)    
     Set the shape of the straight.

serviceId
:   Type:  System Int32    
     Set the service identifier of the straight.

paletteId
:   Type:  System Int32    
     Set the palette identifier of the straight.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[FabricationPartSizeMap Class](b4be4ccc-ac6d-bb65-ef61-a41713b2916f.htm)

[FabricationPartSizeMap Overload](0448905d-7f22-4d62-e8f8-05e4d6141056.htm)

[Autodesk.Revit.DB.Fabrication Namespace](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)