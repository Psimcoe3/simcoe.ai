[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IExternalResourceServer Interface

---



|  |
| --- |
| [Members](60fc99f1-fb15-270f-e2f4-279786ab4ed6.htm)   [See Also](#seeAlsoToggle) |

The interface used to provide custom implementation to provide access to external resources (such as linked files) from arbitrary locations.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public interface IExternalResourceServer : IExternalServer ``` |

 

| Visual Basic |
| --- |
| ``` Public Interface IExternalResourceServer _ 	Inherits IExternalServer ``` |

 

| Visual C++ |
| --- |
| ``` public interface class IExternalResourceServer : IExternalServer ``` |

# Remarks

Certain resources used in a Revit model are stored outside of the .rvt file. For example, the data used for keynotes, images used as decals during rendering, CAD links, and Revit links are all stored outside the model. Creating a new implementation of this server allows the server to supply one or more types of such resources from an arbitrary source. For example, a server could provide the keynote data from a database or from a file format that Revit does not support.

If a model references resources supplied by this server, Revit will request the resource from the server when it is required. Most external resources are loaded into memory at the time the model is loaded. The server will also be invoked if the resource is explicitly reloaded.

IExternalResourceServer can declare that a resource is already up-to-date via  [GetResourceVersionStatus(ExternalResourceReference)](e5699493-c827-d7ba-151c-8d9cdbf894ba.htm)  If the resource is up-to-date, Revit will skip loading to improve performance.

Each resource load request will be associated with a GUID, so that server implementers can uniquely identify a given load request. This may be useful to, for example, store server-side errors associated with an attempt to load a particular resource.

If your server handles Revit or CAD links, you must take special care with link paths. When one of these file types is uploaded to your server, any nested references should be brought to the server along with the main link. Your server will need to repath any nested reference itself; Revit will not handle this automatically.

In the case of DWG links, your server will also need to download and possibly repath any xrefs when LoadResource is called for the top-level link. Revit will only request the top-level link directly.

In the case of Revit links, the ExternalResourceReferences for any nested links will also need to be modified in the host document. The host document should reference the Revit links at their  *server*  locations, not their local file locations. Revit may not be able to find links if the paths are not set up correctly. See  [!:Autodesk::Revit::DB::TransmissionData::ReadTransmissionData]  to inspect the set of links contained within a Revit model. See  [!:Autodesk::Revit::DB::RevitLinkType::LoadFrom]  to reload a Revit link from a server version.

Here is an example which uses nested Revit links: A user has a Revit model containing one link, Link.rvt, which contains one nested link, Nest.rvt. The user uploads Link.rvt to a server, using an add-in provided by that server. The server provider must also take Nest.rvt. Further, the server provider must open Link.rvt and modify the reference to Nest.rvt so that it references the version on the server. Otherwise, Revit will not be able to find Nest.rvt when another user tries to load Link.rvt from the server.

The external resource framework has been designed to allow server authors to display UI related to the resource load operation and UI browse operation.  *No UI should be displayed directly from an IExternalResourceServer.*  Instead, developers should create an IExternalResourceUIServer which will handle UI tasks on behalf of the IExternalResourceServer. For more information, see the documentation for the  [LoadResource(Guid, ExternalResourceType, ExternalResourceReference, ExternalResourceLoadContext, ExternalResourceLoadContent)](f9e67f37-93dc-24a1-70f2-ea603a7719ab.htm)  and  [SetupBrowserData(ExternalResourceBrowserData)](04e7642f-aea8-7996-4f3b-6b5e8834a1f9.htm)  methods.

# See Also

[IExternalResourceServer Members](60fc99f1-fb15-270f-e2f4-279786ab4ed6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)