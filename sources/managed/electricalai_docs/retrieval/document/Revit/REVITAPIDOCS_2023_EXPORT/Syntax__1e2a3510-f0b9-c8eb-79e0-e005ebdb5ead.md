[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (IFCProductWrapper)

---



|  |
| --- |
| [IFCProductWrapper Class](368d2c50-1258-32a9-00ed-cc41059a6694.htm)   [See Also](#seeAlsoToggle) |

Establishes a new product manager for elements and objects derived from a parent product manager.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static IFCProductWrapper Create( 	IFCProductWrapper pProductWrapper ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	pProductWrapper As IFCProductWrapper _ ) As IFCProductWrapper ``` |

 

| Visual C++ |
| --- |
| ``` public: static IFCProductWrapper^ Create( 	IFCProductWrapper^ pProductWrapper ) ``` |

#### Parameters

pProductWrapper
:   Type:  [Autodesk.Revit.DB.IFC IFCProductWrapper](368d2c50-1258-32a9-00ed-cc41059a6694.htm)    
     The parent product manager.

#### Return Value

The new product manager.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[IFCProductWrapper Class](368d2c50-1258-32a9-00ed-cc41059a6694.htm)

[Create Overload](45f71732-6e43-be68-8797-4b69ed236852.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)