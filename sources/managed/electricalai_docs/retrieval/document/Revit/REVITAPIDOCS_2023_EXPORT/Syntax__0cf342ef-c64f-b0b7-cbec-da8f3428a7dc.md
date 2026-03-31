[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetParameters Method

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [See Also](#seeAlsoToggle) |

Retrieves the parameters from the element via the given name.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public IList<Parameter> GetParameters( 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetParameters ( _ 	name As String _ ) As IList(Of Parameter) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<Parameter^>^ GetParameters( 	String^ name ) ``` |

#### Parameters

name
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The name of the parameter to be retrieved.

#### Return Value

A collection containing the parameters having the same given parameter name.

# Remarks

Multiple matches of parameters with the same name can occur because shared parameters or project parameters can be bound to an element category even if there is a built-in parameter with the same name already.

If this method is used to find built-in parameters the code will not be portable to other languages of Revit (because built-in parameter names are translated, and this method matches the translation).

For the reasons above this method should be used sparingly and when portability across multiple languages is not a requirement.

Safer approaches include:

* get\_Parameter(Guid)  to get a shared parameter by stored guid.
* get\_Parameter(BuiltInParameter)  to find a built-in parameter in a language-independent way.

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)