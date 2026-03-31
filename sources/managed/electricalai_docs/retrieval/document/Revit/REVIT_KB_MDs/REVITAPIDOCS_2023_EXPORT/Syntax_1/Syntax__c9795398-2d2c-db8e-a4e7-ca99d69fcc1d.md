[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanDeleteSubelement Method

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [See Also](#seeAlsoToggle) |

Checks if given subelement can be removed from the element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public bool CanDeleteSubelement( 	Subelement subelem ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanDeleteSubelement ( _ 	subelem As Subelement _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanDeleteSubelement( 	Subelement^ subelem ) ``` |

#### Parameters

subelem
:   Type:  [Autodesk.Revit.DB Subelement](2d15bb45-70af-5f84-e899-322742591251.htm)    
     Subelement to check.

#### Return Value

True if subelement can be removed, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)