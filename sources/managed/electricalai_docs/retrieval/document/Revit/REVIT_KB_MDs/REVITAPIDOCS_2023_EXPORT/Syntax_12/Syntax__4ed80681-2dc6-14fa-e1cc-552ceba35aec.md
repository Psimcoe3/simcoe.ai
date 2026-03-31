[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetGlobal2DDirectionHandles Method

---



|  |
| --- |
| [ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)   [See Also](#seeAlsoToggle) |

Sets the handles representing the cardinal directions in 2D.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static void SetGlobal2DDirectionHandles( 	bool positive, 	IFCAnyHandle xDir, 	IFCAnyHandle yDir ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub SetGlobal2DDirectionHandles ( _ 	positive As Boolean, _ 	xDir As IFCAnyHandle, _ 	yDir As IFCAnyHandle _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void SetGlobal2DDirectionHandles( 	bool positive,  	IFCAnyHandle^ xDir,  	IFCAnyHandle^ yDir ) ``` |

#### Parameters

positive
:   Type:  System Boolean    
     True if the handles returned should be in the positive direction, false if the handles should be in the negative direction.

xDir
:   Type:  [Autodesk.Revit.DB.IFC IFCAnyHandle](8b893943-70fa-94bf-90be-1523d516ecb3.htm)    
     The X direction handle.

yDir
:   Type:  [Autodesk.Revit.DB.IFC IFCAnyHandle](8b893943-70fa-94bf-90be-1523d516ecb3.htm)    
     The Y direction handle.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)