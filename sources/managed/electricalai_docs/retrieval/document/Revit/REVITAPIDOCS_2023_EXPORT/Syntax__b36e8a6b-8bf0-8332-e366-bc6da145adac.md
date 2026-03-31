[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [FabricationPartType Class](261b8995-37db-ad23-9ae6-929cb0a77122.htm)   [See Also](#seeAlsoToggle) |

Creates a fabrication part type element based on a specific fabrication servic button and condition.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public static FabricationPartType Create( 	Document document, 	FabricationServiceButton button, 	int condition ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	button As FabricationServiceButton, _ 	condition As Integer _ ) As FabricationPartType ``` |

 

| Visual C++ |
| --- |
| ``` public: static FabricationPartType^ Create( 	Document^ document,  	FabricationServiceButton^ button,  	int condition ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

button
:   Type:  [Autodesk.Revit.DB FabricationServiceButton](6a21f232-3a37-239b-8bb1-a8b02f2984ec.htm)    
     The fabrication service button.

condition
:   Type:  System Int32    
     The condition index.

#### Return Value

The created fabrication part type element.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Fabrication service button contains invalid fittings. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | the index condition is not larger or equal to 0 and less than ConditionCount |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Mechanical Electrical Piping. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The fabrication part type already exists. |

# See Also

[FabricationPartType Class](261b8995-37db-ad23-9ae6-929cb0a77122.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)