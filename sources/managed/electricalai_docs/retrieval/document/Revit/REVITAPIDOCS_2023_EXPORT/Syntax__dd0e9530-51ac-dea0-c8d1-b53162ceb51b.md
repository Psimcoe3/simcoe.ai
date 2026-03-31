[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDescriptionText Method

---



|  |
| --- |
| [FailureDefinition Class](b0c061b0-d712-0c41-6054-b8ce8f996256.htm)   [See Also](#seeAlsoToggle) |

Retrieves the description text of the failure.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public string GetDescriptionText() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetDescriptionText As String ``` |

 

| Visual C++ |
| --- |
| ``` public: String^ GetDescriptionText() ``` |

#### Return Value

The description text.

# Remarks

Retrieved description text for built-in Revit failures is localized. The result may vary from the description text retrieved from the corresponding FailureMessage. A failure definition contains a description string, that may have format specifiers like %s, and "sample" strings, that will be used to resolve them. A FailureMessage will contain "specific" strings. So, in the failure definition description "Cannot keep %s joined" will be converted into "Cannot keep Element joined" while the description in actual FailureMessage will read "Cannot keep Walls joined" or "Cannot keep Beams joined"

# See Also

[FailureDefinition Class](b0c061b0-d712-0c41-6054-b8ce8f996256.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)