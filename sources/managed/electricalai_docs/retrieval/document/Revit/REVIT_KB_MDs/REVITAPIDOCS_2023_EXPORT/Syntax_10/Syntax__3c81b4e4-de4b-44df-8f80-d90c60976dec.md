[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Space Property

---



|  |
| --- |
| [FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)   [See Also](#seeAlsoToggle) |

The space in which the instance is located (during the last phase of the project).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Space Space { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Space As Space 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Space^ Space { 	Space^ get (); } ``` |

# Remarks

This property will be the first space encountered that contains the instance. If more than one space includes this point in its volume only the first one is returned. If no space is found that contains the instance, this property is    a null reference (  Nothing  in Visual Basic)  .

# See Also

[FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)

[Space Overload](983a485b-e825-e91b-8fc2-b00436819169.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)