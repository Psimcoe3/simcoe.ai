[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Extended Property

---



|  |
| --- |
| [IExtension Interface](02355f63-69e9-ae86-31bf-c42c18beef46.htm)   [See Also](#seeAlsoToggle) |

Retrieves or set the extension status at the end

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` bool this[ 	int index ] { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Property Extended ( _ 	index As Integer _ ) As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` property bool Extended[int index] { 	bool get (int index); 	void set (int index, bool value); } ``` |

#### Parameters

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

# Remarks

Property index must be 0 or 1 to indicate two ends, otherwise exceptions will be thrown. For beams, if the beam extension status is changed, other status such as the symbolic extension status, miter status, miter locked status, and other beams extension status will be changed automatically at the same time. This change can protect that a join can have up to two extended beams, if there are two extended beams at the join, they shall be mitered.

# See Also

[IExtension Interface](02355f63-69e9-ae86-31bf-c42c18beef46.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)