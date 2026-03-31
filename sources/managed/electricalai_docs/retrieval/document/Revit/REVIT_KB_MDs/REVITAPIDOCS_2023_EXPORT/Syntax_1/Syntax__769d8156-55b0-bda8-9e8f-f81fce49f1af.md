[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConnectorType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing all connector types for a connection

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` public enum ConnectorType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ConnectorType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ConnectorType ``` |

# Members

| Member name | Description |
| --- | --- |
| Invalid | Invalid connection type |
| End | End connection type |
| Curve | Curve connection type |
| Logical | Logical connection type |
| Reference | Reference connection type |
| Surface | Surface connection type |
| EndSurface | End or Surface connection type |
| Physical | Physical connection type |
| NonEnd | Not end connection type |
| MasterSurface | This value is deprecated and will be removed in a future version of Revit. Please use MainSurface instead. |
| MainSurface | Main surface connection type |
| Family | Family connection type |
| NodeReference | Reference to the layout node type |
| BlankEnd | Blank End type |
| AnyEnd | Any end connection type |
| Super | Connection between a sub-system and a super-system, such as a connection between supply and return sub-systems and a main hydronic piping system or an air system. |
| AllModes | All connection modes |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)