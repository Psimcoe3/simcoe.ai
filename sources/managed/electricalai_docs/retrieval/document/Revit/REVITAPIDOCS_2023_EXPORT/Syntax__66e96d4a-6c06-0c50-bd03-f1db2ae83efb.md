[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LineScaling Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing possible LineType scaling modes.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public enum LineScaling ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration LineScaling ``` |

 

| Visual C++ |
| --- |
| ``` public enum class LineScaling ``` |

# Members

| Member name | Description |
| --- | --- |
| ViewScale | Exporting lines as they were scaled by view scale. This option preserves visual fidelity. |
| ModelSpace | Modelspace scaling. LTSCALE is set to view scale and PSLTSCALE to 0. |
| PaperSpace | Paperspace scaling. Specifies the value 1 for both LTSCALE and PSLTSCALE. |

# Remarks

Whichever option is chosen, line type definitions are created so a dashed line always begins and ends with a dash. Using these options does change the default behavior of exported DWGs. Some lines expected to be dashed may appear solid or in a different scale.

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)