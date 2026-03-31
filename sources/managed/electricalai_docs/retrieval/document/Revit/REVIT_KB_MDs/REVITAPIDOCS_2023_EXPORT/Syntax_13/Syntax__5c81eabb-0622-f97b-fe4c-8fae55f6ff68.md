[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ProcessIFCProject Method (IFCAnyHandle)

---



|  |
| --- |
| [ImporterIFC Class](87327a4b-94fd-5a21-df33-9beb1921cb4d.htm)   [See Also](#seeAlsoToggle) |

The entry point to the native IFC import function. Processes the main IfcProject and creates appropriate Revit elements.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void ProcessIFCProject( 	IFCAnyHandle ifcProject ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ProcessIFCProject ( _ 	ifcProject As IFCAnyHandle _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void ProcessIFCProject( 	IFCAnyHandle^ ifcProject ) ``` |

#### Parameters

ifcProject
:   Type:  [Autodesk.Revit.DB.IFC IFCAnyHandle](8b893943-70fa-94bf-90be-1523d516ecb3.htm)    
     The IfcProject containing the entities in the IFC file.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ImporterIFC Class](87327a4b-94fd-5a21-df33-9beb1921cb4d.htm)

[ProcessIFCProject Overload](2c440232-e770-1a51-a9bf-2070ff1310cd.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)