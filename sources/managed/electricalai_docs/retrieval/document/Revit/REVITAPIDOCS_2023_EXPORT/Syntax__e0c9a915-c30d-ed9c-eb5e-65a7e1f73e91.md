[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetAlphanumericRevisionSettings Method

---



|  |
| --- |
| [RevisionNumberingSequence Class](52b6f8d8-4d5e-dfee-7782-5cd7a77ee543.htm)   [See Also](#seeAlsoToggle) |

Replaces the current alphanumeric revision numbering settings with the provided settings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public void SetAlphanumericRevisionSettings( 	AlphanumericRevisionSettings settings ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetAlphanumericRevisionSettings ( _ 	settings As AlphanumericRevisionSettings _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetAlphanumericRevisionSettings( 	AlphanumericRevisionSettings^ settings ) ``` |

#### Parameters

settings
:   Type:  [Autodesk.Revit.DB AlphanumericRevisionSettings](ee27c0eb-9f9b-b59c-728d-24b2654a2bc2.htm)    
     The AlphanumericRevisionSettings to be applied to alphanumeric revision numbering.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | settings is not a valid AlphanumericRevisionSettings. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RevisionNumberingSequence Class](52b6f8d8-4d5e-dfee-7782-5cd7a77ee543.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)