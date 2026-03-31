[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FindExtrusionCreationParameters Method

---



|  |
| --- |
| [IFCProductWrapper Class](368d2c50-1258-32a9-00ed-cc41059a6694.htm)   [See Also](#seeAlsoToggle) |

Obtains the extrusion creation data associated with the given element.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public IFCExtrusionCreationData FindExtrusionCreationParameters( 	IFCAnyHandle elementHandle ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function FindExtrusionCreationParameters ( _ 	elementHandle As IFCAnyHandle _ ) As IFCExtrusionCreationData ``` |

 

| Visual C++ |
| --- |
| ``` public: IFCExtrusionCreationData^ FindExtrusionCreationParameters( 	IFCAnyHandle^ elementHandle ) ``` |

#### Parameters

elementHandle
:   Type:  [Autodesk.Revit.DB.IFC IFCAnyHandle](8b893943-70fa-94bf-90be-1523d516ecb3.htm)    
     The handle.

#### Return Value

The parameters.    a null reference (  Nothing  in Visual Basic)  if no parameters are associated with the element.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[IFCProductWrapper Class](368d2c50-1258-32a9-00ed-cc41059a6694.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)