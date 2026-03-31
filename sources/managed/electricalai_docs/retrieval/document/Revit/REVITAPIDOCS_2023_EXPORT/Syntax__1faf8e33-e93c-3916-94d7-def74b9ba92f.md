[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IFCTransaction Constructor

---



|  |
| --- |
| [IFCTransaction Class](71896def-755f-1a91-90b0-37b6bb019265.htm)   [See Also](#seeAlsoToggle) |

Instantiates a transaction object.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public IFCTransaction( 	IFCFile file ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	file As IFCFile _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: IFCTransaction( 	IFCFile^ file ) ``` |

#### Parameters

file
:   Type:  [Autodesk.Revit.DB.IFC IFCFile](6f327830-5053-cf5d-c50e-2f5ab037b0b5.htm)    
     The IFC file for which this transaction is going to be used.

# Remarks

The transaction starts by creating a transaction object.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[IFCTransaction Class](71896def-755f-1a91-90b0-37b6bb019265.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)