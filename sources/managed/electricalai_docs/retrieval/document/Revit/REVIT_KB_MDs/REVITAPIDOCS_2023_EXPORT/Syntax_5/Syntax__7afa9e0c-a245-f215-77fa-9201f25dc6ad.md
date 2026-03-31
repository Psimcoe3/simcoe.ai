[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IDataConversionMonitor Interface

---



|  |
| --- |
| [Members](10e80c8a-7f86-85fb-5882-46a0e8c1b3f8.htm)   [See Also](#seeAlsoToggle) |

A base class for an application-specific logger. It should be used to track errors during conversion and/or , track conversion progress, cancel a conversion process if necessary. Implementing a logger class is optional, but highly recommended for all but most basic data converters. The base class is UI- and language-independent. It is up to the using app to implement UI. Language-specifc data may be used to communicate information to application users. English should be used to communicate data of interest to Revit development.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public interface IDataConversionMonitor ``` |

 

| Visual Basic |
| --- |
| ``` Public Interface IDataConversionMonitor ``` |

 

| Visual C++ |
| --- |
| ``` public interface class IDataConversionMonitor ``` |

# See Also

[IDataConversionMonitor Members](10e80c8a-7f86-85fb-5882-46a0e8c1b3f8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)