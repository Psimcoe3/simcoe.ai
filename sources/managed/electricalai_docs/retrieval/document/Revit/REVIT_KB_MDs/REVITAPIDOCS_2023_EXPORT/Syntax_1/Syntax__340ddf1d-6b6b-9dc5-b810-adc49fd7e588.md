[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ColorName Property

---



|  |
| --- |
| [ExportLayerInfo Class](88a99694-968a-99f7-870a-f46737bd5927.htm)   [See Also](#seeAlsoToggle) |

The color name stored in value. For IFC export, the naming is to match the "colornumber" setting -- really, this stores a string that generates the colorNumber (for formats that don't use the color but need a second entry.)

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public string ColorName { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ColorName As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ ColorName { 	String^ get (); 	void set (String^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[ExportLayerInfo Class](88a99694-968a-99f7-870a-f46737bd5927.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)