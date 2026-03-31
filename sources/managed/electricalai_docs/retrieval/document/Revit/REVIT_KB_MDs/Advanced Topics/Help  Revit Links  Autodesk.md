---
created: 2026-01-28T21:18:42 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Linked_Files_Revit_Links_html
author: 
---

# Help | Revit Links | Autodesk

> ## Excerpt
> Revit documents can have links to various external files, including other Revit documents. These types of links in the Revit API are represented by the RevitLinkType and RevitLinkInstance classes. The RevitLinkType class represents another Revit Document ("link") brought into the current one ("host"), while the RevitLinkInstance class represents an instance of a RevitLinkType.

---
Revit documents can have links to various external files, including other Revit documents. These types of links in the Revit API are represented by the RevitLinkType and RevitLinkInstance classes. The RevitLinkType class represents another Revit Document ("link") brought into the current one ("host"), while the RevitLinkInstance class represents an instance of a RevitLinkType.

### Creating New Links

To create a new Revit link, use the static RevitLinkType.Create() method which will create a new Revit link type and load the linked document and the static RevitLinkInstance.Create() method to place an instance of the link in the model. The RevitLinkType.Create() method requires a document (which will be the host), a ModelPath to the file to be linked, and a RevitLinkOptions object. The RevitLinkOptions class represents options for creating and loading a Revit link. Options include whether or not Revit will store a relative or absolute path to the linked file and the workset configuration. The WorksetConfiguration class is used to specify which, if any, worksets will be opened when creating the link. Note that the relative or absolute path determines how Revit will store the path, but the ModelPath passed into the Create() method needs a complete path to find the linked document initially.

The following example demonstrates the use of RevitLinkType.Create(). The variable pathName is the full path to the file on disk to be linked.

<table summary="" id="GUID-0DFBA9EA-0E7B-49D4-9576-6D0528FC0D3C__TABLE_A0816A8F90D8495CBCDFCAFF1A47C994"><tbody><tr><td><b>Code Region: Create new Revit Link</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>ElementId</span><span> </span><span>CreateRevitLink</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>string</span><span> pathName</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilePath</span><span> path </span><span>=</span><span> </span><span>new</span><span> </span><span>FilePath</span><span>(</span><span>pathName</span><span>);</span><span>
    </span><span>RevitLinkOptions</span><span> options </span><span>=</span><span> </span><span>new</span><span> </span><span>RevitLinkOptions</span><span>(</span><span>false</span><span>);</span><span>
    </span><span>// Create new revit link storing absolute path to file</span><span>
    </span><span>LinkLoadResult</span><span> result </span><span>=</span><span> </span><span>RevitLinkType</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> path</span><span>,</span><span> options</span><span>);</span><span>
    </span><span>return</span><span> </span><span>(</span><span>result</span><span>.</span><span>ElementId</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Once the RevitLinkType is created, instances can be added to the document. In the following example, two instances of a RevitLinkType are added, offset by 100'. Until a RevitLinkInstance is created, the Revit link will show up in the Manage Links window, but the elements of the linked file will not be visible in any views.

<table summary="" id="GUID-0DFBA9EA-0E7B-49D4-9576-6D0528FC0D3C__TABLE_A314A2C068AE49879C31807FC70D37D5"><tbody><tr><td><b>Code Region: Create new Revit Link Instance</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateLinkInstances</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>ElementId</span><span> linkTypeId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create revit link instance at origin</span><span>
    </span><span>RevitLinkInstance</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> linkTypeId</span><span>);</span><span>
    </span><span>RevitLinkInstance</span><span> instance2 </span><span>=</span><span> </span><span>RevitLinkInstance</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> linkTypeId</span><span>);</span><span>
    </span><span>// Offset second instance by 100 feet</span><span>
    </span><span>Location</span><span> location </span><span>=</span><span> instance2</span><span>.</span><span>Location</span><span>;</span><span>
    location</span><span>.</span><span>Move</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>0</span><span>));</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The examples above work with files on the local disk. Below is a more complex example involving a link to a model on Revit server.

<table summary="" id="GUID-0DFBA9EA-0E7B-49D4-9576-6D0528FC0D3C__TABLE_049D8737A2184D7381C13CE834018D5F"><tbody><tr><td><b>Code Region: Create new Revit Link to a model located on Revit server</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>CreateLinkToServerModel</span><span>(</span><span>UIApplication</span><span> uiApp</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>UIDocument</span><span> uiDoc </span><span>=</span><span> uiApp</span><span>.</span><span>ActiveUIDocument</span><span>;</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> uiDoc</span><span>.</span><span>Document</span><span>;</span><span>

    </span><span>// Try to get the server path for the particular model on the server</span><span>
    </span><span>Application</span><span> application </span><span>=</span><span> uiApp</span><span>.</span><span>Application</span><span>;</span><span>
    </span><span>String</span><span> hostId </span><span>=</span><span> application</span><span>.</span><span>GetRevitServerNetworkHosts</span><span>().</span><span>First</span><span>();</span><span>
    </span><span>String</span><span> rootFolder </span><span>=</span><span> </span><span>"|"</span><span>;</span><span>
    </span><span>ModelPath</span><span> serverPath </span><span>=</span><span> </span><span>FindModelPathOnServer</span><span>(</span><span>application</span><span>,</span><span> hostId</span><span>,</span><span> rootFolder</span><span>,</span><span> </span><span>"Wall pin model for updaters.rvt"</span><span>);</span><span>

    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Create link"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>
        </span><span>RevitLinkOptions</span><span> options </span><span>=</span><span> </span><span>new</span><span> </span><span>RevitLinkOptions</span><span>(</span><span>false</span><span>);</span><span>

        </span><span>LinkLoadResult</span><span> result </span><span>=</span><span> </span><span>RevitLinkType</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> serverPath</span><span>,</span><span> options</span><span>);</span><span>

        </span><span>RevitLinkInstance</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> result</span><span>.</span><span>ElementId</span><span>);</span><span>
        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>private</span><span> </span><span>static</span><span> </span><span>ModelPath</span><span> </span><span>FindModelPathOnServer</span><span>(</span><span>Application</span><span> app</span><span>,</span><span> </span><span>string</span><span> hostId</span><span>,</span><span> </span><span>string</span><span> folderName</span><span>,</span><span> </span><span>string</span><span> fileName</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Connect to host to find list of available models (the "/contents" flag)</span><span>
    </span><span>XmlDictionaryReader</span><span> reader </span><span>=</span><span> </span><span>GetServerResponse</span><span>(</span><span>app</span><span>,</span><span> hostId</span><span>,</span><span> folderName </span><span>+</span><span> </span><span>"/contents"</span><span>);</span><span>
    </span><span>bool</span><span> found </span><span>=</span><span> </span><span>false</span><span>;</span><span>

    </span><span>// Look for the target model name in top level folder</span><span>
    </span><span>List</span><span>&lt;</span><span>String</span><span>&gt;</span><span> folders </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>String</span><span>&gt;();</span><span>
    </span><span>while</span><span> </span><span>(</span><span>reader</span><span>.</span><span>Read</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>// Save a list of subfolders, if found</span><span>
        </span><span>if</span><span> </span><span>(</span><span>reader</span><span>.</span><span>NodeType</span><span> </span><span>==</span><span> </span><span>XmlNodeType</span><span>.</span><span>Element</span><span> </span><span>&amp;&amp;</span><span> reader</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Folders"</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>while</span><span> </span><span>(</span><span>reader</span><span>.</span><span>Read</span><span>())</span><span>
            </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>reader</span><span>.</span><span>NodeType</span><span> </span><span>==</span><span> </span><span>XmlNodeType</span><span>.</span><span>EndElement</span><span> </span><span>&amp;&amp;</span><span> reader</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Folders"</span><span>)</span><span>
                    </span><span>break</span><span>;</span><span>

                </span><span>if</span><span> </span><span>(</span><span>reader</span><span>.</span><span>NodeType</span><span> </span><span>==</span><span> </span><span>XmlNodeType</span><span>.</span><span>Element</span><span> </span><span>&amp;&amp;</span><span> reader</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Name"</span><span>)</span><span>
                </span><span>{</span><span>
                    reader</span><span>.</span><span>Read</span><span>();</span><span>
                    folders</span><span>.</span><span>Add</span><span>(</span><span>reader</span><span>.</span><span>Value</span><span>);</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
        </span><span>// Check for a matching model at this folder level</span><span>
        </span><span>if</span><span> </span><span>(</span><span>reader</span><span>.</span><span>NodeType</span><span> </span><span>==</span><span> </span><span>XmlNodeType</span><span>.</span><span>Element</span><span> </span><span>&amp;&amp;</span><span> reader</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Models"</span><span>)</span><span>
        </span><span>{</span><span>
            found </span><span>=</span><span> </span><span>FindModelInServerResponse</span><span>(</span><span>reader</span><span>,</span><span> fileName</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>found</span><span>)</span><span>
                </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    reader</span><span>.</span><span>Close</span><span>();</span><span>

    </span><span>// Build the model path to match the found model on the server</span><span>
    </span><span>if</span><span> </span><span>(</span><span>found</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Server URLs use "|" for folder separation, Revit API uses "/"</span><span>
        </span><span>String</span><span> folderNameFragment </span><span>=</span><span> folderName</span><span>.</span><span>Replace</span><span>(</span><span>'|'</span><span>,</span><span> </span><span>'/'</span><span>);</span><span>

        </span><span>// Add trailing "/" if not present</span><span>
        </span><span>if</span><span> </span><span>(!</span><span>folderNameFragment</span><span>.</span><span>EndsWith</span><span>(</span><span>"/"</span><span>))</span><span>
            folderNameFragment </span><span>+=</span><span> </span><span>"/"</span><span>;</span><span>

        </span><span>// Build server path</span><span>
        </span><span>ModelPath</span><span> modelPath </span><span>=</span><span> </span><span>new</span><span> </span><span>ServerPath</span><span>(</span><span>hostId</span><span>,</span><span> folderNameFragment </span><span>+</span><span> fileName</span><span>);</span><span>
        </span><span>return</span><span> modelPath</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>// Try subfolders</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>String</span><span> folder </span><span>in</span><span> folders</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ModelPath</span><span> modelPath </span><span>=</span><span> </span><span>FindModelPathOnServer</span><span>(</span><span>app</span><span>,</span><span> hostId</span><span>,</span><span> folder</span><span>,</span><span> fileName</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>modelPath </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
                </span><span>return</span><span> modelPath</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> </span><span>null</span><span>;</span><span>
</span><span>}</span><span>

</span><span>// This string is different for each RevitServer version</span><span>
</span><span>private</span><span> </span><span>static</span><span> </span><span>string</span><span> revitServerVersion </span><span>=</span><span> </span><span>"/RevitServerAdminRESTService2014/AdminRESTService.svc/"</span><span>;</span><span>

</span><span>private</span><span> </span><span>static</span><span> </span><span>XmlDictionaryReader</span><span> </span><span>GetServerResponse</span><span>(</span><span>Application</span><span> app</span><span>,</span><span> </span><span>string</span><span> hostId</span><span>,</span><span> </span><span>string</span><span> info</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create request    </span><span>
    </span><span>WebRequest</span><span> request </span><span>=</span><span> </span><span>WebRequest</span><span>.</span><span>Create</span><span>(</span><span>"http://"</span><span> </span><span>+</span><span> hostId </span><span>+</span><span> revitServerVersion </span><span>+</span><span> info</span><span>);</span><span>
    request</span><span>.</span><span>Method</span><span> </span><span>=</span><span> </span><span>"GET"</span><span>;</span><span>

    </span><span>// Add the information the request needs</span><span>

    request</span><span>.</span><span>Headers</span><span>.</span><span>Add</span><span>(</span><span>"User-Name"</span><span>,</span><span> app</span><span>.</span><span>Username</span><span>);</span><span>
    request</span><span>.</span><span>Headers</span><span>.</span><span>Add</span><span>(</span><span>"User-Machine-Name"</span><span>,</span><span> app</span><span>.</span><span>Username</span><span>);</span><span>
    request</span><span>.</span><span>Headers</span><span>.</span><span>Add</span><span>(</span><span>"Operation-GUID"</span><span>,</span><span> </span><span>Guid</span><span>.</span><span>NewGuid</span><span>().</span><span>ToString</span><span>());</span><span>

    </span><span>// Read the response</span><span>
    </span><span>XmlDictionaryReaderQuotas</span><span> quotas </span><span>=</span><span>
        </span><span>new</span><span> </span><span>XmlDictionaryReaderQuotas</span><span>();</span><span>
    </span><span>XmlDictionaryReader</span><span> jsonReader </span><span>=</span><span>
        </span><span>JsonReaderWriterFactory</span><span>.</span><span>CreateJsonReader</span><span>(</span><span>request</span><span>.</span><span>GetResponse</span><span>().</span><span>GetResponseStream</span><span>(),</span><span> quotas</span><span>);</span><span>

    </span><span>return</span><span> jsonReader</span><span>;</span><span>
</span><span>}</span><span>

</span><span>private</span><span> </span><span>static</span><span> </span><span>bool</span><span> </span><span>FindModelInServerResponse</span><span>(</span><span>XmlDictionaryReader</span><span> reader</span><span>,</span><span> </span><span>string</span><span> fileName</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Read through entries in this section</span><span>
    </span><span>while</span><span> </span><span>(</span><span>reader</span><span>.</span><span>Read</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>reader</span><span>.</span><span>NodeType</span><span> </span><span>==</span><span> </span><span>XmlNodeType</span><span>.</span><span>EndElement</span><span> </span><span>&amp;&amp;</span><span> reader</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Models"</span><span>)</span><span>
            </span><span>break</span><span>;</span><span>

        </span><span>if</span><span> </span><span>(</span><span>reader</span><span>.</span><span>NodeType</span><span> </span><span>==</span><span> </span><span>XmlNodeType</span><span>.</span><span>Element</span><span> </span><span>&amp;&amp;</span><span> reader</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Name"</span><span>)</span><span>
        </span><span>{</span><span>
            reader</span><span>.</span><span>Read</span><span>();</span><span>
            </span><span>String</span><span> modelName </span><span>=</span><span> reader</span><span>.</span><span>Value</span><span>;</span><span>
            </span><span>if</span><span> </span><span>(</span><span>modelName</span><span>.</span><span>Equals</span><span>(</span><span>fileName</span><span>))</span><span>
            </span><span>{</span><span>
                </span><span>// Match found, stop looping and return</span><span>
                </span><span>return</span><span> </span><span>true</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> </span><span>false</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

In the example below, the WorksetConfiguration is obtained, modified so that only one specified workset is opened and set back to the RevitLinkOptions prior to creating the new link.

<table summary="" id="GUID-0DFBA9EA-0E7B-49D4-9576-6D0528FC0D3C__TABLE_3BF18721D9E147C99E51A9D47AEB5044"><tbody><tr><td><b>Code Region: Create link with one workset open</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>bool</span><span> </span><span>CreateRevitLinkWithOneWorksetOpen</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>string</span><span> pathName</span><span>,</span><span> </span><span>string</span><span> worksetName</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilePath</span><span> path </span><span>=</span><span> </span><span>new</span><span> </span><span>FilePath</span><span>(</span><span>pathName</span><span>);</span><span>
    </span><span>RevitLinkOptions</span><span> options </span><span>=</span><span> </span><span>new</span><span> </span><span>RevitLinkOptions</span><span>(</span><span>true</span><span>);</span><span>

    </span><span>// Get info on all the user worksets in the project prior to opening</span><span>
    </span><span>IList</span><span>&lt;</span><span>WorksetPreview</span><span>&gt;</span><span> worksets </span><span>=</span><span> </span><span>WorksharingUtils</span><span>.</span><span>GetUserWorksetInfo</span><span>(</span><span>path</span><span>);</span><span>
    </span><span>IList</span><span>&lt;</span><span>WorksetId</span><span>&gt;</span><span> worksetIds </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>WorksetId</span><span>&gt;();</span><span>
    </span><span>// Find worksetName</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>WorksetPreview</span><span> worksetPrev </span><span>in</span><span> worksets</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>worksetPrev</span><span>.</span><span>Name</span><span>.</span><span>CompareTo</span><span>(</span><span>worksetName</span><span>)</span><span> </span><span>==</span><span> </span><span>0</span><span>)</span><span>
        </span><span>{</span><span>
            worksetIds</span><span>.</span><span>Add</span><span>(</span><span>worksetPrev</span><span>.</span><span>Id</span><span>);</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>// close all worksets but the one specified</span><span>
    </span><span>WorksetConfiguration</span><span> worksetConfig </span><span>=</span><span> </span><span>new</span><span> </span><span>WorksetConfiguration</span><span>(</span><span>WorksetConfigurationOption</span><span>.</span><span>CloseAllWorksets</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>worksetIds</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        worksetConfig</span><span>.</span><span>Open</span><span>(</span><span>worksetIds</span><span>);</span><span>
    </span><span>}</span><span>
    options</span><span>.</span><span>SetWorksetConfiguration</span><span>(</span><span>worksetConfig</span><span>);</span><span>

    </span><span>LinkLoadResult</span><span> result </span><span>=</span><span> </span><span>RevitLinkType</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> path</span><span>,</span><span> options</span><span>);</span><span>
    </span><span>RevitLinkType</span><span> type </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>result</span><span>.</span><span>ElementId</span><span>)</span><span> </span><span>as</span><span> </span><span>RevitLinkType</span><span>;</span><span>
    </span><span>return</span><span> </span><span>(</span><span>result</span><span>.</span><span>LoadResult</span><span> </span><span>==</span><span> </span><span>LinkLoadResultType</span><span>.</span><span>LinkLoaded</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Whether creating or loading a link, a LinkLoadResult is returned. This class has a property to determine if the link was loaded. It also has an ElementId property that is the id of the created or loaded linked model.

RevitLinkInstance.Create(ImportPlacement placement)creates a new instance of a linked Revit project (RevitLinkType). Instances will be placed origin-to-origin or by shared coordinates according to the input placement type.

### Loading and Unloading Links

RevitLinkType has several methods related to loading links. Load(), LoadFrom() and Unload() allow a link to be loaded or unloaded, or to be loaded from a new location. These methods regenerate the document. The document's Undo history will be cleared by these methods. All transaction phases (e.g. transactions, transaction groups and sub-transactions) that were explicitly started must be finished prior to calling one of these methods.

The static method RevitLinkType.IsLoaded() will return whether or not the link is loaded.

### Getting Link Information

Each RevitLinkType in a document can have one or more associated RevitLinkInstances. The RevitLinkInstance.GetLinkDocument() method returns a Document associated with the Revit link. This document cannot be modified, meaning that operations that require a transaction or modify the document's status in memory (such as Save and Close) cannot be performed.

The associated RevitLinkType for a RevitLinkInstance can be retrieved from the document using the ElementId obtained from the RevitLinkInstance.GetTypeId() method. The RevitLinkType for a linked file has several methods and properties related to nested links. A document that is linked in to another document may itself have links. The IsNested property returns true if the RevitLinkType is a nested link (i.e. it has some other link as a parent), or false if it is a top-level link. The method GetParentId() will get the id of the immediate parent of this link, while GetRootId() will return the id of the top-level link which this link is ultimately linked under. Both methods will return invalidElementId if this link is a top-level link. The method GetChildIds() will return the element ids of all links which are linked directly into this one.

For example, if C is linked into document B and B in turn is linked into document A, calling GetParentId() for the C link will return the id of document B and calling GetRootId() for the C link will return the id of document A. Calling GetChildIds() for document A will only return the id of B's link since C is not a direct link under A.

RevitLinkType also has a PathType property which indicates if the path to the external file reference is relative to the host file's location (or to the central model's location if the host is workshared), an absolute path to a location on disk or the network, or if the path is to a Revit Server location.

The AttachmentType property of RevitLinkType indicates if the link is an attachment or an overlay. "Attachment" links are considered to be part of their parent link and will be brought along if their parent is linked into another document. "Overlay" links are only visible when their parent is opened directly.

The following example gets all RevitLinkInstances in the document and displays some information on them.

<table summary="" id="GUID-0DFBA9EA-0E7B-49D4-9576-6D0528FC0D3C__TABLE_37FBA1DF81EC4336931323A6ACB298F4"><tbody><tr><td><b>Code Region: Getting Link information</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetAllRevitLinkInstances</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
    collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>RevitLinkInstance</span><span>));</span><span>
    </span><span>StringBuilder</span><span> linkedDocs </span><span>=</span><span> </span><span>new</span><span> </span><span>StringBuilder</span><span>();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> elem </span><span>in</span><span> collector</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>RevitLinkInstance</span><span> instance </span><span>=</span><span> elem </span><span>as</span><span> </span><span>RevitLinkInstance</span><span>;</span><span>
        </span><span>Document</span><span> linkDoc </span><span>=</span><span> instance</span><span>.</span><span>GetLinkDocument</span><span>();</span><span>
        linkedDocs</span><span>.</span><span>AppendLine</span><span>(</span><span>"FileName: "</span><span> </span><span>+</span><span> </span><span>Path</span><span>.</span><span>GetFileName</span><span>(</span><span>linkDoc</span><span>.</span><span>PathName</span><span>));</span><span>
        </span><span>RevitLinkType</span><span> type </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>instance</span><span>.</span><span>GetTypeId</span><span>())</span><span> </span><span>as</span><span> </span><span>RevitLinkType</span><span>;</span><span>
        linkedDocs</span><span>.</span><span>AppendLine</span><span>(</span><span>"Is Nested: "</span><span> </span><span>+</span><span> type</span><span>.</span><span>IsNestedLink</span><span>.</span><span>ToString</span><span>());</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit Links in Document"</span><span>,</span><span> linkedDocs</span><span>.</span><span>ToString</span><span>());</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Link Geometry

#### Shared coordinates

The RevitLinkType methods SavePositions() and HasSaveablePositions() support saving shared coordinates changes back to the linked document. Use HasSaveablePositions() to determine if the link has shared positioning changes which can be saved. Call SavePositions() to save shared coordinates changes back to the linked document. SavePositions() requires an instance of the ISaveSharedCoordinatesCallback interface to resolve situations when Revit encounters modified links. The interface's GetSaveModifiedLinksOption() method determines whether Revit should save the link, not save the link, or discard shared positioning entirely.

While SavePositions() does not clear the document's undo history, it cannot be undone since it saves the link's shared coordinates changes to disk.

`ResetSharedCoordinates()` resets the shared coordinates for the host model. It provides the same functionality as the UI Command "Reset Shared Coordinates". After resetting coordinates, the following changes will take place:

-   GIS coordinate system will be erased
-   Shared coordinates?relationships with other linked models will be eliminated.
-   The Survey Point will be moved back to the startup location, where it coincides with the Internal Origin.
-   The angle between Project North and True North will be reset to 0.

Note: There will be no changes to linked models.

#### Conversion of geometric references

The Reference class has members related to linked files that allow conversion between Reference objects which reference only the contents of the link and Reference objects which reference the host. This allows an application, for example, to look at the geometry in the link, find the needed face, and convert the reference to that face into a reference in the host suitable for use to place a face-based instance. Also, these Reference members make it possible to obtain a reference in the host (e.g. from a dimension or family) and convert it to a reference in the link suitable for use in Element.GetGeometryObjectFromReference().

The Reference. LinkedElementId property represents the id of the top-level element in the linked document that is referred to by this reference, or InvalidElementId for references that do not refer to an element in a linked RVT file. The Reference . CreateLinkReference() method uses a RevitLinkInstance to create a Reference from a Reference in a Revit link. And the Reference. CreateReferenceInLink() method creates a Reference in a Revit Link from a Reference in the host file

#### Picking elements in links

The Selection methods PickObject() and PickObjects() allow the selection of objects in Revit links. To allow the user to select elements in linked files, use the ObjectType.LinkedElement enumeration value for the first parameter of the PickObject() or PickObjects(). Note that this option allows for selection of elements in links only, not in the host document.

In the example below, an ISelectionFilter is used to allow only walls to be selected in linked files.

<table summary="" id="GUID-0DFBA9EA-0E7B-49D4-9576-6D0528FC0D3C__TABLE_44433DC9BBAA43E589F3191FE6F3C44B"><tbody><tr><td><b>Code Region: Selecting Elements in Linked File</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SelectElementsInLinkedDoc</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>Selection</span><span> choices </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>;</span><span>
    </span><span>// Pick one wall from Revit link</span><span>
    </span><span>WallInLinkSelectionFilter</span><span> wallFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>WallInLinkSelectionFilter</span><span>();</span><span>
    </span><span>Reference</span><span> elementRef </span><span>=</span><span> choices</span><span>.</span><span>PickObject</span><span>(</span><span>ObjectType</span><span>.</span><span>LinkedElement</span><span>,</span><span> wallFilter</span><span>,</span><span> </span><span>"Select a wall in a linked document"</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>elementRef </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>"Element from link document selected."</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>// This filter allows selection of only a certain element type in a link instance.</span><span>
</span><span>class</span><span> </span><span>WallInLinkSelectionFilter</span><span> </span><span>:</span><span> </span><span>ISelectionFilter</span><span>
</span><span>{</span><span>
    </span><span>private</span><span> </span><span>RevitLinkInstance</span><span> m_currentInstance </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>public</span><span> </span><span>bool</span><span> </span><span>AllowElement</span><span>(</span><span>Element</span><span> e</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Accept any link instance, and save the handle for use in AllowReference()</span><span>
        m_currentInstance </span><span>=</span><span> e </span><span>as</span><span> </span><span>RevitLinkInstance</span><span>;</span><span>
        </span><span>return</span><span> </span><span>(</span><span>m_currentInstance </span><span>!=</span><span> </span><span>null</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>bool</span><span> </span><span>AllowReference</span><span>(</span><span>Reference</span><span> refer</span><span>,</span><span> XYZ point</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>m_currentInstance </span><span>==</span><span> </span><span>null</span><span>)</span><span>
            </span><span>return</span><span> </span><span>false</span><span>;</span><span>

        </span><span>// Get the handle to the element in the link</span><span>
        </span><span>Document</span><span> linkedDoc </span><span>=</span><span> m_currentInstance</span><span>.</span><span>GetLinkDocument</span><span>();</span><span>
        </span><span>Element</span><span> elem </span><span>=</span><span> linkedDoc</span><span>.</span><span>GetElement</span><span>(</span><span>refer</span><span>.</span><span>LinkedElementId</span><span>);</span><span>

        </span><span>// Accept the selection if the element exists and is of the correct type</span><span>
        </span><span>return</span><span> elem </span><span>!=</span><span> </span><span>null</span><span> </span><span>&amp;&amp;</span><span> elem </span><span>is</span><span> </span><span>Wall</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
