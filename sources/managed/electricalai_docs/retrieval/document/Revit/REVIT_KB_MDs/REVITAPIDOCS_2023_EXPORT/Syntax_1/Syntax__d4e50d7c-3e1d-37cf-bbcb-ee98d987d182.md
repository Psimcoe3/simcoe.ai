[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetConnectivityValidation Method

---



|  |
| --- |
| [ConfigurationReloadInfo Class](f19d2d1f-191d-ec90-4b07-20c9307bf537.htm)   [See Also](#seeAlsoToggle) |

Returns information about the post-reload connectivity validation.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public ConnectionValidationInfo GetConnectivityValidation() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetConnectivityValidation As ConnectionValidationInfo ``` |

 

| Visual C++ |
| --- |
| ``` public: ConnectionValidationInfo^ GetConnectivityValidation() ``` |

#### Return Value

Information about the post-reload connectivity validation.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also

[ConfigurationReloadInfo Class](f19d2d1f-191d-ec90-4b07-20c9307bf537.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)