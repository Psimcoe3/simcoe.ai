[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadFamily Method (String)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Loads an entire family and all its types/symbols into the document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool LoadFamily( 	string filename ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function LoadFamily ( _ 	filename As String _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool LoadFamily( 	String^ filename ) ``` |

#### Parameters

filename
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The fully qualified filename of the Family file, usually ending in .rfa.

#### Return Value

True if the entire family was loaded successfully into the project, otherwise False.

# Remarks

Loading an entire family may take a considerable amount of time and memory. It is recommended that you use one of the LoadFamilySymbol() methods and only load those symbols that you need.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when filename is    a null reference (  Nothing  in Visual Basic)  or empty. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[LoadFamily Overload](2966229b-60b0-404d-5ffe-e4c4d85d2d7a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)