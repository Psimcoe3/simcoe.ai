[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IATFTranslationServer Interface

---



|  |
| --- |
| [Members](95182c22-6664-5729-55ef-bd8b2c3890a0.htm)   [See Also](#seeAlsoToggle) |

Interface class for external servers implementing ATF translation.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public interface IATFTranslationServer : IExternalServer ``` |

 

| Visual Basic |
| --- |
| ``` Public Interface IATFTranslationServer _ 	Inherits IExternalServer ``` |

 

| Visual C++ |
| --- |
| ``` public interface class IATFTranslationServer : IExternalServer ``` |

# Remarks

A typical way to use the external server can be:

* Implement a server class that derives from this interface
* Create a new server object and register it with the service, see  ExternalServiceRegistry  .

# See Also

[IATFTranslationServer Members](95182c22-6664-5729-55ef-bd8b2c3890a0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)