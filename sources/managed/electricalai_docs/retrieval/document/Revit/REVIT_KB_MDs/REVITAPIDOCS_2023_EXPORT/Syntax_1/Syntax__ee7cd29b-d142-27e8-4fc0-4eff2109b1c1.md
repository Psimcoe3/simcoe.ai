[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidView Method

---



|  |
| --- |
| [ImageInstance Class](ff77d6c8-a94a-067a-cd95-4f2cd3ec8dcc.htm)   [See Also](#seeAlsoToggle) |

Check that the view is a valid view for ImageInstance elements

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public static bool IsValidView( 	View view ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidView ( _ 	view As View _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidView( 	View^ view ) ``` |

#### Parameters

view
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view to validate

#### Return Value

True if the view can contain ImageInstance elements. False otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ImageInstance Class](ff77d6c8-a94a-067a-cd95-4f2cd3ec8dcc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)