[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Get3DContextHandle Method

---



|  |
| --- |
| [ExporterIFC Class](c8697b81-e080-9202-14d3-ec883f951521.htm)   [See Also](#seeAlsoToggle) |

Obtains the IfcRepresentationContext or IfcRepresentationSubContext handle to be used for 3D entities (Model entities).

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public IFCAnyHandle Get3DContextHandle( 	string subContextName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Get3DContextHandle ( _ 	subContextName As String _ ) As IFCAnyHandle ``` |

 

| Visual C++ |
| --- |
| ``` public: IFCAnyHandle^ Get3DContextHandle( 	String^ subContextName ) ``` |

#### Parameters

subContextName
:   Type:  System String    
     The name of the IfcRepresentationSubContext, or the IfcRepresentationContext if the string is empty, for 3D entities.

#### Return Value

The IfcRepresentationContext for 3D entities.

# Remarks

The context handle automatically incorporates the angle to true north for the document.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExporterIFC Class](c8697b81-e080-9202-14d3-ec883f951521.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)