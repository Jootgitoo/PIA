<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/albumes">
        <html lang="es">

            <head>
                <meta charset="UTF-8"/>
                <title>Canciones de un album concreto</title>
            </head>

            <body>
                <h2>Canciones de un album en concreo</h2>

                <xsl:for-each select="album[titulo = 'Ameri']">
                    <p>Título: <xsl:value-of select="titulo"/></p>

                    <ul>
                        <xsl:for-each select="canciones/cancion">
                            <li><xsl:value-of select="."/></li>
                        </xsl:for-each>
                    </ul>
                </xsl:for-each>

            </body>
        </html>

    </xsl:template>

</xsl:stylesheet>