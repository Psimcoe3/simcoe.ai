[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddSpace Method

---



|  |
| --- |
| [IFCProductWrapper Class](368d2c50-1258-32a9-00ed-cc41059a6694.htm)   [See Also](#seeAlsoToggle) |

Adds an IfcSpace handle to associate with the IfcProduct in this wrapper.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void AddSpace( 	IFCAnyHandle spaceHandle, 	IFCLevelInfo pLevelInfo, 	IFCExtrusionCreationData pParams, 	bool relateToLevel ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddSpace ( _ 	spaceHandle As IFCAnyHandle, _ 	pLevelInfo As IFCLevelInfo, _ 	pParams As IFCExtrusionCreationData, _ 	relateToLevel As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddSpace( 	IFCAnyHandle^ spaceHandle,  	IFCLevelInfo^ pLevelInfo,  	IFCExtrusionCreationData^ pParams,  	bool relateToLevel ) ``` |

#### Parameters

spaceHandle
:   Type:  [Autodesk.Revit.DB.IFC IFCAnyHandle](8b893943-70fa-94bf-90be-1523d516ecb3.htm)    
     The IfcSpace handle.

pLevelInfo
:   Type:  [Autodesk.Revit.DB.IFC IFCLevelInfo](9f287338-fe0c-383b-58be-39105d704a9f.htm)    
     Information on the associated level.

pParams
:   Type:  [Autodesk.Revit.DB.IFC IFCExtrusionCreationData](9447a335-6861-0533-6896-e6ff1fd41761.htm)    
     The extrusion creation data associated with the given space. Optional, can be    a null reference (  Nothing  in Visual Basic)  .

relateToLevel
:   Type:  System Boolean    
     True to relate the space to the level, false otherwise.

# Remarks

If the IFCLevelInfo is not provided, and relateToLevel to true, the handle will be associated to the building handle.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[IFCProductWrapper Class](368d2c50-1258-32a9-00ed-cc41059a6694.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)