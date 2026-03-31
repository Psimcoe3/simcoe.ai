[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanBeSwapped Method

---



|  |
| --- |
| [FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.htm)   [See Also](#seeAlsoToggle) |

Checks if the fabrication configuration can be swapped.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public bool CanBeSwapped() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanBeSwapped As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanBeSwapped() ``` |

#### Return Value

True if the fabrication configuration can be swapped, false otherwise.

# Remarks

Swapping configuration is not permitted if the existing configuration has already been used to create fabrication part elements in the document.

# See Also

[FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)