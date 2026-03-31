[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [LinePatternElement Class](8f4678ba-1824-fd00-73b6-dfb9c7802f83.htm)   [See Also](#seeAlsoToggle) |

Creates a new LinePatternElement.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static LinePatternElement Create( 	Document document, 	LinePattern linePattern ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	linePattern As LinePattern _ ) As LinePatternElement ``` |

 

| Visual C++ |
| --- |
| ``` public: static LinePatternElement^ Create( 	Document^ document,  	LinePattern^ linePattern ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document in which to create the LinePatternElement.

linePattern
:   Type:  [Autodesk.Revit.DB LinePattern](a2de5c67-d9be-760b-638a-579500216874.htm)    
     The LinePattern associated to the newly created LinePatternElement.

#### Return Value

The newly created LinePatternElement.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The Line Pattern is not valid. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[LinePatternElement Class](8f4678ba-1824-fd00-73b6-dfb9c7802f83.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)