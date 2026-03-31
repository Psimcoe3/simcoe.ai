[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### JournalingMode Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

All journaling modes supported by Revit external commands.

**Namespace:**   [Autodesk.Revit.Attributes](59587eb2-4714-707c-9ec9-766e70658df7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public enum JournalingMode ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration JournalingMode ``` |

 

| Visual C++ |
| --- |
| ``` public enum class JournalingMode ``` |

# Members

| Member name | Description |
| --- | --- |
| UsingCommandData | Uses the "StringStringMap" supplied in the command data. Hides all Revit journal entries in between the external command invocation and the StringStringMap entry. Commands which invoke the Revit UI for selection or for responses to task dialogs may not replay correctly. |
| NoCommandData | Does not write contents of the ExternalCommandData.Data map to the Revit journal. But does allow Revit API calls to write to the journal as needed. This option should allow commands which invoke the Revit UI for selection or for responses to task dialogs to replay correctly. |

# See Also

[Autodesk.Revit.Attributes Namespace](59587eb2-4714-707c-9ec9-766e70658df7.htm)