[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AreSolidsEqual Method

---



|  |
| --- |
| [ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)   [See Also](#seeAlsoToggle) |

Determines whether two solids are identical, potentially offset from each other.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static bool AreSolidsEqual( 	Solid first, 	Solid second, 	out Transform trf ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function AreSolidsEqual ( _ 	first As Solid, _ 	second As Solid, _ 	<OutAttribute> ByRef trf As Transform _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool AreSolidsEqual( 	Solid^ first,  	Solid^ second,  	[OutAttribute] Transform^% trf ) ``` |

#### Parameters

first
:   Type:  [Autodesk.Revit.DB Solid](7a3b5ac1-c66d-9f81-a11d-9bcd4e026295.htm)    
     The first solid.

second
:   Type:  [Autodesk.Revit.DB Solid](7a3b5ac1-c66d-9f81-a11d-9bcd4e026295.htm)    
     The second solid

trf
:   Type:  [Autodesk.Revit.DB Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)   %    
     The offset transform

#### Return Value

True if they are identical, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)