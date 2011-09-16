xsltproc -o book.fo /usr/share/xml/docbook/stylesheet/docbook-xsl-ns/fo/docbook_zh.xsl book.xml
fop -c /etc/fop/fop.xconf book.fo -pdf book.pdf