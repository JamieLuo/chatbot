from langchain.schema.document import Document
'''
 * Given a list of documents, this util formats their contents
 * into a string, separated by newlines.
 *
 * @param documents
 * @returns A string of the documents page content, separated by newlines.
 '''


def docToStr(documents):
    docStrList = []
    for file in documents:
        fileStr = []
        for key in file.dict():
            fileStr.append(file.dict()[key].join("\n\n"))
        docStrList.append(fileStr)
    return docStrList
    
    
    
    #docStr = (documents: Document[]): string => documents.map((doc) => doc.pageContent).join("\n\n")