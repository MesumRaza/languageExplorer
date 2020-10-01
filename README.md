# Language Explorer
Language Explorer is a tool for exploring features of language, particularly in natural language documents. The idea is that in many documents, it's useful to view information about individual words and sentences. For instance, it can be useful to know the part of speech value of a word, or the root, or a gloss (if it's a translation), or synonyms, etc. Language Explorer provides a nice reading experience while exposing these attributes as a tooltip on each word.

You can see a demo of this app [here](https://desolate-castle-10591.herokuapp.com/)

## Managing your documents
Document management currently supports two features

1. Adding a document
> Documents require three things to work: 1) a name, 2) attribute names, and 3) a verticalized graph of the document. The name corresponds to the actual name of the document. The attribute names is a comma separated list of the names of the attributes that you will reference in the document. The first attribute must always be word. The verticalized graph of the document is a tab separated document where each word is in its own row. The columns correspond to the attributes. Column A must always be the actual word, but beyond that, feel free to add as many columns as you want - the tool should show however many attributes as you select to see.


2. Removing a document
>WIP

FUTURE: I want to add a document editor so you can add attributes and modify attribute values.

## Viewing your documents
To view a document, select Text Viewer on the left panel and select which text you'd like to view. You can also modulate which attributes (of the defined attributes for this document) you'd like to see, and Text Viewer will not show the attributes you do not select. To see the attributes, simply hover over a word.
