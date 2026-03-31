[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanBeAssociatedWithGlobalParameters Method

---



|  |
| --- |
| [Parameter Class](333ff41b-e6a7-d959-60bf-c3bfae495581.htm)   [See Also](#seeAlsoToggle) |

Tests whether this parameter can be associated with any global parameter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016 Subscription Update

# Syntax

| C# |
| --- |
| ``` public bool CanBeAssociatedWithGlobalParameters() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanBeAssociatedWithGlobalParameters As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanBeAssociatedWithGlobalParameters() ``` |

#### Return Value

True if the given parameter can be associated (is parametrizable); False otherwise.

# Remarks

Only properties defined as parametrizable can be associated with global parameters. That excludes any read-only and formula-driven parameters, as well as those that have other explicit or implicit restrictions imposed by Revit.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This parameter does not exist in the document anymore. |

# See Also

[Parameter Class](333ff41b-e6a7-d959-60bf-c3bfae495581.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)