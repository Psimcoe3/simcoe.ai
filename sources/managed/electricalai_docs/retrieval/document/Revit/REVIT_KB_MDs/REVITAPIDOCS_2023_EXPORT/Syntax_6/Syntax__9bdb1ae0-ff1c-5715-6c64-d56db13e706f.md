[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OnDuplicateTypeNamesFound Method

---



|  |
| --- |
| [IDuplicateTypeNamesHandler Interface](2fa855ba-6a1a-b0af-8079-10415ff7e2d3.htm)   [See Also](#seeAlsoToggle) |

Called when the destination document contains types with the same names as the types being copied.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` DuplicateTypeAction OnDuplicateTypeNamesFound( 	DuplicateTypeNamesHandlerArgs args ) ``` |

 

| Visual Basic |
| --- |
| ``` Function OnDuplicateTypeNamesFound ( _ 	args As DuplicateTypeNamesHandlerArgs _ ) As DuplicateTypeAction ``` |

 

| Visual C++ |
| --- |
| ``` DuplicateTypeAction OnDuplicateTypeNamesFound( 	DuplicateTypeNamesHandlerArgs^ args ) ``` |

#### Parameters

args
:   Type:  [Autodesk.Revit.DB DuplicateTypeNamesHandlerArgs](939b55de-12e5-2117-5fbc-471f8bb009c9.htm)    
     The information about the types with duplicate names.

#### Return Value

The action to be taken: copy only types with unique names or cancel the operation.

# See Also

[IDuplicateTypeNamesHandler Interface](2fa855ba-6a1a-b0af-8079-10415ff7e2d3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)