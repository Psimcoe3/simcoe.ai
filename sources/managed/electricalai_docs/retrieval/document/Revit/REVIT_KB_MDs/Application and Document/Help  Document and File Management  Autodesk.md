---
created: 2026-01-28T20:42:39 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Document and File Management | Autodesk

> ## Excerpt
> Document and file management make it easy to create and find your documents. For information about cloud-based Revit files, see Cloud Models.

---
Document and file management make it easy to create and find your documents. For information about cloud-based Revit files, see [Cloud Models](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Application_and_Document_CloudFiles_html).

### Document Retrieval

The Application class maintains all documents. As previously mentioned, you can open more than one document in a session. The active document is retrieved using the UIApplication class property, ActiveUIDocument.

All open documents, including the active document, are retrieved using the Application class Documents property. The property returns a set containing all open documents in the Revit session.

### Document File Information

The Document class provides two properties for each corresponding file, PathName, and Title.

-   PathName returns the document's fully qualified file path. The PathName returns an empty string if the project has not been saved since it was created.
-   Title is the project title, which is usually derived from the project filename. The returned value varies based on your system settings.

### Basic File Info

BasicFileInfo provides fast access to basic information about a Revit file, including worksharing status, Revit version, username and central path. This is done without fully opening the file.

```
static BasicFileInfo.Extract(string file)
```

Returns a BasicFileInfo object whose properties provide information about the file.

Extract is not forward-compatible, meaning that Calling Extract from a version of Revit prior to Revit 2019 will result in an exception if it is called on a Revit 2019 or later file. This may occur again with future versions of Revit.

### Open a Document

The Application class provides an overloaded method to open an existing project file:

**Table 3: Open Document in API**

<table summary="" id="GUID-5282B7DB-E7A7-465B-A925-53BBBC3CC8D7__TABLE_626DB724E12F4AF7A6D5514683F939F4"><tbody><tr><td><b>Method</b></td><td><b>Event</b></td></tr><tr><td><p><code>Document OpenDocumentFile(string filename)</code></p><p><code>Document OpenDocumentFile(ModelPath modelPath, OpenOptions openOptions)</code></p><p><code>Document OpenDocumentFile(ModelPath modelPath, OpenOptions openOptions, IOpenFromCloudCallback openFromCloudCallback)</code></p></td><td>DocumentOpened</td></tr></tbody></table>

When you specify a string with a fully qualified file path, Revit opens the file and creates a Document instance. Use this method to open a file on other computers by assigning the files Universal Naming Conversion (UNC) name to this method.

The file can be a project file with the extension .rvt, a family file with the extension .rfa, or a template file with the extension .rte.

The second overload takes a path to the model as a ModelPath rather than a string and the OpenOptions parameter offers options for opening the file, such as the ability to detach the opened document from central if applicable, as well as options related to worksharing. For more information about opening a workshared document, see [Opening a Workshared Document](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Opening_a_Workshared_Document_html).

These methods throw specific documented exceptions in the event of a failure. Exceptions fall into 4 main categories.

**Table 4: Types of exceptions thrown**

<table summary="" id="GUID-5282B7DB-E7A7-465B-A925-53BBBC3CC8D7__TABLE_164EE052B85441D78583C6C1043B1088"><tbody><tr><td><b>Type</b></td><td><b>Example</b></td></tr><tr><td>Disk errors</td><td>File does not exist or is wrong version</td></tr><tr><td>Resource errors</td><td>Not enough memory or disk space to open file</td></tr><tr><td>Central model file errors</td><td>File is locked or corrupt</td></tr><tr><td>Central model/server errors</td><td>Network communication error with server</td></tr></tbody></table>

If the document is opened successfully, the DocumentOpened event is raised.

#### Create a Document

Create new documents using the Application methods in the following table.

**Table 5: Create Document in the API**

<table summary="" id="GUID-5282B7DB-E7A7-465B-A925-53BBBC3CC8D7__TABLE_FB13876B60BE4EFEA107B82CDF114FED"><tbody><tr><td><b>Method</b></td><td><b>Event</b></td></tr><tr><td><p><code>Document NewProjectDocument(string templateFileName);</code></p></td><td>DocumentCreated</td></tr><tr><td><p><code>Document NewProjectDocument(UnitSystem unitSystem);</code></p></td><td>DocumentCreated</td></tr><tr><td><p><code>Document NewFamilyDocument(string templateFileName);</code></p></td><td>DocumentCreated</td></tr><tr><td><p><code>Document NewProjectTemplateDocument(string templateFilename);</code></p></td><td>DocumentCreated</td></tr></tbody></table>

For the methods that require a template file name as a parameter, the created document is returned based on the template file. NewProjectDocument(UnitSystem)creates a new imperial or metric project document without a specified template.

#### Save and Close a Document

The Document class provides methods to save or close instances.

**Table 6: Save and Close Document in API**

<table summary="" id="GUID-5282B7DB-E7A7-465B-A925-53BBBC3CC8D7__TABLE_04DB3D7B63204912B4ABA9E24CFD3CF1"><tbody><tr><td><b>Method</b></td><td><b>Event</b></td></tr><tr><td>Save()</td><td>DocumentSaved</td></tr><tr><td>SaveAs()</td><td>DocumentSavedAs</td></tr><tr><td>Close()</td><td>DocumentClosed</td></tr></tbody></table>

Save() has 2 overloads, one with no arguments and one with a SaveOptions argument that can specify whether to force the OS to delete all dead data from the file on disk. If the file has not been previously saved, SaveAs() must be called instead.

SaveAs() has 3 overloads. One overload takes only the filename as an argument and an exception will be thrown if another file exists with the given filename. The other 2 overloads takes a filename as an argument (in the form of a ModelPath in one case) as well as a second SaveAsOptions argument that can be used to specify whether to overwrite an existing file, if it exists. SaveAsOptions can also be used to specify other relevant options such as whether to remove dead data on disk related to the file and worksharing options.

Save() and SaveAs() throw specific documented exceptions in the same 4 categories as when opening a document and listed in Table 4 above.

Close() has two overloads. One takes a Boolean argument that indicates whether to save the file before closing it. The second overload takes no arguments and if the document was modified, the user will be asked if they want to save the file before closing. This method will throw an exception if the document's path name is not already set or if the saving target file is read-only.

Note: The Close() method does not affect the active document or raise the DocumentClosed event, because the document is used by an external application. You can only call this method on non-active documents.

The UIDocument class also provides methods to save and close instances.

**Table 7: Save and Close UIDocument in API**

<table summary="" id="GUID-5282B7DB-E7A7-465B-A925-53BBBC3CC8D7__TABLE_1443F9F4594F424D8C82A53F1A6C4911"><tbody><tr><td><b>Method</b></td><td><b>Event</b></td></tr><tr><td>SaveAndClose()</td><td>DocumentSaved, DocumentClosed</td></tr><tr><td>SaveAs()</td><td>DocumentSavedAs</td></tr></tbody></table>

SaveAndClose() closes the document after saving it. If the document's path name has not been set the "Save As" dialog will be shown to the Revit user to set its name and location.

The SaveAs() method saves the document to a file name and path obtained from the Revit user via the "Save As" dialog.

#### Document Preview

The DocumentPreviewSettings class can be obtained from the Document and contains the settings related to the saving of preview images for a given document.

<table summary="" id="GUID-5282B7DB-E7A7-465B-A925-53BBBC3CC8D7__TABLE_C7DE262D8D244EDBB1BFC7519FFA17E5"><tbody><tr><td><b>Code Region: Document Preview</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SaveActiveViewWithPreview</span><span>(</span><span>UIApplication</span><span> application</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get the handle of current document.</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document </span><span>=</span><span> application</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Document</span><span>;</span><span>

    </span><span>// Get the document's preview settings</span><span>
    </span><span>DocumentPreviewSettings</span><span> settings </span><span>=</span><span> document</span><span>.</span><span>GetDocumentPreviewSettings</span><span>();</span><span>

    </span><span>// Find a candidate 3D view</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>View3D</span><span>));</span><span>

    </span><span>Func</span><span>&lt;</span><span>View3D</span><span>,</span><span> </span><span>bool</span><span>&gt;</span><span> isValidForPreview </span><span>=</span><span> v </span><span>=&gt;</span><span> settings</span><span>.</span><span>IsViewIdValidForPreview</span><span>(</span><span>v</span><span>.</span><span>Id</span><span>);</span><span>

    </span><span>View3D</span><span> viewForPreview </span><span>=</span><span> collector</span><span>.</span><span>OfType</span><span>&lt;</span><span>View3D</span><span>&gt;().</span><span>First</span><span>&lt;</span><span>View3D</span><span>&gt;(</span><span>isValidForPreview</span><span>);</span><span>

    </span><span>// Set the preview settings</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> setTransaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Set preview view id"</span><span>))</span><span>
    </span><span>{</span><span>
        setTransaction</span><span>.</span><span>Start</span><span>();</span><span>
        settings</span><span>.</span><span>PreviewViewId</span><span> </span><span>=</span><span> viewForPreview</span><span>.</span><span>Id</span><span>;</span><span>
        setTransaction</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>

    </span><span>// Save the document</span><span>
    document</span><span>.</span><span>Save</span><span>();</span><span>

</span><span>}</span></code></pre></td></tr></tbody></table>

#### Load Family

The Document class provides you with the ability to load an entire family and all of its symbols into the project. Because loading an entire family can take a long time and a lot of memory, the Document class provides a similar method, LoadFamilySymbol() to load only specified symbols.

For more details, see [Family](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_Family_html).
