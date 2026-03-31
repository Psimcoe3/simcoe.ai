[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AsInteger Method

---



|  |
| --- |
| [Parameter Class](333ff41b-e6a7-d959-60bf-c3bfae495581.htm)   [See Also](#seeAlsoToggle) |

Provides access to the integer number within the parameter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public int AsInteger() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AsInteger As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: int AsInteger() ``` |

#### Return Value

The integer value contained in the parameter.

# Remarks

The AsInteger method should only be used if the StorageType property returns that the internal contents of the parameter is an integer.

# See Also

[Parameter Class](333ff41b-e6a7-d959-60bf-c3bfae495581.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)