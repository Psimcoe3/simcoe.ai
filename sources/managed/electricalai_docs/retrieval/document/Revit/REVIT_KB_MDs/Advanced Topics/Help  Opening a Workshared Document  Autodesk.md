---
created: 2026-01-28T21:20:18 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Opening_a_Workshared_Document_html
author: 
---

# Help | Opening a Workshared Document | Autodesk

> ## Excerpt
> The Application.OpenDocumentFile(ModelPath, OpenOptions) method can be used to set options related to opening a workshared document. In addition to options to detach from the central document or to allow a local file to be opened ReadOnly by a user other than its owner, options may also be set related to worksets. When a workshared document is opened, all system worksets are automatically opened, however user-created worksets can be specified to be opened or closed. Elements in an open workset can be expanded and displayed. However, elements in a closed workset are not displayed to avoid expanding them. By only opening worksets necessary in the current session, Revit's memory footprint is reduced, which can help with performance.

---
The Application.OpenDocumentFile(ModelPath, OpenOptions) method can be used to set options related to opening a workshared document. In addition to options to detach from the central document or to allow a local file to be opened ReadOnly by a user other than its owner, options may also be set related to worksets. When a workshared document is opened, all system worksets are automatically opened, however user-created worksets can be specified to be opened or closed. Elements in an open workset can be expanded and displayed. However, elements in a closed workset are not displayed to avoid expanding them. By only opening worksets necessary in the current session, Revit's memory footprint is reduced, which can help with performance.

In the example below, a document is opened with two worksets specified to be opened. Note that the WorksharingUtils.GetUserWorksetInfo() method can be used to access workset information from a closed Revit document.

<table summary="" id="GUID-F99FBBCC-AE58-46F5-85AF-0A7C3C5C0576__TABLE_FC2899FD121E4503873B3A95C92E0A26"><tbody><tr><td><b>Code Region: Open Workshared Document</b></td></tr><tr><td><pre><code><span>Document</span><span> </span><span>OpenDocumentWithWorksets</span><span>(</span><span>Application</span><span> app</span><span>,</span><span> </span><span>ModelPath</span><span> projectPath</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>try</span><span>
    </span><span>{</span><span>
        </span><span>// Get info on all the user worksets in the project prior to opening</span><span>
        </span><span>IList</span><span>&lt;</span><span>WorksetPreview</span><span>&gt;</span><span> worksets </span><span>=</span><span> </span><span>WorksharingUtils</span><span>.</span><span>GetUserWorksetInfo</span><span>(</span><span>projectPath</span><span>);</span><span>
        </span><span>IList</span><span>&lt;</span><span>WorksetId</span><span>&gt;</span><span> worksetIds </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>WorksetId</span><span>&gt;();</span><span>
        </span><span>// Find two predetermined worksets</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>WorksetPreview</span><span> worksetPrev </span><span>in</span><span> worksets</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>if</span><span> </span><span>(</span><span>worksetPrev</span><span>.</span><span>Name</span><span>.</span><span>CompareTo</span><span>(</span><span>"Workset1"</span><span>)</span><span> </span><span>==</span><span> </span><span>0</span><span> </span><span>||</span><span>
                worksetPrev</span><span>.</span><span>Name</span><span>.</span><span>CompareTo</span><span>(</span><span>"Workset2"</span><span>)</span><span> </span><span>==</span><span> </span><span>0</span><span>)</span><span>
            </span><span>{</span><span>
                worksetIds</span><span>.</span><span>Add</span><span>(</span><span>worksetPrev</span><span>.</span><span>Id</span><span>);</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>

        </span><span>OpenOptions</span><span> openOptions </span><span>=</span><span> </span><span>new</span><span> </span><span>OpenOptions</span><span>();</span><span>
        </span><span>// Setup config to close all worksets by default</span><span>
        </span><span>WorksetConfiguration</span><span> openConfig </span><span>=</span><span> </span><span>new</span><span> </span><span>WorksetConfiguration</span><span>(</span><span>WorksetConfigurationOption</span><span>.</span><span>CloseAllWorksets</span><span>);</span><span>
        </span><span>// Set list of worksets for opening </span><span>
        openConfig</span><span>.</span><span>Open</span><span>(</span><span>worksetIds</span><span>);</span><span>
        openOptions</span><span>.</span><span>SetOpenWorksetsConfiguration</span><span>(</span><span>openConfig</span><span>);</span><span>
        doc </span><span>=</span><span> app</span><span>.</span><span>OpenDocumentFile</span><span>(</span><span>projectPath</span><span>,</span><span> openOptions</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>catch</span><span> </span><span>(</span><span>Exception</span><span> e</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Open File Failed"</span><span>,</span><span> e</span><span>.</span><span>Message</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> doc</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Another option is to open the document while just opening the last viewed worksets.

<table summary="" id="GUID-F99FBBCC-AE58-46F5-85AF-0A7C3C5C0576__TABLE_1DA72F15EB5D4284A4E357B4FC779B2B"><tbody><tr><td><b>Code Region: Open last viewed worksets</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>Document</span><span> </span><span>OpenLastViewed</span><span>(</span><span>UIApplication</span><span> uiApplication</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Application</span><span> application </span><span>=</span><span> uiApplication</span><span>.</span><span>Application</span><span>;</span><span>

    </span><span>// Setup options</span><span>
    </span><span>OpenOptions</span><span> options1 </span><span>=</span><span> </span><span>new</span><span> </span><span>OpenOptions</span><span>();</span><span>

    </span><span>// Default config opens all.  Close all first, then open last viewed to get the correct settings.</span><span>
    </span><span>WorksetConfiguration</span><span> worksetConfig </span><span>=</span><span> </span><span>new</span><span> </span><span>WorksetConfiguration</span><span>(</span><span>WorksetConfigurationOption</span><span>.</span><span>OpenLastViewed</span><span>);</span><span>
    options1</span><span>.</span><span>SetOpenWorksetsConfiguration</span><span>(</span><span>worksetConfig</span><span>);</span><span>

    </span><span>// Open the document</span><span>
    </span><span>Document</span><span> openedDoc </span><span>=</span><span> application</span><span>.</span><span>OpenDocumentFile</span><span>(</span><span>GetWSAPIModelPath</span><span>(</span><span>"WorkaredFileSample.rvt"</span><span>),</span><span> options1</span><span>);</span><span>

    </span><span>return</span><span> openedDoc</span><span>;</span><span>
</span><span>}</span><span>

</span><span>private</span><span> </span><span>static</span><span> </span><span>ModelPath</span><span> </span><span>GetWSAPIModelPath</span><span>(</span><span>string</span><span> fileName</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Utility to get a local path for a target model file</span><span>
    </span><span>FileInfo</span><span> filePath </span><span>=</span><span> </span><span>new</span><span> </span><span>FileInfo</span><span>(</span><span>Path</span><span>.</span><span>Combine</span><span>(@</span><span>"C:\Documents\Revit Projects"</span><span>,</span><span> fileName</span><span>));</span><span>
    </span><span>ModelPath</span><span> mp </span><span>=</span><span> </span><span>ModelPathUtils</span><span>.</span><span>ConvertUserVisiblePathToModelPath</span><span>(</span><span>filePath</span><span>.</span><span>FullName</span><span>);</span><span>

    </span><span>return</span><span> mp</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following two examples demonstrate how to create a new local first from disk or from a Revit server, and then open it. Note that the sample below uses the GetWSAPIModelPath() method used in the previous example.

<table summary="" id="GUID-F99FBBCC-AE58-46F5-85AF-0A7C3C5C0576__TABLE_162B83853A7241DCAFE8A4D788A3CD74"><tbody><tr><td><b>Code Region: Open new local from disk</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>Document</span><span> </span><span>OpenNewLocalFromDisk</span><span>(</span><span>UIApplication</span><span> uiApplication</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create new local from a disk location</span><span>
    </span><span>ModelPath</span><span> newLocalPath </span><span>=</span><span> </span><span>GetWSAPIModelPath</span><span>(</span><span>"LocalWorksharing.rvt"</span><span>);</span><span>
    </span><span>return</span><span> </span><span>(</span><span>OpenNewLocalFromModelPath</span><span>(</span><span>uiApplication</span><span>.</span><span>Application</span><span>,</span><span> </span><span>GetWSAPIModelPath</span><span>(</span><span>"NewLocalWorksharing.rvt"</span><span>),</span><span> newLocalPath</span><span>));</span><span>
</span><span>}</span><span>

</span><span>private</span><span> </span><span>static</span><span> </span><span>Document</span><span> </span><span>OpenNewLocalFromModelPath</span><span>(</span><span>Application</span><span> app</span><span>,</span><span> </span><span>ModelPath</span><span> centralPath</span><span>,</span><span> </span><span>ModelPath</span><span> localPath</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create the new local at the given path</span><span>
    </span><span>WorksharingUtils</span><span>.</span><span>CreateNewLocal</span><span>(</span><span>centralPath</span><span>,</span><span> localPath</span><span>);</span><span>

    </span><span>// Select specific worksets to open</span><span>
    </span><span>// First get a list of worksets from the unopened document</span><span>
    </span><span>IList</span><span>&lt;</span><span>WorksetPreview</span><span>&gt;</span><span> worksets </span><span>=</span><span> </span><span>WorksharingUtils</span><span>.</span><span>GetUserWorksetInfo</span><span>(</span><span>localPath</span><span>);</span><span>
    </span><span>List</span><span>&lt;</span><span>WorksetId</span><span>&gt;</span><span> worksetsToOpen </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>WorksetId</span><span>&gt;();</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>WorksetPreview</span><span> preview </span><span>in</span><span> worksets</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Match worksets to open with criteria</span><span>
        </span><span>if</span><span> </span><span>(</span><span>preview</span><span>.</span><span>Name</span><span>.</span><span>StartsWith</span><span>(</span><span>"O"</span><span>))</span><span>
            worksetsToOpen</span><span>.</span><span>Add</span><span>(</span><span>preview</span><span>.</span><span>Id</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Setup option to open the target worksets</span><span>
    </span><span>// First close all, then set specific ones to open</span><span>
    </span><span>WorksetConfiguration</span><span> worksetConfig </span><span>=</span><span> </span><span>new</span><span> </span><span>WorksetConfiguration</span><span>(</span><span>WorksetConfigurationOption</span><span>.</span><span>CloseAllWorksets</span><span>);</span><span>
    worksetConfig</span><span>.</span><span>Open</span><span>(</span><span>worksetsToOpen</span><span>);</span><span>

    </span><span>// Open the new local</span><span>
    </span><span>OpenOptions</span><span> options1 </span><span>=</span><span> </span><span>new</span><span> </span><span>OpenOptions</span><span>();</span><span>
    options1</span><span>.</span><span>SetOpenWorksetsConfiguration</span><span>(</span><span>worksetConfig</span><span>);</span><span>
    </span><span>Document</span><span> openedDoc </span><span>=</span><span> app</span><span>.</span><span>OpenDocumentFile</span><span>(</span><span>localPath</span><span>,</span><span> options1</span><span>);</span><span>

    </span><span>return</span><span> openedDoc</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following example uses the OpenNewLocalFromModelPath() method demonstrated as part of the previous example.

<table summary="" id="GUID-F99FBBCC-AE58-46F5-85AF-0A7C3C5C0576__TABLE_E6C6F43A63E34845AEBB3BFF72135458"><tbody><tr><td><b>Code Region: Open new local from Revit Server</b></td></tr><tr><td><pre><code><span>/// &lt;summary&gt;</span><span>
</span><span>/// Get the server path for a particular model and open a new local copy</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>public</span><span> </span><span>static</span><span> </span><span>Document</span><span> </span><span>OpenNewLocalFromServer</span><span>(</span><span>UIApplication</span><span> uiApp</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create new local from a server location</span><span>
    </span><span>Application</span><span> app </span><span>=</span><span> uiApp</span><span>.</span><span>Application</span><span>;</span><span>

    </span><span>// Get the host id/IP of the server</span><span>
    </span><span>String</span><span> hostId </span><span>=</span><span> app</span><span>.</span><span>GetRevitServerNetworkHosts</span><span>().</span><span>First</span><span>();</span><span>

    </span><span>// try to get the server path for the particular model on the server</span><span>
    </span><span>String</span><span> rootFolder </span><span>=</span><span> </span><span>"|"</span><span>;</span><span>
    </span><span>ModelPath</span><span> serverPath </span><span>=</span><span> </span><span>FindWSAPIModelPathOnServer</span><span>(</span><span>app</span><span>,</span><span> hostId</span><span>,</span><span> rootFolder</span><span>,</span><span> </span><span>"WorksharingOnServer.rvt"</span><span>);</span><span>

    </span><span>ModelPath</span><span> newLocalPath </span><span>=</span><span> </span><span>GetWSAPIModelPath</span><span>(</span><span>"WorksharingLocalFromServer.rvt"</span><span>);</span><span>
    </span><span>return</span><span> </span><span>(</span><span>OpenNewLocalFromModelPath</span><span>(</span><span>uiApp</span><span>.</span><span>Application</span><span>,</span><span> serverPath</span><span>,</span><span> newLocalPath</span><span>));</span><span>
</span><span>}</span><span>

</span><span>/// &lt;summary&gt;</span><span>
</span><span>/// Uses the Revit Server REST API to recursively search the folders of the Revit Server for a particular model.</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>private</span><span> </span><span>static</span><span> </span><span>ModelPath</span><span> </span><span>FindWSAPIModelPathOnServer</span><span>(</span><span>Application</span><span> app</span><span>,</span><span> </span><span>string</span><span> hostId</span><span>,</span><span> </span><span>string</span><span> folderName</span><span>,</span><span> </span><span>string</span><span> fileName</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Connect to host to find list of available models (the "/contents" flag)</span><span>
    </span><span>XmlDictionaryReader</span><span> reader </span><span>=</span><span> </span><span>GetResponse</span><span>(</span><span>app</span><span>,</span><span> hostId</span><span>,</span><span> folderName </span><span>+</span><span> </span><span>"/contents"</span><span>);</span><span>
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
            found </span><span>=</span><span> </span><span>FindModelInServerResponseJson</span><span>(</span><span>reader</span><span>,</span><span> fileName</span><span>);</span><span>
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
            </span><span>ModelPath</span><span> modelPath </span><span>=</span><span> </span><span>FindWSAPIModelPathOnServer</span><span>(</span><span>app</span><span>,</span><span> hostId</span><span>,</span><span> folder</span><span>,</span><span> fileName</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>modelPath </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
                </span><span>return</span><span> modelPath</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> </span><span>null</span><span>;</span><span>
</span><span>}</span><span>

</span><span>// This string is different for each RevitServer version</span><span>
</span><span>private</span><span> </span><span>static</span><span> </span><span>string</span><span> s_revitServerVersion </span><span>=</span><span> </span><span>"/RevitServerAdminRESTService2014/AdminRESTService.svc/"</span><span>;</span><span>

</span><span>/// &lt;summary&gt;</span><span>
</span><span>/// Connect to server to get list of available models and return server response</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>private</span><span> </span><span>static</span><span> </span><span>XmlDictionaryReader</span><span> </span><span>GetResponse</span><span>(</span><span>Application</span><span> app</span><span>,</span><span> </span><span>string</span><span> hostId</span><span>,</span><span> </span><span>string</span><span> info</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create request    </span><span>
    </span><span>WebRequest</span><span> request </span><span>=</span><span> </span><span>WebRequest</span><span>.</span><span>Create</span><span>(</span><span>"http://"</span><span> </span><span>+</span><span> hostId </span><span>+</span><span> s_revitServerVersion </span><span>+</span><span> info</span><span>);</span><span>
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

</span><span>/// &lt;summary&gt;</span><span>
</span><span>/// Read through server response to find particular model</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>private</span><span> </span><span>static</span><span> </span><span>bool</span><span> </span><span>FindModelInServerResponseJson</span><span>(</span><span>XmlDictionaryReader</span><span> reader</span><span>,</span><span> </span><span>string</span><span> fileName</span><span>)</span><span>
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

## Open detached from central

If an add-in will be working on a workshared file but does not need to make permanet changes, it can open the model detached from the central file.

**Code Region: Open detached**

```
private static Document OpenDetached(Application application, ModelPath modelPath)
{
    OpenOptions options1 = new OpenOptions();

    options1.DetachFromCentralOption = DetachFromCentralOption.DetachAndDiscardWorksets;
    Document openedDoc = application.OpenDocumentFile(modelPath, options1);

    return openedDoc;
}
```

If an application only needs read-only access to a server file, the example below demonstrates how to copy the server model locally and open it detached. Note this code sample re-uses methods demonstrated in previous examples.

<table summary="" id="GUID-F99FBBCC-AE58-46F5-85AF-0A7C3C5C0576__TABLE_3A8EC07A41C44592B6E75E852965C3A4"><tbody><tr><td><b>Code Region: Copy and open detached</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>Document</span><span> </span><span>CopyAndOpenDetached</span><span>(</span><span>UIApplication</span><span> uiApp</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Copy a server model locally and open detached</span><span>
    </span><span>Application</span><span> application </span><span>=</span><span> uiApp</span><span>.</span><span>Application</span><span>;</span><span>
    </span><span>String</span><span> hostId </span><span>=</span><span> application</span><span>.</span><span>GetRevitServerNetworkHosts</span><span>().</span><span>First</span><span>();</span><span>

    </span><span>// Try to get the server path for the particular model on the server</span><span>
    </span><span>String</span><span> rootFolder </span><span>=</span><span> </span><span>"|"</span><span>;</span><span>
    </span><span>ModelPath</span><span> serverPath </span><span>=</span><span> </span><span>FindWSAPIModelPathOnServer</span><span>(</span><span>application</span><span>,</span><span> hostId</span><span>,</span><span> rootFolder</span><span>,</span><span> </span><span>"ServerModel.rvt"</span><span>);</span><span>

    </span><span>// For debugging</span><span>
    </span><span>String</span><span> sourcePath </span><span>=</span><span> </span><span>ModelPathUtils</span><span>.</span><span>ConvertModelPathToUserVisiblePath</span><span>(</span><span>serverPath</span><span>);</span><span>

    </span><span>// Setup the target location for the copy</span><span>
    </span><span>ModelPath</span><span> localPath </span><span>=</span><span> </span><span>GetWSAPIModelPath</span><span>(</span><span>"CopiedModel.rvt"</span><span>);</span><span>

    </span><span>// Copy, allowing overwrite</span><span>
    application</span><span>.</span><span>CopyModel</span><span>(</span><span>serverPath</span><span>,</span><span> </span><span>ModelPathUtils</span><span>.</span><span>ConvertModelPathToUserVisiblePath</span><span>(</span><span>localPath</span><span>),</span><span> </span><span>true</span><span>);</span><span>

    </span><span>// Open the copy as detached</span><span>
    </span><span>Document</span><span> openedDoc </span><span>=</span><span> </span><span>OpenDetached</span><span>(</span><span>application</span><span>,</span><span> localPath</span><span>);</span><span>

    </span><span>return</span><span> openedDoc</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
