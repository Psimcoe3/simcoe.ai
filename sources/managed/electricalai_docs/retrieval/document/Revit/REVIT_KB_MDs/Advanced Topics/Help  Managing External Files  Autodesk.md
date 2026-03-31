---
created: 2026-01-28T21:18:59 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Linked_Files_Managing_External_Files_html
author: 
---

# Help | Managing External Files | Autodesk

> ## Excerpt
> As its name implies, this utility class provides information about external file references. TheExternalFileUtils.GetAllExternalFileReferences() method returns a collection of ElementIds of all elements that are external file references in the document. (Note that it will not return the ids of nested Revit links; it only returns top-level references.) This utility class has two other methods, IsExternalFileReference() and GetExternalFileReference() which perform the same function as the similarly named methods of the Element class, but can be used when you have an ElementId rather than first obtaining the Element.

---
### ExternalFileUtils

As its name implies, this utility class provides information about external file references. TheExternalFileUtils.GetAllExternalFileReferences() method returns a collection of ElementIds of all elements that are external file references in the document. (Note that it will not return the ids of nested Revit links; it only returns top-level references.) This utility class has two other methods, IsExternalFileReference() and GetExternalFileReference() which perform the same function as the similarly named methods of the Element class, but can be used when you have an ElementId rather than first obtaining the Element.

TransmissionDataTransmissionData stores information on both the previous state and requested state of an external file reference. This means that it stores the load state and path of the reference from the most recent time this TransmissionData's document was opened. It also stores load state and path information for what Revit should do the next time the document is opened.

As such, TransmissionData can be used to perform operations on external file references without having to open the entire associated Revit document. The methods ReadTransmissionData and WriteTransmissionData can be used to obtain information about external references, or to change that information. For example, calling WriteTransmissionData with a TransmissionData object which has had all references set to LinkedFileStatus.Unloaded would cause no references to be loaded upon next opening the document.

TransmissionData cannot add or remove references to external files. If AddExternalFileReference is called using an ElementId which does not correspond to an element which is an external file reference, the information will be ignored on file load.

The following example reads the TransmissionData for a file at the given location and sets all Revit links to be unloaded the next time the document is opened.

<table summary="" id="GUID-2C8C4EC0-6EEB-4D0A-A3AB-6F3434A70461__TABLE_15BEED9592504EFEAF1F8928ED3B1A98"><tbody><tr><td><b>Code Region: Unload Revit Links</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>UnloadRevitLinks</span><span>(</span><span>ModelPath</span><span> location</span><span>)</span><span>
</span><span>/// This method will set all Revit links to be unloaded the next time the document at the given location is opened. </span><span>
</span><span>/// The TransmissionData for a given document only contains top-level Revit links, not nested links.</span><span>
</span><span>/// However, nested links will be unloaded if their parent links are unloaded, so this function only needs to look at the document's immediate links. </span><span>
</span><span>{</span><span>
    </span><span>// access transmission data in the given Revit file</span><span>
    </span><span>TransmissionData</span><span> transData </span><span>=</span><span> </span><span>TransmissionData</span><span>.</span><span>ReadTransmissionData</span><span>(</span><span>location</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>transData </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// collect all (immediate) external references in the model</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> externalReferences </span><span>=</span><span> transData</span><span>.</span><span>GetAllExternalFileReferenceIds</span><span>();</span><span>
        </span><span>// find every reference that is a link</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> refId </span><span>in</span><span> externalReferences</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ExternalFileReference</span><span> extRef </span><span>=</span><span> transData</span><span>.</span><span>GetLastSavedReferenceData</span><span>(</span><span>refId</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>extRef</span><span>.</span><span>ExternalFileReferenceType</span><span> </span><span>==</span><span> </span><span>ExternalFileReferenceType</span><span>.</span><span>RevitLink</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>// we do not want to change neither the path nor the path-type</span><span>
                </span><span>// we only want the links to be unloaded (shouldLoad = false)</span><span>
                transData</span><span>.</span><span>SetDesiredReferenceData</span><span>(</span><span>refId</span><span>,</span><span> extRef</span><span>.</span><span>GetPath</span><span>(),</span><span> extRef</span><span>.</span><span>PathType</span><span>,</span><span> </span><span>false</span><span>);</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>

        </span><span>// make sure the IsTransmitted property is set </span><span>
        transData</span><span>.</span><span>IsTransmitted</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        </span><span>// modified transmission data must be saved back to the model</span><span>
        </span><span>TransmissionData</span><span>.</span><span>WriteTransmissionData</span><span>(</span><span>location</span><span>,</span><span> transData</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Unload Links"</span><span>,</span><span> </span><span>"The document does not have any transmission data"</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

#### Construct ModelPath for location on Revit Server

To read the TransmissionData object, you need to call the static method TransmissionData.ReadTransmissionData. It requires a ModelPath object.

There are two ways to construct a ModelPath object that refers to a central file. The first way involves using ModelPathUtils and the base ModelPath class. The steps are as follows:

1.  Compose the user-visible path string of the central file: `RSN://` + “relative path”.
    
    Note: The folder separator used in the "relative path" is a forward slash(/). The correct separator is a forward slash.
    
2.  Create a ModelPath object via the ModelPathUtils.ConvertUserVisiblePathToModelPath() method. Pass in the string composed in the previous step.
    
3.  Read the transmission data via the TransmissionData::ReadTransmissionData() method. Pass in the ModelPath obtained in the previous step.
    

The following example demonstrates this method assuming a central file testmodel.rvt is stored in the root folder of Revit Server, SHACNG035WQRP.

<table summary="" id="GUID-2C8C4EC0-6EEB-4D0A-A3AB-6F3434A70461__TABLE_8D9A6DA3E5804C46AE4F37D20C2611A4"><tbody><tr><td><b>Code Region: Constructing path to central file using ModelPath</b></td></tr><tr><td><pre><code><span>[</span><span>TransactionAttribute</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>TransactionMode</span><span>.</span><span>Manual</span><span>)]</span><span>
</span><span>public</span><span> </span><span>class</span><span> </span><span>RevitCommandLink</span><span> </span><span>:</span><span> </span><span>IExternalCommand</span><span>
</span><span>{</span><span>
  </span><span>public</span><span> </span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span>        
         </span><span>ref</span><span> </span><span>string</span><span> messages</span><span>,</span><span> </span><span>ElementSet</span><span> elements</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>UIApplication</span><span> app </span><span>=</span><span> commandData</span><span>.</span><span>Application</span><span>;</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> app</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>Transaction</span><span> trans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"ExComm"</span><span>);</span><span>
    trans</span><span>.</span><span>Start</span><span>();</span><span>
    </span><span>string</span><span> visiblePath </span><span>=</span><span> </span><span>"RSN://testmodel.rvt"</span><span>;</span><span>
    </span><span>ModelPath</span><span> serverPath </span><span>=</span><span> </span><span>ModelPathUtils</span><span>.</span><span>ConvertUserVisiblePathToModelPath</span><span>(</span><span>visiblePath</span><span>);</span><span>
    </span><span>TransmissionData</span><span> transData </span><span>=</span><span> </span><span>TransmissionData</span><span>.</span><span>ReadTransmissionData</span><span>(</span><span>serverPath</span><span>);</span><span>
    </span><span>string</span><span> mymessage </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>transData </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
         </span><span>//access the data in the transData here.</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
      </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Unload Links"</span><span>,</span><span>
      </span><span>"The document does not have any transmission data"</span><span>);</span><span>
    </span><span>}</span><span>
    trans</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
  </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The second way to construct the ModelPath object that that refers to a central file is to use the child class ServerPath. This way can be used if the program knows the local server name, however, it is not recommended as the server name may be changed by the Revit user from the Revit UI. The steps are as follows:

1.  Create a ServerPath object using ServerPath constructor.
    
    ```
    public ServerPath GetServerPath()
    {
    return new ServerPath("ServerNameOrServerIp", "relative path without the initial forward slash");
    }
    ```
    

Note: The first parameter is the server name, not the "RSN://" string. The second parameter does not include the initial forward slash. See the following sample code. The folder separator is a forward slash(/) too.

1\. Read the TransmissionData object via the TransmissionData.ReadTransmissionData() method.Pass in the ServerPath obtained in the previous step

The following code demonstrates this method.

<table summary="" id="GUID-2C8C4EC0-6EEB-4D0A-A3AB-6F3434A70461__TABLE_25FF84A4048F4110BCE03C0A93D8DA65"><tbody><tr><td><b>Code Region: Constructing path to central file using ServerPath</b></td></tr><tr><td><pre><code><span>[</span><span>TransactionAttribute</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>TransactionMode</span><span>.</span><span>Manual</span><span>)]</span><span>
</span><span>public</span><span> </span><span>class</span><span> </span><span>RevitCommand</span><span> </span><span>:</span><span> </span><span>IExternalCommand</span><span>
</span><span>{</span><span>
  </span><span>public</span><span> </span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span>
         </span><span>ref</span><span> </span><span>string</span><span> messages</span><span>,</span><span> </span><span>ElementSet</span><span> elements</span><span>)</span><span>
  </span><span>{</span><span>
    </span><span>UIApplication</span><span> app </span><span>=</span><span> commandData</span><span>.</span><span>Application</span><span>;</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> app</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>Transaction</span><span> trans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"ExComm"</span><span>);</span><span>
    trans</span><span>.</span><span>Start</span><span>();</span><span>
    </span><span>ServerPath</span><span> serverPath </span><span>=</span><span> </span><span>new</span><span> </span><span>ServerPath</span><span>(</span><span>"SHACNG035WQRP"</span><span>,</span><span> </span><span>"testmodel.rvt"</span><span>);</span><span>
    </span><span>TransmissionData</span><span> transData </span><span>=</span><span> </span><span>TransmissionData</span><span>.</span><span>ReadTransmissionData</span><span>(</span><span>serverPath</span><span>);</span><span>
    </span><span>string</span><span> mymessage </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>transData </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
       </span><span>//access the data in the transData here.</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
      </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Unload Links"</span><span>,</span><span>
         </span><span>"The document does not have any transmission data"</span><span>);</span><span>
    </span><span>}</span><span>
    trans</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
  </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
