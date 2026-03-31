[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [IFCFile Class](6f327830-5053-cf5d-c50e-2f5ab037b0b5.htm)   [See Also](#seeAlsoToggle) |

Creates an IFC file for exporting.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static IFCFile Create( 	IFCFileModelOptions modelOptions ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	modelOptions As IFCFileModelOptions _ ) As IFCFile ``` |

 

| Visual C++ |
| --- |
| ``` public: static IFCFile^ Create( 	IFCFileModelOptions^ modelOptions ) ``` |

#### Parameters

modelOptions
:   Type:  [Autodesk.Revit.DB.IFC IFCFileModelOptions](9cd09052-e2e2-84e3-c500-9b492ad8d78b.htm)    
     The options.

#### Return Value

The IFC file.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[IFCFile Class](6f327830-5053-cf5d-c50e-2f5ab037b0b5.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)