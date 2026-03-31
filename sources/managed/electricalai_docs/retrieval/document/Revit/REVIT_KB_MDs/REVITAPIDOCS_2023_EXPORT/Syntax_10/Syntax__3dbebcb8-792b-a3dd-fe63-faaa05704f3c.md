[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StorageType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing all of the internal parameter data storage types that Autodesk Revit supports.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public enum StorageType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration StorageType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class StorageType ``` |

# Members

| Member name | Description |
| --- | --- |
| None | None represents an invalid storage type. This value should not be used. |
| Integer | The internal data is stored in the form of a signed 32 bit integer. |
| Double | The data will be stored internally in the form of an 8 byte floating point number. |
| String | The internal data will be stored in the form of a string of characters. |
| ElementId | The data type represents an element and is stored as the id of the element. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)