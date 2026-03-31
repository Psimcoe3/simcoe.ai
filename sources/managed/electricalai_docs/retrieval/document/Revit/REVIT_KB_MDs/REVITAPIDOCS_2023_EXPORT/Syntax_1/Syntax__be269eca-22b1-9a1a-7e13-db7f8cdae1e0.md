[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportCategory Property

---



|  |
| --- |
| [EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)   [See Also](#seeAlsoToggle) |

Value is a category indicating which discipline model will be used for GreenBuildingXML export.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ElementId ExportCategory { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ExportCategory As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ ExportCategory { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Remarks

OST\_Rooms will use the architectural 3d rooms for export. OST\_MEPSpaces will use the MEP 3d Spaces for export.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The export category is neither OST\_Rooms nor OST\_MEPSpaces. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)